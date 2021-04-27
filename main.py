import pandas as pd
import numpy as np
import sys,os
import json

#function to calculate bmi,bmi category and health risk
def calc_bmi(tempdat):
    # The formula for calculating bmi
    bmi=tempdat['WeightKg']/((tempdata['HeightCm']/100)**2)
    #print(bmi)
    #conditions
    if bmi < 18.5:
        bmi_category="Underweight"
        health_risk="Malnutrition risk"
    elif bmi>=18.5 and bmi<25:
        bmi_category="Normal weight"
        health_risk="Low risk"
    elif bmi>=25 and bmi<30:
        bmi_category="Overweight"
        health_risk="Enhanced risk"
    elif bmi>=30 and bmi<35:
        bmi_category="Moderately obese"
        health_risk="Medium risk"
    elif bmi>=35 and bmi<40:
        bmi_category="Severely obese"
        health_risk="High risk"
    elif bmi>=40:
        bmi_category="Very severely obese"
        health_risk="Very high risk"
    return bmi,bmi_category,health_risk

data= json.load(open('test.json'))
number_of_overweight = 0
#print(data)
bmi_data = pd.DataFrame(columns =['BMI','BMI Category','Health Risk'])
for tempdata in data:
    bmi,bmi_category,health_risk=calc_bmi(tempdata)
    if bmi_category=="Overweight":
        number_of_overweight+=1
    bmi_data.loc[len(bmi_data.index)]=[bmi,bmi_category,health_risk]
    
print(bmi_data)
#calculate number of overweight in bmi column
number_of_overweight_incol=bmi_data['BMI Category'].eq('Overweight').sum()
#print(number_of_overweight_incol)
if number_of_overweight_incol == number_of_overweight:
    print("The data is consistent")
else:
    print("Data is missing")


