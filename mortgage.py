class Mortgage():
    def __init__(self, debt, year_rate, payback_period_in_years):
        self.debt = debt
        self.start_debt = debt
        self.paid_month = 0
        if year_rate > 1:
            self.month_rate = year_rate/100/12
        else:
            self.month_rate = year_rate/12
        self.payback_period_in_months = payback_period_in_years*12
        self.payment = Mortgage.update_payment(self)
        self.paid = 0

    def __str__(self):
        vars_for_format= self.debt, \
                         self.month_rate*12, \
                         self.payback_period_in_months/12, \
                         self.payback_period_in_months, \
                         self.payment
        return "Debt: {:.2f} rub,\nMonth rate: {}%,\nPayback period: {:.2f} years ({:d} months),\nPayment: {:.2f} rub".format(*vars_for_format)

    def update_payment(self):
        i = self.month_rate
        n = self.payback_period_in_months
        d = self.debt
        return d*i*((1+i)**n)/((1+i)**n-1)

    def update_debt(self):
        i = self.month_rate
        n = self.payback_period_in_months
        if n > 1:
            return self.payment/(i*((1+i)**n)/((1+i)**n-1))
        else:
            return self.debt - self.payment

    def make_payment(self, payment=None):
        if payment is None:
            payment = self.payment
        self.paid += payment
        self.paid_month += 1
        self.payback_period_in_months -= 1
        self.debt = Mortgage.update_debt(self)
        if payment > self.payment:
            self.debt = self.debt - (payment-self.payment)
            self.payment = Mortgage.update_payment(self)


if __name__ == "__main__":
    my = Mortgage(2650000, 7.5, 7)
    print(my)
    while my.debt > 0:
        my.make_payment(80000)
    print(my.start_debt, my.paid, my.paid-my.start_debt, my.paid_month, my.paid_month/12)
