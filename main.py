# Met de type(variabele) functie kun je het type van een object achterhalen. Welke types hebben de volgende objecten? Tip: Probeer het eerst zelf te bedenken, voordat je het met de functie controleert
#Voorbeeld:
from re import LOCALE


var1 = "Test"
# >> Hmm, ik denk dat dit een string is!
type(var1)
# >> <class 'str'>, dit is dus inderdaad een string

a = 6
# a = int
b = "Hello World"
# b = str
c = 2.0
# c = float
d = True
# d = bool

# Als we nu het volgende toevoegen
a = b
# Welke types hebben a en b dan?
# >> Class a en b zijn een str

e = a == b
# >> De variabel e = a staat gelijk aan b
# >> Is een Bool, Return true want a = b
a = 6
# >> a word nu een int
f = a > c
# >> De variabel "f" = a is groter dan c
# >> f is een bool, en returned true


# Doe hetzelfde voor de volgende expressies, maar probeer ook te bedenken wat de resultaten van de expressies zouden moeten zijn. Wederom; probeer dit eerst zelf te bedenken voordat je het laat berekenen door Python

g = 4 + 23
# g = int
#print(type(g))
h = 12 + 0.5
# h = float
#print(type(h))
i = 1.0 - 1.0
# i = float
#print(type(i))

j = 2 * 5
#j=int
k = 2.0 * 10
#k=float
l = k - 1.0
#l=float

m = 10 / 2
#int
n = 11 / 4
#float
o = 11 // 4
#int
p = 8**2
#int
q = 2**8
#int
r = 15 % 3
#int
s = 3 % 15
#int
t = 20 % 8
#int
u = 24
#int
v = 12
#int
u = v = 42
w = u != v
#bool (false)
x = 2 + 3 * 9 + 3**3 / 6
#float
