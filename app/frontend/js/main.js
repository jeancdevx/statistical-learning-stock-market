import {
  backtest,
  fetchModels,
  fetchSystemHealth,
  fetchTickerDates,
  fetchTickerHistory,
  fetchTickers,
  predict
} from '/js/api.js'
import { TickerAutocomplete } from '/js/autocomplete.js'
import { ChartManager } from '/js/chart.js'
import { DateValidator } from '/js/dateValidator.js'
import { UIManager } from '/js/ui.js'

class StockPredictionApp {
  constructor() {
    this.ui = new UIManager()
    this.chartManager = new ChartManager()
    this.dateValidator = null
    this.autocomplete = null
    this.tickers = []
    this.currentHistoryData = null

    this.initializeApp()
  }

  async initializeApp() {
    await this.loadSystemStats()
    await this.loadTickers()
    this.setupEventListeners()
  }

  async loadSystemStats() {
    try {
      const [health, modelsData] = await Promise.all([
        fetchSystemHealth(),
        fetchModels()
      ])

      const tickersData = await fetchTickers()
      this.ui.updateStats(
        tickersData.total,
        modelsData.total,
        health.status === 'healthy' ? 'Operativo' : 'Inactivo'
      )
    } catch (error) {
      console.error('Error loading system stats:', error)
    }
  }

  async loadTickers() {
    try {
      const data = await fetchTickers()
      this.tickers = data.tickers

      const tickerInput = document.getElementById('tickerInput')
      const tickerSuggestions = document.getElementById('tickerSuggestions')
      this.autocomplete = new TickerAutocomplete(
        tickerInput,
        tickerSuggestions,
        this.tickers
      )

      tickerInput.addEventListener('ticker-selected', () =>
        this.handleTickerSelected()
      )
    } catch (error) {
      console.error('Error loading tickers:', error)
    }
  }

  async handleTickerSelected() {
    const ticker = document.getElementById('tickerInput').value
    if (!ticker) return

    try {
      const [dates, history] = await Promise.all([
        fetchTickerDates(ticker),
        fetchTickerHistory(ticker, 9999).catch(() => null)
      ])

      if (!dates.available) {
        this.ui.showError(dates.message)
        return
      }

      this.dateValidator = new DateValidator(dates.min_date, dates.max_date)

      const dateInput = document.getElementById('dateInput')
      dateInput.min = dates.min_date
      dateInput.max = this.dateValidator.getNextDayFormatted()
      dateInput.value = this.dateValidator.getNextDayFormatted()
      dateInput.disabled = false

      import('/js/config.js').then(({ LOGO_API }) => {
        this.ui.displayTickerInfo(ticker, LOGO_API.getLogoUrl(ticker))
      })

      if (history) {
        this.currentHistoryData = history
        this.chartManager.createPriceHistoryChart(history, 'ALL')
        document
          .getElementById('priceHistoryContainer')
          ?.classList.remove('hidden')
      }

      this.updateDateValidation()
    } catch (error) {
      console.error('Error loading ticker dates:', error)
    }
  }

  changeTimeRange(range) {
    if (this.currentHistoryData) {
      this.chartManager.createPriceHistoryChart(this.currentHistoryData, range)

      document
        .querySelectorAll('#priceHistoryContainer button')
        .forEach((btn) => {
          btn.classList.remove('bg-blue-100', 'font-semibold')
          btn.classList.add('hover:bg-blue-50')
        })

      event.target.classList.add('bg-blue-100', 'font-semibold')
      event.target.classList.remove('hover:bg-blue-50')
    }
  }

  setupEventListeners() {
    const dateInput = document.getElementById('dateInput')
    const backtestCheckbox = document.getElementById('backtestMode')
    const predictBtn = document.getElementById('predictBtn')

    dateInput.addEventListener('change', () => this.updateDateValidation())
    backtestCheckbox.addEventListener('change', () =>
      this.updateDateValidation()
    )
    predictBtn.addEventListener('click', () => this.handlePrediction())
  }

  updateDateValidation() {
    if (!this.dateValidator) return

    const dateInput = document.getElementById('dateInput')
    const backtestCheckbox = document.getElementById('backtestMode')
    const dateWarning = document.getElementById('dateWarning')
    const predictBtn = document.getElementById('predictBtn')

    const selectedDate = dateInput.value
    const validation = this.dateValidator.getValidationMessage(selectedDate)

    if (!validation.valid) {
      dateWarning.textContent = validation.message
      dateWarning.classList.remove('hidden')
      predictBtn.disabled = true
      return
    }

    if (validation.mode === 'prediction' && !backtestCheckbox.checked) {
      dateWarning.classList.add('hidden')
      predictBtn.disabled = false
    } else if (validation.mode === 'backtest' && backtestCheckbox.checked) {
      dateWarning.classList.add('hidden')
      predictBtn.disabled = false
    } else if (validation.mode === 'prediction' && backtestCheckbox.checked) {
      dateWarning.textContent =
        'No se puede hacer backtest del día siguiente (aún no hay datos reales)'
      dateWarning.classList.remove('hidden')
      predictBtn.disabled = true
    } else {
      dateWarning.textContent = validation.message
      dateWarning.classList.remove('hidden')
      predictBtn.disabled = true
    }
  }

  async handlePrediction() {
    const ticker = document.getElementById('tickerInput').value
    const date = document.getElementById('dateInput').value
    const model = document.getElementById('modelSelect').value
    const isBacktest = document.getElementById('backtestMode').checked

    if (!ticker || !date) {
      this.ui.showError('Por favor completa todos los campos')
      return
    }

    this.ui.showLoading()
    this.ui.hideResults()

    try {
      let data

      if (isBacktest) {
        data = await backtest(ticker, date, model)
        this.displayBacktestResults(data)
      } else {
        data = await predict(ticker, model)
        this.displayPredictionResults(data)
      }
    } catch (error) {
      console.error('Prediction error:', error)
      this.ui.showError(error.message || 'Error al realizar la predicción')
    } finally {
      this.ui.hideLoading()
    }
  }

  displayPredictionResults(data) {
    this.ui.showResults()
    this.ui.hideBacktest()

    this.ui.displayPrediction(
      data.prediction.direction,
      data.prediction.direction_text,
      data.prediction.probability,
      data.prediction.confidence,
      data.dates
    )

    if (data.features && data.prices) {
      this.chartManager.createIndicatorsChart(data.features)
      this.ui.displayPrices(data.prices)
      this.ui.displayMetrics(data.prices, data.features)
    }
  }

  displayBacktestResults(data) {
    this.ui.showResults()

    this.ui.displayPrediction(
      data.prediction,
      data.direction_text,
      data.probability,
      data.confidence,
      null
    )

    if (data.validation_available && data.real) {
      this.ui.displayBacktest(data.real, data.is_correct)
    }

    if (data.features && data.prices) {
      this.chartManager.createIndicatorsChart(data.features)
      this.ui.displayPrices(data.prices)
      this.ui.displayMetrics(data.prices, data.features)
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.stockApp = new StockPredictionApp()
})
