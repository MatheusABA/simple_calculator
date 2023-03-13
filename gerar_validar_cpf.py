""" Validar CPF
CPF = 789.339.191-04
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma contagem regressiva começando de 10

Somar todos os resultados
Multiplicar o resultado anterior por 10
Obter o resto da divisão da conta anterior por 11
Se o resultado for maior que 9, ele é 0

"""
import random


cpf_digitado = ''


# gerador de cpf
for i in range(9):
    cpf_digitado += str(random.randint(0,9))


condicao = True
soma = 0
soma_2 = 0
cont_regret = 10
cont_regret_2 = 11
res_final = 0
res_final_2 = 0
cpf_nove_digitos = ''

while condicao:
    
   
    if cpf_digitado:
        # altera os parametros . - e espaço para sumirem da variável e juntar os numeros
        cpf_nove_digitos = cpf_digitado.replace('.', '').replace('-','').replace(' ','')
        cpf_nove_digitos = cpf_nove_digitos[:9]
        print('CPF salvo com sucesso! ')
    
    elif not cpf_digitado:
        print('Insira outro cpf! ')
        continue
    
    # Contas primeiro dígito
    
    for num in cpf_nove_digitos:
        res = (int(num)*cont_regret)
        cont_regret -= 1
        soma = soma + res
        print(f'{num} * {cont_regret} = {res}')
    
    print(f'Soma da multiplicação: {soma}')     # apresentando resultado da soma das multiplicações
    
    novo_res = soma * 10
    print(f'Resultado de {soma} * 10 = {novo_res}')
    
    resto = novo_res % 11
    print(f'Resto igual a {resto}')
    
    # Gerando primeiro digito do cpf
    
    if resto > 9:
        res_final = 0
    else:
        res_final = resto
        
    print(f'Primeiro digito igual a: {res_final}')
    
    
    # Contas segundo dígito
    cpf_nove_digitos = cpf_digitado.replace('.', '').replace('-','').replace(' ','')
    cpf_nove_digitos = cpf_nove_digitos[:10]
    
    for num in cpf_nove_digitos:
        res_2 = (int(num)*cont_regret_2)
        cont_regret_2 -= 1
        soma_2 = soma_2 + res_2
        print(f'{num} * {cont_regret_2} = {res_2}')
    
    print(f'Soma da multiplicação: {soma_2}')     # apresentando resultado da soma das multiplicações
    
    novo_res_2 = soma_2 * 10
    print(f'Resultado de {soma_2} * 10 = {novo_res_2}')
    
    resto_2 = novo_res_2 % 11
    print(f'Resto igual a {resto_2}')
    
    
    if resto_2 > 9:
        res_final_2 = 0
    else:
        res_final_2 = resto_2
        
    print(f'Primeiro digito igual a: {res_final_2}')
    
    
    
    
    print(f'Seu cpf é igual a {str(cpf_nove_digitos[:9])+str(res_final)+str(res_final_2)}')
    break


    
    
    
    