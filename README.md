# Employee Attrition Prediction
![image](https://github.com/user-attachments/assets/2e8afbaa-6058-45f6-9925-25b369144eb3)
![Screenshot 2024-09-14 141619](https://github.com/user-attachments/assets/ecefad33-8c6c-4ab4-b385-86d6f0ee4416)

![Screenshot 2024-09-14 141639](https://github.com/user-attachments/assets/5ea0aede-1ac5-4c9f-8f83-e9951beee0bc)


## Overview
    * This project aims to predict employee attrition using a machine learning model.
    * It leverages employee data such as age, business travel frequency, department, job role, salary, overtime, and years at the company to predict whether an employee is likely to leave the organization.
    * A RandomForestClassifier was used for building the model, and the project is deployed using a Django web application.

## Features
    * Predict Employee Attrition: The model predicts whether an employee is likely to stay or leave the company based on input features.
    * Web Application: A simple and interactive web interface for user input and real-time predictions using Django.
    * Scalable Solution: The app handles feature engineering (one-hot encoding, scaling) and ensures that predictions are as accurate as possible for new data.
    * Data Preprocessing: Managed categorical variables and feature scaling using StandardScaler to ensure consistency with the training data.

## Tech Stack
    * Frontend: HTML, CSS 
    * Backend: Python, Django
    * Machine Learning: Scikit-learn (RandomForestClassifier)
    * Data Processing: Pandas, NumPy
    * Deployment: Django's development server
## Dataset
The dataset includes the following features:

    * Age: Employee's age
    * Business Travel: Frequency of business travel
    * Department: Department of the employee
    * Job Role: Employee's job role
    * Marital Status: Marital status of the employee
    * Salary: Employee's salary category
    * Overtime: Whether the employee works overtime or not
    * Years at Company: Total number of years spent at the company
    * Years in Most Recent Role: Total number of years spent in the most recent role
    * Years Since Last Promotion: Number of years since the employee's last promotion
    * Attrition (target variable): Whether the employee left the company (Yes/No)


## Installation
1.Clone the repository:

       git clone https://github.com/yourusername/employee-attrition-prediction.git
2.Navigate to the project directory:
   
       cd employee-attrition-prediction

3.Create a virtual environment and activate it:

     python -m venv employee_env
     source employee_env/bin/activate  # On Windows: employee_env\Scripts\activate
4.Install the required dependencies:

    pip install -r requirements.txt
5.Run the Django development server:

    python manage.py runserver
6.Access the application at: 

    http://127.0.0.1:8000/


## Usage
    * Input employee details (such as age, department, salary, etc.) through the web interface.
    * Submit the form, and the application will predict whether the employee is likely to leave or stay at the company.
    * The result will be displayed on the output page.
  
## Model Training
    * Preprocessing: The dataset was processed using one-hot encoding for categorical variables and scaled using StandardScaler.
    * Model: A RandomForestClassifier was trained on the processed dataset.
    * Evaluation: The model achieved a training accuracy of 92% testing accuracy 85%.
    
## File Structure

    ├── attrition_app/           # Django application
    │   ├── migrations/          # Django migration files
    │   ├── static/              # Static files (CSS, images)
    │   ├── templates/           # HTML templates
    │   ├── views.py             # View logic for the app
    │   └── models.py            # Model handling (Django models)
    ├── employee_env/            # Virtual environment files
    ├── manage.py                # Django project management
    ├── model.pkl                # Saved RandomForest model
    ├── scaler.pkl               # Saved StandardScaler instance
    ├── columns.pkl              # Saved columns for feature consistency
    ├── requirements.txt         # Python package dependencies
    └── README.md                # Project README file


   
