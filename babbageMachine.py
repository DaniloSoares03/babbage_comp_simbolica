def nextValue(diffs):
    linha = len(diffs) - 1
    proximoTermo = 0
    for i in range(linha):
        proximoTermo += abs(diffs[i][-1])
    print(f"valor do proximo termo: {proximoTermo}\n")   
    #print(diffs)
    return
    

def babbage(eixo_y):
    n=len(eixo_y)
    tabela=[eixo_y]
  
    for i in range(n-1):
        linha = []
        for j in range(n-i-1):
            v = tabela[i][j] - tabela[i][j+1]
            linha.append(v) 
        tabela.append(linha)
    return tabela
    
def polinomio(x, coeficientes, grau):
    soma = 0
    i = 0
    while(i<=grau):
        soma += coeficientes[i] * (x**(grau-i))
        i += 1
    return round(soma, 2)

coeficientes = [2, -3, 2]
grau = len(coeficientes)-1
# cria uma tabela de diferença com 10 termos e depois a preenche substituindo o valor com o resolucao do polinomio 
eixo_x = list(range(11))
eixo_y = [polinomio(x, coeficientes, grau) for x in eixo_x]
#print("eixo y")
#print(eixo_y)

diffs = babbage(eixo_y)


#print("tabela de diferença")
#print(diffs)
#print(eixo_x)
print(f"\neixo y: {eixo_y}\n")
print(f"eixo x: {eixo_x}\n")
nextValue(diffs)

eixo_x_decimal = [round(i * 0.1, 2) for i in range(10)]
eixo_y_decimal = [polinomio(x, coeficientes, grau) for x in eixo_x_decimal]
diffs_decimal = babbage(eixo_y_decimal)


print(f"valor do eixo x em decimal: {eixo_x_decimal}\n")
print(f"valor do eixo y em decimal: {eixo_y_decimal}\n")


nextValue(diffs_decimal)

#print("tabela de diferenças:")
#for c, linha in enumerate(diffs):
 #   print(f"nível {c}: {linha}")
   


    
