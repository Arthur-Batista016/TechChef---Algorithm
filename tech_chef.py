import os
import time
from tkinter import E
from tokenize import Double



#1- Criar Receita
def CriarReceita(rec_dict:dict, medidas:list)->None:
    receita = str(input("Digite o nome da sua receita: "))
    quant_ing = 0
    ings_add = []

    while True:

        ing = input("Digite o nome do ingrediente: ")
        valor_ing = float(input("Qual a quantidade desse ingrediente? (Apenas o Valor numerico): "))
        med = input("Qual a unidade de medida? (ex: ml, kg, L, (u) - para unidades): ")
        if med in medidas:
            valor_med = f"{ing},{valor_ing:.2f},{med}" 
            ings_add.append(valor_med)

            os.system("cls")
            rec_dict[receita] = ings_add
            print("Ingrediente adicionado com sucesso!")
            time.sleep(1)

            add = int(input("Deseja adicionar mais um ingrediente [1-Sim, 2-Nao]: "))
            os.system("cls")

            if add == 1:
                quant_ing += 1

            elif add == 2:
                os.system("cls")
                porc = int(input("Quantas pessoas podem ser servidas com essa receita: "))
                ings_add.append("Serve " + str(porc) + " Pessoas")
                rec_dict[receita] = ings_add

                print(rec_dict)
                os.system("cls")
                print(f"RECEITA -> | {receita} | CRIADA COM SUCESSO! VOLTANDO AO MENU.")
                time.sleep(5)
                os.system("cls")
                break
        else:
            os.system("cls")
            print("Digite uma unidade de medida valida!, tente Novamente")
            time.sleep(3)
            os.system("cls")

            
            

            

#2- Editar Receita
def EditarReceita(rec_dict:dict, medidas:list)->None:
    while True:
        ListarReceitas_min(rec_dict)
        print("\n\nDeseja redimensionar alguma de suas receitas? ")
        print("[1]- Sim [2]- Não")
        change = int(input("Escolha: "))   
        os.system('cls')
        if change == 1:
            porc_antiga = ""
            ListarReceitas_min(rec_dict)
            receita =  str(input("\n\n-Digite o nome da receita que deseja alterar: "))
            if receita in rec_dict:
                nova_porc = int(input("Digite o novo valor de pessoas: "))               
                for p in rec_dict[receita][-1]:
                    if p.isdigit():
                        porc_antiga += p
                red_porc = nova_porc / int(porc_antiga)
                rec_dict[receita][-1] = "Serve " + str(nova_porc) + " Pessoas"
              
         

                for i in range(len(rec_dict[receita]) - 1):
                    valor_a_alterar = ""
                    un_medida = ""
                    ingrediente = rec_dict[receita][i]


                    partes = ingrediente.split(",")
                    nome = partes[0]  # Nome do ingrediente
                    valor_a_alterar = float(partes[1])  # Quantidade
                    un_medida = partes[2].strip(",") 
                    novo_valor_ing = float(valor_a_alterar) * red_porc
                    rec_dict[receita][i] = f"{nome},{novo_valor_ing:.2f},{un_medida}"

               
             
                print("RECEITA REDIMENSIONADA COM SUCESSO! VOLTANDO AO MENU.")
                time.sleep(5)
                os.system("cls")
                break
            else:
                print("Receita não encontrada. Tente Novamente !")
                time.sleep(2)
                os.system('cls')
        else:
            print("Redimensionamento cancelado. Voltando ao menu.")
            print("VOLTANDO AO MENU")
            break
       
     
# metodo sem sleep
def ListarReceitas_min(rec_dict:dict)->None:
    if rec_dict == {}:
        print("Nenhuma receita cadastrada. Volte ao menu para criar uma receita.")
        time.sleep(5)
    else:
        print("-----Receitas-----")

        for k, v in rec_dict.items():
            ingredientes_formatados = []

            for ing in v[:-1]:
                partes = ing.split(",")
                nome = partes[0]
                valor = partes[1]
                unidade = partes[2]
                ingredientes_formatados.append(f"{nome} {valor} {unidade}")
           
            ingredientes = ", ".join(ingredientes_formatados)
            porcoes = v[-1]

            print(f"{k} -> Ingredientes: {ingredientes} -> Porções: {porcoes}")



#3- Listar Receitas

def ListarReceitas(rec_dict:dict)->None:
    if rec_dict == {}:
        print("Nenhuma receita cadastrada. Volte ao menu para criar uma receita.")
        time.sleep(5)
    else:
        print("-----Receitas-----")

        for k, v in rec_dict.items():
            ingredientes_formatados = []

            for ing in v[:-1]:
                partes = ing.split(",")
                nome = partes[0]
                valor = partes[1]
                unidade = partes[2]
                ingredientes_formatados.append(f"{nome} {valor} {unidade}")
           
            ingredientes = ", ".join(ingredientes_formatados)
            porcoes = v[-1]

            print(f"{k} -> Ingredientes: {ingredientes} -> Porções: {porcoes}")
        time.sleep(5)    
           
    os.system("cls")

     
        





#4 - Deletar Receitas
def ExcluirReceita(rec_dict:dict)->None:
    while True:
        ListarReceitas_min(rec_dict)
        choice  = str(input("Digite o nome da receita que deseja excluir: "))
        if choice in rec_dict:
            del rec_dict[choice]
            os.system('cls')
            print(f"Receita '{choice}' excluída com sucesso!")
            print("VOLTANDO AO MENU")
            time.sleep(5)
            os.system("cls")
            break
        else:
            print("Receita não encontrada. Tente novamente.")
            time.sleep(2)
            os.system('cls')






#MENU----------------------------------------------------
receitas_dict = {

}  

unidades = ["g","kg","mg","ml","l","colher","xicara", 'u', 'U']

while True:
    escolha = input('''
------BEM VINDO AO TECH CHEF - SEU CHEFE DIGITAL DE RECEITAS!------
                        
Aqui voce pode criar, organizar e visualizar receitas, adicionando ingredientes, quantidades e unidades de medida.
O sistema tambem permite redimensionar receitas, ajustando automaticamente os ingredientes conforme o numero de pessoas.

0- Sair
1- Criar Receita
2- Redimensionar Receita
3- Listar Receitas
4-Excluir uma receita

O que deseja fazer?? 
Escolha: ''')

    if escolha == '1':
        os.system('cls')
        CriarReceita(receitas_dict,unidades)
    elif escolha == '2':
        os.system('cls')
        EditarReceita(receitas_dict,unidades)
    elif escolha == '3':
        os.system('cls')
        ListarReceitas(receitas_dict)
    elif escolha == '4':
        os.system('cls')
        ExcluirReceita(receitas_dict)
    elif escolha == '0':
        os.system('cls')
        print("MUITO OBRIGADO POR UTILIZAR O PROGRAMA!")
        print("SAINDO")
        exit()
    else:
        os.system("cls")
        print("Opção inválida. Tente novamente.")
        time.sleep(5)
        os.system("cls")
        
        
        

