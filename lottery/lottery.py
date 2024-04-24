from models_lottery import Lottery

lottery = Lottery()
winning_combination = lottery.winning_combination()

count = 0
flag = True

while flag:
    ticket = lottery.generates_tickets()
    count += 1
    print(count)
    if ticket == winning_combination:
        flag = False

print(count)
