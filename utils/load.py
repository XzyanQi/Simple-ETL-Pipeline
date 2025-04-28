import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from sqlalchemy import create_engine

def save_to_csv(df, filename="products.csv"):
    df.to_csv(filename, index=False)

def save_to_google_sheets(df, spreadsheet_id, range_name):
    creds = Credentials.from_service_account_file('bold-guide-456709-g6-2009d1b733eb.json')
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    
    values = df.values.tolist()
    body = {
        'values': values
    }
    
    sheet.values().update(
    spreadsheetId=spreadsheet_id,
    range=range_name,
    valueInputOption='RAW',
      body=body
    ).execute()

def load_to_postgresql(df, table_name='products'):
    try:
        # buat koneksi ke PostgreSQL
        username = 'postgres'
        password = 'Ihsan129129?'
        host = 'localhost'
        port = '5432'
        database = 'xzyanqidb'
        
        # Buat engine SQLAlchemy
        engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')
        
        # Simpan ke database (replace kalau ada)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data berhasil disimpan ke PostgreSQL table '{table_name}'.")
    
    except Exception as e:
        print(f"Gagal menyimpan ke PostgreSQL: {e}")