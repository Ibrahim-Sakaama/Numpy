def saisir():
    file=open("concours.txt",'a')
    cond="o"
    decision={"a":"admis","r":"refuse","aj":"ajourne"}
    while cond=="o":
        ncin=input("Donner le numero du NCIN ")
        nom=input("Donner le nom ")
        prenom=input("Donner le prenom ")
        age=input("Donner l'age ")
        dec=input("donner la decision a:admis r:refuse aj:ajourne ")
        file.write(ncin+";"+nom+";"+prenom+";"+age+";"+decision[dec]+"\n")
        cond=input("y a t-il un autre condidat à enregistrer? o: oui n:non ")
    file.close()

# saisir()

def admis():
    file=open("concours.txt","r")
    l=file.readlines()
    file.close()
    file2=open("admis.txt","w")
    for i in l:
        li = i.split(";")
        if li[-1].strip()=="admis":
            file2.write(i)
    file2.close()

# admis()

def attente():
    file=open("admis.txt","r")
    l=file.readlines()
    file.close()
    file2=open("attente.txt","w")
    for i in l:
        li = i.split(";")
        if (int(li[-2])>30):
            file2.write(li[0]+";"+li[1]+";"+li[2]+"\n")
    file2.close()
    # print(l)

# attente()


def statistique(dec):
    file=open("concours.txt","r")
    l=file.readlines()
    file.close()
    #file2=open("stat.txt","w")
    adm=0
    ref=0
    ajo=0
    nbr_total=len(l)
    for i in l:
        li = i.split(";")
        if li[-1].strip()=="admis":
            adm+=1
        elif li[-1].strip()=="refuse":
            ref+=1
        elif li[-1].strip()=="ajourne":
            ajo+=1
    if dec=="admis":
        print("le pircentage des condidatures qui sont admis ",(adm/nbr_total)*100)
    elif dec=="refuse":
        print("le pircentage des condidatures qui sont refuses ",(ref/nbr_total)*100)
    elif dec=="ajourné":
        print("le pircentage des condidatures qui sont ajournés ",(ajo/nbr_total)*100)
    #file2.close()

statistique("admis")


def supprimer():
    file=open("admis.txt","r")
    L=file.readlines()
    file.close()
    file2=open("admis.txt","w")

    for i in L:
        li = i.split(";")
        if li[-2]<="30":
            file2.write(i)
    file2.close()

supprimer()


















