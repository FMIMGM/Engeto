vyska = 1.8 # in units of m / v jednotkách m
vaha = 70 # , in units of kg / v jednotkách kg
jmeno = "Honza"
bmi = vaha/vyska**2
kategorie = None

if bmi < 18.5:
    kategorie = "Podvýživa"
elif bmi >= 18.5 and bmi <= 24.9:
    kategorie = "Zdravá váha"
elif bmi >= 25 and bmi <= 29.9:
    kategorie = "Mírná nadváha"
elif bmi >= 30 and bmi <= 39.9:
    kategorie = "Obezita"
else:
    kategorie = "Těžká obezita"

print ("Jméno: ", jmeno,", kategorie: ", kategorie)