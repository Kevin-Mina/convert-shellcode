shellcode = r"shellcode aqui"

# Dividir o shellcode em 130 colunas e o restante em linhas
colunas = 130
linhas = [shellcode[i:i+colunas] for i in range(0, len(shellcode), colunas)]

# Salvar o resultado em um novo arquivo
with open("shellcode_dividido.c", "w") as arquivo:
    for linha in linhas:
        arquivo.write('"' + linha + '"\n')

print("Shellcode dividido salvo em 'shellcode_dividido.c'.")
