export const API_BASE_URL = 'http://localhost:8000'

export const API_ENDPOINTS = {
  health: '/health',
  predict: '/api/v1/predict',
  backtest: '/api/v1/backtest',
  tickers: '/api/v1/tickers',
  tickerDates: (ticker) => `/api/v1/tickers/${ticker}/dates`,
  tickerHistory: (ticker) => `/api/v1/tickers/${ticker}/history`,
  models: '/api/v1/models',
  datasetInfo: '/api/v1/dataset/info'
}

export const CHART_COLORS = {
  primary: 'rgba(59, 130, 246, 0.8)',
  secondary: 'rgba(156, 163, 175, 0.6)',
  success: 'rgba(34, 197, 94, 0.8)',
  danger: 'rgba(239, 68, 68, 0.8)',
  warning: 'rgba(251, 191, 36, 0.8)'
}

export const LOGO_API = {
  getLogoUrl: (ticker) => {
    const cleanTicker = ticker.replace('.US', '').toUpperCase()
    return `https://financialmodelingprep.com/image-stock/${cleanTicker}.png`
  },
  fallbackUrl:
    'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y=".9em" font-size="90">📊</text></svg>'
}
