
a,b,c,d,e = 10,1.05,1,1.06,2.718 # e=2.718(euler number)

p=1   # price=1 (min)

def demand(p):  # given in question
    g= e
    g**=(c+(d*p))
    return g
def supply(p):   # given in question
    g= e
    g**=(a-(b*p))
    return g
x,y=0,0
j=0
l=False
if(supply(p) > demand(p)):
    l= True
while(supply(p) > demand(p)):
    x = supply(p)
    y = demand(p)
    j =p
    p+= p*0.05

l1=x-y
l2=demand(p)-supply(p)

if(l):
    if(l1<l2):
        p = j
    print("Equillibrium price:",p)
    print("Supply at price :",supply(p))
    print("Demand at price:",demand(p))
else:
    print("No solution")
