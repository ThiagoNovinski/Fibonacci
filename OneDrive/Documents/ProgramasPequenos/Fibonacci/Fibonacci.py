#DESAFIO: Uma empresa deseja calcular o 2000° termo da sequência de fibonacci porém o código abaixo trava, como você solucionaria?
"""def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        return result"""
        
def fibonacci(n):
    global calculados
    if n == 1 or n == 2:
        return 1
    else:
        if len(calculados)>=n-1:
            result = calculados[n-3] + calculados[n-2]
            if result not in calculados:
                calculados.append(result)  
        else:
            result = fibonacci(n-1)+ fibonacci(n-2)
            if result not in calculados:
                calculados.append(result)    
        return result
calculados=[1,1]
for i in range(1,2001):
    print(f"Este é o {i}° termo da sequência de fibonacci: {fibonacci(i)}")
