with open('nb.txt') as f:
  for l in f.readlines():
    try:
      print(chr(abs(int(l))), end='')
    except:
      pass
print()