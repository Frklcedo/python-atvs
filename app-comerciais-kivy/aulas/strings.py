s = "Olá"
s2 = 'Mundo'
p = ''' esse
texto
está
definido 
como
parágrafo
'''
print(s,s2)
p2 = """Esse
Também
"""
print(p)
print(p2)
print()

#

s = "Para o Python, toda String é uma lista imutável."
print(s[0])
print(s[-1])
print(s[7:13])
print(s[15:])
print(s[::-1])
print(s[::2])

print('"a" > "A" : ' ,"a" > "A")
print('"a" > "6" : ' ,"a" > "6")
print("ord a", ord("a"))
print("ord A", ord("A"))
print("ord 6", ord("6"))

for c in range(123):
    print(str(c) , chr(c))

#
s = "Lista de Caracteres"
arr = s.split(" ")
print(arr)
replaced_s = s.replace("de","De")
print("replace():", replaced_s)
print("id de s", id(s))
print("id de replaced_s", id(replaced_s))
print("id de s == id de replaced_s: ", id(s) == id(replaced_s))

for c in s:
    print(c)
print()
index = 0
while(index < len(s)):
    print(index, s[index])
    index += 1
print()
for k, v in enumerate(s):
    print(k, v)