status=input("Какой у вас статус? ")
taxfree=int(input("Какая сумма не облагается налогом? "))
tax=0
a=[]
b=["январе","феврале","марте","апреле","мае","июне","июле","августе","сентябре","октябре","ноябре","декабре"]
for i in range (0,12):
    a.append(int(input("Сколько вы заработали в "+b[i]+"? ")))
for i in range(0, 12):

    if status == "родитель-одиночка":
        if 0 <= a[i] - taxfree <= 12950:
            tax = tax + (a[i] - taxfree) * 0.1
        elif 12951 <= a[i] - taxfree <= 49400:
            tax = tax + (a[i] - 12951 - taxfree) * 0.15
            tax = tax + (12950) * 0.1
        elif 49401 <= a[i] - taxfree <= 127550:
            tax += 0.25 * (a[i] - taxfree - 49401)
            tax += (49400 - 12951) * 0.15
            tax += (12950) * 0.1
        elif 127551 <= a[i] - taxfree <= 206600:
            tax += 0.28 * (a[i] - taxfree - 127551)
            tax += 0.25 * (127550 - 49401)
            tax += (49400 - 12951) * 0.15
            tax += (12950) * 0.1
        elif 206601 <= a[i] - taxfree <= 405100:
            tax += 0.33 * (a[i] - taxfree - 206601)
            tax += 0.28 * (206600 - 127551)
            tax += 0.25 * (127550 - 49401)
            tax += (49400 - 9076) * 0.15
            tax += (9075) * 0.1
        elif 405101 <= a[i] - taxfree <= 432200:
            tax += 0.35 * (a[i] - taxfree - 405101)
            tax += 0.33 * (405100 - 186351)
            tax += 0.28 * (186350 - 89351)
            tax += 0.25 * (89350 - 36901)
            tax += (36900 - 12951) * 0.15
            tax += (12950) * 0.1
        elif 432201 <= a[i] - taxfree:
            tax += 0.396 * (a[i] - taxfree - 432201)
            tax += 0.35 * (432200 - 405101)
            tax += 0.33 * (405100 - 206601)
            tax += 0.28 * (206600 - 127551)
            tax += 0.25 * (127550 - 49401)
            tax += (49400 - 12951) * 0.15
            tax += (12950) * 0.1
        


for i in range (0,12):
   
    if status=="один субъект":
        if 0<=a[i]-taxfree<=9075:
            tax=tax+(a[i]-taxfree)*0.1
        elif 9076<=a[i]-taxfree<=36900:
            tax=tax+(a[i]-9076-taxfree)*0.15
            tax=tax+(9075)*0.1
        elif 36901 <= a[i]-taxfree <= 89350:
            tax += 0.25 * (a[i]-taxfree-36901)
            tax += (36900-9076)*0.15
            tax += (9075)*0.1
        elif 89351 <= a[i]-taxfree <= 186350:
            tax += 0.28 * (a[i]-taxfree-89351)
            tax += 0.25 * (89350-36901)
            tax += (36900-9076)*0.15
            tax += (9075)*0.1
        elif 186351 <= a[i]-taxfree <= 405100:
            tax += 0.33 * (a[i]-taxfree -186351)
            tax += 0.28 * (186350-89351)
            tax += 0.25 * (89350-36901)
            tax += (36900-9076)*0.15
            tax += (9075)*0.1
        elif 405101 <= a[i]-taxfree <= 406750:
            tax += 0.35 * (a[i]-taxfree-405101)
            tax += 0.33 * (405100-186351)
            tax += 0.28 * (186350-89351)
            tax += 0.25 * (89350-36901)
            tax += (36900-9076)*0.15
            tax += (9075)*0.1
        elif 406751 <= a[i]-taxfree:
            tax += 0.396 * (a[i]-taxfree-406751)
            tax += 0.35 * (406750-405101)
            tax += 0.33 * (405100-186351)
            tax += 0.28 * (186350-89351)
            tax += 0.25 * (89350-36901)
            tax += (36900-9076)*0.15
            tax += (9075)*0.1



        
        
for i in range(0, 12):

    if status == "для супружеской пары":
        if 0 <= a[i] - taxfree <= 18150:
            tax = tax + (a[i] - taxfree) * 0.1
        elif 18151 <= a[i] - taxfree <= 73800:
            tax = tax + (a[i] - 9076 - taxfree) * 0.15
            tax = tax + (18150) * 0.1
        elif 73801 <= a[i] - taxfree <= 148850:
            tax += 0.25 * (a[i] - 73801 - taxfree)
            tax += (73800 - 18151) * 0.15
            tax += (18150) * 0.1
        elif 148851 <= a[i] - taxfree <= 226850:
            tax += 0.28 * (a[i] - 148851 - taxfree)
            tax += 0.25 * (148850 - 73801)
            tax += (73800 - 18151) * 0.15
            tax += (18150) * 0.1
        elif 226851 <= a[i] - taxfree <= 405100:
            tax += 0.33 * (a[i] - 226851 - taxfree)
            tax += 0.28 * (226850 - 148851)
            tax += 0.25 * (148850 - 73801)
            tax += (73800 - 18151) * 0.15
            tax += (18150) * 0.1
        elif 405101 <= a[i] - taxfree <= 457600:
            tax += 0.35 * (a[i] - 405101 - taxfree)
            tax += 0.33 * (405100 - 226851)
            tax += 0.28 * (226850 - 148851)
            tax += 0.25 * (148850 - 73801)
            tax += (73800 - 18151) * 0.15
            tax += (18150) * 0.1
        elif 457601 <= a[i] - taxfree:
            tax += 0.396 * (a[i] - 406751 - taxfree)
            tax += 0.35 * (406750 - 405101)
            tax += 0.33 * (405100 - 226851)
            tax += 0.28 * (226850 - 148851)
            tax += 0.25 * (148850 - 73801)
            tax += (73800 - 18151) * 0.15
            tax += (18150) * 0.1


print(tax)
