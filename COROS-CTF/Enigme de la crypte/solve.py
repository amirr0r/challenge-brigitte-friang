from enigma.machine import EnigmaMachine


machine = EnigmaMachine.from_key_sheet(
    rotors='I III V',
    reflector='B',
    ring_settings=[18, 5, 10], # R, E, J (Ringstellung)
    plugboard_settings=None
)

# set machine initial starting position (Grundstellung)
machine.set_display('MER')
ciphertext = 'IVQDQT NHABMPSVBYYUCJIYMJBRDWXAXP  THYVCROD'
# ciphertext = 'IVQDQTNHABMPSVBYYUCJIYMJBRDWXAXPTHYVCROD'
plaintext = machine.process_text(ciphertext)
print(plaintext)

# majuscules =  ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# decrypt the message key
# for a in majuscules:
#     for b in majuscules:
#         for c in majuscules:
#             key = f'{a}{b}{c}'
#             msg_key = machine.process_text(key)
#             # decrypt the cipher text with the unencrypted message key
#             machine.set_display(msg_key)
#             print(f"Key:{key}\n{plaintext}\n{'=' * 50}")