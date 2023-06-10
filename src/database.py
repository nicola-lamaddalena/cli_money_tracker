from csv import writer
from os import mkdir
import os.path
import sqlite3
from datetime import datetime

db_name = "expenseTracker.db"
db_dir = "../dbFiles"

if not os.path.exists(db_dir):
    mkdir(db_dir)

conn = sqlite3.connect(os.path.join(db_dir, db_name))
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
    if name == "":
        name = "default"
    if type == "":
        type = "out"
    cursor.execute(
        """
        insert or ignore into expenses(name, value, type, day, month, year)
        values (?,?,?,?,?,?);
        """,
        (
            name,
            float(value),
            type,
            datetime.now().day,
            datetime.now().month,
            datetime.now().year,
        ),
    )
    conn.commit()


# todo: the function displays all the records, insert a limit argument
def display_records(time_step: str = None, time_filter: int = None):
    match time_step:
        case "month":
            cursor.execute(
                """
                select * 
                from expenses
                where month = ?
                """,
                (time_filter,),
            )
            return cursor.fetchall()
        case "year":
            cursor.execute(
                """
                select * 
                from expenses
                where year = ?
                """,
                (time_filter,),
            )
            return cursor.fetchall()

        case None:
            cursor.execute(
                """
                select *
                from expenses
                """,
            )
            return cursor.fetchall()


def export_database(file_name: str):
    dir = "../exportFiles"
    if not os.path.exists(dir):
        os.mkdir(dir)

    records = display_records()
    file_name += ".csv"
    with open(os.path.join(dir, file_name), "w", newline="") as csv_file:
        csv_writer = writer(csv_file, delimiter=",")
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
