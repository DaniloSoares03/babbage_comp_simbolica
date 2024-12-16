import decimal
import time

# Define a precisão dos cálculos com decimal para 1000 casas decimais
decimal.getcontext().prec = 1000  

class Symbolic:
    """
    Classe para representar e manipular variáveis simbolicamente com precisão decimal.
    """
    def __init__(self, value, symbol=None):
        self.value = decimal.Decimal(value)
        self.symbol = symbol

    def __str__(self):
        if self.symbol:
            return f"{self.symbol}"
        return f"{self.value}"

    def __add__(self, other):
        if isinstance(other, Symbolic):
            return Symbolic(self.value + other.value)
        return Symbolic(self.value + decimal.Decimal(other))

    def __mul__(self, other):
        if isinstance(other, Symbolic):
            return Symbolic(self.value * other.value)
        return Symbolic(self.value * decimal.Decimal(other))

    def __abs__(self):
        return Symbolic(abs(self.value))
    
    def __gt__(self, other):
        if isinstance(other, Symbolic):
            return self.value > other.value
        return self.value > decimal.Decimal(other)

def calcular_ex_taylor_simbolico(x, epsilon):
    """
    Inicializa o termo (x^0 / 0!), ou seja, 1.
    :param x: Valor de x
    :param epsilon: Limiar de precisão para interrupção do cálculo
    :return: Aproximação de e^x simbolicamente e número de termos usados
    """
    # Representando x simbolicamente
    x = Symbolic(x)
    resultado = Symbolic(1)
    termo = Symbolic(1)      
    k = 1
    num_termos = 1

    # Calculando de forma simbólica até a precisão ser atingida
    while abs(termo) > Symbolic(epsilon):  
        termo = termo * x / k
        resultado = resultado + termo
        k += 1
        num_termos += 1
    
    return resultado, num_termos

def calcular_ex_taylor_com_decomposicao_simbolico(x, epsilon):
    """
    Calcula e^x simbolicamente para valores grandes de x usando decomposição.
    :param x: Valor de x
    :param epsilon: Limiar de precisão para interrupção do cálculo
    :return: Aproximação de e^x simbolicamente e número de termos usados
    """
    # Divide o número em parte inteira e fração
    inteiro = int(x)
    fracao = x - inteiro
        
    # Decomposição exponencial: e^x = e^(parte inteira) * e^(parte fracionária)
    resultado_inteiro, num_termos_inteiro = calcular_ex_taylor_simbolico(inteiro, epsilon)
    resultado_fracao, num_termos_fracao = calcular_ex_taylor_simbolico(fracao, epsilon)
        
    return resultado_inteiro * resultado_fracao, num_termos_inteiro + num_termos_fracao


if __name__ == "__main__":
    print("Cálculo de e^x para números de qualquer magnitude sem overflow")
    
    # Entrada é um número
    x = float(input("Digite o valor de x: "))
    
    """
    Entrada deve ser 1e-x (exemplo: 1e−6 significa 1×10^−6, ou seja, 0.000001)
    está dizendo que a diferença entre o valor calculado da função e^x e o valor exato deve ser menor do que 0.000001 para que a soma da série de Taylor seja interrompida.
    """
    epsilon = float(input("Digite o valor do limiar de precisão (epsilon): "))
    
    # Marca o tempo de início
    start_time = time.time()

    resultado, num_termos = calcular_ex_taylor_com_decomposicao_simbolico(x, epsilon)
    
    # Marca o tempo de fim
    end_time = time.time()
    
    # Calcula o tempo de execução
    elapsed_time = end_time - start_time
    
    print(f"O valor aproximado de e^{x} simbolicamente é: {resultado}")
    print(f"Foi necessário usar {num_termos} termos para alcançar a precisão desejada.")
    print(f"Tempo de execução: {elapsed_time:.6f} segundos")
