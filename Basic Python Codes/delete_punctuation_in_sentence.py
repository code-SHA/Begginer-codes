puntuation='''|()[]{}:;,.!@#$%^&*_+=~`\/<>'''
s=input("Enter a Sentence: ")
no_puntuation=""
for i in s:
    if i not in puntuation:
        no_puntuation=no_puntuation+i
print(no_puntuation)