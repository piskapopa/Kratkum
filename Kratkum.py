import json
import sys
if len(sys.argv) > 1 and sys.argv[1].startswith("-i"):
    if not sys.argv[1].endswith("r"):
        with open(f"{sys.argv[2]}.ktkm") as ktkm:
            vyrazh = ktkm.read().replace("\n", " ")
    else:
        with open(sys.argv[2]) as ktkm:
            vyrazh = ktkm.read().replace("\n", " ")
else:
    vyrazh = input()
w = []
yyy = ["+", "-", "/", "*", "^", "=", "_", "Σ", "?", "!", "→", "⏟",
"//"]
itog = "<math></math>"
ops = ["×"]
with open("aliases.json", "r") as aliases: 
    aliases = json.load(aliases)
vyrazhh = vyrazh.split()
newvyrazhh = []
for j, i in enumerate(vyrazhh):
    if i in aliases.keys():
        vyrazhh[j] = aliases[i]
        newvyrazhh.append(vyrazhh[j])
    elif i.startswith("\\"):
        vyrazhh[j] = i[1::]
        newvyrazhh.append(vyrazhh[j])
    elif i.startswith("#"):
        ops.append(i[1::])
    else:
        newvyrazhh.append(vyrazhh[j])
newvyrazhh = [i.split() for i in newvyrazhh]
newvyrazhh = [i for govno in newvyrazhh for i in govno]
vyrazhh = newvyrazhh
yyy+=ops
for i in vyrazhh:
    if not i in yyy:
        if not i.endswith("\\"):
            w.append(f"<mi>{i}</mi>")
        else:
            w.append(f"<mi>{i[:-1]}</mi>")
    elif i == "^":
        r = [w.pop(), w.pop()][::-1]
        w.append(f"<msup><mrow>{r[0]}</mrow><mrow>{r[1]}</mrow></msup>")
    elif i == "_":
        r = [w.pop(), w.pop()][::-1]
        w.append(f"<msub><mrow>{r[0]}</mrow><mrow>{r[1]}</mrow></msub>")
    elif i == "Σ":
        r = [w.pop(), w.pop(), w.pop()][::-1]
        w.append(f"<munderover><mo>Σ</mo><mrow>{r[0]}</mrow><mrow>{r[1]}</mrow></munderover>{r[2]}")
    elif i in (["+", "-", "/", "*", "="] + ops):
        r = [w.pop(), w.pop()][::-1]
        w.append(f"<mrow>{r[0]}</mrow><mo>{i}</mo><mrow>{r[1]}</mrow>")
    elif i == "⏟":
        r = [w.pop(), w.pop()][::-1]
        w.append(f"<munderover><mo>⏟</mo><mrow>{r[0]}</mrow><mrow>{r[1]}</mrow></munderover>")
    elif i == "?":
        r = [w.pop(), w.pop()][::-1]
        w.append(f"{r[0]}{r[1]}")
    elif i == "!":
        r = [w.pop(), w.pop()][::-1]
        w.append(f'{r[0]}<mspace width="10px"/>{r[1]}')
    elif i == "//":
        r = [w.pop(), w.pop()][::-1]
        w.append(f"<mfrac><mrow>{r[0]}</mrow><mrow>{r[1]}</mrow></mfrac>")

if len(w) > 1:
    print(w)
    raise Exception("Exception")
else:
    itog = f"<math>{w[0]}</math>"
    with open("ddd.html", "w") as w:
        w.write(itog)
