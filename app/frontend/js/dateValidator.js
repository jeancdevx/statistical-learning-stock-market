export class DateValidator {
    constructor(minDate, maxDate) {
        this.minDate = new Date(minDate);
        this.maxDate = new Date(maxDate);
        this.nextDate = new Date(this.maxDate);
        this.nextDate.setDate(this.nextDate.getDate() + 1);
    }

    isValidDate(dateString) {
        const date = new Date(dateString);
        return date >= this.minDate && date <= this.maxDate;
    }

    isFutureDate(dateString) {
        const date = new Date(dateString);
        return date > this.maxDate;
    }

    isNextDay(dateString) {
        const date = new Date(dateString);
        return date.toDateString() === this.nextDate.toDateString();
    }

    canUseBacktest(dateString) {
        return this.isValidDate(dateString);
    }

    canUsePrediction(dateString) {
        return this.isNextDay(dateString);
    }

    getValidationMessage(dateString) {
        if (this.isNextDay(dateString)) {
            return { valid: true, mode: 'prediction', message: 'Predicción para el día siguiente' };
        }
        
        if (this.isValidDate(dateString)) {
            return { valid: true, mode: 'backtest', message: 'Usar modo backtest para fechas históricas' };
        }
        
        if (this.isFutureDate(dateString)) {
            return { valid: false, message: 'Solo se puede predecir el día siguiente' };
        }
        
        return { valid: false, message: 'Fecha fuera del rango disponible' };
    }

    formatDate(date) {
        return date.toISOString().split('T')[0];
    }

    getNextDayFormatted() {
        return this.formatDate(this.nextDate);
    }
}
