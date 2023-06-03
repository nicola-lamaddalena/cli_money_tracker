# CLI money tracker app

The CLI app saves in a database new expenses or displays the old ones.

Actions:

    add: inserts the expense into the database. It needs 3 other inputs:
        type of the record: str - "in" for income and "out" for expense;
        name of the record: str
        value of the record: int | float - every value will be casted into float
    
    see: displays the expenses present into the database. It can accept 2 other input:
        filter + name: 
            day + number of the day: str + int
            month + number of the month: str + int
            month + name of the month: str + str - it accepts the whole name of the month or the first 3 letters
            year + number of the year: str + int
        if no inputs are supplied it will display the 20 most recent records.
        
    export: exports the database to a csv file. It needs a name for the csv file as second input:
        name of the csv file: str

Example: python main.py add in tv 599
Example: python main.py see month feb
Example: python main.py export nuovoFile
