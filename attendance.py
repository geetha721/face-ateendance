import csv
from datetime import datetime
import os

folder_path = "attendance"
file_path = os.path.join(folder_path, "attendance.csv")

def mark_attendance(name):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")

    file_exists = os.path.isfile(file_path)

    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "Date", "Time"])
        writer.writerow([name, date, time])


