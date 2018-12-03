n = int(input('dizinin eleman sayisini giriniz:     '))
a = []

for i in range(n):

    a.append(input('sayiyi gir'))

for i in range(n):

    for j in range(i+1):

        if a[j] > a[i]:

            g = a[i]
            a[i] = a[j]
            a[j] = g


print('sorted uygulanmis hali  {}'.format(a))
