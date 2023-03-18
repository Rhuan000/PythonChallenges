#coloquei um while pra exemplificar mais de uma vez e eu sou preguiçoso
while True:

    #isso aq seria seu prinf e scamf tudo junto e ja transforma em int
    salario = int(input('digite seu salario: '))

    #a lógica que dispensa comentário:
    if salario >= 1300 and salario <= 2500:
        salario_final = salario + 1000

        #só pra retornar na tela o valor final e uma frase bonitinha
        print(f'você terá um aumento de 1000, seu salário final será {salario_final}')

        #ignora essa parte, é só pra melhorar a visibildiade
        print('-'* 100, '\n')

    elif salario < 1300:
        salario_final = salario + 2000

        #só pra retornar na tela o valor final e uma frase bonitinha
        print(f'você terá um aumento de 2000, o seu salário ficou em {salario_final}')

        # ignora essa parte, é só pra melhorar a visibildiade
        print('-' * 100, '\n')