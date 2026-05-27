# Task 2: Data Cleaning and Preprocessing

## Objective
The objective of this task is to learn the basics of data cleaning and preprocessing using Python libraries such as Pandas and NumPy. The dataset was cleaned and prepared for further analysis by handling missing values, removing duplicates, normalizing numerical features, and addressing outliers.

## Dataset Information
- Dataset Name: Student Performance Dataset (Portuguese Language)
- Source: UCI Machine Learning Repository
- File Format: CSV
- Number of Records: 649
- Number of Features: 33

## Tools Used
- Python
- Pandas
- NumPy

## Data Cleaning Steps Performed

### 1. Missing Value Handling
- Checked the dataset for missing values.
- Filled missing numerical values using the median.
- Filled missing categorical values using the mode.

### 2. Duplicate Removal
- Identified duplicate records.
- Removed duplicate rows from the dataset.

### 3. Feature Encoding
- Converted categorical features into numerical format using one-hot encoding.

### 4. Normalization
- Applied Min-Max Normalization to numerical features such as:
  - Age
  - Absences
  - G1
  - G2
  - G3

### 5. Outlier Handling
- Detected outliers using the Interquartile Range (IQR) method.
- Removed records containing extreme outlier values.

## Output
The cleaned and preprocessed dataset was saved as:

clean_student_performance.csv

## Files Included
- student-por.csv (Original Dataset)
- clean_student_performance.csv (Cleaned Dataset)
- task2_preprocessing.py (Python Code)
- README.md

## Learning Outcome
Through this task, I learned:
- How to inspect and clean raw data.
- How to handle missing values and duplicates.
- How to normalize numerical features.
- How to identify and remove outliers.
- Basic data preprocessing techniques used in data analytics projects.
