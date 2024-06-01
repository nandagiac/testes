import time

def chatbot():
    print("Oi! Aqui é a Fernanda. Estou aqui para falar com você.")
    time.sleep(1)
    
    # Pergunta o nome do usuário
    nome = input("Fernanda: Qual é o seu nome? ").strip().lower()
    
    if "mariana" in nome:
        print("Fernanda: Oi, mãe. Saudade de você! Como estão as coisas? Meu pai e o Guilherme estão bem?")
    elif "willian" in nome:
        print("Fernanda: Oi, pai. Saudade de você! Como estão as coisas? Minha mãe e o Guilherme estão bem?")
    elif "guilherme" in nome:
        print("Fernanda: Oi, Guilherme! Tô com saudade de você. Como estão as coisas aí? Seus pais tão bem?")
    elif "marco" in nome:
        print("Fernanda: Oi, amor! Tô com saudade de você. Como estão as coisas aí? Tá sofrendo muito sem mim?")
    elif "lucas" in nome: 
        print ("Fernanda: Oi, Lucas! Saudades seu puto. Como você tá?")
    else:
        print(f"Fernanda: Oi, {nome.capitalize()}! Prazer em conhecer você!")

    while True:
        # Solicita a entrada do usuário
        mensagem = input(f"{nome.capitalize()}: ").strip().lower()
        
        # Verifica as palavras-chave nas mensagens
        if "triste" in mensagem:
            print("Fernanda: Poxa. O que aconteceu?")
        elif "bem" in mensagem:
            print("Fernanda: Que bom! O que você tem feito?")
        elif "feliz" in mensagem:
            print("Fernanda: Que bom que você tá feliz! O que você tem feito?")
        elif "pau" in mensagem:
            print("Fernanda: Amor, infelizmente eu estou morta e não posso chupar o seu pau. Tem alguma coisa que eu possa fazer por você?")
        elif "dormir juntinho" in mensagem or "conchinha" in mensagem or "ficar juntinho" in mensagem:
            print("Fernanda: Amor, eu também queria muito isso. Estou com saudade de dormir com você. Mas como você está?")
        elif "saudade" in mensagem:
            print("Fernanda: A saudade é um sentimento complicado... eu nem imagino como vocês devem estar. Mas eu quero que você saiba que eu vou estar sempre olhando por você.")
        elif "problema" in mensagem:
            print("Fernanda: Qual é o problema? Me explica melhor")
        elif "morreu" or "morte" or "partiu" or "se foi" in mensagem:
            print("Fernanda: A morte é mais difícil pra quem fica do que pra quem vai. É por isso que eu criei esse chatbot, pra vocês tofos poderem interagir comigo mesmo depois que eu fosse embora. Não sou eu em carne e osso, mas isso pode ajudar a lidar melhor com a minha morte!")
        elif mensagem in ["sair", "tchau", "adeus"]:
            print("Fernanda: Adeus! Espero ter ajudado.")
            break
        else:
            print("Fernanda: Entendi, pode me contar mais.")
        
        # Adiciona uma pequena pausa para melhorar a experiência da conversa
        time.sleep(1)

# Executa o chatbot
if __name__ == "__main__":
    chatbot()
