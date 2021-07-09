def computepay(h,r):
    if h>40:
    	gen=40*r
    	over=(h-40)*(1.5*r)
    	pay=gen+over
        return pay
    else:
        pay=h*r
        return pay
    

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("enter the rate:")
r = float(rate)
p = computepay(h,r)
print("Pay",p)
