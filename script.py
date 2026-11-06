def criptografar_cesar(texto, deslocamento):
    """Criptografa o texto usando a Cifra de César (Substituição por deslocamento)."""
    resultado = ""
    for char in texto:
        if char.isalpha():
            # Define se a letra é maiúscula ou minúscula
            base = ord('A') if char.isupper() else ord('a')
            # Aplica o deslocamento circular (módulo 26)
            char_cifrado = chr((ord(char) - base + deslocamento) % 26 + base)
            resultado += char_cifrado
        else:
            # Mantém espaços, números e pontuações inalterados
            resultado += char
    return resultado

def descriptografar_cesar(texto_cifrado, deslocamento):
    """Descriptografa o texto aplicando a lógica inversa do deslocamento."""
    # A descriptografia nada mais é do que cifrar com o deslocamento negativo
    return criptografar_cesar(texto_cifrado, -deslocamento)


if __name__ == "__main__":
    mensagem_original = "Seguranca de Redes e Criptografia"
    chave_deslocamento = 3
    
    # Processo de Criptografia
    texto_cifrado = criptografar_cesar(mensagem_original, chave_deslocamento)
    print(f"Texto Cifrado: {texto_cifrado}")
    
    # Processo de Descriptografia (Lógica Inversa)
    texto_recuperado = descriptografar_cesar(texto_cifrado, chave_deslocamento)
    print(f"Texto Recuperado: {texto_recuperado}")