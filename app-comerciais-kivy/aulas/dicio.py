tel = {
    30301122: "Pericles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tieste",
}

print(tel)
print(len(tel))

tel[33946529] = "Agamemnon"
print(tel)
print(len(tel))
del(tel[30301122])
print(tel)
print(len(tel))

print(tel.keys())
print(tel.values())
print(type(tel.keys()))
print(type(tel.values()))
print(tel.get(33946529))

tel2 = {33445321: "Páris", 39632123: "Heitor"}

tel.update(tel2)

while(len(tel)):
    print(tel.popitem())