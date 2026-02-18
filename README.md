# Data Analyst Intern Assignment

## Overview

This project contains the solution for the Data Analyst Intern
Assignment. The analysis includes data cleaning, funnel metrics
calculation, customer insights, and visualizations.

## Files Included

1.  Data_Analyst_Intern_Assignment_Solution.py
    -   Python script containing full cleaning, analysis, and
        visualization code.
2.  Data_Analyst_Intern_Assignment_Report_With_Visuals.pdf
    -   Final report including:
        -   Data cleaning steps
        -   Funnel metrics explanation
        -   Daily trend visualizations
        -   Revenue by acquisition channel chart
        -   Business insights

## Analysis Steps Performed

### 1. Data Cleaning

-   Converted date columns to datetime format.
-   Removed duplicate records.
-   Filtered only valid orders.
-   Ensured consistent ID formats for proper joins.

### 2. User Engagement → Purchase Funnel

-   Counted unique users with events.
-   Counted users with valid orders.
-   Calculated conversion rate.
-   Generated daily active users and ordering customers trends.

### 3. Customer Behavior Insight

-   Joined orders with customer data.
-   Analyzed revenue by acquisition channel.
-   Evaluated average order value by city.
-   Identified key revenue-driving segment.

## Assumptions

-   Only orders with status 'valid' were considered.
-   All datasets were assumed to be properly structured and complete.
-   Sample data may be used in report visuals if full dataset was
    unavailable.

## How to Run the Code

1.  Place datasets in the same folder as the Python script.
2.  Install required libraries:
    -   pandas
    -   matplotlib
    -   reportlab (for PDF generation)
3.  Run the Python script: python
    Data_Analyst_Intern_Assignment_Solution.py

## Author

Mehtab Alam

