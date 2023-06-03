import csv
import sqlite3
from datetime import datetime

db_name = "expenseTracker.db"
# db_name = ":memory:"

conn = sqlite3.connect(db_name)
cursor = conn.cursor()


def create_table():
    cursor.execute(
        """
        create table if not exists expenses(
            id integer primary key autoincrement,
            name varchar(200) not null,
            value decimal not null,
            type varchar(5) not null,
            record_date datetime not null
        );
        """
    )


def add_record(name: str, value: int | float, type: str):
    cursor.execute(
        """
        insert or ignore into expenses(name, value, type, record_date)
        values (?,?,?,?);
        """,
        (
            name,
            value,
            type,
            datetime.now(),
        ),
    )
    conn.commit()


def display_records():
    cursor.execute(
        """
        select * from expenses
        """
    )
    return cursor.fetchall()


def export_database(file_name: str):
    records = display_records()
    file_name += ".csv"
    with open(file_name, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(
            ["RecordId", "RecordName", "RecordValue", "RecordType", "RecordDate"]
        )
        for row in records:
            csv_writer.writerow(row)
