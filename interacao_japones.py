# Isso é um comentário, então não vai aparecer quando eu executar esse código 

# Vou fazer um chamando o Lucas pra comer japonês na quarta de noite
print("Oi, Lucas! Não sei se isso vai dar certo, mas olha o que eu tô tentando aprender a fazer")

# Solicita a resposta do usuário
resposta = input("Você quer ver? (responda com 'sim' ou 'não'): ").strip().lower()

# Verifica a resposta do usuário
if resposta == "sim":
    status = "sim"
    print("Beleza, vamos lá")
    # Nova pergunta com opções
    nova_resposta = input("Você quer comer japonês essa semana comigo e o Marco? (responda com 'sim' ou 'não'): ").strip().lower()
    
    if nova_resposta == "sim":
        print("Você escolheu SIM!")
        # Adicione mais funcionalidades para a resposta 'sim'
        print(f"Show! A gente marca a hora depois.")
        
    elif nova_resposta == "não":
        print("Você escolheu NÃO! MORRAAAAAAA")
        
    else:
        print("Opção inválida. Por favor, responda com 'sim' ou 'não'.")
else:
    status = "não"
    print("Vai se foder seu merdinha")
