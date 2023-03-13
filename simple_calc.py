# # SIMPLE CALCULATOR WITH LOOP WHILE
# THE CALCULATOR WITH FUNCTIONS IS BELOW THIS CODE



# while True:
#     opcao_invalida = 'abcdefghijklmnopqrstuvwxyz'
    
#     print('----------- Menu Calculadora -------------')
#     print('[1] Soma')
#     print('[2] Subtração')
#     print('[3] Multiplicação')
#     print('[4] Divisão')
#     print('[0] Sair\n')
#     # pega a operação realiza e armazena como string  
#     opcao_inicial = input('Digite o numero de qual operação deseja realizar: ')
    
#     # verifica se o dado inserido é um digito ou não, após isso realiza a condição if
#     # true = funciona calculadora
#     if opcao_inicial.isdigit():
#         opcao = int(opcao_inicial)
#         if opcao > 0 and opcao <= 4:    
#             val_1 = input('Agora digite o primeiro valor: ')
#             val_2 = input('Digite o segundo valor: ')
#             valor_1 = float(val_1)
#             valor_2 = float(val_2)
#             numeros_validos = True
#             if opcao == 1:
#                 res = valor_1 + valor_2
#                 print(f'O resultado é: {res}')
#             elif opcao == 2:
#                 res = valor_1 - valor_2
#                 print(f'O resultado é: {res}')
#             elif opcao == 3:
#                 res = valor_1 * valor_2
#                 print(f'O resultado é: {res}')
#             elif opcao == 4:
#                 res = valor_1 / valor_2
#                 print(f'O resultado é:{res:.2f}')    # divisão não inteira com  2 casas decimais
                
#         elif opcao < 0 or opcao > 4:#usuário quer fazer operação fora dos valores disponiveis
#             print('Opção inválida. Digite uma opção valida do menú! ')
#             continue    #volta pro menu da calculadora
        
        
#         elif opcao == 0:
#             print('A calculadora será finalizada! ')
#             break
    
#     # se alguma letra ou dados fora do range foram inseridos no campo, um erro será apresentado na tela
#     else:
#         print('Opção inválida. Digite uma opção válida do menú')
#         continue  
    
    
    
# SIMPLE CALCULATOR WITH FUNCTION AND LOOPS  
import os


# def <função>(pode ser vazio ou incluir variáveis a serem usadas)

def soma(val_1_int, val_2_int):
    res = val_1_int + val_2_int
    print(f'O resultado da soma é igual a {res}')
    
    
    
def sub(val_1_int, val_2_int):
    res = val_1_int - val_2_int
    print(f'O resultado da subtração é igual a {res}')

def mult(val_1_int, val_2_int):
    res = val_1_int * val_2_int
    print(f'O resultado da multiplicação é igual a {res}')
    
    
def div(val_1_int, val_2_int):
    res = val_1_int / val_2_int
    print(f'O resultado da divisão é igual a {res}')
    
    

def menu():
    
    while True:
        
        op = input(f'Bem-vindo ao menú, abaixo as opções listadas para escolher\n\
1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- [S]air\nOpção desejada: ').lower()
        os.system('cls')
        
        
        try:
            op.isdigit()
            opcao = int(op)
            if opcao == 1:
                val_1 = input('Digite o primeiro valor da soma: ')
                val_2 = input('Agora digite o último valor: ')
                try:
                    val_1.isnumeric()
                    val_2.isnumeric()
                    val_1_int = int(val_1)
                    val_2_int = int(val_2)
                    soma(val_1_int,val_2_int)
                except:
                    print('Valor inserido é invalido, tente novamente! ')
                    continue
                
                
            elif opcao == 2:
                val_1 = input('Digite o primeiro valor para subtração: ')
                val_2 = input('Agora digite o último valor: ')
                try:
                    val_1.isnumeric()
                    val_2.isnumeric()
                    val_1_int = int(val_1)
                    val_2_int = int(val_2)
                    sub(val_1_int, val_2_int)
                except:
                    print('Valor inserido é invalido, tente novamente! ')
                    continue
                
                
            elif opcao == 3:
                val_1 = input('Digite o primeiro valor para multiplicação: ')
                val_2 = input('Agora digite o último valor: ')
                try:
                    val_1.isnumeric()
                    val_2.isnumeric()
                    val_1_int = int(val_1)
                    val_2_int = int(val_2)
                    mult(val_1_int, val_2_int)
                except:
                    print('Valor inserido é invalido, tente novamente! ')
                    continue
                
                
            elif opcao == 4:
                val_1 = input('Digite o primeiro valor para divisão: ')
                val_2 = input('Agora digite o último valor: ')
                try:
                    val_1.isnumeric()
                    val_2.isnumeric()
                    val_1_int = int(val_1)
                    val_2_int = int(val_2)
                    div(val_1_int, val_2_int)
                except:
                    print('Valor inserido é invalido, tente novamente! ')
                    continue                
            
            
        except:
            if op.startswith('s') and len(op) == 1:
                print('O programa foi finalizado!!')
                break                
            else:
                print('Valor inválido, tente novamente! ')
                continue


menu()
            
     