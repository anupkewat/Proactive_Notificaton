import csv
import os
def write_to_csv(file_path, data):
    file_exists = False
    if os.path.exists(file_path):
        file_exists = True

    with open(file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if not file_exists:
            # when new , add column names
            writer.writerow(['email', 'date_time', 'messages','notification','message_comparison','notification_comparison'])  
        writer.writerow(data)

# Example usage
# csv_file_path = "data.csv"
# data = ['Value1', 'Value2', 'Value3']
# write_to_csv(csv_file_path, data)