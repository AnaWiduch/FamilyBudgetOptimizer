a, b = float(input()), float(input())
c = a * 100 + b * 100

vacation = 0.1 * c
food = 0.3 * c
utility_bills = 0.05 * c
leisure = 0.15 * c
savings = 0.4 * c + (vacation - int(vacation)) + (food - int(food)) + (utility_bills - int(utility_bills)) + (leisure - int(leisure))

print(f'Vacation: {int(vacation) // 100} rub. {int(vacation) % 100} kop.')
print(f'Food and Groceries: {int(food) // 100} rub. {int(food) % 100} kop.')
print(f'Utility Bills: {int(utility_bills) // 100} rub. {int(utility_bills) % 100} kop.')
print(f'Leisure: {int(leisure) // 100} rub. {int(leisure) % 100} kop.')
print(f'Savings: {int(savings) // 100} rub. {int(savings) % 100} kop.')
