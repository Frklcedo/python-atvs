x = 0
x =11
print("while")
while(x<=10):
    print(x)
    x+=1
else:
    print("Olaaaaaa")
print("fim while")
print()

for c in "python":
    print(c)
print()
for c in "php":
    print(c)
print()
# range function

print("start, end, 2 steps:", list(range(0,10,2)))
print("start, end, 1 step:", list(range(0,10,1)))
print("start, end:", list(range(4,10)))
print("end:", list(range(10)))
print()

for i in range(10):
    print(i)
print()
for i in range(10,0,-1):
    print(i)
print()
for i in range(10):
    print(i)
    if(i%2 ==1):
        continue
    print("Oh the misery")
    if(i == 6):
        break
print()
