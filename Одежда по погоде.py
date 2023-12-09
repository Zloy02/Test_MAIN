


temp = int(input("vvedi temp "))
osad = bool(input("vvedi osad "))
sil = bool(input("vvedi sil osad "))


if 20<temp<30:
    if osad:
        print("Футболка, шёрты, дождевик")
    else: print("Футболка, шёрты")
else:
    if temp>0:
        if osad:
            if sil:
                print("Пальто, сапог, зонт")
            else:
                print("Пальто и дождевик")
        else:
            print("Пальто")
    else:
        print("Пуховик")
