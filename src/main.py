from sys import argv
from database import create_table, add_record, display_records, export_database


def main():
    create_table()
    action = argv[1]
    match action:
        case "add":
            record_name, record_value, record_type = argv[2:5]
            add_record(record_name, record_value, record_type)
        case "see":
            print(display_records())
        case "export":
            file_name = argv[2]
            export_database(file_name)


if __name__ == "__main__":
    main()
