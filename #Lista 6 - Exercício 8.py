num = [0]*10
qnt = 0
x = float(input('Insira um número qualquer: '))


for i in range (10):
    num[i] = float(input(f'Insira o {i+1}º número de um vetor de 10 números: '))
    if x!=0:
        if num[i]%x==0:
            qnt+=1

mult = [0]*qnt
mult2 = [0]*qnt
    
if x!=0:
    for i in range(10):
        if num[i]%x==0:
            for c in range(qnt):
                if mult[c] == 0 and mult2[c] == 0:
                    mult[c] = num[i]
                    mult2[c] = mult[c] / x
                    break       
if x == 0:
    print(f'Todos os 10 números {num} são múltiplos de {x}.')
elif len(mult) == 0:
    print(f'Dentre os 10 números informados para compor o vetor, nenhum é múltiplo inteiro de {x}.')       
else:
    print(f'Dentre os 10 números informados para compor o vetor, {qnt} são múltiplos de {x}: {mult}. \nSendo esses resultados da multiplicação de {x} por {mult2}.')       
            
