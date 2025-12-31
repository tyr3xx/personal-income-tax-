class TaxCalculator:
    def __init__(self, status, income):
        self.status = status
        self.income = income

    def calculate_tax(self):
        tax = 0

        # SINGLE
        if self.status == 0:
            if self.income <= 8350:
                tax = self.income * 0.10
            elif self.income <= 33950:
                tax = 8350 * 0.10 + (self.income - 8350) * 0.15
            elif self.income <= 82250:
                tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (self.income - 33950) * 0.25
            else:
                tax = (
                    8350 * 0.10 +
                    (33950 - 8350) * 0.15 +
                    (82250 - 33950) * 0.25 +
                    (self.income - 82250) * 0.28
                )

        # MARRIED FILING JOINTLY
        elif self.status == 1:
            if self.income <= 16700:
                tax = self.income * 0.10
            elif self.income <= 67900:
                tax = 16700 * 0.10 + (self.income - 16700) * 0.15
            else:
                tax = (
                    16700 * 0.10 +
                    (67900 - 16700) * 0.15 +
                    (self.income - 67900) * 0.25
                )

        # MARRIED FILING SEPARATELY
        elif self.status == 2:
            if self.income <= 8350:
                tax = self.income * 0.10
            elif self.income <= 33950:
                tax = 8350 * 0.10 + (self.income - 8350) * 0.15
            else:
                tax = (
                    8350 * 0.10 +
                    (33950 - 8350) * 0.15 +
                    (self.income - 33950) * 0.25
                )

        # HEAD OF HOUSEHOLD
        elif self.status == 3:
            if self.income <= 11950:
                tax = self.income * 0.10
            elif self.income <= 45500:
                tax = 11950 * 0.10 + (self.income - 11950) * 0.15
            else:
                tax = (
                    11950 * 0.10 +
                    (45500 - 11950) * 0.15 +
                    (self.income - 45500) * 0.25
                )

        return tax


print("Enter filing status:")
print("0 - Single")
print("1 - Married Filing Jointly")
print("2 - Married Filing Separately")
print("3 - Head of Household")

status = int(input("Status: "))
income = float(input("Taxable income: "))

tax_object = TaxCalculator(status, income)
tax = tax_object.calculate_tax()

print("Your tax is $", round(tax, 2))
