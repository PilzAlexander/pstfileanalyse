from os import write
import sys
import csv
import pandas as pd
from matplotlib import pyplot as plt

file = 'C:\\Users\\Alexp\\PycharmProjects\\pstfileanalyse\\Sender.CSV'


def get_emails(file):
    emails = []
    with open(file, 'r', encoding='UTF8') as in_file:
        for row in csv.reader(in_file):
            if row[0] in emails:
                index = emails.index(row[0])
                emails[index + 1] = emails[index + 1] + 1
            else:
                address = row[0]
                emails.append(address)
                emails.append(1)
    return emails


emails = get_emails(file)

with open('FromCount.csv', mode='w', encoding='UTF8', newline='') as out_file:
    header = ['Sender', 'Received Mails']
    writer = csv.writer(out_file)  # create the writer
    writer.writerow(header)  # write the header rows
    length = int(len(emails) / 2)
    for i in range(0, length):
        writer.writerow([emails[(i * 2)], emails[(i * 2) + 1]])
