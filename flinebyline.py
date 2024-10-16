file=open("casual.txt","r")
content=file.readline()
while content:
    print(content)
    content=file.readline()
