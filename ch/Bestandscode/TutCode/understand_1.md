title: Codeverständnis
stage: draft
timevalue: 1.0
difficulty: 2
---
Betrachten Sie folgenden Code. Warum ist er Ihrer Meinung nach schwer zu lesen?

```python
l = map(ord, [*input()])
c = ord(input()[0])-97
r = []

def valid(x):
  if x | 0x20 <= 64 or x | 0x20 > 90:
    result = False
  else:
    result = True
  return result

try:
  while True:
    e = next(l)
    if valid(e):
      o = e & 0x20
      r.append(chr((e & 0x1F + ord(c)) % 26 + o + 65))
except StopIteration:
  pass

print("".join(r))
```
