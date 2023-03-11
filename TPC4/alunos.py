import json
import re

notasre =re.compile(r',Notas{(?P<n1>\d),?(?P<n2>\d)?}:?:?(?P<cal>\w+)?')
with open('alunos.csv', 'r') as file:
    n = notasre.search(file.readline())
   
    if n :
        if n.group("n2"):
            numNotas = range(int(n.group("n1")),int(n.group("n2"))+1)
        else:
            numNotas = range(int(n.group("n1")),int(n.group("n1"))+1)
    
    data = []

    for line in file:
        words = line.replace('\n','').split(',')
        dic = {}
        dic["Número"] = words[0]
        dic["Nome"] = words[1]
        dic["Curso"] = words[2]
        if n :
            i = 0
            r = 0
            if n.group("cal") == "sum" and len(words)-3 in numNotas:
                r = sum(int(x) for x in words[3:])
                dic["Notas_sum"] = r
            elif n.group("cal") == "media" and len(words)-3 in numNotas:
                r = sum(int(x) for x in words[3:]) / len(words[3:])
                dic["Notas_media"] = r
            elif len(words)-3 in numNotas:
                notasList = [int(x) for x in words[3:]]
                dic["Notas"] = notasList
                

        data.append(dic)

        

with open('alunos.json', 'w') as jsonfile:
    json.dump(data, jsonfile,ensure_ascii=False, indent=4)


