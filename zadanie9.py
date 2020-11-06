#!/usr/bin/env python3

cal = int(input("Podaj wartość w calach: "))
stopa = int(input("Podaj wartość w stopach: "))

calToCm = cal * 2.54
stopaToCm = stopa * 30.48

print("Podana ilość cali wynosi {:.2f}".format(calToCm), "centymetrów")
print("Podana ilość stóp wynosi {:.2f}".format(stopaToCm), "centymetrów")