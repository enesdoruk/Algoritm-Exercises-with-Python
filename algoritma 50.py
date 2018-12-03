
c = int(input('eklemek istediginiz sayi sayisi '))
n = []

for i in range(1,c,1):
    n.append(i)
    
ara = int(input('aramak istediğiniz sayi  '))

b =len(n)
adim=int(pow(b,1/2))
indis = 1

if(n[adim]<a):
    indis =adim
    adim= 2*adim
    if adim>b:
        if a[indis]<ara:
            indis += 1
            if indis>n:
                if a[indis]==ara:
                    print('buldunuz ')
                else:
                    print('aradiginiz sayi yoktur')
                    
        
    