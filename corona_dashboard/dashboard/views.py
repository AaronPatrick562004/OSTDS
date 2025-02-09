"""
Django Views for COVID-19 Data Visualization Dashboard

This module loads a processed COVID-19 dataset, cleans it, and generates various visualizations,
which are then rendered in a Django template.

Author: Aaron Patrick
Date: 9th Feb 2025
"""

from django.shortcuts import render
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def render_image(image_data):
    """
    Converts a Matplotlib figure to a base64-encoded PNG image.

    Args:
        image_data (matplotlib.figure.Figure): Matplotlib figure to be converted.

    Returns:
        str: Base64-encoded string representation of the image.
    """
    buffer = BytesIO()
    image_data.savefig(buffer, format="png")
    buffer.seek(0)
    img_str = base64.b64encode(buffer.read()).decode('utf-8')
    return img_str

def home(request):
    """
    Handles the request for the dashboard homepage, processes COVID-19 data,
    generates visualizations, and renders them in a Django template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page with visualized COVID-19 data.
    """
    csv_file_path = "C:\\Users\\hp\\Desktop\\OSTDS\\assgn_1_corona\\data\\processed_data.csv"
    data = pd.read_csv(csv_file_path)
    df = pd.DataFrame(data)

     
    df.dropna(inplace=True)
    df['Last_Update'] = pd.to_datetime(df['Last_Update'])
    df = df[df['Country_Region'] == 'US']
    df = df.drop(columns=['Long_', 'Lat'], errors='ignore')

     
    if 'Deaths' in df.columns and 'Confirmed' in df.columns:
        df['Case_Fatality_Ratio'] = (df['Deaths'] / df['Confirmed']) * 100
        plt.figure(figsize=(12, 8))
        sns.histplot(df['Case_Fatality_Ratio'], kde=True)
        plt.title("Distribution of Case Fatality Ratio")
        plt.xlabel("Case Fatality Ratio (%)")
        case_fatality_image = render_image(plt)

     
    numeric_data = df.select_dtypes(include=['float64', 'int64'])
    correlation = numeric_data.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    correlation_image = render_image(plt)

     
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Province_State', y='Confirmed', data=df)
    plt.title("Confirmed Cases by Province/State")
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.25)
    confirmed_cases_image = render_image(plt)

    
    if 'Recovered' in df.columns and 'Confirmed' in df.columns:
        df['Recovery_Rate'] = (df['Recovered'] / df['Confirmed']) * 100
        plt.figure(figsize=(12, 8))
        sns.barplot(x='Province_State', y='Recovery_Rate', data=df)
        plt.title("Recovery Rates by Province/State")
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.25)
        recovery_rates_image = render_image(plt)
    
     
    df_grouped = df.groupby('Last_Update')['Active'].sum().reset_index()
    plt.figure(figsize=(12, 8))
    sns.lineplot(x='Last_Update', y='Active', data=df_grouped)
    plt.title("Active Cases Trends Over Time")
    active_cases_image = render_image(plt)

    return render(request, 'dashboard/home.html', {
        'case_fatality_image': case_fatality_image,
        'correlation_image': correlation_image,
        'confirmed_cases_image': confirmed_cases_image,
        'recovery_rates_image': recovery_rates_image,
        'active_cases_image': active_cases_image
    })
