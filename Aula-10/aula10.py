  # Sistema de notas de alunos - Visão do professor
senha_correta = "1234"
tentativas = 3
acesso_permitido = False

# Controle de acesso com while (3 chances)
while tentativas > 0:
  senha_digitada = input("Digite a senha do professor: ")
  if senha_digitada == senha_correta:
    print("Acesso permitido!")
    acesso_permitido = True
    break
  else:
    tentativas -= 1
    print(f"Senha incorreta. Você ainda tem {tentativas} tentativa(s).")

if not acesso_permitido:
  print("Conta bloqueada (senha incorreta).")
else:
  # Inserção de notas e cálculo da média
  aluno_dados = {"nome": input("Digite o nome do aluno: "), "notas": []}

  quantidade_notas = int(
      input("Quantas notas deseja inserir para este aluno? ")
  )

  for i in range(quantidade_notas):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    aluno_dados["notas"].append(nota)

  # Cálculo da média
  notas_tupla = tuple(aluno_dados["notas"])
  if len(notas_tupla) > 0:
    media = sum(notas_tupla) / len(notas_tupla)
    print(f"\nAluno: {aluno_dados['nome']}")
    print(f"Média final: {media:.2f}")
  else:
    print("Nenhuma nota foi cadastrada.")

input("Digite enter para sair")