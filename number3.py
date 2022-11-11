# Input a string or text. Remove the duplicate value in the string.

text = input("Enter a string/text: ")
txt_list = []

i = 0
for i in range(len(text)):
    if text[i] not in txt_list:
        txt_list.insert(i, text[i].lower())
        i += 1

text = ""
text = text.join(txt_list)
print("New String:", text.title())