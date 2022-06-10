import sys
import mailbox
import csv
from email.header import decode_header

infile = sys.argv[1]
outfile = sys.argv[2]
writer = csv.writer(open(outfile, "w"))


def get_content(part):
    content = ''
    payload = part.get_payload()
    if isinstance(payload, str):
        content += payload
    else:
        for part in payload:
            content += get_content(part)
    return content


writer.writerow(['date', 'from', 'to', 'subject', 'content'])
for index, message in enumerate(mailbox.mbox(infile)):
    content = get_content(message)
    row = [
        message['date'],
        message['from'].strip('>').split('<')[-1],
        message['to'],
        decode_header(message['subject'])[0][0],
        content
    ]
    writer.writerow(row)