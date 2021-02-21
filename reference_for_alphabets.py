special symbols = [".", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "~", "`", "{", "}", "[", "]", "|", ":", ';', "<", ">", "?", "/", "."]
alpha = []
Alpha = []
num = []
for i in range(26):
    alpha.append(str(chr(i + 97)))
print(alpha)  # Lowercase alphabets
for i in range(26):
    Alpha.append(str(chr(i + 65)))
print(Alpha)  # Uppercase alphabets
for i in range(26):
    num.append(i)
print(num)
print(dict(zip(alpha, num)))
