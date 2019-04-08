hrs = input("Enter Hours:")
rate = input("Enter Rate:")

if(int(hrs)<=40):
    pay = int(hrs) * float(rate)
elif(int(hrs)>40):
    pay =(40 * float(rate))+(int(hrs)-40)*(float(rate)*1.5)
    
print(pay)