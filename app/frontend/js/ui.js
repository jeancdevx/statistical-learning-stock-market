export class UIManager {
  constructor() {
    this.elements = {
      totalTickers: document.getElementById('totalTickers'),
      totalModels: document.getElementById('totalModels'),
      systemStatus: document.getElementById('systemStatus'),
      predictBtn: document.getElementById('predictBtn'),
      resultsPanel: document.getElementById('resultsPanel'),
      predictionCard: document.getElementById('predictionCard'),
      probabilityBar: document.getElementById('probabilityBar'),
      probabilityValue: document.getElementById('probabilityValue'),
      confidenceLevel: document.getElementById('confidenceLevel'),
      backtestCard: document.getElementById('backtestCard'),
      realDirection: document.getElementById('realDirection'),
      realChange: document.getElementById('realChange'),
      validationResult: document.getElementById('validationResult'),
      dateInfo: document.getElementById('dateInfo'),
      openPrice: document.getElementById('openPrice'),
      highPrice: document.getElementById('highPrice'),
      lowPrice: document.getElementById('lowPrice'),
      closePrice: document.getElementById('closePrice')
    }
  }

  showLoading() {
    this.elements.predictBtn.disabled = true
    this.elements.predictBtn.innerHTML = `
            <svg class="animate-spin h-5 w-5 mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            Procesando...
        `
  }

  hideLoading() {
    this.elements.predictBtn.disabled = false
    this.elements.predictBtn.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-8.707l-3-3a1 1 0 00-1.414 1.414L10.586 9H7a1 1 0 100 2h3.586l-1.293 1.293a1 1 0 101.414 1.414l3-3a1 1 0 000-1.414z" clip-rule="evenodd" />
            </svg>
            Predecir
        `
  }

  updateStats(tickersCount, modelsCount, systemStatus) {
    this.elements.totalTickers.textContent = tickersCount.toLocaleString()
    this.elements.totalModels.textContent = modelsCount
    const statusEmoji = systemStatus === 'Operativo' ? '🟢' : '🔴'
    this.elements.systemStatus.textContent = statusEmoji
  }

  showError(message) {
    alert(message)
  }

  showResults() {
    this.elements.resultsPanel.classList.remove('hidden')
  }

  hideResults() {
    this.elements.resultsPanel.classList.add('hidden')
  }

  displayPrediction(direction, directionText, probability, confidence, dates) {
    const isUp = direction === 1

    this.elements.predictionCard.className = `text-center p-8 rounded-lg ${
      isUp
        ? 'bg-green-50 border-2 border-green-200'
        : 'bg-red-50 border-2 border-red-200'
    }`
    this.elements.predictionCard.innerHTML = `
            <div class="text-6xl mb-4">${isUp ? '📈' : '📉'}</div>
            <div class="text-3xl font-bold ${
              isUp ? 'text-green-700' : 'text-red-700'
            } mb-2">
                ${directionText}
            </div>
            <div class="text-gray-600 text-sm">Predicción: ${
              direction === 1 ? '+1' : '0'
            }</div>
        `

    const probabilityPercent = (probability * 100).toFixed(1)
    this.elements.probabilityBar.style.width = probabilityPercent + '%'
    this.elements.probabilityBar.className = `h-full rounded-full transition-all duration-500 ${
      isUp ? 'bg-green-500' : 'bg-red-500'
    }`
    this.elements.probabilityValue.textContent = probabilityPercent + '%'

    const confidenceColors = {
      Alta: 'text-green-600',
      Media: 'text-yellow-600',
      Baja: 'text-red-600'
    }
    this.elements.confidenceLevel.textContent = confidence
    this.elements.confidenceLevel.className = `font-semibold ${
      confidenceColors[confidence] || 'text-gray-600'
    }`

    if (dates) {
      this.elements.dateInfo.innerHTML = `
                <p class="text-sm text-gray-600">Datos hasta: <span class="font-semibold">${dates.data_until}</span></p>
                <p class="text-sm text-gray-600">Prediciendo para: <span class="font-semibold">${dates.predicting_for}</span></p>
            `
    } else {
      this.elements.dateInfo.innerHTML = ''
    }
  }

  displayBacktest(real, isCorrect) {
    this.elements.backtestCard.classList.remove('hidden')

    const isRealUp = real.direction === 1
    const priceChange = real.open - real.prev_close
    const changeClass = real.change_pct >= 0 ? 'text-green-600' : 'text-red-600'

    this.elements.backtestCard.innerHTML = `
            <h4 class="font-semibold text-gray-800 mb-4 flex items-center">
                <svg class="w-5 h-5 mr-2 ${
                  isCorrect ? 'text-green-600' : 'text-red-600'
                }" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="${
                      isCorrect ? 'M5 13l4 4L19 7' : 'M6 18L18 6M6 6l12 12'
                    }"></path>
                </svg>
                Comparación con Datos Reales
            </h4>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                <div class="bg-blue-50 p-4 rounded-lg text-center">
                    <p class="text-xs text-gray-600 font-medium mb-2">Dirección Real</p>
                    <p class="text-2xl font-bold ${
                      isRealUp ? 'text-green-600' : 'text-red-600'
                    }">
                        ${isRealUp ? '📈 SUBIDA' : '📉 BAJADA'}
                    </p>
                </div>
                <div class="bg-green-50 p-4 rounded-lg text-center">
                    <p class="text-xs text-gray-600 font-medium mb-2">Cambio Real</p>
                    <p class="text-2xl font-bold ${changeClass}">
                        ${priceChange >= 0 ? '+' : ''}$${Math.abs(
      priceChange
    ).toFixed(2)}
                    </p>
                    <p class="text-sm ${changeClass}">
                        ${
                          real.change_pct >= 0 ? '+' : ''
                        }${real.change_pct.toFixed(2)}%
                    </p>
                </div>
                <div class="bg-gray-50 p-4 rounded-lg text-center">
                    <p class="text-xs text-gray-600 font-medium mb-2">Validación</p>
                    <p class="text-2xl font-bold ${
                      isCorrect ? 'text-green-600' : 'text-red-600'
                    }">
                        ${isCorrect ? '✓ CORRECTO' : '✗ INCORRECTO'}
                    </p>
                </div>
            </div>
            
            <div class="bg-gray-50 rounded-lg p-4 border-l-4 ${
              isCorrect ? 'border-green-500' : 'border-red-500'
            }">
                <p class="text-sm text-gray-700 mb-2">
                    <span class="font-semibold">Cierre del día anterior:</span> $${real.prev_close.toFixed(
                      2
                    )}
                </p>
                <p class="text-sm text-gray-700 mb-2">
                    <span class="font-semibold">Apertura del día siguiente:</span> $${real.open.toFixed(
                      2
                    )}
                </p>
                <p class="text-sm text-gray-700">
                    <span class="font-semibold">Diferencia:</span> 
                    <span class="${changeClass}">
                        ${priceChange >= 0 ? '+' : ''}$${priceChange.toFixed(
      2
    )} 
                        (${
                          real.change_pct >= 0 ? '+' : ''
                        }${real.change_pct.toFixed(2)}%)
                    </span>
                </p>
            </div>
            
            <div class="mt-4 p-3 bg-blue-50 rounded-lg">
                <p class="text-xs text-blue-800 font-medium mb-1">
                    💡 ¿Qué es el gap overnight?
                </p>
                <p class="text-xs text-blue-700">
                    Es la diferencia entre el <strong>cierre de un día</strong> y la <strong>apertura del día siguiente</strong>. 
                    El modelo predice si esta diferencia será positiva (SUBIDA) o negativa/cero (BAJADA).
                </p>
                <p class="text-xs text-gray-600 mt-2 text-center">
                    ${
                      isCorrect
                        ? '🎯 El modelo acertó la dirección del gap'
                        : '❌ El modelo no acertó la dirección del gap'
                    }
                </p>
            </div>
        `
  }

  hideBacktest() {
    this.elements.backtestCard.classList.add('hidden')
  }

  displayPrices(prices) {
    this.elements.openPrice.textContent = '$' + prices.open.toFixed(2)
    this.elements.highPrice.textContent = '$' + prices.high.toFixed(2)
    this.elements.lowPrice.textContent = '$' + prices.low.toFixed(2)
    this.elements.closePrice.textContent = '$' + prices.close.toFixed(2)
  }

  displayTickerInfo(ticker, logoUrl) {
    const tickerInfoElement = document.getElementById('tickerInfo')
    if (!tickerInfoElement) return

    tickerInfoElement.innerHTML = `
            <div class="flex items-center space-x-4 p-4 bg-white rounded-lg shadow-sm">
                <img 
                    src="${logoUrl}" 
                    alt="${ticker}" 
                    class="w-12 h-12 rounded-lg object-contain"
                />
                <div>
                    <div class="text-2xl font-bold text-gray-800">${ticker}</div>
                    <div class="text-sm text-gray-500">NYSE Stock</div>
                </div>
            </div>
        `
    tickerInfoElement.classList.remove('hidden')
  }

  displayMetrics(prices, features) {
    const metricsElement = document.getElementById('additionalMetrics')
    if (!metricsElement || !prices || !features) return

    const priceChange = prices.close - prices.open
    const priceChangePercent = (priceChange / prices.open) * 100
    const dayRange = prices.high - prices.low
    const dayRangePercent = (dayRange / prices.close) * 100

    const vol5 = features.vol_5 || features.std_5 || 0
    const rsi = features.rsi_14 || 50

    metricsElement.innerHTML = `
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div class="text-center p-3 bg-gray-50 rounded-lg">
                    <p class="text-xs text-gray-600 mb-1">Cambio Diario</p>
                    <p class="text-lg font-bold ${
                      priceChange >= 0 ? 'text-green-600' : 'text-red-600'
                    }">
                        ${priceChange >= 0 ? '+' : ''}${priceChange.toFixed(2)}
                    </p>
                    <p class="text-xs ${
                      priceChange >= 0 ? 'text-green-600' : 'text-red-600'
                    }">
                        ${
                          priceChange >= 0 ? '+' : ''
                        }${priceChangePercent.toFixed(2)}%
                    </p>
                </div>
                <div class="text-center p-3 bg-gray-50 rounded-lg">
                    <p class="text-xs text-gray-600 mb-1">Rango del Día</p>
                    <p class="text-lg font-bold text-gray-800">$${dayRange.toFixed(
                      2
                    )}</p>
                    <p class="text-xs text-gray-600">${dayRangePercent.toFixed(
                      2
                    )}%</p>
                </div>
                <div class="text-center p-3 bg-gray-50 rounded-lg">
                    <p class="text-xs text-gray-600 mb-1">Volatilidad 5d</p>
                    <p class="text-lg font-bold text-gray-800">${(
                      vol5 * 100
                    ).toFixed(2)}%</p>
                </div>
                <div class="text-center p-3 bg-gray-50 rounded-lg">
                    <p class="text-xs text-gray-600 mb-1">RSI (14)</p>
                    <p class="text-lg font-bold ${
                      rsi > 70
                        ? 'text-red-600'
                        : rsi < 30
                        ? 'text-green-600'
                        : 'text-gray-800'
                    }">
                        ${rsi.toFixed(1)}
                    </p>
                    <p class="text-xs text-gray-600">
                        ${
                          rsi > 70
                            ? 'Sobrecompra'
                            : rsi < 30
                            ? 'Sobreventa'
                            : 'Neutral'
                        }
                    </p>
                </div>
            </div>
        `
    metricsElement.classList.remove('hidden')
  }

  formatTimeAgo(dateString) {
    const date = new Date(dateString)
    const now = new Date()
    const diffTime = Math.abs(now - date)
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24))

    if (diffDays === 0) return 'Hoy'
    if (diffDays === 1) return 'Ayer'
    if (diffDays < 7) return `Hace ${diffDays} días`
    if (diffDays < 30) return `Hace ${Math.floor(diffDays / 7)} semanas`
    return `Hace ${Math.floor(diffDays / 30)} meses`
  }
}
