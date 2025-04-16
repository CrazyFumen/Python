import sys

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print("Digite seu time de futebol: ")
equipe = sys.stdin.readline()

print("Nome: "+ nome + "\n" + "Time: %sIdade: %s" %(equipe,idade))