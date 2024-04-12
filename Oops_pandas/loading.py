import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataLoader():
    def __init__(self):
        pass
    def load_csv(self, file_path):
        try:
            df = pd.read_csv(file_path)
            return df
        except FileNotFoundError:
            print("Error: File not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
    
    def load_excel(self, file_path):
        try:
            df = pd.read_excel(file_path)
            return df
        except FileNotFoundError:
            print("Error: File not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

class DataCleaner():
    def __init__(self):
        pass
    
    def clean_data(self, data):
        try:
            cleaned_data = data.dropna()  
            return cleaned_data
        except Exception as e:
            print(f"An error occurred during data cleaning: {str(e)}")
            return None

class DataAnalyzer():
    def __init__(self):
        pass
    
    def analyze_data(self, data):
        try:
            
            summary_stats = data.describe()
            return summary_stats
        except Exception as e:
            print(f"An error occurred during data analysis: {str(e)}")
            return None
    
    def visualize_data(self, data):
        try:
            
            data.plot(kind='hist', bins=20)
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            plt.title('Histogram of Data')
            plt.show()
        except Exception as e:
            print(f"An error occurred during data visualization: {str(e)}")


file_path = "data.csv"
data_loader = DataLoader()
df = data_loader.load_csv(file_path)

if df is not None:
    print("Data loaded successfully.")
    print(df.head())

data_cleaner = DataCleaner()
cleaned_df = data_cleaner.clean_data(df)

if cleaned_df is not None:
    print("Data cleaned successfully.")
    print(cleaned_df.head())

data_analyzer = DataAnalyzer()
summary_stats = data_analyzer.analyze_data(cleaned_df)

if summary_stats is not None:
    print("Summary statistics:")
    print(summary_stats)


data_analyzer.visualize_data(cleaned_df)
