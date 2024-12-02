const FinancialCalculator = require('./FinancialCalculator');
const assert = require('assert');

describe('FinancialCalculator', function () {
    let calculator;

    beforeEach(function () {
        calculator = new FinancialCalculator(1000);
    });

    it('compoundInterestTest', function () {
        const result = calculator.compoundInterest(5, 10);
        assert.strictEqual(result, 1628.89);
    });

    it('loanPaymentTest', function () {
        const result = calculator.loanPayment(50000, 5, 15);
        assert.strictEqual(result, 395.64);
    });

    it('netPresentValueTest', function () {
        const cashFlows = [1000, 800, 600, 400, 200];
        const result = calculator.netPresentValue(5, cashFlows);
        assert.strictEqual(result, 2843.58);
    });

    it('internalRateOfReturnTest', function () {
        const cashFlows = [-5000, 2000, 2000, 2000, 1000];
        const result = calculator.internalRateOfReturn(cashFlows);
        assert(result > 0 && result < 0.5);
    });
    
});