n1=int(input("Enter the index till which digits should be printed:"))
X=[]


for i in range (1,(n1+1)):
    if len(str(i))!=1:
        l= len(str(i))
        
        while l!=1:
            v=(i//(10**(l-1)))
            if (len(str(v))>1):
               (v%(10))
               X.append(v%(10))
            else:
               X.append(v)
            l-=1
        x=i%10
        X.append(x)
    else:
        x=i
        X.append(x)
if i in range(9,189):
    if (int(n1-1))%2==1:
               Y=(int(X[n1-1])*10)+(int(X[n1])) 
    else:
          Y=((int(X[n1-2]))*10)+(int(X[n1-1]))
elif i in range (189,2889):
  if (int(n1-3))%3==0:
     Y =(int(X[n1-3])*100)+(int(X[n1-2])*10)+(int(X[n1-1]))
  elif (int(n1-2))%3==0:
    Y=((int(X[n1-2])*100)+(int(X[n1-1])*10)+(int(X[n1])))
  elif (int(n1-1))%3==0:
    Y=((int(X[n1-1])*100)+(int(X[n1])*10)+(int(X[n1+1])))
elif i in range(2889,38889):
    if (int(n1-1))%4==1:
        Y=(int(X[n1-1])*1000)+(int(X[n1])*100)+(int(X[n1+1])*10)+(int(X[n1+2]))
    elif (int(n1-1))%4==2:
        Y=(int(X[n1-2])*1000)+(int(X[n1-1])*100)+(int(X[n1])*10)+(int(X[n1+1]))
    elif (int(n1-1))%4==3:
        Y=(int(X[n1-3])*1000)+(int(X[n1-2])*100)+(int(X[n1-1])*10)+(int(X[n1]))
    elif (int(n1-1))%4==0:
        Y=(int(X[n1-4])*1000)+(int(X[n1-3])*100)+(int(X[n1-2])*10)+(int(X[n1-1]))
print(Y)
print(X[(n1-1)])
#print(X)
