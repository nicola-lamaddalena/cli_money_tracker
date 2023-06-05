from sys import argv
from database import create_table, add_record, display_records, export_database


def add():
    record_name = input("Insert a name for the record: ")
    record_value = float(input("Insert a value for the record (int or float): "))
    record_type = input("Insert a type for the record (in/out): ")
    return record_name, record_value, record_type


def see():
    time_step = input("Insert a time step (month/year): ")
    time_filter = input("Insert a time filter (int): ")
    return time_step, time_filter


def export():
    file_name = input("Insert a name for the CSV file: ")
    return file_name


def main():
    create_table()
    action = argv[1]
    match action:
        case "add":
            record_name, record_value, record_type = add()
            add_record(record_name, record_value, record_type)
        case "see":
            time_step, time_filter = see()
            records = display_records((time_step, time_filter))
            for record in records:
                print(record)
        case "export":
            file_name = export()
            export_database(file_name)


if __name__ == "__main__":
    main()
