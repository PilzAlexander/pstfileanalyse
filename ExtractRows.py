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
        maxInt = int(maxInt/10)

# with open('Date.csv', mode='w', encoding='UTF8') as employee_file:
#     with open('Posteingang.csv', 'r', encoding='UTF8') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             print(row[1])
#             employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#             employee_writer.writerow([row[1]])

with open('MessagesPD.csv', 'r', encoding='UTF8') as in_file:
    with open('Subject.csv', mode='w', encoding='UTF8', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if any(field.strip() for field in row):
                writer.writerow([row[0]])
                # counter = counter + 1

with open('MessagesPD.csv', 'r', encoding='UTF8') as in_file:
    with open('Sender.csv', mode='w', encoding='UTF8', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if any(field.strip() for field in row):
                writer.writerow([row[1]])

with open('MessagesPD.csv', 'r', encoding='UTF8') as in_file:
    with open('Datetime.csv', mode='w', encoding='UTF8', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if any(field.strip() for field in row):
                writer.writerow([row[2]])

with open('MessagesPD.csv', 'r', encoding='UTF8') as in_file:
    with open('Text.csv', mode='w', encoding='UTF8', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if any(field.strip() for field in row):
                writer.writerow([row[3]])

#with open('MessagesPD.csv', 'r', encoding='UTF8') as in_file:
  #  with open('Message.csv', mode='w', encoding='UTF8', newline='') as out_file:
  #      writer = csv.writer(out_file)
    #    for row in csv.reader(in_file):
    #        if any(field.strip() for field in row):
       #         writer.writerow([row[4]])