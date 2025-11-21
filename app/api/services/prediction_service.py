import numpy as np
import pandas as pd
from typing import Dict, Optional
import logging
from datetime import timedelta
from .model_loader import ModelLoader
from .data_service import DataService
from app.config import FEATURE_COLUMNS

logger = logging.getLogger(__name__)

class PredictionService:
    def __init__(self, model_loader: ModelLoader = None, data_service: DataService = None):
        self.model_loader = model_loader or ModelLoader()
        self.data_service = data_service or DataService()
        self.feature_columns = FEATURE_COLUMNS
    
    def predict_future(self, ticker: str, model_name: str = "rf") -> Dict:
        try:
            model_data = self.model_loader.load_model(model_name)
            model = model_data['model']
            
            last_row = self.data_service.get_last_row(ticker)
            
            if last_row is None:
                return {
                    'error': True,
                    'message': f'Ticker {ticker} no encontrado en el dataset'
                }
            
            features = self._extract_features(last_row)
            
            prediction = model.predict(features)[0]
            probability = model.predict_proba(features)[0][1]
            
            last_date = last_row['Date']
            next_date = last_date + timedelta(days=1)
            
            confidence = self._get_confidence_level(probability)
            
            feature_dict = {name: float(features[0][i]) for i, name in enumerate(model_data.get('feature_names', []))}
            
            return {
                'error': False,
                'ticker': ticker,
                'model': model_name,
                'prediction': {
                    'direction': int(prediction),
                    'direction_text': 'SUBIDA' if prediction == 1 else 'BAJADA',
                    'probability': float(probability),
                    'confidence': confidence
                },
                'dates': {
                    'data_until': last_date.strftime('%Y-%m-%d'),
                    'predicting_for': next_date.strftime('%Y-%m-%d')
                },
                'last_close': float(last_row['Close']),
                'features': feature_dict,
                'prices': {
                    'open': float(last_row['Open']),
                    'high': float(last_row['High']),
                    'low': float(last_row['Low']),
                    'close': float(last_row['Close'])
                }
            }
            
        except FileNotFoundError as e:
            return {'error': True, 'message': str(e)}
        except Exception as e:
            logger.error(f"Error en predict(): {e}")
            return {'error': True, 'message': f'Error interno: {str(e)}'}
    
    def predict_with_validation(
        self, 
        ticker: str, 
        date: str, 
        model_name: str = "rf"
    ) -> Dict:
        try:
            model_data = self.model_loader.load_model(model_name)
            model = model_data['model']
            
            row = self.data_service.get_last_row(ticker, date)
            
            if row is None:
                return {
                    'error': True,
                    'message': f'No hay datos para {ticker} en {date}'
                }
            
            features = self._extract_features(row)
            prediction = model.predict(features)[0]
            probability = model.predict_proba(features)[0][1]
            
            feature_dict = {name: float(features[0][i]) for i, name in enumerate(model_data.get('feature_names', []))}
            
            next_day = self.data_service.get_next_day(ticker, date)
            
            if next_day is None:
                return {
                    'error': False,
                    'ticker': ticker,
                    'model': model_name,
                    'date': date,
                    'prediction': int(prediction),
                    'direction_text': 'SUBIDA' if prediction == 1 else 'BAJADA',
                    'probability': float(probability),
                    'confidence': self._get_confidence_level(probability),
                    'features': feature_dict,
                    'prices': {
                        'open': float(row['Open']),
                        'high': float(row['High']),
                        'low': float(row['Low']),
                        'close': float(row['Close'])
                    },
                    'validation_available': False,
                    'message': 'Datos del día siguiente no disponibles para validación'
                }
            
            real_direction = int(next_day['target'])
            prev_close = float(row['Close'])
            next_open = float(next_day['Open'])
            price_change = ((next_open - prev_close) / prev_close) * 100
            
            is_correct = (prediction == real_direction)
            
            return {
                'error': False,
                'ticker': ticker,
                'model': model_name,
                'date': date,
                'prediction': int(prediction),
                'direction_text': 'SUBIDA' if prediction == 1 else 'BAJADA',
                'probability': float(probability),
                'confidence': self._get_confidence_level(probability),
                'features': feature_dict,
                'prices': {
                    'open': float(row['Open']),
                    'high': float(row['High']),
                    'low': float(row['Low']),
                    'close': float(row['Close'])
                },
                'real': {
                    'direction': int(real_direction),
                    'direction_text': 'SUBIDA' if real_direction == 1 else 'BAJADA',
                    'open': next_open,
                    'prev_close': prev_close,
                    'change_pct': float(price_change)
                },
                'is_correct': bool(is_correct),
                'validation_available': True
            }
            
        except FileNotFoundError as e:
            return {'error': True, 'message': str(e)}
        except Exception as e:
            logger.error(f"Error en predict_with_validation(): {e}")
            return {'error': True, 'message': f'Error interno: {str(e)}'}
    
    def _extract_features(self, row: pd.Series) -> np.ndarray:
        features = [row[col] for col in self.feature_columns]
        return np.array([features])
    
    def _get_confidence_level(self, probability: float) -> str:
        if probability > 0.65 or probability < 0.35:
            return 'Alta'
        elif probability > 0.55 or probability < 0.45:
            return 'Media'
        else:
            return 'Baja'


import pandas as pd
