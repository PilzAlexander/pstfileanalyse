import csv

spamWordList = ['€€€',
                '$$$', '100% gratis', '100% kostenlos', 'Sichere Anlage', 'Bargeld', 'Bargeld-günstig', 'Begünstigter',
                'Cash', 'Einkommen verdoppeln',
                'Einkommen von Zuhause', 'Extra Bargeld verdienen', 'Fondsmanagement', 'Geld verdienen leicht gemacht',
                'Günstiger Kredit', 'Günstige Refinanzierung',
                'Hypothek', 'Ihr Zahlungsverzug', 'Kostenlos', 'Kontosicherheit', 'Paypal', 'Rechnung', 'Rendite',
                'Senken Sie Ihre Hypothek', 'Schulden beseitigen',
                'Verdienen Sie “x” pro Woche', 'Versteckte Kosten', 'Viel Geld sparen', 'Visa/Mastercard',
                'Völlig kostenlos', 'Von Zuhause arbeiten',
                '100% unentgeltlich', 'Vergütung', 'Geschenk', 'Rückzahlung', 'gebührenfrei',
                'kostenlos anmelden', 'gratis testen', 'Gewinn',
                'garantiert', '100% sicher', 'zertifiziert', 'risikofrei', 'Angebot', 'Bonus',
                'Schnäppchen', 'gesehen im TV', 'Deal', 'es funktioniert', 'keine Abzocke',
                'kein Spam', 'keine versteckten Kosten', 'Passwort', 'persönliche Angaben',
                'machen Sie schnell', 'sofort', 'jetzt profitieren', 'limitiertes Angebot', 'Ab jetzt', 'nur heute',
                'zögern Sie nicht', 'greifen Sie zu', 'läuft bald ab',
                'Sie haben gewonnen', 'Bravo', 'klicken', 'um Ihr Geschenk zu erhalten', 'außergewöhnliches Geschenk',
                'gewinnen', 'Sie wurden ausgewählt', 'Glückwunsch', 'Belohnung',
                'Gewicht verlieren', 'schnell abnehmen', 'zu viele Kilos', 'wie abnehmen', 'Diät', 'Verjüngung',
                'Schonkost', 'Erektion', 'Falten', 'Schnarchen', 'Altern', 'Glatze', 'ohne Aufwand', 'Ausdauer',
                'Abnehmen über Nacht', 'Besser im Bett werden', 'Cellulite weg in XXX', 'Drogen legal kaufen',
                'Falten entfernen', 'Glatze weg', 'Gras günstig kaufen', 'Günstige Medikamente',
                'Haarausfall behandeln', 'Leicht abnehmen', 'Prognose', 'Schnarchen behandeln',
                'Schnell Gewicht verlieren', 'Sixpack über Nacht', 'Sofort Gewicht verlieren', 'Kilos verlieren',
                'Therapie', 'Valium',
                'Viagra', 'Weed günstig kaufen', 'Wunderheilung',
                'Abverkauf', 'Alles muss raus', 'Angebot endet heute', 'Angebot läuft „x“ ab', 'Ausverkauf',
                'Begrenzte Zeit', 'Chance nicht verpassen', 'Countdown läuft', 'Discount',
                'Eilig', 'Greifen Sie zu', 'Jetzt kaufen', 'Jetzt sichern', 'Jetzt zugreifen', 'Jetzt zuschlagen',
                'Kaufen, kaufen, kaufen', 'Kräftige Rabatte', 'Limitiertes Angebot',
                'Nur heute verfügbar', 'Nur solange der Vorrat reicht', 'Preissensation', 'Preisknüller', 'Schnäppchen',
                'Special Deal', 'Sonderangebot', 'Attraktiv', 'Date', 'Exklusives Kennenlernen', 'Fetisch',
                'Freunde finden', 'Heiße Männer/Frauen', 'Lieber Freund', 'Nicht mehr allein sein',
                'Nicht mehr einsam sein', 'Nude', 'Partner finden', 'Partnerschaftsanfrage', 'Sex', 'Sexy',
                'Sexy Männer/Frauen', 'Singles kennenlernen', 'Traummann/Traumfrau', 'Treffen', 'Völlig harmlos',
                'Völlig unverbindliches Treffen', 'Achtung!', 'Bitte helfen Sie mir', 'Dies ist kein Spam', 'Dringend',
                'Endlich online', 'Freier Zugang', 'Für Sie', 'Hier klicken', 'Ihre angeforderten Informationen',
                'Jetzt anrufen', 'Jetzt handeln', 'Jetzt öffnen', 'Jobangebot', 'Kostenlose Info',
                'Neue Herausforderungen', 'Nicht löschen', 'Profis', 'Sehen Sie sich dies an', 'STOP', 'Vergleichen',
                'Werden Sie Ihr eigener Chef', 'Wie im Fernsehen gesehen', 'Wir haben eine Stelle für Sie', 'XXX'

                ]

for i in range(len(spamWordList)):
    tmp_string = ''.join(spamWordList[i])

    if tmp_string.islower():
        print(spamWordList[i])

counter = 0
word_list = []

with open('MessagesPD.csv', encoding='UTF8') as f:
    contents = f.read()
    for i in range(len(spamWordList)):
        tmp_word = spamWordList[i]
        # count = contents.count(list[i].lower)
        count = contents.count(tmp_word)
        print(spamWordList[i], count)
        if count != 0:
            word_list.append(spamWordList[i])
            word_list.append(count)

with open('SpamWordHits.csv', mode='w', encoding='UTF8', newline='') as out_file:
    header = ['SpamWords', 'Hits']
    writer = csv.writer(out_file)
    writer.writerow(header)  # write the header rows
    tmp_length = int(len(word_list) / 2)
    for i in range(0, tmp_length):
        writer.writerow([word_list[(i * 2)], word_list[(i * 2) + 1]])