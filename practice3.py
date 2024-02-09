def compound_intrest (principle, rate, time):
    Amount=principle * (pow((1+rate/100), time))
    CI=Amount-principle
    print("Compound intrest is : ", CI)
compound_intrest(10000,10.25, 5)
