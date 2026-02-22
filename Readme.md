# ETL Project (Python)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Tests](https://img.shields.io/badge/tests-pytest-blue)
![Coverage](https://img.shields.io/badge/coverage-81%25-green)
![pandas](https://img.shields.io/badge/pandas-3.0.0-purple)


Simple CLI ETL (Extract, Transform, Load) application written in Python.
The program allows loading data from CSV or Excel files, performing basic cleaning, and saving the result to CSV, Excel, or JSON.

## Features

### Extract data from:
- CSV files
- Excel files (.xls, .xlsx)

### Transform data:

- remove missing values
- remove duplicates

### Load data to:

- CSV
- Excel
- JSON
- Interactive CLI menu

### Project structure

```
etl_project/
│
├── main.py
├── extract.py
├── transform.py
├── load.py
├── logo.py
├── requirements.txt
│
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   ├── test_load.py
│   ├── test_main.py
│   └── test_logo.py
│
└── README.md
```
## Instalaltion

Clone the repository:

https://github.com/AlexArciszewski/001_etl_project.git

```
git clone https://github.com/AlexArciszewski/001_etl_project.git
cd etl_project
```

Create virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Dependencies installation:

```
pip install -r requirements.txt
```


## How to run

Run the program:

python main.py

Follow the menu instructions in the terminal.

## Example workflow

- Choose Extract Data
- Provide file path
- Transform data
- Save data to selected format

## Technologies used

- Python
- pandas
- openpyxl
- colorama

## Tests

This project includes unit tests written with pytest to ensure correctness and reliability of the ETL pipeline.

Tests cover:

- data extraction
- data transformation
- data loading
- CLI behavior
- edge cases and error handling

Run tests with coverage report:

```
pytest --cov=. --cov-report=term
```

## Purpose

This project was created as a learning exercise to practice:

- ETL pipeline design
- Python modular structure
- pandas data processing
- CLI application development