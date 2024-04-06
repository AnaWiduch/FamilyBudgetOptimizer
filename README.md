# FamilyBudgetOptimizer
It takes the monthly incomes of a husband and wife as input and calculates the amount to be allocated to each category according to the specified percentages.  



The Family Budget Optimizer program helps families optimize their financial expenses by calculating how much money should be allocated to each category based on a predefined scheme.

The family has devised the following scheme:

10% of the income is allocated for vacation
30% of the income is allocated for food and groceries
5% for utility bills
15% for leisure activities
the remaining 40% is saved
If it's impossible to allocate the exact percentage due to fractional amounts, the excess goes into savings. For example:

If the income is 50,001.25 rubles, 10% of this amount is 5000.125 rubles. Since there is no half kopeck in currency, this excess goes into savings.

The program takes two float numbers as input, where the integer part represents rubles and the fractional part represents kopecks.

The output displays the amount in rubles and kopecks for each category in the following format:

Vacation: 10 rub. 5 kop.
Food and Groceries: 30 rub. 15 kop.
Utility Bills: 5 rub. 0 kop.
Leisure: 10 rub. 11 kop.
Savings: 50 rub. 3 kop.

Sample Input 1:

30000.50

20000.75

Sample Output 1:

Vacation: 5000 rub. 12 kop.
Food and Groceries: 15000 rub. 37 kop.
Utility Bills: 2500 rub. 6 kop.
Leisure: 7500 rub. 18 kop.
Savings: 20000 rub. 52 kop.

Sample Input 2:

123.45

24.56

Sample Output 2:

Vacation: 14 rub. 80 kop.
Food and Groceries: 44 rub. 40 kop.
Utility Bills: 7 rub. 40 kop.
Leisure: 22 rub. 20 kop.
Savings: 59 rub. 21 kop.





