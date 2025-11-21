from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.api.routes import predict
from app.config import CORS_ORIGINS
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="NYSE Stock Predictor API",
    description="API REST para predicción de dirección de precios del mercado NYSE usando Random Forest",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict.router)

app.mount("/js", StaticFiles(directory="app/frontend/js"), name="js")

@app.get("/", include_in_schema=False)
async def root():
    """Serve the frontend application"""
    return FileResponse("app/frontend/index.html")

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "NYSE Stock Predictor API",
        "version": "1.0.0"
    }

@app.on_event("startup")
async def startup_event():
    logger.info("=" * 60)
    logger.info("🚀 NYSE Stock Predictor API iniciando...")
    logger.info("=" * 60)
    logger.info("📊 Versión: 1.0.0")
    logger.info("🌐 App: http://localhost:8000")
    logger.info("📚 API Docs: http://localhost:8000/docs")
    logger.info("=" * 60)
    
    logger.info("📦 Pre-cargando dataset...")
    try:
        from app.api.routes.predict import data_service
        data_service.load_dataset()
        logger.info("✓ Dataset pre-cargado y listo para usar")
    except Exception as e:
        logger.error(f"❌ Error pre-cargando dataset: {e}")
        logger.warning("⚠️  El dataset se cargará en la primera request")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("👋 NYSE Stock Predictor API detenida")
