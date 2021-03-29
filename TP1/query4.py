import re
import generalFunctions as gf

def procuraMae(mae):
    f=open('processos.xml','r')
    processos = gf.getProcessos(f.read())
    
    processos_avaliados = set()

    flag = False

    for p in processos:
        pr = p[0]
        
        if _id_:= gf.getId(pr):
            
            if _id_ in processos_avaliados:
                pass
            else:
                processos_avaliados.add(_id_)
                
                if re.search(r'<mae>{mae}</mae>',pr):
                    if flag:
                        print(f'{mae} tem mais do que um filho.')
                        return
                    else:
                        flag = True
                            
    print(f'{mae} não tem mais que um filho.')
    f.close()
                
                
                
        
def procuraPai(pai):
    processos_avaliados = set()
    f = open('processos.xml', 'r')
    processos = gf.getProcessos(f.read())

    flag = False

    for p in processos:
        pr = p[0]
        
        if _id_ := gf.getId(pr):

            if _id_ in processos_avaliados:
                pass
            else:
                processos_avaliados.add(_id_)

                if re.search(rf'<pai>{pai}</pai>',pr):
                    if flag:
                        print(f'{pai} tem mais do que um filho.')
                        return
                    else:
                        flag = True
    print(f'{pai} não tem mais que um filho.')
    f.close()

def Query4():

    opcao = -1
    while opcao != 0:
        print('1 - Pesquisar por Pai')
        print('2 - Pesquisar por Mãe')
        print('0 - Sair')
        opcao = int(input('Indique a sua opção: '))
        
        if opcao == 1:
            pai = input('Indique o nome do Pai: ')
            procuraPai(pai)
        elif opcao == 2:
            mae = input('Indique o nome da Mãe: ')
            procuraMae(mae)
        elif opcao < 0 and opcao > 2:
            print("Opção inexistente.\nTry again.")
    