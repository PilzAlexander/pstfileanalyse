# import csv

# csv_file = input('From.csv')
# txt_file = input('From.txt')

# with open(txt_file, "w", encoding='UTF8') as my_output_file:
#     with open(csv_file, "r", encoding='UTF8') as my_input_file:
#         [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
#     my_output_file.close()

# csv_file = input('Date.csv')
# txt_file = input('Date.txt')

text_list = []

with open('Message.csv', "r", encoding='UTF8') as my_input_file:
    for line in my_input_file:
        line = line.split(",", 2)
        text_list.append(" ".join(line))

with open('Message.txt', "w", encoding='UTF8', newline='') as my_output_file:
    my_output_file.write("#1\n")
    my_output_file.write("double({},{})\n".format(len(text_list), 2))
    for line in text_list:
        my_output_file.write("  " + line)
    print('File Successfully written.')