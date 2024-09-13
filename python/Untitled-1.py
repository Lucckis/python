#Python 13/9/24

nome = input("Insira seu nome: ")
sobrenome = input("Insire seu sobrenome: ")

print ("Olá, ", nome, sobrenome, ", seja bem vindo!")

nascimento = int(input("Qual ano que voce nasceu?"))
idade = 2024 - nascimento

print(f'Sua idade maxima possivel é ', idade)

if nascimento <= 2000 and nascimento >= 1901:
    print("Voce nasceu no século XX.")
elif nascimento >= 2001 and nascimento <= 2100: 
    print("Voce nasceu no século XXI.")
else:
    print("Fonte: confia")
    
    
    
seculo = int(input("Qual seculo? "))

ano_final = seculo * 100
ano_inicial = ano_final - 99 

print('Este seculo vai do ano', ano_inicial, 'até o ano', ano_final)

if ano_final > 2024 and ano_inicial <= 2001:
    print("Esse é o século atual")
else:
    print("Este NÃO é o século atual")