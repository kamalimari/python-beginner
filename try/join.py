
s = "-"
seq = ('aa', '12', 'g')
seq1 = ["a", "d", "g"]

print (s.join(seq))
s1 = 'abc'
s2 = '123'

print('s1.join(s2):', s1.join(s2))

print('s2.join(s1):', s.join(s2))

print(hex(id(seq[0])))
print(hex(id(seq[1])))
print(hex(id(seq[2])))
print(hex(id(seq1[0])))
print(hex(id(seq1[1])))

print(hex(id(seq1[2])))

