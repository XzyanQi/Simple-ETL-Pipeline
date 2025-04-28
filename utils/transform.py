import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('future.no_silent_downcasting', True)

def transform_data(products):
    # Data Produknya dibuat dari DataFrame
    df = pd.DataFrame(products)
    
    # kalau title invalid, hapus baris
    df = df[df['title'].str.lower() != 'unknown product']
    
    # Konversi price dari string ke float lalu ke rupiah
    df['price'] = df['price'].replace(r'[^\d.]', '', regex=True)
    df['price'] = df['price'].replace('', np.nan)
    df.dropna(subset=['price'], inplace=True)
    
    # Konversi harga menjadi float dan x dengan nilai tukar
    df['price'] = df['price'].astype(float) * 16000
    
    # Konversi rating
    df['rating'] = df['rating'].replace(r'[^0-9.]', '', regex=True)
    df['rating'] = df['rating'].replace('', np.nan)
    df.dropna(subset=['rating'], inplace=True)
    
    # Konversi rating menjadi float
    df['rating'] = df['rating'].astype(float)
    
    # Bersihkan colors (hanya angka yang dipertahankan)
    df['colors'] = df['colors'].replace(r'\D', '', regex=True)
    df['colors'] = df['colors'].replace('', np.nan)
    df.dropna(subset=['colors'], inplace=True)
    
    # Konversi colors menjadi integer
    df['colors'] = df['colors'].astype(int)
    
    # Bersihkan size dan gender
    df['size'] = df['size'].replace(r'Size:\s*', '', regex=True)
    df['gender'] = df['gender'].replace(r'Gender:\s*', '', regex=True)
    
    # Drop duplicates & null
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    
    # Tambahkan kolom timestamp
    df['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return df