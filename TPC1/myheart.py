import matplotlib.pyplot as plt
matriz = []

def main():   
    file = open("myheart.csv")
    i=0
    d=0
    
    for linha in file:
        if i != 0:
            matriz.append(linha.replace('\n', '').split(','))
            if matriz[i-1][5]=='1':
                d += 1
        i+=1
    
    distFMD(i-1)

    distEscalaoEtario(i-1,d)

    distColesterol(i-1,d)


def distFMD(n):
    fd = 0
    md = 0 
    for x in range(n):
        if matriz[x][5]=='1':
            if matriz[x][1] == 'F':
                fd += 1
            else:
                md += 1
    Xaxis = ["Femenino","Masculino"]
    Yaxis = [round((fd/(fd+md))*100,2),round((md/(fd+md))*100,2)]
    
    print( "Porcentagem de doentes do sexo femenino : " + str((fd/(fd+md))*100) 
       + "\nPorcentagem de doentes do sexo masculino : " + str((md/(fd+md))*100))
   
    print( "_____________________________________")
    print( "| Porcentagem de doentes por genero |")
    print( "|___________________________________|")
    print( "|     Masculino   |     Feminino    |")
    print( "|_________________|_________________|")
    print(f"|      {str(round((fd/(fd+md))*100,2))}       |      {str(round((md/(fd+md))*100,2))}      |")
    print(f"|_________________|_________________|")
    
    data = [["Masculino","Feminino"],[str(round((fd/(fd+md))*100,2))+"%",str(round((md/(fd+md))*100,2))+"%"]]
    
    plt.axis('off')
    plt.title("Porcentagem de doentes por genero")
    table = plt.table(cellText=data,  cellLoc='center', loc='center')
    table.set_fontsize(14)
    table.scale(1, 2)
    plt.show()

    plt.bar(Xaxis, Yaxis)
    plt.title("Porcentagem de doentes por genero")
    plt.xlabel("Porcentagem (%)")
    plt.ylabel("Genero")
    plt.show()
    

def distEscalaoEtario(n,d):
    restante = d
    escalao = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in range(n):
        if  matriz[x][5]=='1' and int(matriz[x][0])>29:
            while  len(escalao)-1 < (int(matriz[x][3]))//10 : 
                escalao.append(0)
            escalao[(int(matriz[x][0])-30)//5]+=1

    Xaxis = []
    Yaxis = []

    print( "______________________________________")
    print( "| Porcentagem de doentes por escalão |")
    print( "|____________________________________|")
    
    data=[]

    for x in range(0,len(escalao)):
        if (escalao[x]/d)*100 != 0:
            if ((escalao[x]/d)*100)>10: print(f"| [{30+5*x}-{34+5*x}] |           {round((escalao[x]/d)*100,1)}           |")
            else :print(f"| [{30+5*x}-{34+5*x}] |           {round((escalao[x]/d)*100,1)}            |")
            print( "|_________|__________________________|")
            if escalao[x]!=0 :
                Xaxis.append(f"[{30+5*x}-{34+5*x}]")
                Yaxis.append(round((escalao[x]/d)*100,1))
                data.append([f"[{30+5*x}-{34+5*x}]",str(round((escalao[x]/d)*100,1))+"%"])


    plt.axis('off')
    plt.title("Porcentagem de doentes por escalão")
    table = plt.table(cellText=data,  cellLoc='center', loc='center')
    table.set_fontsize(14)
    table.scale(1, 2)
    plt.show()
    
    plt.bar(Xaxis, Yaxis)
    plt.title("Porcentagem de doentes por escalão")
    plt.xlabel("Entervalos")
    plt.ylabel("Porcentagem (%)")
    plt.show()
    




def distColesterol(n,d):
    escalao = [0,0,0,0,0,0]
    
    for x in range(n):
        if  matriz[x][5]=='1':
            while  len(escalao)-1 < (int(matriz[x][3]))//10 : 
                escalao.append(0)
            escalao[(int(matriz[x][3]))//10]+=1

    Xaxis = []
    Yaxis = []

    print( "______________________________________")
    print( "|    Porcentagem de doentes por      |")
    print( "|       niveis de colesterol         |")
    print( "|____________________________________|")

    data=[]

    for x in range(0,len(escalao)):
        if (escalao[x]/d)*100 != 0:
            if ((escalao[x]/d)*100)>10: print(f"| [{10*x}-{9+10*x}]     |           {round((escalao[x]/d)*100,1)}         |")
            else :print(f"| [{10*x}-{9+10*x}] |           {round((escalao[x]/d)*100,1)}          |")
            print( "|___________|________________________|")
            if escalao[x]!=0 :
                Xaxis.append(f"[{10*x}-{9+10*x}]")
                Yaxis.append(round((escalao[x]/d)*100,1))
                data.append([f"[{10*x}-{9+10*x}]",str(round((escalao[x]/d)*100,1))+"%"])
    
    plt.axis('off') 
    plt.title("Porcentagem de doentes por escalão")
    table = plt.table(cellText=data,  cellLoc='center', loc='center')
    table.set_fontsize(10)
    table.scale(1, 1)
    plt.show()

    plt.bar(Xaxis, Yaxis)
    plt.title("Porcentagem de doentes por niveis de colesterol")
    plt.xlabel("Porcentagem (%)")
    plt.ylabel("Colesterol")
    plt.show()


main()