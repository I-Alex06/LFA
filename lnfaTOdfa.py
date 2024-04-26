
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
        # nr_cuvinte=int(f.readline())
        # cuvinte=[]
        # for _ in range(nr_cuvinte):
        #     cuvinte.append(f.readline().strip())
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
    #generare dictionar lambda litera lambda pt fiecare stare{(stare,litera):lista_stari}
    lambda_litera_lambda={}
    for x in stari:
        l=lambda_inchidere[x]
        for y in l:
            for lit in litere:
                if (x,lit) not in lambda_litera_lambda:
                    lambda_litera_lambda[(x,lit)]=[]
                if (y,lit) in tranzitii_litere:
                    for z in tranzitii_litere[(y,lit)]:
                        if z not in lambda_litera_lambda[(x,lit)]:
                            lambda_litera_lambda[(x,lit)].append(z)
                # if x==6:
                #     print(x,lit,lambda_litera_lambda[(x,lit)])
                temp=[]
                for z in lambda_litera_lambda[(x,lit)]:
                    for w in lambda_inchidere[z]:
                        if w not in temp:
                            temp.append(w)
                lambda_litera_lambda[(x,lit)]=temp
    # for x in lambda_litera_lambda:
    #     l=lambda_litera_lambda[x]
    #     print(x,sorted(l))
    # print(tranzitii_litere[6,'b'])
    # return    
    #generare dictionar tranzitii dfa{tuple(lista_stari,litera):lista_stari}
    tranzitii_dfa={}
    lista_stari_dfa=[sorted(lambda_inchidere[stare_initiala])]
    i=0
    while i<len(lista_stari_dfa):
        for litera in litere:
            lista_stari_noi=[]
            for x in lista_stari_dfa[i]:
                if (x,litera) in lambda_litera_lambda:
                    for y in lambda_litera_lambda[(x,litera)]:
                        if y not in lista_stari_noi:
                            lista_stari_noi.append(y)
            lista_stari_noi.sort()
            if len(lista_stari_noi)!=0:
                if lista_stari_noi not in lista_stari_dfa:
                    lista_stari_dfa.append(lista_stari_noi)
                tranzitii_dfa[(tuple(lista_stari_dfa[i]),litera)]=lista_stari_noi
        i+=1
    # for x in tranzitii_dfa:
    #     print(x,tranzitii_dfa[x])
    # print()
    # for x in lista_stari_dfa:
    #     print(x)
    # return
    stari_finale_dfa=[]
    for x in lista_stari_dfa:
        for y in x:
            if y in stari_finale:
                stari_finale_dfa.append(lista_stari_dfa.index(x)+1)
                break
    print(stari_finale_dfa)
    #tranzitii_dfa_scurt={(lista_stari_dfa.index(list(x)),y):lista_stari_dfa.index(tranzitii_dfa[x,y]) for (x,y) in tranzitii_dfa}
    tranzitii_dfa_scurt=[[lista_stari_dfa.index(list(x))+1,y,lista_stari_dfa.index(tranzitii_dfa[x,y])+1] for (x,y) in tranzitii_dfa]
    # for x in tranzitii_dfa_scurt:
    #     print(x)
    with open("outputs.txt",'w') as f:
        f.write(str(len(lista_stari_dfa))+'\n')
        for x in range(len(lista_stari_dfa)):
            f.write(str(x+1)+' ')
        f.write('\n')
        f.write(str(nr_litere)+'\n')
        for x in litere:
            f.write(x+' ')
        f.write('\n')
        f.write(str(1)+'\n')
        f.write(str(len(stari_finale_dfa))+'\n')
        for x in stari_finale_dfa:
            f.write(str(x)+' ')
        f.write('\n')
        f.write(str(len(tranzitii_dfa_scurt))+'\n')
        for x in tranzitii_dfa_scurt:
            f.write(str(x[0])+' '+x[1]+' '+str(x[2])+'\n')
    #main
    # for x in stari:
    #     print(x,lambda_inchidere[x])
    # f=open("outputs.txt",'w')
    # for cuvant in cuvinte:
    #     cuv_acceptat=True
    #     stare_curenta=lambda_inchidere[stare_initiala]
    #     for litera in cuvant:
    #         if litera not in litere:
    #             cuv_acceptat=False
    #             break
    #         stare_noua=[]
    #         for x in stare_curenta:
    #             if (x,litera) in tranzitii_litere:
    #                 for y in tranzitii_litere[(x,litera)]:
    #                     if y not in stare_noua:
    #                         stare_noua.append(y)
    #         stare_curenta=[]
    #         for x in stare_noua:
    #             for y in lambda_inchidere[x]:
    #                 if y not in stare_curenta:
    #                     stare_curenta.append(y)
    #         if len(stare_curenta)==0:
    #             cuv_acceptat=False
    #             break
    #     if cuv_acceptat:
    #         cuv_acceptat=False
    #         for x in stare_curenta:
    #             if x in stari_finale:
    #                 cuv_acceptat=True
    #                 break
    #     if cuv_acceptat:
    #         f.write("DA\n")
    #     else:
    #         f.write("NU\n")
    # f.close()
    print("DONE")
if __name__=="__main__":
    main()