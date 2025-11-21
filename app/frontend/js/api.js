import { API_BASE_URL, API_ENDPOINTS } from '/js/config.js';

export async function fetchSystemHealth() {
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.health}`);
    return await response.json();
}

export async function fetchModels() {
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.models}`);
    return await response.json();
}

export async function fetchTickers() {
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.tickers}`);
    return await response.json();
}

export async function fetchTickerDates(ticker) {
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.tickerDates(ticker)}`);
    return await response.json();
}

export async function predict(ticker, model) {
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.predict}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ticker, model })
    });
    
    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Error en la predicción');
    }
    
    return await response.json();
}

export async function backtest(ticker, date, model) {
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.backtest}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ticker, date, model })
    });
    
    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Error en el backtest');
    }
    
    return await response.json();
}

export async function fetchTickerHistory(ticker, days = 30) {
    const response = await fetch(`${API_BASE_URL}${API_ENDPOINTS.tickerHistory(ticker)}?days=${days}`);
    
    if (!response.ok) {
        throw new Error('Error al obtener historial');
    }
    
    return await response.json();
}
