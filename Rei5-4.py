k12=set()
for s in range(1,13):
    if 12%s==0:
        k12.add(s)

k18=set()
for a in range(1,19):
    if 18%a==0:
        k18.add(a)

print(k18&k12)
