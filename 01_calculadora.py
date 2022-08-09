# Rafael Bonfim Zacco

'''
Você deverá desenvolver um programa, na sua linguagem de programação favorita, que leia 
uma string de entrada e execute a operação matemática contida nesta string. Esta string irá 
representar operações matemáticas segundo uma variação da RPN, que inclui obrigatoriamente 
parênteses para limitar as operações, conforme exemplos a seguir: 

a) (2 3 +) = 5 
b) (3 4 *) = 12 
c) (4 2 2 /) = 1 
d) ((4 2 +) 3 *) = 18  

O seu programa deverá ser capaz de realizar as seguintes operações:  
• Adição representada por +; 
• Subtração representada por -; 
• Multiplicação representada por *; 
• Divisão representada por /; 

As operações devem ser realizadas com número reais, mesmo que todos os exemplos aqui 
utilizados sejam com números inteiros. As operações podem ser aninhadas, sem qualquer limite, 
como pode ser visto nos exemplos a seguir:  

• ((3 4 +) (4 2 /) *) = 14 
• ((3 4 +) (4 (1 1 +) /) *) = 14 

Os operandos serão separados de outros operandos e dos operadores por um caractere de 
espaço. Por fim, O sinal de igual e todos os resultados que estão a direita deste símbolo neste 
enunciado não fazem parte da string que deverá ser lida e estão aqui apenas para facilitar o 
entendimento. 

O teste será realizado diretamente no ambiente do repl.it, com a digitação de um conjunto 
de expressões pelo professor.
'''


print("---Calculadora RPN---\n")
operacao = input("Insira a operação: ")

pilha = []
digito = []

parcial = 0

for i in range(len(operacao)):

    if operacao[i] != '(' and operacao[i] != ')':  

        if operacao[i] == '+':
            for j in range(len(pilha)-1):
                parcial = float(parcial) + float(pilha[j+1])
        if operacao[i] == '-':
            for j in range(len(pilha)-1):
                parcial = float(parcial) - float(pilha[j+1])
        if operacao[i] == '*':
            for j in range(len(pilha)-1):
                parcial = float(parcial) * float(pilha[j+1])
        if operacao[i] == '/':
            for j in range(len(pilha)-1):
                parcial = float(parcial) / float(pilha[j+1])

        if operacao[i] == ' ':
            pilha.append("".join(digito))
            digito = []
            if parcial == 0:
                parcial = pilha[0]
        else:
            digito.append(operacao[i])

'''
for i in range(len(pilha)):
    print("[" + str(i) + "] = " + str(pilha[i]))
'''

print("Resultado: " + str(parcial))