from sys import argv
import pandas as pd
import models.connector, models.record


def add() -> tuple[str, str, float]:
    record_name = input("Insert a name for the record: ").title().strip()
    record_type = (
        input("Insert a type for the record (in | out). Default is out: ")
        .strip()
        .lower()
    )
    try:
        record_value = float(
            input("Insert a numeric value for the record (int | float): ")
        )
        return record_name, record_type, record_value
    except ValueError:
        print("Insert numeric value (int | float).")


def see() -> tuple[str, int]:
    time_step = input("Insert a time step (month | year). Default is year: ")
    if time_step not in ["month", "year"]:
        time_step = "year"
        print("Using year as time step.\n")
    try:
        time_filter = int(
            input(
                "Insert a time filter (int: Example: 2023 for the year or 12 for the month.): "
            )
        )
        return time_step, time_filter
    except ValueError:
        print("Insert a numeric value for the time filter (int)")


def main() -> None:
    db_name = "newDb.db"
    connector = models.connector.Connector(db_name=db_name)
    action = argv[1]
    match action:
        case "add":
            record_name, record_type, record_value = add()
            record = models.record.Record(
                name=record_name, value=record_value, type=record_type
            )
            connector.add(record=record)
        case "see":
            try:
                step, filter = see()
                records = pd.DataFrame(
                    connector.display(step=step, filter=filter),
                    columns=[
                        "RecordId",
                        "RecordName",
                        "RecordValue",
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
                connector.export(file_name)
            except IndexError:
                print(
                    "Error: No name for the CSV file.\nThe second argument cannot be empty."
                )


if __name__ == "__main__":
    main()
