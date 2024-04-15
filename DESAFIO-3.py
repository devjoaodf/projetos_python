import re

def validate_numero_telefone(phone_number):
    # Definindo o padrão de expressão regular (regex) para validar números de telefone celular no formato (XX) 9XXXX-XXXX ou (XX) XXXXX-XXXX:
    pattern = r'\(\d{2}\)\s9\d{4}-\d{4}'  
    
    # A função 're.match()' verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number):  
        # Se o número de telefone for válido, retorna "Número válido":
        return "Número de telefone válido."
    else:
        # Se o número de telefone for inválido, retorna "Número inválido":
        return "Número de telefone inválido."

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number':
phone_number = input()  

# Chama a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazena o resultado retornado na variável 'result':
result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)