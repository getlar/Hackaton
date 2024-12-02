class FinancialCalculator {
    constructor(initialBalance = 0) {
        this.balance = initialBalance;
    }

    compoundInterest(rate, years) {
        return this.balance * (Math.pow((1 + rate / 100), years));
    }

    loanPayment(principal, rate, years) {
        const monthlyRate = rate / 100 / 12;
        const n = years * 12;
        return (principal * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -n));
    }

    netPresentValue(rate, cashFlows) {
        let npv = 0;
        for (let i = 0; i < cashFlows.length; i++) {
            npv += cashFlows[i] / Math.pow(1 + rate / 100, i + 1);
        }
        return npv;
    }

    internalRateOfReturn(cashFlows) {
        let rate = 0.1;
        let npv;
        do {
            npv = this.netPresentValue(rate, cashFlows);
            rate += 0.001;
        } while (npv > 0);
        return rate;
    }
}

module.exports = FinancialCalculator;