alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
direction = input("Enter 'encode' to encrypt and 'decode' to decrypt: ").lower()
text = input("Enter your message: ").lower()
shift = int(input("Enter the shift number: "))

encode = ""
decode = ""

for i in range(0, len(text)):
    for j in range(0, len(alphabet)):
        if direction == "encode":
            if text[i] == alphabet[j]:
                encode = encode + alphabet[(j + shift) % len(alphabet)] 
        elif direction == "decode":
            if text[i] == alphabet[j]:
                decode = decode + alphabet[(j - shift) % len(alphabet)]
            
print(encode)
print(decode)