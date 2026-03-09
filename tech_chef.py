from cgi import print_arguments
from distutils.command.install_egg_info import install_egg_info
import os
import string
import time
from tkinter import E
from tokenize import Double



#1- Criar Receita
def CriarReceita(rec_dict:dict)->None:
    receita = str(input("digite o Nome da sua receita: "))
    quant_ing = 0
    ings_add = []
    while True:

        ing = str(input(("Digite o nome do ingrediente: ")))
        valor_ing = int(input("Qual a quantidade desse ingrediente: "))
        med = str(input("Qual a unidade de medida (ex: ml,kg,L): "))
        valor_med = str(ing) + " " + str(valor_ing) + str(med) + ","
        ings_add.append(valor_med)
        print("Ingrediente adicionado com sucesso!") 
        print(ings_add)
        add = int(input("Deseja adicionar mais um ingrediente [1-Sim, 2-Nao]:"))
        if add == 1:
            quant_ing +=1
        elif add ==2:
            porc = int(input("Quantas pessoas podem ser servidas com essa receita: "))
            ings_add.append("Serve " + str(porc) + " Pessoas")
            rec_dict[receita] = ings_add
            print(rec_dict)
            os.system("cls")
            print(f"RECEITA -> | {receita} | CRIADA COM SUCESSO! VOLTANDO AO MENU.")
            print(str(receitas_dict))
            break  
           

            

#2- Editar Receita
def EditarReceita(rec_dict:dict, medidas:list)->None:
    while True:
        ListarReceitas(rec_dict)
        print("Deseja redimensionar alguma de suas receitas? ")
        print("[1]- Sim [2]- Não")
        change = int(input("Escolha: "))   
        os.system('cls')
        if change == 1:
            valor_a_alterar = ""
            un_medida = ""
            porc_antiga = ""
            ListarReceitas(rec_dict)
            receita =  str(input("Digite o nome da receita que deseja alterar: "))
            if receita in rec_dict:
                nova_porc = int(input("Digite o novo valor de pessoas: "))               
                for p in rec_dict[receita][-1]:
                    if p.isdigit():
                        porc_antiga += p
                rec_dict[receita][-1] = "Serve " + str(nova_porc) + "Pessoas"
                red_porc = nova_porc / int(porc_antiga)
                # antes dessa linha esta correto









                for i in range(len(rec_dict[receita]) - 1):
                    ingrediente = rec_dict[receita][i]
                    for c in ingrediente:
                        if c.isdigit():
                            un_medida += i
                        else:
                            valor_a_alterar += str(i)

                    novo_valor_ing = int(valor_a_alterar) * red_porc
                    rec_dict[receita][i][:-1] = str(valor_a_alterar) + un_medida
                print(rec_dict)
                time.sleep(5)         
                
                print(rec_dict[receita][:-1])
                print(rec_dict[receita][:1])
                time.sleep(5)
            else:
                print("Receita não encontrada. Escreva uma receita existente")
                os.system('cls')
        else:
            print("Redimensionamento cancelado. Voltando ao menu.")
            print("VOLTANDO AO MENU")
            break
       
     
            print(rec_dict)
            print("RECEITA REDIMENSIONADA COM SUCESSO! VOLTANDO AO MENU.")
            break


    

#3- Listar Receitas
def ListarReceitas(rec_dict:dict)->None:
    if rec_dict == {}:
        print("Nenhuma receita cadastrada. Volte ao menu para criar uma receita.")
        time.sleep(5)
    else:
        print("-----Receitas-----")
        for k,v in rec_dict.items():
            print(f"{k} -> Ingredientes: {v[:-1]} -> Porcoes: {v[-1]}" )
            time.sleep(5)
        





#4 - Deletar Receitas
def ExcluirReceita(rec_dict:dict)->None:
    while True:
        print("-----Receitas-----")
        for k,v in rec_dict.items():
            print(f"{k} -> Ingredientes: {v}")
            time.sleep(5)
        choice  = str(input("Digite o nome da receita que deseja excluir: "))
        if choice in rec_dict:
            del rec_dict[choice]
            os.system('cls')
            print(f"Receita '{choice}' excluída com sucesso!")
            print("VOLTANDO AO MENU")
            break
        else:
            print("Receita não encontrada. Tente novamente.")
            os.system('cls')






#MENU----------------------------------------------------
receitas_dict = {

}  

unidades = ["m","g","k","z","l","m","c","d",
"f","p","s","x","i"]

while True:
    escolha = int(input('''
------BEM VINDO AO TECH CHEF - SEU CHEFE DIGITAL DE RECEITAS!------
                        
Aqui voce pode criar, organizar e visualizar receitas, adicionando ingredientes, quantidades e unidades de medida.
O sistema tambem permite redimensionar receitas, ajustando automaticamente os ingredientes conforme o numero de pessoas.

0- Sair
1- Criar Receita
2- Redimensionar Receita
3- Listar Receitas
4-Excluir uma receita

O que deseja fazer?? 
Escolha: '''))

    if escolha == 1:
        os.system('cls')
        CriarReceita(receitas_dict)
    elif escolha == 2:
        os.system('cls')
        EditarReceita(receitas_dict,unidades)
    elif escolha == 3:
        os.system('cls')
        ListarReceitas(receitas_dict)
    elif escolha == 4:
        os.system('cls')
        ExcluirReceita(receitas_dict)
    elif escolha == 0:
        os.system('cls')
        print("MUITO OBRIGADO POR UTILIZAR O PROGRAMA!")
        print("SAINDO")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(5)
        
        

