#idade doar sangue

ano = int(input("Em que ano voce nasceu? "))
idade = 2024 - ano

if idade >= 16 and idade < 18:
    print("Voce pode doar com a autorização de um responsavel")
elif idade >= 18 and idade <= 60:
    print("Voce pode doar sangue quando quiser")
elif idade > 60 and idade <=69:
    print("Voce pode doar sangua desde que seja registrado como doador")
else:
    print("Voce não pode doar sangue")