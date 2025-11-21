export class TickerAutocomplete {
    constructor(inputElement, listElement, tickers) {
        this.input = inputElement;
        this.list = listElement;
        this.tickers = tickers;
        this.selectedIndex = -1;
        this.filteredTickers = [];
        
        this.input.addEventListener('input', () => this.handleInput());
        this.input.addEventListener('keydown', (e) => this.handleKeydown(e));
        document.addEventListener('click', (e) => this.handleClickOutside(e));
    }

    handleInput() {
        const value = this.input.value.toUpperCase();
        
        if (value.length === 0) {
            this.list.innerHTML = '';
            this.list.classList.add('hidden');
            return;
        }

        this.filteredTickers = this.tickers
            .filter(ticker => ticker.includes(value))
            .slice(0, 10);

        if (this.filteredTickers.length === 0) {
            this.list.innerHTML = '<div class="px-4 py-2 text-gray-500">No se encontraron resultados</div>';
            this.list.classList.remove('hidden');
            return;
        }

        this.list.innerHTML = this.filteredTickers.map((ticker, index) => 
            `<div class="autocomplete-item px-4 py-2 hover:bg-blue-50 cursor-pointer ${index === this.selectedIndex ? 'bg-blue-50' : ''}" 
                 data-ticker="${ticker}">
                ${ticker}
            </div>`
        ).join('');
        
        this.list.querySelectorAll('.autocomplete-item').forEach(item => {
            item.addEventListener('click', () => this.selectTicker(item.dataset.ticker));
        });
        
        this.list.classList.remove('hidden');
    }

    handleKeydown(e) {
        if (this.filteredTickers.length === 0) return;

        if (e.key === 'ArrowDown') {
            e.preventDefault();
            this.selectedIndex = (this.selectedIndex + 1) % this.filteredTickers.length;
            this.updateSelection();
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            this.selectedIndex = this.selectedIndex <= 0 ? 
                this.filteredTickers.length - 1 : this.selectedIndex - 1;
            this.updateSelection();
        } else if (e.key === 'Enter' && this.selectedIndex >= 0) {
            e.preventDefault();
            this.selectTicker(this.filteredTickers[this.selectedIndex]);
        } else if (e.key === 'Escape') {
            this.list.classList.add('hidden');
        }
    }

    updateSelection() {
        const items = this.list.querySelectorAll('.autocomplete-item');
        items.forEach((item, index) => {
            if (index === this.selectedIndex) {
                item.classList.add('bg-blue-50');
            } else {
                item.classList.remove('bg-blue-50');
            }
        });
    }

    selectTicker(ticker) {
        this.input.value = ticker;
        this.list.classList.add('hidden');
        this.selectedIndex = -1;
        this.input.dispatchEvent(new Event('ticker-selected'));
    }

    handleClickOutside(e) {
        if (!this.input.contains(e.target) && !this.list.contains(e.target)) {
            this.list.classList.add('hidden');
        }
    }
}
