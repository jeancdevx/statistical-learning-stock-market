import { CHART_COLORS } from '/js/config.js';

export class ChartManager {
    constructor() {
        this.chartInstance = null;
    }

    createIndicatorsChart(features) {
        const canvas = document.getElementById('indicatorsChart');
        const ctx = canvas.getContext('2d');

        if (this.chartInstance) {
            this.chartInstance.destroy();
        }

        const labels = Object.keys(features);
        const originalValues = Object.values(features);
        
        const normalizedData = originalValues.map(val => {
            if (Math.abs(val) > 1000) {
                return val / 100000;
            }
            return val;
        });

        this.chartInstance = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Valor',
                    data: normalizedData,
                    backgroundColor: CHART_COLORS.primary,
                    borderColor: CHART_COLORS.primary,
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    title: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const originalValue = originalValues[context.dataIndex];
                                return `Valor: ${originalValue.toFixed(4)}`;
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: false,
                        grid: {
                            color: 'rgba(0, 0, 0, 0.05)'
                        },
                        ticks: {
                            callback: function(value) {
                                return value.toFixed(2);
                            }
                        }
                    },
                    x: {
                        grid: {
                            display: false
                        },
                        ticks: {
                            maxRotation: 45,
                            minRotation: 45
                        }
                    }
                }
            }
        });
    }

    createPriceHistoryChart(historyData, range = 'ALL') {
        const canvas = document.getElementById('priceHistoryChart');
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');

        if (this.priceChartInstance) {
            this.priceChartInstance.destroy();
        }

        this.fullHistoryData = historyData;

        let filteredData = this.filterDataByRange(historyData, range);

        const candlestickData = filteredData.dates.map((date, i) => ({
            x: new Date(date).getTime(),
            o: filteredData.open[i],
            h: filteredData.high[i],
            l: filteredData.low[i],
            c: filteredData.close[i]
        }));

        this.priceChartInstance = new Chart(ctx, {
            type: 'candlestick',
            data: {
                datasets: [{
                    label: 'Precio',
                    data: candlestickData,
                    borderColor: {
                        up: 'rgba(34, 197, 94, 1)',
                        down: 'rgba(239, 68, 68, 1)',
                        unchanged: 'rgba(156, 163, 175, 1)'
                    },
                    backgroundColor: {
                        up: 'rgba(34, 197, 94, 0.3)',
                        down: 'rgba(239, 68, 68, 0.3)',
                        unchanged: 'rgba(156, 163, 175, 0.3)'
                    }
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            title: function(context) {
                                const date = new Date(context[0].parsed.x);
                                return date.toLocaleDateString('es-ES', { 
                                    year: 'numeric', 
                                    month: 'short', 
                                    day: 'numeric' 
                                });
                            },
                            label: function(context) {
                                const data = context.raw;
                                const idx = filteredData.dates.findIndex(d => 
                                    new Date(d).getTime() === data.x
                                );
                                const vol = idx >= 0 ? filteredData.volume[idx] : 0;
                                
                                return [
                                    `Apertura: $${data.o.toFixed(2)}`,
                                    `Máximo: $${data.h.toFixed(2)}`,
                                    `Mínimo: $${data.l.toFixed(2)}`,
                                    `Cierre: $${data.c.toFixed(2)}`,
                                    `Volumen: ${(vol / 1000000).toFixed(2)}M`
                                ];
                            }
                        }
                    }
                },
                scales: {
                    x: {
                        type: 'time',
                        time: {
                            unit: this.getTimeUnit(range),
                            displayFormats: {
                                day: 'MMM dd',
                                week: 'MMM dd',
                                month: 'MMM yyyy',
                                quarter: 'MMM yyyy',
                                year: 'yyyy'
                            }
                        },
                        grid: {
                            display: false
                        },
                        ticks: {
                            maxRotation: 0,
                            autoSkip: true,
                            maxTicksLimit: 10
                        }
                    },
                    y: {
                        position: 'right',
                        grid: {
                            color: 'rgba(0, 0, 0, 0.05)'
                        },
                        ticks: {
                            callback: function(value) {
                                return '$' + value.toFixed(2);
                            }
                        }
                    }
                }
            }
        });
    }

    getTimeUnit(range) {
        switch(range) {
            case '1M': return 'day';
            case '3M': return 'week';
            case '6M': return 'week';
            case '1Y': return 'month';
            case 'ALL': return 'month';
            default: return 'day';
        }
    }

    filterDataByRange(data, range) {
        if (range === 'ALL' || !data.dates || data.dates.length === 0) {
            return data;
        }

        const lastDate = new Date(data.dates[data.dates.length - 1]);
        let cutoffDate = new Date(lastDate);

        switch(range) {
            case '1M':
                cutoffDate.setMonth(cutoffDate.getMonth() - 1);
                break;
            case '3M':
                cutoffDate.setMonth(cutoffDate.getMonth() - 3);
                break;
            case '6M':
                cutoffDate.setMonth(cutoffDate.getMonth() - 6);
                break;
            case '1Y':
                cutoffDate.setFullYear(cutoffDate.getFullYear() - 1);
                break;
        }

        const cutoffTime = cutoffDate.getTime();
        const startIndex = data.dates.findIndex(date => new Date(date).getTime() >= cutoffTime);
        
        if (startIndex === -1) return data;

        return {
            dates: data.dates.slice(startIndex),
            open: data.open.slice(startIndex),
            high: data.high.slice(startIndex),
            low: data.low.slice(startIndex),
            close: data.close.slice(startIndex),
            volume: data.volume.slice(startIndex)
        };
    }

    destroy() {
        if (this.chartInstance) {
            this.chartInstance.destroy();
            this.chartInstance = null;
        }
        if (this.priceChartInstance) {
            this.priceChartInstance.destroy();
            this.priceChartInstance = null;
        }
    }
}
