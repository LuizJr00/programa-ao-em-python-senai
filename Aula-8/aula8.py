# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida.
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida.
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferent
l1=  int(input('Lado 1 '))
l2=  int(input('Lado 2 '))
l3=  int(input('Lado 3 '))



if l1 == l2  == l3  == l1:
    print('equilatero')
elif l1 != l2 != l3 != l1:
    print('escaleno')    
else:
    print('Iscosceles')    

# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferent
idade =  int(input('Idade:  '))
if idade >= 16 and idade <=17:
    print('Pode votar')
elif idade >= 18 and idade <= 65:
    print('Deve votar')
else:
    print('Não precisa votar')  


numero = int(input('numero>> '))
match numero:
    case x if x  % 2 ==0:
        print('par')
    case _:
        print('impar')    
	

#  Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)  



idade =  int(input('Idade: '))
match idade:
    case idade if idade <= 12:
        print('Criança')
    case idade if idade >= 13 and idade <=17:
        print('Adolescente')
    case idade if idade >= 18  and idade <= 35:
        print('Jovem')
    case idade if idade > 35 and idade <= 65:
        print('Adulto')
    case _:
        print('Idoso')      




import random




# escolha_pc = random.choice(opcao_pc)
# print(escolha_pc)
   
for chance in range(1,4):
    opcao_pc  =  ['✂️','🪨', '🧻']
    escolha_pc = random.choice(opcao_pc)
    # print(escolha_pc)
    minha_escolha = input('Escolha>>')
    if escolha_pc == minha_escolha:
        print('Acertou vc escolheu', minha_escolha)
        print('A maquina escolheu ',escolha_pc)
        break
    else:
        print('Errou feio, vc escolheu...', minha_escolha)
        print('A maquina escolheu ',escolha_pc)
else:
    print('Chances esgotadas')            



	




import random

meus_pontos = 0
pontas_maquina = 0

# escolha_pc = random.choice(opcao_pc)
# print(escolha_pc)
    
add  =  [3,2,1]

for chance in add:
    opcao_pc  =  ['✂️']
    escolha_pc = random.choice(opcao_pc)
    # print(escolha_pc)
    minha_escolha = input('Escolha>>')
    if escolha_pc == minha_escolha:
        print('Empate')
        pontas_maquina = pontas_maquina + 1
        meus_pontos = meus_pontos + 1
        add.append(1)
        print(add)
        
        
    elif escolha_pc == '✂️' and minha_escolha == '🧻':
        print('Maquina ganhou')
        pontas_maquina = pontas_maquina + 1
        print(add)
    elif escolha_pc == '🧻' and minha_escolha == '🪨':
        print('Maquina ganhou')
        pontas_maquina = pontas_maquina + 1
        print(add)  
    elif escolha_pc == '🪨' and minha_escolha == '✂️':
        print('Maquina ganhou')  
        pontas_maquina = pontas_maquina  + 1
        print(add)             
    else:
        print('Você ganhou!!!!')
        meus_pontos =  meus_pontos + 1

else:
   
    if meus_pontos > pontas_maquina:
        print('Vc é o vencedor do jogo 🏆')
    elif  meus_pontos == pontas_maquina:
        print('EMPATE GERAL')    
    else:
        print('A MÁQUINA É O VENCEDOR!! 🏆')    

    print('Chances esgotadas')       
    print(f'''
             PLACAR
----------------------------------             
seus pontos{meus_pontos}
pontos da maquina {pontas_maquina} 
----------------------------------

''')     


