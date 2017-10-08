class Mortgage():
    def __init__(self, debt, year_rate, payback_period_in_years):
        self.debt = debt
        if year_rate > 1:
            self.month_rate = year_rate/100/12
        else:
            self.month_rate = year_rate/12
        self.payback_period_in_months = payback_period_in_years*12
        self.payment = Mortgage.update_payment(self)

    def __str__(self):
        return "Debt: {} rub,\nMonth rate: {}%,\nPayback period: {} years ({} months,\nPayment: {:.2f} rub".format(self.debt,
                                                                               self.month_rate*12,
                                                                               self.payback_period_in_months/12,
                                                                               self.payback_period_in_months,
                                                                                                       self.payment)

    def update_payment(self):
        i = self.month_rate
        n = self.payback_period_in_months
        d = self.debt
        return d*i*((1+i)**n)/((1+i)**n-1)

if __name__ == "__main__":
    my = Mortgage(2650000, 7.5, 7)
    print(my)