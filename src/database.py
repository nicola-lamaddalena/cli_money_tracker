import csv
import os
import os.path
import sqlite3
from datetime import datetime


db_name = "expenseTracker.db"

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
            day integer not null,
            month integer not null,
            year integer not null
        );
        """
    )


def add_record(name: str, value: int | float, type: str):
    cursor.execute(
        """
        insert or ignore into expenses(name, value, type, day, month, year)
        values (?,?,?,?,?,?);
        """,
        (
            name,
            value,
            type,
            datetime.now().day,
            datetime.now().month,
            datetime.now().year,
        ),
    )
    conn.commit()


def display_records(time_step: int = None, month_or_year: str = None):
    match month_or_year:
        case "month":
            cursor.execute(
                """
                select * 
                from expenses
                where month = ?
                limit 20
                """,
                (time_step,),
            )
            return cursor.fetchall()

        case "year":
            cursor.execute(
                """
                select * 
                from expenses
                where year = ?
                limit 20
                """,
                (time_step,),
            )
            return cursor.fetchall()

        case None:
            cursor.execute(
                """
                select *
                from expenses
                limit 20
                """
            )
            return cursor.fetchall()


def export_database(file_name: str):
    dir = "../exportFiles"
    if not os.path.exists(dir):
        os.mkdir(dir)

    records = display_records()
    file_name += ".csv"
    with open(os.path.join(dir, file_name), "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(
            [
                "RecordId",
                "RecordName",
                "RecordValue",
                "RecordType",
                "RecordDay",
                "RecordMonth",
                "RecordYear",
            ]
        )
        for row in records:
            csv_writer.writerow(row)
