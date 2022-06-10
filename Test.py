# importing library
import pandas as pd
  
# Then loading csv file
df = pd.read_csv('C:\\Users\\Alexp\\PycharmProjects\\pstfileanalyse\\CSVFiles\\From.csv', 'r', encoding='UTF8')
  
# converting ;FRUIT_NAME' column into list
a = list(df['from'])
  
# converting list into string and then joining it with space
b = ' '.join(str(e) for e in a)
  
# printing result
print(b)
  

with open(b, "w", encoding='UTF8') as my_output_file:
    my_output_file.write("#1\n")
    my_output_file.write("double({},{})\n".format(len(b), 2))
    for line in b:
        my_output_file.write("  " + line)
    print('File Successfully written.')


# converting 'PRICE' column into list
# d = list(df['PRICE'])
  
# # another way for joining used
# e = '\n'.join(map(str, d))
  
# # printing result
# print(e)