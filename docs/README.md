# Yelp_Data ETL and Analysis

## Overview:

This project focuses on extracting, transforming, and loading (ETL) Yelp data for analysis. The data is downloaded and connected to the PGAdmin4 using a Python script that follows the ETL pipeline. The pipeline involves processing raw data, creating dimension and fact tables, and conducting analysis for valuable insights.

### Folder Structure:

The project directory is structured as follows:

- data

  |- [all the json files]
  
- docs 

  |- [all the extra documents and the md files]
  
- dwh 

  |- [contains all the execution for loading the data into the dimension and fact tables]
  
- raw 

  |- [contains the create files for the execution of the raw tables]
  
- src 

  |- [contains all the related files for running the complete pipeline for the raw table]
  
- gitignore

  |- [keeping all the extra modules and libraries as well as the venvs]
  
- main.py 

  |- [runs the execution for the raw pipeline]
  
- mig.py

  |- [runs the complete execution for the std pipeline]


------------------------
### Problems Faced:

- Large Data Size: Loading the data into the raw tables took around 3 hours due to the large volume of data. This led to slow execution times for the entire system.

- System Limitations: Creating separate lookup tables was not feasible due to system limitations caused by the large data volume.

---------------------
### Steps Taken:

- Raw Data Processing: Initially, the focus was on creating and loading the raw tables, which acted as the OLAP (Online Analytical Processing) layer. All the data was stored in this layer.

- Dimension and Fact Tables: After loading the raw data, worked on identifying the dimension and fact tables required for analysis.

- Selective Cleaning: To tackle the challenge of dealing with the large dataset, I decided to focus on cleaning and loading only the essential attributes and data into the dimension tables. These dimension tables were then treated as standard tables for analysis.


### Functions

*def execute_sql_file(cursor, sql_file_path)*

```This function executes the SQL commands stored in a SQL file. It takes in a database cursor and the path to the SQL file as inputs.``` 
```The function reads the SQL file, parses the commands, and executes the files present in the directory sequentially using the provided cursor.```

*def create_tables(connection, tables_sql_directory)*

``` The create_tables function is responsible for creating database tables based on the SQL scripts stored in the tables_sql_directory.``` 
 ```It takes a database connection and the path to the directory containing the SQL scripts for table creation as input. The function reads each SQL file in the directory and executes the commands to create the tables in the database. ```

*def insert_json_data(connection, json_file_path, table_name)*

``` This function inserts JSON data from the data folder that contains the specified file into a corresponding database table. It takes a database connection, the path to the JSON file containing the data, and the target table name as inputs.```
``` The function reads the JSON data, processes it, and inserts it into the specified table in the database. ```

*def insert_data(connection, directory_path)*

``` The insert_data function is used to insert data from multiple JSON files in a directory into their respective tables in the database. It takes a database connection and the path to the directory containing JSON files as input.``` 
```The function iterates through each JSON file, determines the corresponding table, and inserts the data into the database. ```


****************************************************************************************************************************************************
**Analysis and Results**:

-- The queries are inside the:
  
- docs 
  
  |- [analysis]

*These analysis provide valuable insights into business performance, customer behavior, and popular trends in the Yelp dataset.*

1. **Highest Rating Businesses:** Retrieves the top 5 businesses with the highest ratings.

2. **Top 10 Reviewers:** Retrieves the top 10 users who have given the most reviews, ordered by the number of reviews and their average rating.

3. **Repeated Customers:** Identifies users who have given more than one review, along with the number of reviews they've submitted.

4. **Business Success and Impact:** Presents business information along with the number of reviews and average rating by repeat customers, highlighting the impact of repeated reviews on business success.

5. **Busiest Business Categories:** Lists business categories along with the total number of check-ins, ordered by the highest check-ins.

6. **Average Check-ins per Business:** Calculates the average check-ins per business by dividing the total check-ins by the number of distinct dates.

7. **Peak Check-in Hour:** Identifies the peak check-in hour for each business based on the number of check-ins on a specific date.

8. **Peak Check-in Time:** Identifies the specific date and time with the highest check-ins among all businesses.

9. **Peak Time for Each Business:** Lists the peak check-in time for each business, showing the time with the highest check-ins.

10. **Peak Time for Top 5 Businesses:** Lists the peak check-in time for the top 5 businesses based on the highest check-ins.

-----------------------
## Visualization

And, the visualization has been done using **Power BI**

*In this project, we present visualizations to gain valuable insights from the Yelp data analysis.*

**Average Rate of Businesses:** Visualizing the average rating of businesses to understand the overall satisfaction level of customers.

**Top 5 Business Ratings by Name:** Displaying the ratings of the top 5 businesses, along with their names, to identify the highest-rated businesses.

**Average Rating by Review Count:** Plotting the average rating given by users based on their review counts to see if there's any correlation between frequent reviewers and their rating trends.

**Top 5 Businesses with the Most Useful Votes:** Visualizing the businesses that receive the highest number of useful votes to identify highly influential and helpful businesses.

**Top 10 Users by Review Count:** Creating a bar chart or table to showcase the top 10 users who have contributed the most reviews to the platform.

**Average Rating by Business ID and State:** Using a geographical visualization using choropleth map, to visualize the average ratings of businesses based on their IDs and states.

**Number of Repeated Users:** Displaying the count of users who have given more than one review, illustrating the level of customer loyalty and engagement.

**Total Number of Useful, Funny, and Cool Votes:** Visualizing the total counts of useful, funny, and cool votes given by users to understand the engagement and sentiment around reviews.


### Metrics and KPIs:

**Metrics:** The metrics that had been visualized are average rating, review count, useful votes count, and counts of funny and cool votes.

**KPIs:** Key performance indicators in this context would be identifying the top-rated businesses, top reviewers, businesses with the most useful votes, and understanding the level of user engagement and loyalty based on the number of reviews contributed by repeated users.

***********************************************************************************************************************************************

**How to Run the Pipeline**

1. Ensure you have Python and the required libraries installed.

2. Run **main.py** to execute the raw data pipeline, loading the data into the raw tables.

3. Run **mig.py** to execute the standard pipeline, which processes and loads data into the dimension and fact tables.

----------------------
**Document Link**:

[All the screenshots of the analysis are kept here ](https://docs.google.com/document/d/1USr7yQkzmcx9m8-XWBUvIq5u_f-7jXAThRHSrcOw5h0/edit?usp=sharing)












