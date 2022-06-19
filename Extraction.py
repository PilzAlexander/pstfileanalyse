import pypff
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pst = pypff.file()
pst.open("C:\\Users\\Alexp\\PycharmProjects\\pstfileanalyse\\PSTFiles\\LRKO.pst")

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
                "text": message.plain_text_body
            })
    print(countEmails)
    return messages


messages = parse_folder(root)

df = pd.DataFrame(messages)
df.to_csv('MessagesPD.csv', index=False)

df['datetime'] = df['datetime'].dt.tz_localize(tz='UTC')
df['datetime'] = df['datetime'].dt.tz_convert(tz='Europe/Paris')

df['hour'] = df['datetime'].dt.hour + df['datetime'].dt.minute / 60
df['date'] = df['datetime'].dt.year + df['datetime'].dt.dayofyear / 365

plt.clf()
ax = sns.scatterplot(x="date", y="hour", s=10, alpha=.3, linewidth=0, marker=".", data=df)
ax.set(xlim=(2020, 2022.5), ylim=(1, 24))
ax.invert_yaxis()
sns.despine()
ax.get_figure().savefig("plot.png", dpi=1200)
