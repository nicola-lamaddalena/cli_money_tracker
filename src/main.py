from sys import argv
from database import create_table, add_record, display_records, export_database
import pandas as pd


def add():
    record_name = input("Insert a name for the record: ").capitalize().strip()
    record_type = input("Insert a type for the record (in/out): ").strip().lower()
    try:
        record_value = float(
            input("Insert a numeric value for the record (int or float): ")
        )
        return record_name, record_value, record_type
    except ValueError:
        print("Insert numeric value (int or float).")


def see():
    time_step = input("Insert a time step (month/year): ")
    if time_step not in ["month", "year"]:
        time_step = "year"
        print("Using year as time step.\n")
    try:
        time_filter = int(input("Insert a time filter (int | float): "))
        return time_step, time_filter
    except ValueError:
        print("Insert a numeric value for the time filter (int | float)")


def main():
    create_table()
    action = argv[1]
    match action:
        case "add":
            record_name, record_value, record_type = add()
            add_record(record_name, record_value, record_type)
        case "see":
            try:
                time_step, time_filter = see()
                records = pd.DataFrame(
                    display_records(time_step, time_filter),
                    columns=[
                        "RecordId",
                        "RecordName",
                        "RecordValue",
                        "RecordType",
                        "RecordDay",
                        "RecordMonth",
                        "RecordYear",
                    ],
                )
                records.set_index("RecordId", inplace=True)
                print(records)
            except TypeError:
                print("Error: Check your inputs.")
        case "export":
            try:
                file_name = argv[2]
                export_database(file_name)
            except IndexError:
                print(
                    "Error: No name for the CSV file.\nThe second argument cannot be empty."
                )


if __name__ == "__main__":
    main()
