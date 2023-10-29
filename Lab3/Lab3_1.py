def spisok(tovar,pred):
    am = 0
    for i in range(len(tovar)):
        if pred == tovar[i]:
          am = am+1
          i=i+1
    if am >= 1:
        ind = tovar.index(pred)
        return(ind)
    else:
        return(None)

tovar = ["Шлем","Перчатки","Мяч","Ракетка","Шлем"]
pred = "Шлем"
print(spisok(tovar,pred))
