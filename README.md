# CLI money tracker app

The CLI app can save new expenses, display the old ones or export the database table to a CSV file.

Actions:

    add: inserts a record into the database.
        type of the record: str - "in" for income and "out" for expense
        name of the record: str
        value of the record: int | float - every value will be casted into float

        The default name for the record is "default" (used when the input is empty); the default type for the record is out (used when the input is empty)

    see: displays the expenses present into the database. It can accept 2 other input:
            month + number of the month: str + int
            year + number of the year: str + int
        if no inputs are supplied it will display the 20 most recent records.
        
    export: exports the database to a csv file.
        name of the csv file: str

        If the file already exists it will be overwritten.
