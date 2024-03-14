import itertools  # Importa o módulo itertools, que contém funções para iterar sobre dados iteráveis de maneiras eficientes.

# Solicita ao usuário que insira a string a ser permutada e armazena-a na variável 'string'.
string = input("String a ser permutada: ")

# Gera todas as permutações possíveis da string inserida pelo usuário e armazena-as na variável 'resultado'.
resultado = itertools.permutations(string, len(string))

# Solicita ao usuário que insira o nome do arquivo onde a wordlist será salva (sem a extensão) e armazena-o na variável 'nome_arquivo'.
nome_arquivo = input("Nome do arquivo para salvar a wordlist (sem extensão): ")

# # Abre um arquivo para escrita ('w') com o nome inserido pelo usuário, acrescentando '.txt' como extensão, associando-o à variável 'file'.
with open(nome_arquivo + '.txt', 'w') as file:
    # Itera sobre cada permutação gerada na variável 'resultado'.
    for i in resultado:
        # Converte a permutação atual em uma string concatenando todos os caracteres e armazena-a na variável 'word'.
        word = ''.join(i)
        # Escreve a palavra atual seguida de uma quebra de linha no arquivo associado à variável 'file'.
        file.write(word + '\n')

# Exibe uma mensagem indicando que a wordlist foi gerada e salva com sucesso, mostrando o nome do arquivo criado.
print(f"Wordlist gerada e salva como '{nome_arquivo}.txt'")

