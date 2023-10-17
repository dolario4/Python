spisok = [1,2,3,4,5,None,7,8,9]
for i in range(len(spisok)):
    if spisok[i] is None:
        spisok[i] = 0
        result = sum(spisok) / (len(spisok)-1)
        spisok[i] = result
print(spisok)




