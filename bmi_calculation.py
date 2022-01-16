# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
import pandas as pd

def bmi_kg_per_m2(mass_kg, height_cm):
    '''
    Calculate BMI using following formula:
        BMI(kg/m^2) = mass(kg) / height(m)^2
    '''
    bmi_kg_per_m2 = 0
    try:
        bmi_kg_per_m2 = round(mass_kg / (height_cm/100)**2,2)
    except ZeroDivisionError as err:
        print('Error: ', err)
    return bmi_kg_per_m2

def bmi_category(bmi_inference):
    '''Identify the weight category based on BMI value'''
    bmi_category = 'Invalid'
    try:
        if 0 < bmi_inference <= 18.4:
            bmi_category = 'Underweight'
        elif 18.4 < bmi_inference <= 24.9:
            bmi_category = 'Normal weight'
        elif 24.9 < bmi_inference <= 29.9:
            bmi_category = 'Overweight'
        elif 29.9 < bmi_inference <= 34.9:
            bmi_category = 'Moderately obese'
        elif 34.9 < bmi_inference <= 39.9:
            bmi_category = 'Severely obese'
        elif bmi_inference > 39.9:
            bmi_category = 'Very severely obese'
    except ValueError as err:
        print('Error: ', err)
    return bmi_category

def health_risk(bmi_category):
    '''Identify the health risk based on category'''
    health_risk = 'N/A'
    try:
        if bmi_category == 'Underweight':
            health_risk = 'Malnutrition risk'
        elif bmi_category == 'Normal weight':
            health_risk = 'Low risk'
        elif bmi_category == 'Overweight':
            health_risk = 'Enhanced risk'
        elif bmi_category == 'Moderately obese':
            health_risk = 'Medium risk'
        elif bmi_category == 'Severely obese':
            health_risk = 'High risk'
        elif bmi_category == 'Very severely obese':
            health_risk = 'Very high risk'
    except ValueError as err:
        print('Error: ', err)
    return health_risk

def main():
    ''' Main Funtion'''
    with open('input_data.json') as json_data:
        records = json.load(json_data)
        json_data.close()
    df_bmi = pd.DataFrame(records)
    df_bmi['bmi_value'] = ''
    df_bmi['bmi_category'] = ''
    df_bmi['health_risk'] = ''
    df_bmi['bmi_value'] = df_bmi.apply(lambda x: \
                                               bmi_kg_per_m2(x['WeightKg'], \
                                                             x['HeightCm']), \
                                                   axis=1)
    df_bmi['bmi_category'] = df_bmi.apply(lambda x: \
                                                  bmi_category(x['bmi_value']), \
                                                      axis=1)
    df_bmi['health_risk'] = df_bmi.apply(lambda x: \
                                                 health_risk(x['bmi_category']), \
                                                     axis=1)
    df_bmi.to_csv('bmi_results.csv')
    print('Overweight people count: ', \
          df_bmi[df_bmi['bmi_category'] == 'Overweight'].shape[0])

if __name__ == '__main__':
    main()
    