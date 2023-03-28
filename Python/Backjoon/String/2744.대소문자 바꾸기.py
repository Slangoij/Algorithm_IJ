inputstr = input()
buffer = ""
for crt in inputstr:
    if crt.isupper():
        buffer += crt.lower()
    else:
        buffer += crt.upper()
print(buffer)
