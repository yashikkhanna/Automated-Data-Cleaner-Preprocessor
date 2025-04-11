import os
import pandas as pd
import requests
from sqlalchemy import create_engine

DATA_DIR=os.path.join(os.path.dirname(os.path.abspath(__file__)),"../data")

class DataIngestion:
    def __init__(self,db_url=None):
        """ Initialize data ingestion with an optional database connection."""
        self.engine=create_engine(db_url) if db_url else None

    def load_csv(self,file_name):
        """Loads a csv file into a dataframe"""
        file_path=os.path.join(DATA_DIR,file_name)
        try:
            df=pd.read_csv(file_path)
            print(f"CSV file loaded sucessfullly: {file_path}")
            return df
        except Exception as e:
            print(f"Error loading csv:{e}")
            return None 

    def load_excel(self,file_name,sheet_name=0):
        """Loads data from excel sheet into dataframe"""
        file_path=os.path.join(DATA_DIR,file_name)
        try:
            df=pd.read_excel(file_path,sheet_name=sheet_name)
            print(f"Excel Loading Sucessfull:{file_path}")
            return df
        except Exception as e:
            print(f"Error Loading Excell:{e}")
            return None
        
    def connect_database(self,db_url):
        """Establishes a database connection"""
        try:
            self.engine=create_engine(db_url)
            print("Database connection successful")
        except Exception as e:
            print(f"Errror connecting to database:{e}")
            
    def load_from_database(self,query):
        """Fethes data from a database"""
        if not self.engine:
            print("No database connection. call connect_database() first.")
            return None
        try:
            df=pd.read_sql(query,self.engine)
            print("Data loaded from Database successfully")
            return df
        except Exception as e:
            print(f"Error loading data from database:{e}")
            return None
        
    def fetch_from_api(self,api_url,params=None):
        """Fetch data from API and return it as DataFrame."""
        try:
            response=requests.get(api_url,params=params)
            if response.status_code==200:
                data=response.json()
                df=pd.DataFrame(data)
                print("Data Fetched From API successfully")
                return df
            else:
                print(f"API Request Failed:{response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching data from API:{e}")
            return None
    
      