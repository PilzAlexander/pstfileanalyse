import csv
import datetime
import pypff
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pst = pypff.file()
# pst.open("C:\\Users\\Alexp\\PycharmProjects\\pstfileanalyse\\PSTFiles\\LRKO.pst")
# pst.open("C:\\Users\\Alexp\\PycharmProjects\\pstfileanalyse\\PSTFiles\\MergedPstAPW_backupA.pst")
pst.open("C:\\Users\\Alexp\\PycharmProjects\\pstfileanalyse\\PSTFiles\\BigMerge.pst")

root = pst.get_root_folder()


def parse_folder(base):
    messages = []
    countEmails = 0
    for folder in base.sub_folders:
        if folder.number_of_sub_folders:
            messages += parse_folder(folder)
        print(folder.name)
        for message in folder.sub_messages:
            countEmails += 1
            messages.append({
                "subject": message.subject,
                "sender": message.sender_name,
                "datetime": message.client_submit_time,
                "text": message.plain_text_body,
                "attachments": message.number_of_attachments
            })
    print(countEmails)
    return messages


def get_total_number_of_emails(messages):
    count = 0
    for message in messages:
        count += 1
    return count

def get_weekday_count(messages):
    count = [0, 0, 0, 0, 0, 0, 0]
    for message in messages:
        if message["datetime"].weekday() == 0:
            count[0] += 1
        elif message["datetime"].weekday() == 1:
            count[1] += 1
        elif message["datetime"].weekday() == 2:
            count[2] += 1
        elif message["datetime"].weekday() == 3:
            count[3] += 1
        elif message["datetime"].weekday() == 4:
            count[4] += 1
        elif message["datetime"].weekday() == 5:
            count[5] += 1
        elif message["datetime"].weekday() == 6:
            count[6] += 1
    return count


def plot_weekdays_from_list(weekdays):
    plt.bar(range(len(weekdays)), weekdays)
    plt.xticks(range(len(weekdays)), ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.show()

messages = parse_folder(root)
get_weekday_count(messages)
weekdays = get_weekday_count(messages)
plot_weekdays_from_list(weekdays)

totalnumber = get_total_number_of_emails(messages)
print(totalnumber)

df = pd.DataFrame(messages)


df.to_csv('MessagesPD.csv', index=False)

df['datetime'] = df['datetime'].dt.tz_localize(tz='UTC')
df['datetime'] = df['datetime'].dt.tz_convert(tz='Europe/Paris')

df['hour'] = df['datetime'].dt.hour + df['datetime'].dt.minute / 60
df['date'] = df['datetime'].dt.year + df['datetime'].dt.dayofyear / 365

plt.clf()
ax = sns.scatterplot(x="date", y="hour", s=10, alpha=.3, linewidth=0, marker=".", data=df)
ax.set(xlim=(2022, 2022.5), ylim=(1, 24))
ax.invert_yaxis()
sns.despine()
ax.get_figure().savefig("plot.png", dpi=1200)


