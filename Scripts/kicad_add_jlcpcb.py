import os
import re


with open("bomjlc2.csv") as f:
    bom = [l.split(";") for l in f.read().split("\n")[:-1]]
print(bom)

schs = [fil for fil in os.listdir() if fil.endswith(".kicad_sch")]
for sch in schs:
    with open(sch) as f:
        dat = f.read()
        f.close()
    #value = input("Value: ")
    #footpr = input("Footprint: ")
    #jlc = input("JLCPCB: ")
    for bo in bom[:-1]:
        footpr, value, jlc = bo
        dat = re.sub(rf'("Value" "{re.escape(value)}" \(([^\(]+).+\n.+\n.+\n.+"Footprint" "\S*:{re.escape(footpr)}".+\n.+\n.+)', 
                    rf'\1\n    (property "JLCPCB" "{jlc}" (\2)\n      (effects (font (size 1.27 1.27)) hide)\n    )', 
                    dat)
    with open(sch, "w") as f:
        f.write(dat)
        f.close()