class DivisionByNull:
    def __init__(self, divider, dividend):
        self.divider = divider
        self.denominator = dividend

    @staticmethod
    def divide_by_null(divider, dividend):
        try:
            return (divider / dividend)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.6))
print(div.divide_by_null(1, 0))
