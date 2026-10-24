#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Sample, Data Collection Procedure, and Measures

## Introduction

#For my research project, I used the **Healthcare Dataset** published by Prasad Patil on Kaggle. The dataset is a **synthetic healthcare dataset**, meaning that the records were artificially generated to resemble healthcare information rather than collected from actual patients. It contains **55,500 hospitalization records and 15 variables**, including patient demographics, medical conditions, admission and discharge information, billing amounts, medications, insurance providers, and test results.

#My primary research interest was examining whether characteristics such as **patient age** are related to **billing amount**, as well as whether this relationship varies across different patient groups.

## Sample

#The analytical sample consists of **55,500 synthetic patient hospitalization records**. Each row represents a simulated hospital admission record rather than necessarily a unique real-world individual.

#The dataset includes patients with ages ranging from approximately adolescence through older adulthood and includes both male and female records. The medical-condition categories represented in the dataset include **Arthritis, Asthma, Cancer, Diabetes, Hypertension, and Obesity**.

#Other characteristics represented in the sample include blood type, admission type, hospital, physician, insurance provider, medication, billing amount, dates of admission and discharge, and test results. The dataset therefore provides simulated examples of demographic, clinical, administrative, and financial healthcare information.

#Because this is a synthetic dataset, the records should not be interpreted as a probability sample of patients from a particular hospital, geographic area, or national population. Conclusions from my analyses describe patterns within this simulated dataset and should not automatically be generalized to actual patients.

## Data Collection Procedure

#Unlike a traditional health study in which investigators recruit participants, conduct interviews, review medical records, or collect clinical measurements, this dataset was **artificially generated to simulate healthcare records**.

#The dataset was developed for purposes such as data analysis, machine learning, and practicing healthcare analytics. Published descriptions of the dataset identify it as synthetic, and documentation associated with its use reports that artificial patient information was generated rather than obtained from identifiable patients. One description of the dataset reports the use of Python's **Faker** library to generate simulated healthcare records.

#Each synthetic record contains information such as age, gender, blood type, medical condition, date of admission, doctor, hospital, insurance provider, billing amount, room number, admission type, discharge date, medication, and test result.

#Therefore, there was no direct participant recruitment, survey administration, clinical examination, or extraction of identifiable real-patient medical records for this dataset. This is an important limitation when interpreting the results. The dataset is useful for practicing statistical methods, but its artificial construction means that relationships found in the data should not be interpreted as evidence of real-world clinical relationships.

## Measures

### Age

#**Age** is a quantitative variable representing patient age in years. I converted Age to numeric format and treated values below 0 or above 120 as invalid and missing.

#For some portions of the project, I also created an **Age Group** variable by categorizing age into the following groups:

#- 0–17 years
#- 18–34 years
#- 35–49 years
#- 50–64 years
#- 65 years and older

#Creating these categories allowed me to examine age using frequency distributions, graphs, and analysis of variance.

### Billing Amount

#**Billing Amount** is a quantitative variable representing the simulated amount billed for a hospitalization.

#I converted this variable to numeric form and treated billing values of zero or less as invalid for my analysis. These observations were coded as missing.

# Project Title

#**Relationship Between Patient Age and Healthcare Billing Amount in a Synthetic Healthcare Dataset**

## Step 1: Description of the Sample

### a. Study population

#The data used in this project come from a synthetic healthcare dataset designed to resemble hospital patient records. The records contain simulated information about patients, including age, gender, blood type, medical condition, hospital admission, billing amount, medication, and medical test results.

#Because the dataset is synthetic, the individuals represented in the data are not actual patients. The dataset was created to imitate the structure of healthcare information so that students and analysts can practice data management and statistical analysis without using confidential patient information.

### b. Level of analysis

#The level of analysis is the **individual hospitalization record**. Each row represents one simulated patient admission or healthcare encounter rather than an aggregate group such as a hospital, county, or state.

### c. Number of observations

#The complete dataset contains **55,500 observations** and 15 variables.

#The simulated patient ages range from **13 to 89 years**.

### d. Data analytic sample

#For my main analyses, I examined the relationship between **patient age** and **billing amount**.

#Age was treated as a quantitative explanatory variable, and billing amount was treated as a quantitative response variable. Records with valid values for both variables were retained for the correlation analysis. Billing amounts equal to or below zero were treated as invalid and coded as missing.

#This resulted in an analytic sample of **55,392 observations** for analyses involving age and valid billing amount.

#For other assignments, I also grouped age into categories, created a length-of-stay variable, examined medical condition and test results, and used gender as a potential moderator.

### URL

#https://www.kaggle.com/datasets/prasad22/healthcare-dataset

#**Paste your published blog-post URL here after you publish it.**

#### Title

#**Sample Description for the Healthcare Data Analysis Project**

### Caption

#This project analyzes 55,500 synthetic hospitalization records to examine relationships among patient characteristics, healthcare utilization, and billing amounts.

#---

# Step 2: Data Collection Procedures

### a. Study design

#The dataset was generated using a **synthetic data-generation design** rather than a survey, experiment, clinical trial, or observational study of actual patients.

#The data imitate the types of information normally found in healthcare and hospital records.

### b. Original purpose of the data

#The dataset was created to provide accessible healthcare-like data for **education, data analysis, machine learning, and experimentation**. Synthetic healthcare data are useful because real patient information is often difficult to access because of privacy and confidentiality requirements.

#Documentation describing this dataset indicates that simulated healthcare information was generated using Python's **Faker** library. The intention was to create records that resemble the structure of healthcare data while avoiding disclosure of real patient information.

### c. How the data were collected

#The data were not collected through interviews, questionnaires, physical examinations, or extraction of actual medical records.

#Instead, patient characteristics and healthcare information were **artificially generated by computer software**. The simulated records include information such as age, gender, medical condition, admission date, hospital, physician, insurance provider, billing amount, medication, discharge date, and test results.

#Therefore, it is more accurate to describe the process as **data generation rather than traditional data collection**.

### d. When the data were collected

#Because these are synthetic records, there was no actual period during which patients were recruited or observed.

#The simulated **dates of admission in the dataset range from May 8, 2019 through May 7, 2024**. These dates are part of the generated data and should not be interpreted as dates when real-world data collection occurred.

### e. Where the data were collected

#There was no real geographic data-collection site because the records were artificially generated.

#The dataset contains simulated hospital names and healthcare information, but these should not be interpreted as evidence that actual patients were studied at those locations.

#The dataset was made publicly available through **Kaggle**.

### URL

#https://www.kaggle.com/datasets/prasad22/healthcare-dataset
#Use the original dataset page as your source:

#**Kaggle – Healthcare Dataset by Prasad Patil**

#---

# Step 3: Description of the Variables

## Explanatory Variable: Patient Age

### a. What the variable measures

#Patient Age represents the simulated patient's age in years.

#In my primary research question, Age is the **explanatory variable** because I examined whether differences in patient age are associated with differences in billing amount.

### b. Response scale

#Age is a **quantitative numerical variable**, measured in years.

#The ages in the dataset range from **13 to 89 years**.

#For analyses requiring a categorical explanatory variable, I grouped Age into:

#- 0–17 years
#- 18–34 years
#- 35–49 years
#- 50–64 years
#- 65 years and older

### c. Data management

#I converted Age to numeric format to ensure that it could be analyzed statistically. I also established a valid age range of 0 through 120 years so that impossible values would be coded as missing.

#For the ANOVA and frequency-distribution assignments, I created the grouped age variable described above.

#For the correlation and moderation analyses, I retained Age as a continuous quantitative variable.

## Response Variable: Billing Amount

### a. What the variable measures

#Billing Amount represents the simulated monetary amount charged for a patient's hospitalization.

#It served as the **response variable** in my primary research question because I examined whether patient age was related to differences in billing amount.

### b. Response scale

#Billing Amount is a **continuous quantitative variable measured in dollars**.

#For analyses requiring categories, I grouped billing amount into:

#- Less than $10,000
#- $10,000–$24,999
#- $25,000–$39,999
#- $40,000 or more

### c. Data management

#I converted Billing Amount to numeric format.

#I identified **108 records with billing amounts equal to or below zero**. Because these values were not considered meaningful positive healthcare charges for my analysis, I coded them as missing.

#For the correlation and moderation analyses, I used the cleaned continuous billing amount. For descriptive frequency analyses, I also created the four billing categories listed above.

## Additional Managed Variables

#I also created a **Length of Stay** variable by subtracting each patient's admission date from the discharge date. I grouped length of stay into:

#- 0–7 days
#- 8–14 days
#- 15–21 days
#- 22 or more days

#For the Chi-Square analysis, I transformed the original three-category test-results variable into a binary variable:

#- Abnormal
#- Not abnormal

#The original Normal and Inconclusive categories were combined into the Not abnormal category.

#Gender was retained as a categorical variable and was used as a potential moderator when examining the relationship between Age and Billing Amount.

### URL

#https://www.kaggle.com/datasets/prasad22/healthcare-dataset
#Use the same original dataset page:

#**Kaggle – Healthcare Dataset by Prasad Patil**

#---

# Overall Assessment

#The healthcare dataset contains a large sample of simulated hospitalization records that is useful for practicing data management, visualization, and statistical testing. The main strength of the dataset is that it provides healthcare-like information without exposing confidential information from real patients.

#The most important limitation is that the observations are **synthetically generated rather than obtained from actual patients**. Therefore, results from this project should be interpreted only as patterns in the simulated dataset and should not automatically be generalized to real patient populations.

#My data-management decisions included checking numeric values, coding invalid values as missing, grouping continuous variables when categorical analyses were required, and creating new variables such as length of stay. These steps allowed me to examine the relationship between patient Age and Billing Amount consistently across the different statistical assignments.

