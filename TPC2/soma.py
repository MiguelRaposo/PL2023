def main():
    a = input("Pretende ler um ficheiro? s/n\n")
    soma = 0
    readflag = True
    if a != "s":
        line = input("input : ")
        words = splitwords(line)
        print(words)
        if line != '':
            for word in words:
                if word.isdigit() and readflag:
                    soma += int(word)
                if word == "=":
                    print(soma)
                if word in ("on","On","oN","ON"):
                    readflag = True
                if word in ("off","Off","oFf","ofF","OFf","oFF","OfF","OFF"):
                    readflag = False
    else :
        a = input("Caminho do ficheiro : ")
        try:
            f = open(a,"r")
            for line in f:
                words = splitwords(line)
                print(words)
                if line != '':
                    for word in words:
                        if word.isdigit() and readflag:
                            soma += int(word)
                        if word == "=":
                            print(soma)
                        if word in ("on","On","oN","ON"):
                            readflag = True
                        if word in ("off","Off","oFf","ofF","OFf","oFF","OfF","OFF"):
                            readflag = False
        except FileNotFoundError:
            print("\nCaminho do ficheiro errado")

def splitwords(string):
    r=[]
    aux=""
    flag=-1
    for c in string:
        if not c.isdigit() and flag == 0:
            r.append(aux)
            aux = ""
        if c.isdigit():
            aux += c
            flag = 0
        elif c in ["o","O"]:
            flag = 1
        elif c in ["n","N"] and flag==1:
            r.append("on")
        elif c in ["f","F"]:
            if flag == 1:
                flag = 2
            elif flag == 2:
                r.append("off")
                flag = -1
        elif c == "=":
            r.append("=")
            flag = -1
        else :
            flag = -1

    return r

main()