

def cash (f):
    slovar = {}
    def deistvie (chislo):
        nonlocal slovar
        if chislo not in slovar:
            slovar[chislo] = func(chislo)
            print(f"Добавление результата в словарь: {slovar[chislo]}")
        else:
            print(f"Результат из словаря: {slovar[chislo]}")
        print(f"словарь- {slovar}")
        return slovar[chislo]
    return deistvie


@cash
def func (i):
    return i * 10

func(10)