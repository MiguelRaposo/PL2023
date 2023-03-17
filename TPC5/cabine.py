import re

def troco(d):
    aux = d
    troco = {"2e" : 0,
             "1e" : 0,
             "50c" : 0,
             "20c" : 0,
             "10c" : 0,
             "5c" : 0,
             "2c" : 0,
             "1c" : 0,
             }
    while True:
        if aux == 0:
            string = ""
            for t in troco:
                if troco[t] != 0:
                    string += f"{troco[t]}x{t} ,"

            return string
        elif aux - 200 >= 0:
            aux -= 200
            troco["2e"]+=1
        elif aux - 100 >= 0:
            aux -= 100
            troco["1e"]+=1
        elif aux - 50 >= 0:
            aux -= 50
            troco["50c"]+=1
        elif aux - 20 >= 0:
            aux -= 20
            troco["20c"]+=1
        elif aux - 10 >= 0:
            aux -= 10
            troco["10c"]+=1
        elif aux - 5 >= 0:
            aux -= 5
            troco["5c"]+=1
        elif aux - 2 >= 0:
            aux -= 2
            troco["2c"]+=1
        elif aux - 1 >= 0:
            aux -= 1
            troco["1c"]+=1

def moedas(list):
    total = 0
    string = ""
    for l in list:
        r = re.match(r'(\d+)([c|e])',l)
        if r.group(2) == "c":
            mult = 1
        elif r.group(2) == "e":
            mult = 100

        if l[:-1] in ["2e","1e","50c","20c","10c","5c","2c","1c"]:
            total += int(r.group(1))*mult
        else :
            string += f"{l} - moeda inválida;"

    return (string,total)
    
        


def main():
    pousar = False
    saldo = 0
    while not pousar:
        op = input("user: ")
        word = re.match(r'^(\w+)',op).group(1)
        if word == "LEVANTAR":
            print("maq: Introduza moedas.")
        elif word == "MOEDA":
            r = re.findall(r'\d+[c|e][,|.]',op)
            string , moedascolocadas = moedas(r)
            saldo += moedascolocadas
            string += f"saldo = {saldo//100}e{saldo - 100*(saldo//100)}c"
            print(string)

        elif re.match(r'^T=(00\d+)|T=(\d{9})$',op):
            r = re.match(r'^T=(00\d+)|T=(\d{9})$',op)
            tel = r.group(2)
            if r.group(1):
                if saldo - 150 >=0:
                    saldo -= 150
                    print(f"maq: saldo = {saldo//100}e{saldo - 100*(saldo//100)}c")        
                else:
                    print("maq: sem saldo")        
            elif tel[:3] in ["601","641"]:
                print("maq: Chamada bloqueada")        
            else : 
                if tel[:3] == "808":
                    if saldo - 10 >=0:
                        saldo -= 10
                        print(f"maq: saldo = {saldo//100}e{saldo - 100*(saldo//100)}c")  
                    else:
                        print("maq: sem saldo")
                elif tel[:1] == "2":  
                    if saldo - 25 >=0:
                        saldo -= 25
                        print(f"maq: saldo = {saldo//100}e{saldo - 100*(saldo//100)}c")  
                    else:
                        print("maq: sem saldo")
        elif word == "POUSAR":
            print (f"troco= {troco(saldo)}; Volte sempre!")
            saldo = 0
        elif word == "ABORTAR":
            saldo = 0
            break 
            



main()