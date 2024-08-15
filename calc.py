escolha_input = int(input("Escolha qual operação deseja fazer: 0 se quiser Decimal para Binário | 1 se quiser Binário para Decimal "))



def invert_nums(nums_array):
    nums_returned = []
    for i in range(len(nums_array)):
        #Pegar o total de números dentro da lista de resto de divisão e ir subtraindo 1 até chegar em 0 para ele pegar o ultimo número até o primeiro.
        nums_returned.append(nums_array[(len(nums_array) - 1) - i])
    
    return nums_returned

def get_bi_by_dec(number):
    x = number # Número escolhido
    list_nums = [] # Lista do resto da divisão
    
    while x > 1:
        z = x // 2 
        # Z é o resultado da divisão, ele vai e ter que sempre ser inteiro;
        y = x % 2 
        # Y é o que sobrou dessa divisão;
        list_nums.append(y) 
        # Colocar o Y (que vai ser sempre 0 ou 1) dentro da lista den números;
        x = z 
        # Trocar o X pelo resultado da divisão, pro loop ir até ele chegar em 1;
    if x == 1:
        list_nums.append(x) 
        # Se der 1 ele vai retornar ele mesmo (podia retornar 1 direto, pois o primeiro número binário vai sempre ser 1 por algum motivo)
    
    return invert_nums(list_nums)

def get_dec_by_bi(number):
    x_string = str(number) #Número escolhido
    list_nums = [] #Lista de cada número que o usuário colocou
    list_inverted = [] #Lista invertida de cada número que o usuário colocou
    for i in range(0,len(x_string)):
        #Transformar o número que o usuário colocou em uma string, e pra cada número, colocar dentro da list
        calc_x = int(x_string[i])
        list_nums.append(calc_x)
    
    list_inverted = invert_nums(list_nums) #Inverter a lista que contém os números
    result = 0
    for v in range(0,len(x_string)):
         #Somar o antigo número mais o número atual da lista invertida, multiplicado por 2 elevado ao Index do número invertido na lista
         result = result + list_inverted[v] * (2 ** v)

         #Se quiser fazer com outras bases decimais, só trocar o 2 pela base decimal que deseja.
    return result

if(escolha_input == 0):
    numero_input = int(input("Digite o número decimal que deseja converter: "))
    print(numero_input, "convertido em binário fica: ",get_bi_by_dec(numero_input))
elif (escolha_input == 1):
    numero_input = int(input("Digite o número binário que deseja converter: "))
    print(numero_input, "convertido em decimal fica:", get_dec_by_bi(numero_input))
else:
    print("Escolha uma opção válida.")

# print(get_bi_by_dec(11)) #Mostra como seria o 11 na tabela binária. Ex : 1011 é o número binário que representa a 11

# print(get_dec_by_bi(11)) #Mostra qual número na tabela binária é o 11. Ex : 11 é o número binário que corresponde a 3