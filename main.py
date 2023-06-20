import pandas as pd
from get_notifications_messages import get_notification_and_messages
from user_logins import decrypt_data, get_key
from send_mail import send_proactive_email
from export_data import write_to_csv
from datetime import datetime
import os
from user_logins import add_user
import time
def search_for_last(export_file_path , email_id):
        
    df = pd.read_csv(export_file_path)
    last_entries = df.groupby('email').last()

    # print(last_entries)
    df = last_entries.reset_index()

    try:
        number_of_last_messages = df[df['email'] == email_id].values[0][2]
    except:
        number_of_last_messages = 0
    try:
        number_of_last_notifications = df[df['email'] == email_id].values[0][3]
    except:
        number_of_last_notifications = 0


    # print(" last msgs, notif : ",number_of_last_messages , number_of_last_notifications)
    return  number_of_last_messages , number_of_last_notifications 
def get_data():
    df = pd.read_csv('userdata.csv', header =None)
    # print()
    df.columns = ['email' , 'pass']

    for index in range(len(df)):
        
        row = df.iloc[index]
        # Access row data using row[column_name]
        email_id = row['email']
        password = row['pass']
        k = get_key()
        # print( email_id, decrypt_data(k, password))
        notifications,messages = get_notification_and_messages(email_id , decrypt_data(k, password) ) 
        send_proactive_email(notifications, messages , [email_id])
        current_datetime = datetime.now()
        
        export_file_path = "notification_data.csv"
        if os.path.exists(export_file_path):
            file_exists = True
            last_messages,last_notification = search_for_last(export_file_path, email_id)
        
        inc_msgs = (int(messages) - last_messages) / 100
        inc_notifs = (int(notifications) - last_notification) / 100
        write_to_csv(export_file_path, [email_id, current_datetime, messages, notifications,inc_msgs,inc_notifs])

        print('Succesfully written to CSV')


number_of_users = int(input("Enter Number of new users : "))
for i in range( number_of_users):
    add_user()

def repeat_code():
    get_data()

interval = 3 * 60 * 60
while True:
    repeat_code()
    time.sleep(interval)