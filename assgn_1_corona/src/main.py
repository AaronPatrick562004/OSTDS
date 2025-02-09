"""
File: data_cleaning_analysis.py

Description:
This script loads COVID-19 data from a CSV file, cleans the data by removing null values,
filters for the US region, and drops unnecessary columns. It then performs an analysis
on the cleaned data, including descriptive statistics, case fatality ratio calculations,
and visualization of correlations and distributions.

Author: Aaron Patrick
Date: 9th Feb 2025
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from logger import setup_logger

def clean_data(df, logger):
    """
    Cleans the input DataFrame by performing the following steps:
    - Drops rows with missing values.
    - Converts 'Last_Update' column to datetime format.
    - Filters data for the US region if 'Country_Region' column exists.
    - Drops unnecessary columns ('Long_', 'Lat').
    
    Parameters:
    df (pd.DataFrame): The raw input DataFrame.
    logger: Logger instance for logging messages.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    df.dropna(inplace=True)   
    df['Last_Update'] = pd.to_datetime(df['Last_Update'])   

    logger.info(f"Columns in the dataset: {df.columns.tolist()}")

    if 'Country_Region' in df.columns:
        df = df[df['Country_Region'] == 'US']
        if df.empty:
            logger.warning("No data available for US. Returning empty DataFrame.")
            return df
    else:
        logger.error("'Country_Region' column not found.")
        return df  

    df.drop(columns=['Long_', 'Lat'], errors='ignore', inplace=True)  
    return df

if __name__ == '__main__':
    """
    Main execution of the script:
    - Sets up the logger.
    - Loads the dataset from a CSV file.
    - Cleans the dataset using clean_data().
    - Saves the cleaned dataset.
    - Performs statistical analysis and visualization.
    """
    logger = setup_logger(log_level="DEBUG")
    csv_file_path = "C:\\Users\\hp\\Desktop\\OSTDS\\assgn_1_corona\\data\\processed_data.csv"
    logger.warning("Running analysis on a single file only")

    try:
        data = pd.read_csv(csv_file_path)
        df = pd.DataFrame(data)
        logger.info("Data successfully loaded")
    except FileNotFoundError:
        logger.error(f"File not found at path: {csv_file_path}. Please check the file path.")
        df = None  
    except pd.errors.ParserError:
        logger.error("Error reading the CSV file. It may be malformed.")
        df = None
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        df = None

    if df is not None:
        cleaned_data = clean_data(df, logger)

        processed_file_path = "C:\\Users\\hp\\Desktop\\OSTDS\\assgn_1_corona\\data\\processed_data.csv"
        cleaned_data.to_csv(processed_file_path, index=False)
        logger.info(f"Cleaned data saved to {processed_file_path}")

        if 'Province_State' in cleaned_data.columns:
            statewise_summary = cleaned_data.groupby('Province_State').describe()
            statewise_summary.to_csv("statewise_summary.csv")
            logger.info("Statewise summary saved as CSV.")

        if 'Deaths' in cleaned_data.columns and 'Confirmed' in cleaned_data.columns:
            cleaned_data = cleaned_data[cleaned_data['Confirmed'] > 0]
            cleaned_data['Case_Fatality_Ratio'] = (cleaned_data['Deaths'] / cleaned_data['Confirmed']) * 100

            plt.figure(figsize=(10, 6))
            sns.histplot(cleaned_data['Case_Fatality_Ratio'], kde=True)
            plt.title("Distribution of Case Fatality Ratio")
            plt.xlabel("Case Fatality Ratio (%)")
            plt.savefig("case_fatality_distribution.png")
            plt.show()

        numeric_data = cleaned_data.select_dtypes(include=['float64', 'int64'])
        correlation = numeric_data.corr()

        plt.figure(figsize=(10, 6))
        sns.heatmap(correlation, annot=True, cmap='coolwarm')
        plt.title("Correlation Matrix")
        plt.savefig("correlation_matrix.png")
        plt.show()
    else:
        logger.error("Data loading failed. Exiting the script.")


# """
# File: data_cleaning_analysis.py

# Description:
# This script loads COVID-19 data from a CSV file, cleans the data by removing null values,
# filters for the US region, and drops unnecessary columns. It then performs an analysis
# on the cleaned data, including descriptive statistics, case fatality ratio calculations,
# and visualization of correlations and distributions.

# Author: Aaron Patrick
# Date: 9th Feb 2025
# """

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from logger import setup_logger

# def clean_data(df):
#     """
#     Cleans the input DataFrame by performing the following steps:
#     - Drops rows with missing values.
#     - Converts 'Last_Update' column to datetime format.
#     - Filters data for the US region if 'Country_Region' column exists.
#     - Drops unnecessary columns ('Long_', 'Lat').
    
#     Parameters:
#     df (pd.DataFrame): The raw input DataFrame.

#     Returns:
#     pd.DataFrame: The cleaned DataFrame.
#     """
#     df.dropna(inplace=True)   
#     df['Last_Update'] = pd.to_datetime(df['Last_Update'])   
    
#     logger.info(f"Columns in the dataset: {df.columns.tolist()}")
    
#     if 'Country_Region' in df.columns:
#         df = df[df['Country_Region'] == 'US']   
#     else:
#         logger.error("'Country_Region' column not found.")
#         return df  
    
#     exclude_columns = ['Long_', 'Lat']
#     df = df.drop(columns=exclude_columns, errors='ignore')   
    
#     return df

# if __name__ == '__main__':
#     """
#     Main execution of the script:
#     - Sets up the logger.
#     - Loads the dataset from a CSV file.
#     - Cleans the dataset using clean_data().
#     - Saves the cleaned dataset.
#     - Performs statistical analysis and visualization.
#     """
#     logger = setup_logger(log_level="DEBUG")
#     csv_file_path = "C:\\Users\\hp\\Desktop\\OSTDS\\assgn_1_corona\\data\\processed_data.csv"
#     logger.warning("Running analysis on a single file only")
    
#     try:
#         data = pd.read_csv(csv_file_path)
#         df = pd.DataFrame(data)
#         logger.info("Data successfully loaded")
#     except FileNotFoundError:
#         logger.error(f"File not found at path: {csv_file_path}. Please check the file path.")
#         df = None  
#     except pd.errors.ParserError:
#         logger.error("Error reading the CSV file. It may be malformed.")
#         df = None
#     except Exception as e:
#         logger.error(f"An unexpected error occurred: {e}")
#         df = None
    
#     if df is not None:
#         cleaned_data = clean_data(df)
        
         
#         processed_file_path = "C:\\Users\\hp\\Desktop\\OSTDS\\assgn_1_corona\\data\\processed_data.csv"
#         cleaned_data.to_csv(processed_file_path, index=False)
#         logger.info(f"Cleaned data saved to {processed_file_path}")
        
         
#         if 'Province_State' in cleaned_data.columns:
#             statewise_summary = cleaned_data.groupby('Province_State').describe()
#             print(statewise_summary)
        
         
#         if 'Deaths' in cleaned_data.columns and 'Confirmed' in cleaned_data.columns:
#             cleaned_data['Case_Fatality_Ratio'] = (cleaned_data['Deaths'] / cleaned_data['Confirmed']) * 100
#             plt.figure(figsize=(10, 6))
#             sns.histplot(cleaned_data['Case_Fatality_Ratio'], kde=True)
#             plt.title("Distribution of Case Fatality Ratio")
#             plt.xlabel("Case Fatality Ratio (%)")
#             plt.show()
        
         
#         numeric_data = cleaned_data.select_dtypes(include=['float64', 'int64'])
#         correlation = numeric_data.corr()
#         sns.heatmap(correlation, annot=True, cmap='coolwarm')
#         plt.title("Correlation Matrix")
#         plt.show()
#     else:
#         logger.error("Data loading failed. Exiting the script.")
