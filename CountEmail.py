from os import write
import sys
import csv
import pandas as pd

emails = []

file = 'C:\\Users\\Alexp\\PycharmProjects\\pstfileanalyse\\CSVFiles\\LRKOPosteingang.CSV'

with open(file, 'r', encoding='UTF8') as in_file:
    for row in csv.reader(in_file):
        if not row:
            test = 0
        else:
            if row[0] in emails:
                index = emails.index(row[0])
                emails[index + 1] = emails[index + 1] + 1
            else:
                tmp_word = row[0]
                emails.append(tmp_word)
                emails.append(1)

with open('FromCount.csv', mode='w', encoding='UTF8', newline='') as out_file:
    header = ['Sender', 'Received Mails']

    writer = csv.writer(out_file) # create the writer
    writer.writerow(header) # write the header rows
    length = int(len(emails) / 2)
    for i in range(0, length):
        writer.writerow([emails[(i * 2)], emails[(i * 2) + 1]])
