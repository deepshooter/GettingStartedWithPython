def computepay(h,r):
    if(int(h)<=40):
        pay = int(h) * float(r)
    elif(int(h)>40):
        pay =(40 * float(r))+(int(h)-40)*(float(r)*1.5)
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs,rate)
print(p)


