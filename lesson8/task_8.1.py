class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if year >= 0:
                    return f'OK'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'дата {Date.extract(self.day_month_year)}'


day = Date('25 - 4 - 1996')
print(day)
print(Date.valid(11, 11, 2023))
print(day.valid(11, 13, 1999))
print(day.extract('11 - 11 - 2020'))
print(Date.valid(1, 11, 2000))
