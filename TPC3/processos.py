import re
import json

def main():
    f = open("processos.txt")

    
    all=re.compile(r'(?P<id>\d+)::(?P<ano>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})::(?P<nome>[a-zA-Z ]+)::(?P<nomeP>[a-zA-Z ]+)::(?P<nomeM>[a-zA-Z ]+)::(?P<nomeEtc>[\w\.\, ]+)?::\n')
    pnome=re.compile(r'^[a-zA-Z]+')
    unome=re.compile(r'[a-zA-Z]+$')
    relacao=re.compile(r',(\w[a-zA-Z ]+)\.\s*Proc\.')

    PPA = {} # precessos por ano
    anos = []
    
    PrimeiroNomeSec = {}
    UltimoNomeSec = {}

    DR = {} # Dicionario de relações
    
    for line in f:
        r = all.fullmatch(line)
        if r!=None:
            _ , ano ,_ ,_ , nome , _ , _ , extraRelacao = r.groups()
            if ano in PPA :
                PPA[ano]+=1
            else : 
                PPA[ano]=1
                anos.append(ano)
            
            seculo = (int(ano) - 1) // 100 + 1
            primeiroNome = pnome.search(nome)[0]
            ultimoNome = unome.search(nome)[0]
            
            if (extraRelacao!=None) : 
                relacoes = relacao.findall(extraRelacao)
                if(relacoes):
                    for r in relacoes:
                        if r in DR:
                            DR[r]+=1
                        else : 
                            DR[r]=1
                        


            if seculo not in PrimeiroNomeSec:
                PrimeiroNomeSec[seculo] = {}
                UltimoNomeSec[seculo] = {}
            
            if primeiroNome in PrimeiroNomeSec[seculo]:
                    PrimeiroNomeSec[seculo][primeiroNome]+=1
            else :
                PrimeiroNomeSec[seculo][primeiroNome]=1


            if ultimoNome in UltimoNomeSec[seculo]:
                UltimoNomeSec[seculo][ultimoNome]+=1
            else :
                UltimoNomeSec[seculo][ultimoNome]=1
            



            
    while(True):
        inputUser = input("Escolha o exercicio (a,b,c,d) : ")
        print('-------------------------------------')        
        if (inputUser == 'a'):
            anos.sort()
            for a in anos:
                print(f"{a}: {PPA[a]}")

        elif (inputUser == 'b'):
            nomeSec = dict(sorted(PrimeiroNomeSec.items()))
            for s in nomeSec:
                aux = reversed(dict(sorted(nomeSec[s].items(), key=lambda item: item[1])))
                i=1
                print(f' Primeiro nome mais usado no seculo {s} ')        
                for n in aux:
                    print(f'{i}º nome: {n}  {nomeSec[s][n]}')
                    i+=1
                    if i==6:
                        break
            
            print('-------------------------------------')        
                    
            nomeSec = dict(sorted(UltimoNomeSec.items()))
            for s in nomeSec:
                aux = reversed(dict(sorted(nomeSec[s].items(), key=lambda item: item[1])))
                i=1
                print(f' Apelido nome mais usado no seculo {s} ')        
     
                for n in aux:
                    print(f'{i}º nome: {n}  {nomeSec[s][n]}')
                    i+=1
                    if i==6:
                        break
                  
                
                    
        elif (inputUser == 'c'):
            DRaux = reversed(dict(sorted(DR.items(), key=lambda item: item[1])))
            print(f' Numero de relações de tipo')
            for r in DRaux:
                print(f'   {r} : {DR[r]}')
        
        elif (inputUser == 'd'):
            records = []
            f = open("processos.txt")
            i=0
            for line in f:
                # split the line by '::' delimiter
                fields = line.strip().split('::')
                
                # create a dictionary for the record
                if (len(fields)>=5):
                    record = {
                        'id': fields[0],
                        'birth_date': fields[1],
                        'name': fields[2],
                        'father_name': fields[3],
                        'mother_name': fields[4],
                        'other_relatives': fields[5]
                    }

                    # append the record to the list of records
                    records.append(record)
                    i+=1
                if i==20:
                    break

            with open('db.json', 'w') as jsonfile:
                json.dump(records, jsonfile)
            print('Ficheiro db.json criado com 20 registos')        
            



        else: break
        print('-------------------------------------')        



main()
