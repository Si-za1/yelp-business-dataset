# Yelp Data ETL and Analysis

## Overview
This project focuses on extracting, transforming, and loading (ETL) Yelp data for analysis. The data is downloaded and connected to the PGAdmin4 using a Python script that follows the ETL pipeline. The pipeline involves processing raw data, creating dimension and fact tables, and conducting analysis for valuable insights.

## Folder Structure
The project directory is structured as follows:

- data
  - all the .json data files
- docs
  - analysis [all the queries are kept here]
  - all the extra files and .md files
- dwh
    - insert
        - all insert files for the std pipeline
    - tables
      - all create files for the raw pipeline
    - pipeline
      - extraction.py
      - load.py
- src
  - database
     - __init__.py
     - connection.py
  - pipeline
     - extraction.py
     - load.py
  - sql
     - all insert files for the raw pipeline
- .gitignore
- main.py
- mig.py

## Problems Faced
- **Large Data Size:** Loading the data into the raw tables took around 3 hours due to the large volume of data. This led to slow execution times for the entire system.
- **System Limitations:** Creating separate lookup tables was not feasible due to system limitations caused by the large data volume.

## Steps Taken
1. **Raw Data Processing:** Initially, the focus was on creating and loading the raw tables, which acted as the OLAP (Online Analytical Processing) layer. All the data was stored in this layer.
2. **Dimension and Fact Tables:** After loading the raw data, worked on identifying the dimension and fact tables required for analysis.
3. **Selective Cleaning:** To tackle the challenge of dealing with the large dataset, I decided to focus on cleaning and loading only the essential attributes and data into the dimension tables. These dimension tables were then treated as standard tables for analysis.

## Functions
- `execute_sql_file(cursor, sql_file_path)`: Executes the SQL commands stored in a SQL file using the provided database cursor.
- `create_tables(connection, tables_sql_directory)`: Creates database tables based on the SQL scripts stored in the specified directory.
- `insert_json_data(connection, json_file_path, table_name)`: Inserts JSON data from the data folder into the corresponding database table.
- `insert_data(connection, directory_path)`: Inserts data from multiple JSON files in a directory into their respective tables in the database.

## Analysis and Results
The analysis provides valuable insights into business performance, customer behavior, and popular trends in the Yelp dataset. The queries and results can be found in the `docs/analysis` directory.

## Visualization
The visualization has been done using Power BI to gain valuable insights from the Yelp data analysis.

## Metrics and KPIs
- Metrics: The metrics that had been visualized are average rating, review count, useful votes count, and counts of funny and cool votes.
- KPIs: Key performance indicators include identifying the top-rated businesses, top reviewers, businesses with the most useful votes, and understanding user engagement and loyalty based on the number of reviews contributed by repeated users.

## How to Run the Pipeline
1. Ensure you have Python and the required libraries installed.
2. Run `main.py` to execute the raw data pipeline, loading the data into the raw tables.
3. Run `mig.py` to execute the standard pipeline, which processes and loads data into the dimension and fact tables.

## Document Link
All the screenshots of the analysis are kept [here](link_to_documentation).
