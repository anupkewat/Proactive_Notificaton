import pandas as pd
# df = pd.read_csv('notification_data.csv')
# last_entries = df.groupby('email').last()
# df = last_entries.reset_index()
# number_of_last_messages = df[df['email'] == 'svsmart2@gmail.com'].values[0][2]
# number_of_last_notifications = df[df['email'] == 'svsmart2@gmail.com'].values[0][3]
# print( number_of_last_messages , number_of_last_notifications)



# print(last_entries)
# print( df.groupby('email'))
# print( df)

df = pd.read_csv('notification_data.csv')
last_entries = df.groupby('email').last()

# print(last_entries)
df = last_entries.reset_index()

try:
    number_of_last_messages = df[df['email'] == 'svsmart4@gmail.com'].values[0][2]
except:
    number_of_last_messages = 0
try:
    number_of_last_notifications = df[df['email'] == 'svsmart4@gmail.com'].values[0][3]
except:
    number_of_last_notifications =0


# print(" last msgs, notif : ",number_of_last_messages , number_of_last_notifications)
print( number_of_last_messages , number_of_last_notifications)