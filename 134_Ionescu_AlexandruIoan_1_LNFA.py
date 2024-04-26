def main():
    with open("inputs.txt",'r') as f:
        nr_stari=int(f.readline())
        stari=[int(x) for x in f.readline().split()]
        nr_litere = int(f.readline())
        litere=[x for x in f.readline().split()]
        stare_initiala=int(f.readline())
        nr_stari_finale=int(f.readline())
        stari_finale=[int(x) for x in f.readline().split()]
        nr_tranzitii=int(f.readline())
        tranzitii=[]
        for _ in range(nr_tranzitii):
            x=f.readline().split()
            x[0]=int(x[0])
            x[2]=int(x[2])
            tranzitii.append(x)
        nr_cuvinte=int(f.readline())
        cuvinte=[]
        for _ in range(nr_cuvinte):
            cuvinte.append(f.readline().strip())
    #generare dictionar tranzitii lambda{stare:lista_stari}
    tranzitii_lambda={}
    for x in tranzitii:
        if x[1]=='.':
            if x[0] not in tranzitii_lambda:
                tranzitii_lambda[x[0]]=[x[2]]
            else:
                tranzitii_lambda[x[0]].append(x[2])
    #generare dictionar tranzitii litere{tuple(stare,litera):lista_stari}
    tranzitii_litere={}
    for x in tranzitii:
        if x[1]!='.':
            if (x[0],x[1]) not in tranzitii_litere:
                tranzitii_litere[(x[0],x[1])]=[x[2]]
            else:
                tranzitii_litere[(x[0],x[1])].append(x[2])
    #generare dictionar lambda inchidere{stare:lista_stari}
    lambda_inchidere={}
    for x in stari:
        if x in tranzitii_lambda:
            l=[x]
            i=0
            while i<len(l):
                if l[i] in tranzitii_lambda:
                    for y in tranzitii_lambda[l[i]]:
                        if y not in l:
                            l.append(y)
                i+=1
            lambda_inchidere[x]=l
        else:
            lambda_inchidere[x]=[x]
    #main
    # for x in stari:
    #     print(x,lambda_inchidere[x])
    f=open("outputs.txt",'w')
    for cuvant in cuvinte:
        cuv_acceptat=True
        stare_curenta=lambda_inchidere[stare_initiala]
        for litera in cuvant:
            if litera not in litere:
                cuv_acceptat=False
                break
            stare_noua=[]
            for x in stare_curenta:
                if (x,litera) in tranzitii_litere:
                    for y in tranzitii_litere[(x,litera)]:
                        if y not in stare_noua:
                            stare_noua.append(y)
            stare_curenta=[]
            for x in stare_noua:
                for y in lambda_inchidere[x]:
                    if y not in stare_curenta:
                        stare_curenta.append(y)
            if len(stare_curenta)==0:
                cuv_acceptat=False
                break
        if cuv_acceptat:
            cuv_acceptat=False
            for x in stare_curenta:
                if x in stari_finale:
                    cuv_acceptat=True
                    break
        if cuv_acceptat:
            f.write("DA\n")
        else:
            f.write("NU\n")
    f.close()
    print("DONE")
if __name__=="__main__":
    main()