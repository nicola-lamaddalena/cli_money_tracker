import sqlite3
from datetime import datetime
from .record import Record
from csv import writer
from os import mkdir
import os.path


class Connector:
    def __init__(self, db_name: str):
        self.db_dir = r"../dbFiles"
        if not os.path.exists(self.db_dir):
            mkdir(self.db_dir)
        self.db_name = db_name
        self.conn = sqlite3.connect(os.path.join(self.db_dir, db_name))
        self.cursor = self.conn.cursor()
        self.create_table()

    def __str__(self) -> str:
        return self.db_name

    def create_table(self):
        self.cursor.execute(
            """
            create table if not exists expenses (
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
        self.conn.commit()

    def add(self, record: Record):
        self.cursor.execute(
            """
            insert or ignore into expenses(
                name, value, type, day, month, year
            )
            values (?,?,?,?,?,?);
            """,
            (
                record.name,
                record.value,
                record.type,
                datetime.now().day,
                datetime.now().month,
                datetime.now().year,
            ),
        )
        self.conn.commit()

    def display(self, step: str = None, filter: str = None) -> list[str]:
        match step:
            case "month":
                self.cursor.execute(
                    """
                    select *
                    from expenses
                    where month = ?
                    """,
                    (filter,),
                )
                return self.cursor.fetchall()
            case "year":
                self.cursor.execute(
                    """
                    select *
                    from expenses
                    where year = ?
                    """,
                    (filter,),
                )
                return self.cursor.fetchall()
            case None:
                self.cursor.execute(
                    """
                    select *
                    from expenses
                    """
                )
                return self.cursor.fetchall()

    def export(self, file_name: str = "default"):
        csv_dir = r"../exportFiles"
        if not os.path.exists(csv_dir):
            mkdir(csv_dir)

        records = self.display()
        file_name += ".csv"
        with open(os.path.join(csv_dir, file_name), "w", newline="") as csv_file:
            csv_writer = writer(csv_file, delimiter=",")
            csv_writer.writerow(
                [
                    "Record Id",
                    "Record Name",
                    "Record Value",
                    "Record Type",
                    "Record Day",
                    "Record Month",
                    "Record Year",
                ]
            )

            for record in records:
                csv_writer.writerow(record)
