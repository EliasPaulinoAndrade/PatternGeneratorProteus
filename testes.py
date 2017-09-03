a = [1,2,3,4,5]
rot = []
t = a[:]
for i in t:
    aux = t.pop()
    t.insert(0, aux)
    rot.append(t)
print(a)
print(rot)