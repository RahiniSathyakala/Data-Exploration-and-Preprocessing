# 📊 Data Exploration & Preprocessing on Restaurant Dataset

## 📌 Overview
This project focuses on exploring and preprocessing a restaurant dataset to understand its structure, clean the data, and analyze the distribution of key variables.

## 🎯 Objective
- Understand dataset structure and features  
- Handle missing values  
- Analyze the target variable (Aggregate Rating)  
- Visualize data distribution  

## 🛠️ Tools & Technologies
- Python  
- Pandas  
- Matplotlib  

## 📂 Dataset Information
- Total Rows: 9551  
- Total Columns: 21  
- Contains features like:
  - Restaurant Name  
  - Location (City, Country Code)  
  - Cuisines  
  - Price Range  
  - Aggregate Rating  
  - Votes  

## 🔍 Steps Performed

### 1. Data Loading
- Loaded dataset using Pandas  

### 2. Data Inspection
- Viewed first 5 rows  
- Checked dataset shape  
- Used `.info()` to understand structure  

### 3. Missing Value Handling
- Identified missing values  
- Removed rows with missing data using `dropna()`  

### 4. Data Type Analysis
- Verified column data types  

### 5. Target Variable Analysis
- Analyzed **Aggregate Rating**  
- Calculated statistics:
  - Mean: ~2.66  
  - Max: 4.9  
  - Min: 0  

### 6. Visualization
- Created histogram for Aggregate Ratings  

## 📊 Key Insights
- Most ratings fall between **3.0 – 4.0**  
- A significant number of entries have **0 rating**  
- Dataset is clean after removing missing values  

## 📷 Output
(Add your histogram screenshot here)

## 🚀 Conclusion
This task helped in understanding the dataset structure, handling missing values, and performing basic exploratory data analysis. It forms the foundation for further data science tasks like modeling and prediction.
