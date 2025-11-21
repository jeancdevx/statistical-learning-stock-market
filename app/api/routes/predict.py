from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from ..services.prediction_service import PredictionService
from ..services.data_service import DataService
from ..services.model_loader import ModelLoader

router = APIRouter(prefix="/api/v1", tags=["Prediction"])

data_service = DataService()
model_loader = ModelLoader()
prediction_service = PredictionService(model_loader=model_loader, data_service=data_service)


class PredictRequest(BaseModel):
    ticker: str = Field(..., description="Símbolo del ticker (ej: AAPL)", example="AAPL")
    model: str = Field("rf", description="Modelo a usar: rf, logreg, svm", example="rf")

class BacktestRequest(BaseModel):
    ticker: str = Field(..., description="Símbolo del ticker", example="AAPL")
    date: str = Field(..., description="Fecha en formato YYYY-MM-DD", example="2025-10-15")
    model: str = Field("rf", description="Modelo a usar", example="rf")


@router.post("/predict")
async def predict(request: PredictRequest):
    result = prediction_service.predict_future(request.ticker, request.model)
    
    if result.get('error'):
        raise HTTPException(status_code=404, detail=result['message'])
    
    return result

@router.post("/backtest")
async def backtest(request: BacktestRequest):
    result = prediction_service.predict_with_validation(
        request.ticker,
        request.date,
        request.model
    )
    
    if result.get('error'):
        raise HTTPException(status_code=404, detail=result['message'])
    
    return result

@router.get("/tickers")
async def get_tickers():
    try:
        tickers = data_service.get_all_tickers()
        return {
            "tickers": tickers,
            "total": len(tickers)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/tickers/{ticker}/dates")
async def get_ticker_dates(ticker: str):
    dates = data_service.get_available_dates(ticker)
    
    if not dates['available']:
        raise HTTPException(status_code=404, detail=dates['message'])
    
    return dates

@router.get("/tickers/{ticker}/history")
async def get_ticker_history(ticker: str, days: int = 30):
    try:
        history = data_service.get_ticker_history(ticker, days)
        return history
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models")
async def get_models():
    try:
        models = model_loader.get_available_models()
        return {
            "models": models,
            "total": len(models),
            "default": "rf"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/dataset/info")
async def get_dataset_info():
    try:
        info = data_service.get_dataset_info()
        return info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
