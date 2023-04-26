print("Enter the number of frames: ",end="")
n = int(input())
f,st,fault,pf = [],[],0,'Hit'
print("Enter the reference string: ",end="")
s = list(map(int,input().strip().split()))
print("\nString|Frame →\t",end='')
for i in range(n):
    print(i,end=' ')
print("Fault\n   ↓\n")
for i in s:
    if i not in f:
        if len(f)<n:
            f.append(i)
            st.append(len(f)-1)
        else:
            ind = st.pop(0)
            f[ind] = i
            st.append(ind)
        pf = 'Miss'
        fault += 1
    else:
        st.append(st.pop(st.index(f.index(i))))
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
