from random import sample


class Lottery:
    '''
    Создает список в котором есть значения из
    которых будет формироваться выгрышная комбинация
    '''
    values = (4, 7, 98, 'a', 6, 7, 45, 'b', 'zec', 9, 1, 4, 111, 'fgg', 'ya')

    def winning_combination(self):
        winning_combination = sample(self.values, 4)
        return winning_combination

    def generates_tickets(self):
        ticket = sample(self.values, 4)
        return ticket