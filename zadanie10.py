#!/usr/bin/env python3

sex = input("Czy chcesz obliczyć BMI dla kobiety czy dla mężczyzny?: (k/m) ")

if sex == "k":
    wagaKobieta = int(input("Podaj swoją wagę: "))
    wzrostKobieta = int(input("Podaj swój wzrost: "))
    print("Twoje BMI wynosi: {:.2f}".format(wagaKobieta/(wzrostKobieta/100)**2))
else:
    wagaMezczyzny = int(input("Podaj swoją wagę: "))
    wzrostMezczyzny = int(input("Podaj swój wzrost: "))
    print("Twoje BMI wynosi: {:.2f}".format(wagaMezczyzny/(wzrostMezczyzny/100)**2))
