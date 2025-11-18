#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
import time

def main():
    csv_path = Path("datasets/processed/dataset_modelado.csv")
    parquet_path = Path("datasets/processed/dataset_modelado.parquet")
    
    if not csv_path.exists():
        print(f"❌ Error: No se encuentra {csv_path}")
        return
    
    print(f"📄 Leyendo CSV: {csv_path}")
    print(f"   Tamaño: {csv_path.stat().st_size / 1024 / 1024:.2f} MB")
    
    start = time.time()
    df = pd.read_csv(csv_path, parse_dates=['Date'])
    load_time = time.time() - start
    
    print(f"✓ CSV cargado en {load_time:.2f} segundos")
    print(f"   Registros: {len(df):,}")
    print(f"   Columnas: {len(df.columns)}")
    
    print("\n🔧 Optimizando tipos de datos...")
    df['Ticker'] = df['Ticker'].astype('category')
    df['split'] = df['split'].astype('category')
    
    print(f"\n💾 Guardando Parquet: {parquet_path}")
    start = time.time()
    df.to_parquet(
        parquet_path,
        engine='pyarrow',
        compression='snappy',
        index=False
    )
    save_time = time.time() - start
    
    print(f"✓ Parquet guardado en {save_time:.2f} segundos")
    print(f"   Tamaño: {parquet_path.stat().st_size / 1024 / 1024:.2f} MB")
    
    print("\n🚀 Probando velocidad de carga Parquet...")
    start = time.time()
    df_test = pd.read_parquet(parquet_path)
    parquet_load_time = time.time() - start
    
    print(f"✓ Parquet cargado en {parquet_load_time:.2f} segundos")
    print(f"\n📊 Mejora de velocidad: {load_time / parquet_load_time:.1f}x más rápido")
    print(f"   CSV:     {load_time:.2f}s")
    print(f"   Parquet: {parquet_load_time:.2f}s")
    
    csv_size = csv_path.stat().st_size / 1024 / 1024
    parquet_size = parquet_path.stat().st_size / 1024 / 1024
    compression_ratio = (1 - parquet_size / csv_size) * 100
    
    print(f"\n💽 Comparación de tamaño:")
    print(f"   CSV:     {csv_size:.2f} MB")
    print(f"   Parquet: {parquet_size:.2f} MB ({compression_ratio:.1f}% más pequeño)")
    
    print(f"\n✅ Conversión completada exitosamente!")
    print(f"   Ahora puedes usar {parquet_path.name} en tu aplicación")

if __name__ == "__main__":
    main()
