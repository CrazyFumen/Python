def boletim_escolar():

    nota1 = float(input("Digite a nota do 1° Bimestre: "))
    nota2 = float(input("Digite a nota do 2° Bimestre: "))
    nota3 = float(input("Digite a nota do 3° Bimestre: "))
    nota4 = float(input("Digite a nota do 4° Bimestre: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    print(f"\nBoletim de {nome}: ")
    print(f"Média Final: {media:.2f} ")

    if media >= 6:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")