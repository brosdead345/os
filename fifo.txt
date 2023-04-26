print("Enter the number of frames: ",end="")
n = int(input())
f = []
fault = 0
top = 0
pf = 'Hit'
print("Enter the reference string: ",end="")
s = list(map(int,input().strip().split()))
print("\nString|Frame →\t",end='')
for i in range(n):
    print(i,end=' ')
print("Fault\n   ")
for i in s:
    if i not in f:
        if len(f)<n:
            f.append(i)
        else:
            f[top] = i
            top = (top+1)%n
        fault += 1
        pf = 'Miss'
    else:
        pf = 'Hit'
    print("   %d\t\t"%i,end='')
    for x in f:
        print(x,end=' ')
    for x in range(n-len(f)):
        print(' ',end=' ')
    print(" %s"%pf)
print("\nTotal requests: ",len(s))
print("Total Page Faults: ",fault)
print("Fault Rate:",(fault/len(s))*100)
