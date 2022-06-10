#! /usr/bin/env python3
# ~*~ utf-8 ~*~

import mailbox
from os import write
import bs4
import csv

header = ['date', 'from', 'to', 'subject', 'text']
message_list = []
counter = 1

def get_html_text(html):
    try:
        return bs4.BeautifulSoup(html, 'lxml').body.get_text(' ', strip=True)
    except AttributeError: # message contents empty
        return None

class GmailMboxMessage():
    def __init__(self, email_data):
        if not isinstance(email_data, mailbox.mboxMessage):
            raise TypeError('Variable must be type mailbox.mboxMessage')
        self.email_data = email_data

    def parse_email(self, counter):
        message_list = []
        email_labels = self.email_data['X-Gmail-Labels']
        email_date = self.email_data['Date']
        email_from = self.email_data['From']
        email_to = self.email_data['To']
        email_subject = self.email_data['Subject']
        email_text = self.read_email_payload() 
        
        # message_list.append(email_labels)
        message_list.append(email_date)
        message_list.append(email_from)
        message_list.append(email_to)
        message_list.append(email_subject)
        message_list.append(email_text)
        return message_list

            # for word in message_list:
            #     writer.writerow([counter, word])
            # # writer.writerow([counter, message_list])
            # writer.writerow([0,header])
            # writer.writerow([counter,email_date])
            # writer.writerow([counter,email_from])
            # writer.writerow([counter,email_to])
            # writer.writerow([counter,email_subject])
            # writer.writerow([counter,email_text])

    def read_email_payload(self):
        email_payload = self.email_data.get_payload()
        if self.email_data.is_multipart():
            email_messages = list(self._get_email_messages(email_payload))
        else:
            email_messages = [email_payload]
        return [self._read_email_text(msg) for msg in email_messages]

    def _get_email_messages(self, email_payload):
        for msg in email_payload:
            if isinstance(msg, (list,tuple)):
                for submsg in self._get_email_messages(msg):
                    yield submsg
            elif msg.is_multipart():
                for submsg in self._get_email_messages(msg.get_payload()):
                    yield submsg
            else:
                yield msg

    def _read_email_text(self, msg):
        content_type = 'NA' if isinstance(msg, str) else msg.get_content_type()
        encoding = 'NA' if isinstance(msg, str) else msg.get('Content-Transfer-Encoding', 'NA')
        if 'text/plain' in content_type and 'base64' not in encoding:
            msg_text = msg.get_payload()
        elif 'text/html' in content_type and 'base64' not in encoding:
            msg_text = get_html_text(msg.get_payload())
        elif content_type == 'NA':
            msg_text = get_html_text(msg)
        else:
            msg_text = None
        return (content_type, encoding, msg_text)

######################### End of library, example of use below

mbox_obj = mailbox.mbox('Posteingang.mbox')

num_entries = len(mbox_obj)
with open('Posteingang.csv', 'w', encoding='UTF8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['date', 'from', 'to', 'subject', 'text'])

    for idx, email_obj in enumerate(mbox_obj):
        email_data = GmailMboxMessage(email_obj)
        tmp_list = email_data.parse_email(counter)
        writer.writerow([tmp_list[0],tmp_list[1],tmp_list[2],tmp_list[3],tmp_list[4]])
        print('Parsing email {0} of {1}'.format(idx, num_entries))
        counter = counter + 1