
n = int(input('n sayisi gir'))

a=[]
tam =0
g = []

for i in range(1,n,1):
    a.append(i)
    
    
m = tam(n/2)

if m>0:
    for i in range(m,n,1):
        g=a[i]
        j=i
        m = int(m/2)
        
    if j>m and a[j-m]>g:
        a[j]=a[j-m]
        j =j-m

for i in range(1,n,1):
    print(a[i])        
