#Questionário para diagnóstico
print ('Responda o seguinte questionario para receber seu diagnostico.(Apenas com s ou n)')
A=str(input ('Sente dor no corpo? '))
B=str(input ('Voce tem febre? '))
C=str(input ('Voce tem tosse? '))
D=str(input ('Esta com congestao nasal? '))
E=str(input ('Tem manchas no corpo? '))
 
#Diagnostico tabela
def diagnostico (A,B,C,D,E):
    resp = (A,B,C,D,E)
    diagns = {"dengue":('s','s','n','n','s'), "gripe1":('s','s','s','s','n'), "gripe2":('n','s','s','s','n'), "gripe3":('s','s','s','s','n')}
    if diagns ["dengue"]==resp : {
        print ('Voce esta com dengue.')
    } 
    elif diagns ["gripe1"]==resp : {
        print ('Voce esta com gripe')
    }
    elif diagns ["gripe2"]==resp : {
        print ('Voce esta com gripe')
    }
    elif diagns ["gripe3"]==resp : {
        print ('Voce esta com gripe')
    }
    else : {
        print('Desconhecido, procure tratamento')
    }
diagnostico (A,B,C,D,E)
       