from os import write
import sys
import csv

maxInt = sys.maxsize

counter = 1

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)

##############################################
email_list = []

# 'C:\\Users\\Alexp\\PycharmProjects\\pstfileanalyse\\CSVFiles\\APWPosteingang.CSV'

with open('C:\\Users\\Alexp\\PycharmProjects\\pstfileanalyse\\CSVFiles\\From.csv', 'r', encoding='UTF8') as in_file:
    for row in csv.reader(in_file):
        if not row:
            test = 0
        else:
            if row[0] in email_list:
                index = email_list.index(row[0])
                email_list[index + 1] = email_list[index + 1] + 1
            else:
                tmp_word = row[0]
                email_list.append(tmp_word)
                email_list.append(1)

with open('FromCount.csv', mode='w', encoding='UTF8', newline='') as out_file:
    writer = csv.writer(out_file)
    tmp_length = int(len(email_list) / 2)
    for i in range(0, tmp_length):
        writer.writerow([email_list[(i * 2)], email_list[(i * 2) + 1]])
