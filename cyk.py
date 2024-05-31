def main():
    #citire date
    with open("inputs3.txt",'r') as f:
        nr_productii=int(f.readline())
        prod_initiala=f.readline().strip()
        productii=dict()
        for _ in range(nr_productii):
            x=f.readline().split('->')
            l=x[0].strip()
            r=[y.strip() for y in x[1].split('|')]
            if l not in productii:
                productii[l]=r
            else:
                for y in r:
                    if y not in productii[l]:
                        productii[l].append(y)
        nr_litere=int(f.readline())
        litere=[]
        for _ in range(nr_litere):
            litere.append(f.readline().strip())
    #productii_terminale=dict{nonterminal:lista_terminale(string)}
    productii_terminale=dict()
    #productii_neterminale=dict{nonterminal:lista_perechi(nonterminal_1,nonterminal_2)}
    productii_neterminale=dict()
    for x in productii:
        for y in productii[x]:
            if len(y)==0 or y[0]<'A' or y[0]>'Z':
                if x not in productii_terminale:
                    productii_terminale[x]=[y]
                else:
                    productii_terminale[x].append(y)
            else:
                for temp in productii:
                    if y.startswith(temp) and y[len(temp):] in productii:
                        y1=temp
                        y2=y[len(temp):]
                if x not in productii_neterminale:
                    productii_neterminale[x]=[(y1,y2)]
                else:
                    productii_neterminale[x].append((y1,y2))
    #verificare pt ""
    if nr_litere==0:
        if prod_initiala in productii_terminale and "" in productii_terminale[prod_initiala]:
            print("Cuvantul este generat de gramatica")
            f=open("outputs3.txt",'w')
            f.write("DA")
            f.close()
            return
        print("Cuvantul nu este generat de gramatica")
        f=open("outputs3.txt",'w')
        f.write("NU")
        f.close()
        return
    #generare "matrice" CYK
    m=[]
    l=[]
    for i in range(nr_litere):
        l2=[]
        for temp in productii_terminale:
            if litere[i] in productii_terminale[temp]:
                l2.append(temp)
        l.append(list(set(l2)))
    m.append(l)
    for i in range(1,nr_litere):
        l=[]
        for j in range(nr_litere-i):
            l2=[]
            for k in range(i):
                for x in m[k][j]:
                    for y in m[i-k-1][j+k+1]:
                        for temp in productii_neterminale:
                            if (x,y) in productii_neterminale[temp]:
                                l2.append(temp)
            l.append(list(set(l2)))
        m.append(l)
    # for p in m:
    #     print(p)
    f=open("outputs3.txt",'w')
    if prod_initiala in m[-1][0]:
        print("Cuvantul este generat de gramatica")
        f.write("DA")
    else:
        print("Cuvantul nu este generat de gramatica")
        f.write("NU")

    f.close()
if __name__ == "__main__":
    main()
    print("Done")