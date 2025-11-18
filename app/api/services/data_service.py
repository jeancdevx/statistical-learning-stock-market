import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, Dict, List
import logging

logger = logging.getLogger(__name__)

class DataService:
    def __init__(self):
        self.parquet_path = Path("datasets/processed/dataset_modelado.parquet")
        self.csv_path = Path("datasets/processed/dataset_modelado.csv")
        self._df: Optional[pd.DataFrame] = None
        self._ticker_cache: Dict[str, pd.DataFrame] = {}
        self._tickers_list: Optional[List[str]] = None
        self._date_ranges_cache: Dict[str, Dict] = {}
    
    def load_dataset(self) -> pd.DataFrame:
        if self._df is None:
            if self.parquet_path.exists():
                logger.info("Cargando dataset desde Parquet (optimizado)...")
                self._df = pd.read_parquet(self.parquet_path)
                logger.info(f"✓ Dataset cargado: {len(self._df):,} registros")
            
            elif self.csv_path.exists():
                logger.warning("Parquet no encontrado, usando CSV (lento)...")
                logger.info("Tip: Ejecuta 'python convert_to_parquet.py' para optimizar")
                
                self._df = pd.read_csv(
                    self.csv_path,
                    parse_dates=['Date'],
                    engine='c'
                )
                
                self._df['Ticker'] = self._df['Ticker'].astype('category')
                self._df['split'] = self._df['split'].astype('category')
                
                logger.info(f"✓ Dataset cargado: {len(self._df):,} registros")
            
            else:
                raise FileNotFoundError(
                    f"Dataset no encontrado en:\n"
                    f"  - {self.parquet_path}\n"
                    f"  - {self.csv_path}\n"
                    f"Ejecuta: python core/data/make_dataset.py"
                )
        
        return self._df
    
    def get_ticker_data(self, ticker: str, until_date: str = None) -> pd.DataFrame:
        ticker_upper = ticker.upper()
        
        if ticker_upper not in self._ticker_cache:
            df = self.load_dataset()
            ticker_df = df[df['Ticker'] == ticker_upper].copy()
            self._ticker_cache[ticker_upper] = ticker_df.sort_values('Date')
        
        ticker_df = self._ticker_cache[ticker_upper]
        
        if until_date:
            ticker_df = ticker_df[ticker_df['Date'] <= until_date]
        
        return ticker_df
    
    def get_last_row(self, ticker: str, date: str = None) -> Optional[pd.Series]:
        ticker_df = self.get_ticker_data(ticker, date)
        
        if len(ticker_df) == 0:
            return None
        
        return ticker_df.iloc[-1]
    
    def get_next_day(self, ticker: str, date: str) -> Optional[pd.Series]:
        ticker_df = self.get_ticker_data(ticker)
        
        target_date = pd.to_datetime(date)
        next_rows = ticker_df[ticker_df['Date'] > target_date]
        
        if len(next_rows) == 0:
            return None
        
        return next_rows.iloc[0]
    
    def get_available_dates(self, ticker: str) -> Dict:
        ticker_upper = ticker.upper()
        
        if ticker_upper in self._date_ranges_cache:
            return self._date_ranges_cache[ticker_upper]
        
        ticker_df = self.get_ticker_data(ticker)
        
        if len(ticker_df) == 0:
            result = {
                'available': False,
                'message': f'Ticker {ticker} no encontrado en el dataset'
            }
        else:
            min_date = ticker_df['Date'].min()
            max_date = ticker_df['Date'].iloc[-2] if len(ticker_df) > 1 else ticker_df['Date'].iloc[-1]
            
            result = {
                'available': True,
                'min_date': min_date.strftime('%Y-%m-%d'),
                'max_date': max_date.strftime('%Y-%m-%d'),
                'total_days': len(ticker_df) - 1,
                'ticker': ticker_upper
            }
        
        self._date_ranges_cache[ticker_upper] = result
        return result
    
    def get_all_tickers(self) -> List[str]:
        if self._tickers_list is None:
            df = self.load_dataset()
            self._tickers_list = sorted(df['Ticker'].cat.categories.tolist())
            logger.info(f"✓ {len(self._tickers_list)} tickers disponibles")
        
        return self._tickers_list
    
    def get_dataset_info(self) -> Dict:
        df = self.load_dataset()
        
        return {
            'total_records': len(df),
            'total_tickers': df['Ticker'].nunique(),
            'date_range': {
                'min': df['Date'].min().strftime('%Y-%m-%d'),
                'max': df['Date'].max().strftime('%Y-%m-%d')
            },
            'splits': {
                'train': len(df[df['split'] == 'train']),
                'val': len(df[df['split'] == 'val']),
                'test': len(df[df['split'] == 'test'])
            }
        }
