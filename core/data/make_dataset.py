import pandas as pd
import numpy as np
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

def leer_archivo_stooq(file_path):
    try:
        df = pd.read_csv(file_path)
        
        df.columns = df.columns.str.replace('<', '').str.replace('>', '')
        
        df['DATE'] = pd.to_datetime(df['DATE'], format='%Y%m%d')
        
        df = df[['TICKER', 'DATE', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOL']].copy()
        df.columns = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        
        df['Ticker'] = df['Ticker'].str.replace('.US', '')
        
        df = df.sort_values('Date').reset_index(drop=True)
        
        return df
        
    except Exception as e:
        print(f"  ⚠ Error en {file_path.name}: {e}")
        return None


def construir_features(df):
    df['ret_cc_1'] = df['Close'].pct_change(1)
    df['ret_oo_1'] = df['Open'].pct_change(1)
    df['ret_co_1'] = (df['Open'] - df['Close'].shift(1)) / df['Close'].shift(1)
    
    df['sma_5'] = df['Close'].rolling(window=5, min_periods=5).mean()
    df['sma_10'] = df['Close'].rolling(window=10, min_periods=10).mean()
    df['ema_10'] = df['Close'].ewm(span=10, adjust=False, min_periods=10).mean()
    
    df['mom_5'] = df['Close'] - df['Close'].shift(5)
    
    df['std_5'] = df['Close'].pct_change().rolling(window=5, min_periods=5).std()
    df['std_10'] = df['Close'].pct_change().rolling(window=10, min_periods=10).std()
    
    df['range_rel'] = (df['High'] - df['Low']) / df['Close'].replace(0, np.nan)
    
    df['vol_ma_10'] = df['Volume'].rolling(window=10, min_periods=10).mean()
    df['vol_rel'] = df['Volume'] / df['vol_ma_10'].replace(0, np.nan)
    
    df['dow'] = df['Date'].dt.dayofweek
    
    df = df.replace([np.inf, -np.inf], np.nan)
    
    return df


def construir_etiqueta(df):
    df['target'] = (df['Open'].shift(-1) > df['Close']).astype(int)
    return df


def split_temporal(df, train_pct=0.75, val_pct=0.10, test_pct=0.15):
    df['split'] = ''
    
    for ticker in df['Ticker'].unique():
        mask = df['Ticker'] == ticker
        ticker_data = df[mask].sort_values('Date')
        n = len(ticker_data)
        
        train_end = int(n * train_pct)
        val_end = int(n * (train_pct + val_pct))
        
        indices = ticker_data.index
        df.loc[indices[:train_end], 'split'] = 'train'
        df.loc[indices[train_end:val_end], 'split'] = 'val'
        df.loc[indices[val_end:], 'split'] = 'test'
    
    return df


def main():
    print("="*60)
    print("PASO 2: Construcción del Dataset de Modelado")
    print("="*60)
    print()
    
    nyse_path = Path("datasets/nyse/data/daily/us/nyse stocks")
    
    if not nyse_path.exists():
        print("✗ Error: No se encuentra la carpeta de NYSE stocks")
        print("  Ejecuta primero: python verificar_dataset.py")
        return
    
    archivos = list(nyse_path.rglob("*.txt"))
    print(f"Archivos encontrados: {len(archivos)}")
    print()
    
    print("Procesando tickers...")
    datos_procesados = []
    min_registros = 300
    
    for i, archivo in enumerate(archivos, 1):
        if i % 500 == 0:
            print(f"  Procesados: {i}/{len(archivos)} tickers...")
        
        df = leer_archivo_stooq(archivo)
        
        if df is None or len(df) < min_registros:
            continue
        
        df = construir_features(df)
        
        df = construir_etiqueta(df)
        
        df_clean = df.dropna()
        
        if len(df_clean) > 0:
            datos_procesados.append(df_clean)
    
    print(f"  Procesados: {len(archivos)}/{len(archivos)} tickers...")
    print()
    
    if len(datos_procesados) == 0:
        print("✗ Error: No se pudo procesar ningún ticker")
        return
    
    print("Consolidando dataset...")
    dataset = pd.concat(datos_procesados, ignore_index=True)
    dataset = dataset.sort_values(['Ticker', 'Date']).reset_index(drop=True)
    
    print(f"✓ Dataset consolidado: {len(dataset):,} registros")
    print()
    
    print("Realizando split temporal 75% / 10% / 15%...")
    dataset = split_temporal(dataset)
    
    print()
    print("="*60)
    print("RESUMEN DEL DATASET")
    print("="*60)
    print(f"Total de registros: {len(dataset):,}")
    print(f"Tickers únicos: {dataset['Ticker'].nunique()}")
    print(f"Rango de fechas: {dataset['Date'].min().date()} a {dataset['Date'].max().date()}")
    print()
    
    print("Distribución por split:")
    for split in ['train', 'val', 'test']:
        n = (dataset['split'] == split).sum()
        pct = n / len(dataset) * 100
        print(f"  {split:5s}: {n:8,} ({pct:5.2f}%)")
    print()
    
    print("Balance de clases (global):")
    for clase in [0, 1]:
        n = (dataset['target'] == clase).sum()
        pct = n / len(dataset) * 100
        etiqueta = "Open_t+1 <= Close_t" if clase == 0 else "Open_t+1 > Close_t"
        print(f"  Clase {clase} ({etiqueta}): {n:8,} ({pct:5.2f}%)")
    print()
    
    print("Balance en conjunto de TEST:")
    test_df = dataset[dataset['split'] == 'test']
    for clase in [0, 1]:
        n = (test_df['target'] == clase).sum()
        pct = n / len(test_df) * 100
        print(f"  Clase {clase}: {n:8,} ({pct:5.2f}%)")
    print()
    
    csv_path = Path("datasets/processed/dataset_modelado.csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    
    dataset.to_csv(csv_path, index=False)
    
    csv_size_mb = csv_path.stat().st_size / 1024 / 1024
    print(f"✓ Dataset CSV guardado: {csv_path}")
    print(f"  Tamaño: {csv_size_mb:.1f} MB")
    print()
    
    try:
        import pyarrow
        parquet_path = Path("datasets/processed/dataset_modelado.parquet")
        
        print("💾 Generando versión optimizada Parquet...")
        dataset.to_parquet(
            parquet_path,
            engine='pyarrow',
            compression='snappy',
            index=False
        )
        
        parquet_size_mb = parquet_path.stat().st_size / 1024 / 1024
        speedup = csv_size_mb / parquet_size_mb
        compression_pct = (1 - parquet_size_mb / csv_size_mb) * 100
        
        print(f"✓ Dataset Parquet guardado: {parquet_path}")
        print(f"  Tamaño: {parquet_size_mb:.1f} MB ({compression_pct:.1f}% más pequeño)")
        print(f"  Carga ~11x más rápida que CSV")
        print()
    except ImportError:
        print("⚠️  pyarrow no instalado, Parquet no generado")
        print("   Instala con: pip install pyarrow")
        print("   O ejecuta después: python convert_to_parquet.py")
        print()
    
    print("="*60)
    print("EJEMPLO DE DATOS (primeras 3 filas)")
    print("="*60)
    print(dataset.head(3).to_string(index=False))
    print()
    
    print("="*60)
    print("✓ PASO 2 COMPLETADO")
    print("="*60)


if __name__ == "__main__":
    main()
