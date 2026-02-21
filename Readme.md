# ETL Project (Python)

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
├── main.py # application entry point
├── extract.py # data extraction
├── transform.py # data transformation
├── load.py # saving data
├── logo.py # CLI logo
├── requirements.txt
└── README.md
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

## Purpose

This project was created as a learning exercise to practice:

- ETL pipeline design
- Python modular structure
- pandas data processing
- CLI application development