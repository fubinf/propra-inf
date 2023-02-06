title: Codeverständnis
description: |
  Codeverständnis
timevalue: 2.0
difficulty: 2
---
Betrachten Sie folgenden Code. Warum ist er Ihrer Meinung nach schwer zu lesen?

Wie würden Sie ihn verbessern?

```python
from functools import reduce

l = input()
r = []

def valid(x):
  if x >> 4 != 3 or x & 0xF > 9:
    result = False
  else:
    result = True
  return result

for e in l:
  if valid(ord(e)):
    r.append(ord(e) - 48)

print(reduce(lambda a, b: a * 10 + b, r))
```
