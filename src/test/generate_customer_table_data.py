import random
from faker import Faker
from datetime import datetime
import csv

fake = Faker('en_IN')

file_location = r"D:\Training\PySpark\MK_Project\YT_Project_1\youtube_de_project1\spark_data\customers.csv"

with open(file_location, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "first_name",
        "last_name",
        "address",
        "pincode",
        "phone_number",
        "customer_joining_date"
    ])

    for _ in range(5000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = "Delhi"
        pincode = "122009"
        phone_number = "91" + "".join(str(random.randint(0,9)) for _ in range(10))
        joining_date = fake.date_between_dates(
            date_start=datetime(2020,1,1),
            date_end=datetime(2023,8,20)
        ).strftime('%Y-%m-%d')

        writer.writerow([
            first_name,
            last_name,
            address,
            pincode,
            phone_number,
            joining_date
        ])