# weird because of the rounding up with python errors

import math

interest, repayment = [int(x) for x in input().split()]

debt = 100.0
repaid = 0

while debt != 0:
    to_add = interest / 100 * debt
    to_add = math.ceil(to_add * 100) / 100
    debt += to_add
    paid = max(50.0, repayment / 100 * debt)
    paid = math.ceil(paid * 100) / 100
    repaid += min(debt, paid)
    debt -= min(debt, paid)

repaid = math.ceil(repaid * 100)
repaid = str(repaid)

print(repaid[:-2] + '.' + repaid[-2:])
