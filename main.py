weight=float(input("Enter Your Weight In Kilo-Grams(KG)="))
height=float(input("Enter Your Height In Centi-Meters(CM)="))

bmi=weight/(height/100)**2

print("BMI",bmi)

if bmi<= 18.9:
    print("You Are Under-Weight")

elif bmi<=29.5:
    print("You are Healthy")   

elif bmi<=29.9:
    print("You Are Over-Weight")

elif bmi<=34.9:
    print("You Are Severely-OverWeight")  

elif bmi<=39.9:
    print("You Are Obese")

else:
    print("You Are Severly-Obese")    

    print("THANK YOU FOR USING MY B.M.I.CALCULATOR")