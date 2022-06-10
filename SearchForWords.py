import csv


list = ['€€€',
    '$$$',
    '100% gratis',
    '100% kostenlos',
    'Sichere Anlage',
    'Bargeld',
    'Bargeld-günstig',
    'Begünstigter',
    'Cash',
    'Einkommen verdoppeln',
    'Einkommen von Zuhause',
    'Extra Bargeld verdienen',
    'Fondsmanagement',
    'Geld verdienen leicht gemacht',
    'Günstiger Kredit',
    'Günstige Refinanzierung',
    'Hypothek',
    'Ihr Zahlungsverzug',
    'Kostenlos',
    'Kontosicherheit',
    'Paypal',
    'Rechnung',
    'Rendite',
    'Senken Sie Ihre Hypothek',
    'Schulden beseitigen',
    'Verdienen Sie “x” pro Woche',
    'Versteckte Kosten',
    'Viel Geld sparen',
    'Visa/Mastercard',
    'Völlig kostenlos',
    'Von Zuhause arbeiten',
    'Kostenlos', '100% unentgeltlich', 'Vergütung', 'Geschenk', 'Rückzahlung', 'gebührenfrei', 'kostenlos anmelden', 'gratis testen', 'Gewinn',
    'garantiert', '100% kostenlos', '100% sicher', 'zertifiziert', 'risikofrei', 'Angebot', 'Bonus', 'Schnäppchen', 'gesehen im TV', 'Deal', 'es funktioniert', 'keine Abzocke', 'kein Spam', 'keine versteckten Kosten', 'Passwort', 'persönliche Angaben',
    'machen Sie schnell', 'sofort', 'jetzt profitieren', 'limitiertes Angebot', 'Ab jetzt', 'nur heute', 'zögern Sie nicht', 'greifen Sie zu', 'läuft bald ab',
    'Sie haben gewonnen', 'Bravo', 'klicken', 'um Ihr Geschenk zu erhalten', 'außergewöhnliches Geschenk', 'gewinnen', 'Sie wurden ausgewählt', 'Glückwunsch', 'Belohnung',
    'Gewicht verlieren', 'schnell abnehmen', 'zu viele Kilos', 'wie abnehmen', 'Diät', 'Verjüngung', 'Schonkost', 'Erektion', 'Falten', 'Schnarchen', 'Altern', 'Glatze', 'ohne Aufwand', 'Ausdauer' 
]

for i in range(len(list)):
    tmp_string = ''.join(list[i])

    if tmp_string.islower() == True:
        print(list[i])


# fname = "OutputFiles/Message.txt"
# word= "%"
# k = 0

# with open(fname, 'r', encoding='UTF8') as f:
#     for line in f:
#         words = line.split()
#         for j in range(len(words)):
#             tmp_word = words[j]
#             tmp_word = tmp_word.replace('\\','')
#             # tmp_word.replace("\",'')
#             words[j] = tmp_word

#         # for i in words:
#         for k in range(len(words)):
#             for i in range(len(list)):
#                 # str1 = ''.join(words)
#                 if(words[k]==list[i]):
#                     k=k+1
#         print(list[i], k)

# print("Occurrences of the word:")
# print(k)


# import re
# count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape('payback'), open('OutputFiles/Message.txt', encoding='UTF8')))

counter = 0
word_list = []

with open('OUTPUTFiles/Message.txt', encoding='UTF8') as f:
    contents = f.read()
    for i in range(len(list)):
        tmp_word = list[i]
        # count = contents.count(list[i].lower)
        count = contents.count(tmp_word)
        print(list[i], count)
        if count != 0:
           word_list.append(list[i])
           word_list.append(count)
           
with open('CounterWords.csv', mode='w', encoding='UTF8', newline='') as out_file:
    writer = csv.writer(out_file)
    tmp_length = int(len(word_list)/2)
    for i in range(0,tmp_length):
        writer.writerow([word_list[(i*2)], word_list[(i*2)+1]])

# # with open('OutputFiles/Message.txt', encoding='UTF8') as file:
# with open('test.txt', encoding='UTF8') as file:
#     contents = file.read()
#     search_word = "Test"
#     if search_word in contents:
#         counter = counter + 1
#         print ('word found')
#     else:
#         print ('word not found')