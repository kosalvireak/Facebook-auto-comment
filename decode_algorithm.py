#text = input("Enter the phrase: ")
text = "b sl o eng"
out = ""


def decode(text):
    for i in range(0, len(text)):
        a = ord(text[i])
        a = a + 12
        if a > 122:
            a = a -12
        # print(a)
        b = chr(a)
        global out
        out += b
    print(out)

decode(text)
text = input("Enter the phrase: ")

out_encode = ""
def encode(text):
    for i in range(0, len(text)):
        a = ord(text[i])
        if a + 12 > 123:
            a = a -12
        elif a + 12 < 123 :
            a = a + 24
        
        # elif (a + 12) < 122 :
        #     a = a -12
        # print(a)
        b = chr(a)
        global out_encode
        out_encode += b
    print(out_encode)


#decode(text)
encode(text)
