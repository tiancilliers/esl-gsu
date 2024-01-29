import re
import pyperclip

input("Copy first group and press enter...")
sch1 = pyperclip.paste()
input("Copy second group and press enter...")
sch2 = pyperclip.paste()

parts1 = re.findall(r'\(symbol.+at (\S+) (\S+).+\n.+\n.+\n.+Reference" "(.+)"', sch1)
parts2 = re.findall(r'\(symbol.+at (\S+) (\S+).+\n.+\n.+\n.+Reference" "(.+)"', sch2)

assert len(parts1) == len(parts2)
n = len(parts1)

offset = (sum(float(e[1][0])-float(e[0][0]) for e in zip(parts1, parts2))/len(parts1), sum(float(e[1][1])-float(e[0][1]) for e in zip(parts1, parts2))/len(parts1))

parts1 = sorted([(round(float(e[0]),2), round(float(e[1]),2), e[2]) for e in parts1])
parts2 = sorted([(round(float(e[0])-offset[0],2), round(float(e[1])-offset[1],2), e[2]) for e in parts2])

pmap = [(e[0][2], e[1][2]) for e in zip(parts1, parts2)]
print(pmap)

input("Copy PCB layout and press enter...")
pcb1 = pyperclip.paste()

for t in pmap:
    pcb1 = pcb1.replace(t[0], t[1])

pyperclip.copy(pcb1)