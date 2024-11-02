
quantidade = int(input('Digite a quantidade de alunos: '))
notas_turma = []


for notas in range(quantidade):
    alunos = input('Digite o nome do aluno:')
    notas1 = float(input('Digite a nota do aluno:'))
    notas2 = float(input('Digite a nota do aluno:'))
    notas3 = float(input('Digite a nota do aluno:'))

    soma = notas1 + notas2 + notas3
    media = soma / 3
    notas_turma.append(media)

    
    if media > 7:
        print(f'{alunos}, foi aprovado com {notas1}, {notas2}, {notas3}, sendo assim sua média foi {media}')
    elif media < 7:
        print(f'{alunos}, foi reprovado com {notas1}, {notas2}, {notas3}, sendo assim sua média foi {media}')



    if notas_turma:
        media_geral = sum(notas_turma) / len(notas_turma)
        print(f'A média geral da turma é: {media_geral:.2f}')
    
print( f'esse é o número de alunos na sala: {quantidade}') 
    
    
   
    
    

    

