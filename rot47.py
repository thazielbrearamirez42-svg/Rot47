 # Thaziel
# Fundamentos de Criptografía

def rot47_cipher(text_to_cypher):
    ciphered_text = []
    for character in range(len(text_to_cypher)):
        ord_value = ord(text_to_cypher[character])
        if ord_value >= 33 and ord_value <= 126:
            ciphered_text.append(chr(33 + ((ord_value + 14) % 94)))
        else:
            ciphered_text.append(text_to_cypher[character])
    return ciphered_text


temp_text = input("Type the text you want to cipher: ")
print(rot47_cipher(temp_text))
