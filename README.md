# OOP Data Processing

## Lab Overview
This lab demonstrates how to design and implement an Object-Oriented Programming (OOP) data processing system in Python. Refactoring earlier procedural data-processing logic into modular classes (`DataLoader`, `Table`, and `DB`), the program ingests relational CSV datasets (`Cities.csv` and `Countries.csv`), stores them inside an in-memory database, and performs SQL-like operations including inner joins, filtering, column selection, and statistical aggregation.

## Project Structure
```text
oop_lab_1/
│
├── README.md               # Project documentation (Lab Overview, Structure, Design, and Usage)
├── Cities.csv              # Dataset containing city names, countries, coordinates, and temperatures
├── Countries.csv           # Dataset containing country names, populations, EU status, and coastline info
└── data_processing.py      # Main Python script containing DataLoader, Table, DB classes, and test suite
```

## Design Overview

### 1. `DataLoader` Class
Handles locating CSV files on disk and converting them into Python data structures.
- **Attributes:**
  - `base_path` (`Path`): The directory path where dataset files are stored. Defaults to the directory containing `data_processing.py`.
- **Key Methods:**
  - `__init__(self, base_path=None)`: Initializes the `DataLoader` instance and resolves `base_path`.
  - `load_csv(self, filename)`: Reads the specified CSV file with UTF-8 encoding using `csv.DictReader` and returns a `list` of `dict` objects (each dictionary represents one row).

### 2. `Table` Class
Represents a structured relational table and provides methods to query, join, and aggregate data.
- **Attributes:**
  - `table_name` (`str`): The unique identifier name of the table (e.g., `'cities'`, `'countries'`).
  - `table` (`list[dict]`): A list of dictionaries representing the rows of the table.
- **Key Methods:**
  - `__init__(self, table_name, table)`: Initializes a `Table` object with its name and row data.
  - `join(self, other_table, common_key)`: Performs an inner join between the current table and `other_table` on matching values of `common_key` (e.g., `'country'`), returning a new combined `Table` named `<table1>_joins_<table2>` without mutating original rows.
  - `filter(self, condition)`: Filters rows using a boolean function (`condition`) and returns a new `Table` object named `<table_name>_filtered` containing only matching rows.
  - `aggregate(self, aggregation_function, aggregation_key)`: Extracts values from the column specified by `aggregation_key`, converts numeric strings to `float` (preserving strings for non-numeric columns), and applies `aggregation_function` (e.g., `sum`, `min`, `max`, `len`) to return a computed result.
  - `select(self, attributes_list)`: Projects specific columns listed in `attributes_list` and returns a `list` of dictionaries containing only those keys.
  - `__str__(self)`: Returns a formatted string displaying `table_name` and the table contents.

### 3. `DB` Class
Acts as a lightweight in-memory relational database managing multiple `Table` objects.
- **Attributes:**
  - `database` (`list[Table]`): A list storing inserted `Table` instances.
- **Key Methods:**
  - `__init__(self)`: Initializes an empty `database` list.
  - `insert(self, table)`: Adds a `Table` object into `self.database`.
  - `search(self, table_name)`: Searches `self.database` by `table_name` and returns the matching `Table` object, or `None` if not found.

## How to Test and Run Your Code
1. Ensure Python 3 is installed on your machine.
2. Verify that `Cities.csv`, `Countries.csv`, and `data_processing.py` are in the same directory.
3. Open a terminal, navigate to the project directory, and execute:
   ```bash
   cd path/to/oop_lab_1
   python data_processing.py
   ```
4. Confirm that all test cases run without errors and output the expected results for table searches, filtering, aggregations, and table joins.