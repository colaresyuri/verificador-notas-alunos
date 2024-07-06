##Sistema de notas escolares##
#Programa que leia o nome do aluno e suas 4 notas, e calcule.

#input do aluno(a)

nome = input("Digite o nome do Aluno(a):")
print(f"Seja bem-vindo(a),{nome}")

#notas dos bimestres

bimestre1 = 30
bimestre2 = 72
bimestre3 = 75
bimestre4 = 78

#Calculo das notas
media = ((bimestre1 + bimestre2 + bimestre3 + bimestre4)/4)

print(f"{nome}, sua nota final é:{media}")

#Verificação de notas

if media < 70:
    print("Reprovado!")
else:
    print("Aprovado!")

