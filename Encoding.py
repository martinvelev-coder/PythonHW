text = input("Enter a string to encode: ")
result = ""
i = 0

while i < len(text):
    count = 1
    while i + 1 < len(text) and text[i] == text[i + 1]:
        count += 1
        i += 1
    result += text[i] + str(count)
    i += 1

print(result)