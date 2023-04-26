print("Enter the number of frames: ",end="")
n = int(input())
f=[]
fault=0
pf='Hit'
print("Enter the reference string: ",end="")
s = list(map(int,input().strip().split()))
print("\nString|Frame →\t",end='')
for i in range(n):
    print(i,end=' ')
print("Fault\n   ↓\n")
o = [None for i in range(n)]
for i in range(len(s)):
    if s[i] not in f:
        if len(f)<n:
            f.append(s[i])
        else:
            for x in range(len(f)):
                if f[x] not in s[i+1:]:
                    f[x] = s[i]
                    break
                else:
                    o[x] = s[i+1:].index(f[x])
            else:
                f[o.index(max(o))] = s[i]
        fault += 1
        pf = 'Miss'
    else:
        pf = 'Hit'
    print("   %d\t\t"%s[i],end='')
    for x in f:
        print(x,end=' ')
    for x in range(n-len(f)):
        print(' ',end=' ')
    print(" %s"%pf)
print("\nTotal requests: ",len(s))
print("Total Page Faults: ",fault)
print("Fault Rate:",(fault/len(s))*100)