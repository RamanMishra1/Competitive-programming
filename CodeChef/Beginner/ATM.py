test=input().split()
x=int(test[0])
y=float(test[1])
if x%5==0 and x+0.50<=y:
        y=y-x-0.50
        print("%.2f"%(y))
else:
    print(y)
