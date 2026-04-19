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
<img width="1828" height="907" alt="Image" src="https://github.com/user-attachments/assets/efce9c8b-7a0e-4b18-8013-2dbc6bd8f973" />
<img width="1479" height="951" alt="Image" src="https://github.com/user-attachments/assets/bb30775b-d2bd-4252-b250-c90cf83d3212" />
<img width="1504" height="947" alt="Image" src="https://github.com/user-attachments/assets/a3f8a960-7a5e-4058-bb7b-8532611bfd2a" />
<img width="1481" height="961" alt="Image" src="https://github.com/user-attachments/assets/92fe25e0-e03d-4c04-a1b2-e458faebc77f" />
<img width="1483" height="958" alt="Image" src="https://github.com/user-attachments/assets/e23ef1a6-9a63-450b-a6d0-46480cae8b2f" />
<img width="1476" height="912" alt="Image" src="https://github.com/user-attachments/assets/555e6957-6a95-41e5-b9c3-3484a8fcf029" />

## 🚀 Conclusion
This task helped in understanding the dataset structure, handling missing values, and performing basic exploratory data analysis. It forms the foundation for further data science tasks like modeling and prediction.
