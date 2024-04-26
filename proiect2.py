i=1
stari_finale=[]
tranzitii=[]
def f(exp:str, stare_inainte):
    plstack=[]
    prstack=[]
    lista_sau=[]
    for j in range(len(exp)):
        if exp[j]=='(':
            plstack.append(j)
        if exp[j]==')':
            prstack.append(j)
        if exp[j]=='|' and len(plstack)==len(prstack):
            lista_sau.append(j)
    if len(lista_sau)!=0:
        stare_inainte2=tranzitii[-1][2] if len(tranzitii)!=0 else 1
        f(exp[:lista_sau[0]],stare_inainte2)
        for j in range(1,len(lista_sau)):
            f(exp[lista_sau[j-1]+1:lista_sau[j]],stare_inainte2)
        f(exp[lista_sau[-1]+1:],stare_inainte2)
        return
    #print(exp,stare_inainte)
    if len(exp)==1:
        global i
        i+=1
        tranzitii.append((stare_inainte,exp,i))
    #plm nu mai stiu ce voiam sa fac
def main():
    #re=input("Introduceti expresia regulata: ")
    re="a|b*abb(a|b)*d|(cb)*"
    f(re,1)
if __name__ == "__main__":
    main()

