from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmployeeForm
import pickle
import pandas as pd
from django.contrib import messages

def homepage(request):
    return render(request, "input.html")

def evaluate_model_on_new_data(model, scaler, new_data, columns, training_columns):
    new_df = pd.DataFrame(new_data, columns=columns)
    print('dataframe')
    print(new_df)
    print(new_df.dtypes)
    #  Apply one-hot encoding
    X_new = pd.get_dummies(new_df,drop_first=True)
    print('after get_dummies')
    print(X_new)

    # Add missing columns from the training set
    missing_cols = set(training_columns) - set(X_new.columns)
    for col in missing_cols:
        X_new[col] = 0  # Add missing columns with zeros
    print(X_new.shape[1])

    # Reorder columns to match the training data
    X_new = X_new[training_columns]

    X_new_scaled = scaler.transform(X_new)
    print("after scaled")
    print(X_new_scaled)

    #  Make predictions
    y_pred_new = model.predict(X_new_scaled)
    
    if y_pred_new == 1:
        result = "likely to left company"
    elif y_pred_new==0:
        result = "likely to stay with the company"
    else:
        print('Nothing')

    # Return the predicted class
    return result


def employee_predict(request):
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        business_travel = request.POST.get('business_travel')
        department = request.POST.get('department')
        job_role = request.POST.get('job_role')
        marital_status = request.POST.get('marital_status')
        salary = int(request.POST.get('salary'))
        overtime = request.POST.get('overtime')
        years_at_company = int(request.POST.get('years_at_company'))
        years_in_most_recent_role = int(request.POST.get('years_in_most_recent_role'))
        years_since_last_promotion = int(request.POST.get('years_since_last_promotion'))
        
        new_data = [[age, business_travel, department, job_role, marital_status,
                     salary, overtime, years_at_company, years_in_most_recent_role,
                     years_since_last_promotion]]

        columns = ['Age', 'BusinessTravel', 'Department', 'JobRole', 'MaritalStatus',
                'Salary', 'OverTime', 'YearsAtCompany', 'YearsInMostRecentRole', 
                'YearsSinceLastPromotion']

        with open('model_1.pkl', 'rb') as model_file:
            model = pickle.load(model_file)

        with open('scaler_1.pkl', 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)


        with open('columns.pkl', 'rb') as column_file:
            training_columns = pickle.load(column_file)

    
        # evaluate_model_on_new_data function
        result = evaluate_model_on_new_data(model, scaler, new_data, columns, training_columns)
        print(result)

        return render(request,'output.html', {'prediction': result})
        
    else:
        form = EmployeeForm()
    return render(request, 'input.html', {'form': form})




# form method
# def employee_predict(request):
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             new_data = [[
#                 form.cleaned_data['age'],
#                 form.cleaned_data['business_travel'],
#                 form.cleaned_data['department'],
#                 form.cleaned_data['job_role'],
#                 form.cleaned_data['marital_status'],
#                 form.cleaned_data['salary'],
#                 form.cleaned_data['overtime'],
#                 form.cleaned_data['years_at_company'],
#                 form.cleaned_data['years_in_most_recent_role'],
#                 form.cleaned_data['years_since_last_promotion'],
#             ]]
        

#             columns = ['Age', 'BusinessTravel', 'Department', 'JobRole', 'MaritalStatus',
#                     'Salary', 'OverTime', 'YearsAtCompany', 'YearsInMostRecentRole', 
#                     'YearsSinceLastPromotion']

#             with open('model.pkl', 'rb') as model_file:
#                 model = pickle.load(model_file)

#             with open('scaler.pkl', 'rb') as scaler_file:
#                 scaler = pickle.load(scaler_file)

#             X_new = pd.DataFrame(new_data, columns=columns)
#             X_new = pd.get_dummies(X_new, drop_first=True)

#             with open('columns.pkl', 'rb') as column_file:
#                 training_columns = pickle.load(column_file)
            
#             missing_cols = set(training_columns) - set(X_new.columns)
#             for col in missing_cols:
#                 X_new[col] = 0
#             X_new = X_new[training_columns]

#             X_new_scaled = scaler.transform(X_new)
#             prediction = model.predict(X_new_scaled)
#             print('prediction:', prediction[0])
#             return render(request, 'output.html', {'prediction': prediction[0]})
#         else:

#             # print(messages.error(request,form.errors)
#             return render(request, 'input.html', {'form': form})
#     else:
#         form = EmployeeForm()
#     return render(request, 'input.html', {'form': form})
