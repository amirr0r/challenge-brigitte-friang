import gmpy
import binascii

def chiffrer(message, e, n):
  i=0
  message_chiffre = ""
  while i != len(message):
    bloc = str(pow(ord(message[i]), e)%n)
    #print bloc
    # while (len(bloc) != 6):
    #   bloc = "0" + bloc
    message_chiffre = message_chiffre + bloc
    i = i + 1
  return message_chiffre

p = 221
q = 7
n = p * q
phin = (p - 1) * (q - 1)

e = 65537
d  = gmpy.invert(e, phin)

print(d)
# print(chiffrer("221 x 7", e, n))