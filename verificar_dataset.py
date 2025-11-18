import os
from pathlib import Path

def main():
    print("=== Verificación del Dataset NYSE (Stooq) ===\n")
    
    nyse_path = Path("datasets/nyse/data/daily/us/nyse stocks")
    
    if not nyse_path.exists():
        print(f"✗ Error: No se encuentra la carpeta {nyse_path}")
        print("  Asegúrate de haber extraído d_us_txt.zip en datasets/nyse/")
        return
    
    archivos = list(nyse_path.rglob("*.txt"))
    print(f"Archivos encontrados: {len(archivos)}")
    
    if len(archivos) == 0:
        print("✗ No se encontraron archivos .txt")
        return
    
    archivo_ejemplo = archivos[0]
    print(f"\nArchivo de ejemplo: {archivo_ejemplo.name}")
    
    with open(archivo_ejemplo, 'r') as f:
        lineas = f.readlines()
        print(f"Total de líneas: {len(lineas)}")
        print(f"\nPrimeras 5 líneas:")
        for i, linea in enumerate(lineas[:5], 1):
            print(f"  {i}: {linea.strip()}")
    
    print(f"\n✓ Dataset extraído correctamente")
    print(f"  Total de tickers NYSE: {len(archivos)}")
    print(f"  Ubicación: {nyse_path}")


if __name__ == "__main__":
    main()
