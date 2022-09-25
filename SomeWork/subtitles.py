f = open("subs.txt", 'r')

v = open("subsDONE.txt", 'w')

while True:
    line = f.readline()
    if not line:
        break
    v.write(line.strip()+' ')

print("OK")
f.close()
v.close()

#print("qwerty"[:-2:])