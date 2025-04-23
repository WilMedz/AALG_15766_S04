
def busqiterativa(lis, busca):
    inicio=0
    final=len(lis)-1
    medio=(inicio+final)//2
    while inicio<=final:
        if lis[medio]==busca:
            return medio
        elif lis[medio]<busca:
            inicio= medio+1
        else:
            final= medio-1
        medio= (inicio+final)//2
    return -1 #el elemento no existe
        
lis=[11,13,15,17,19,21,23]

def busqrecursiva(lis,inicio,final,busca):
    if inicio>final:
        return -1
    medio=(inicio+final)//2
    if lis[medio]==busca:
        return medio
    elif lis[medio]<busca:
        return busqrecursiva(lis,medio+1,final,busca)
    else:
        return busqrecursiva(lis,inicio,medio - 1,busca)

for i in range(10,24):
    print(i,busqiterativa(lis,i))
    print(i,busqrecursiva(lis,0,len(lis)-1,i))

