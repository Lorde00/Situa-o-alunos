def media(n):
    if not n:
        return f'Nenhuma nota foi adcionada.'
    
    med = (sum(n) / len(n))
    medias.append(med)
    return f'\nA média calculada das {len(n)} notas é de {medias[0]}\n'
            
def sitaluno(medias):
    
    if not medias:
        return 'Nenhuma média calculada. Envie as notas primeiro.'
    
    for m in medias:
        
        if m <= 6.99:
            return f'Você foi reprovado com média igual a {m}'
        
        elif m >= 7:
            return f'Você foi aprovado com média igual a {m}! Parabéns!!'
        
        elif m == 10:
            return f'Você passou voando! Sua média foi igual a {m}! Incrível!!'


notas = []
medias = []

while True:
    decisao = int(input('\nDigite a opção que deseja escolher:\n \n(1)Enviar notas\n \n(2)Calcular média\n \n(3)Situação do aluno\n \n(4)Apagar notas\n \n(5)Sair\n'))

    match decisao:

        case 1:
            qtd = int(input('\nQuantas notas você quer calcular?\n'))
            for i in range(qtd):
                valor = int(input(f'\nDigite quanto você tirou na {i + 1}º nota:\n'))
                notas.append(valor)

        case 2:
            print(media(notas))

        case 3:
            print(sitaluno(medias))

        case 4:
            print('Média e notas removidas.')
            notas.clear()
            medias.clear()

        case 5:
            print('Obrigado por usar o programa!')
            break
        