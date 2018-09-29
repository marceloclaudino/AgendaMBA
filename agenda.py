#Agenda Telefonica
#Alterarei aqui Euuuuu
import funcoes

funcoes.bemvindo()

#Opcoes do Usuario
opcao = int(raw_input())
print("Selecionou a ", opcao)


#Estrutura de controle
if opcao == 2:
	funcoes.adicionar()
elif opcao == 2:
	funcoes.listar()
else:
	funcoes.falha()


