
textList = []

with open('Message.csv', "r", encoding='UTF8') as my_input_file:
    for line in my_input_file:
        line = line.split(",", 2)
        textList.append(" ".join(line))

with open('Message.txt', "w", encoding='UTF8', newline='') as my_output_file:
    my_output_file.write("#1\n")
    my_output_file.write("double({},{})\n".format(len(textList), 2))
    for line in textList:
        my_output_file.write("  " + line)
    print('File Successfully written.')