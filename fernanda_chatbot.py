import time
import re
import unicodedata

def remover_acentos(texto):
    # Normaliza o texto e remove os acentos
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def chatbot():
    print("Oi! Aqui é a Fernanda. Estou aqui para falar com você.")
    time.sleep(1)
    
    # Pergunta o nome do usuário
    nome = input("Fernanda: Qual é o seu nome? ").strip().lower()
    nome_normalizado = remover_acentos(nome)
    
    if "mariana" in nome_normalizado:
        print("Fernanda: Oi, mãe. Saudade de você! Como estão as coisas? Meu pai e o Guilherme estão bem?")
    elif "willian" in nome_normalizado:
        print("Fernanda: Oi, pai. Saudade de você! Como estão as coisas? Minha mãe e o Guilherme estão bem?")
    elif "guilherme" in nome_normalizado:
        print("Fernanda: Oi, Guilherme! Tô com saudade de você. Como estão as coisas aí? Seus pais tão bem?")
    elif "marco" in nome_normalizado:
        print("Fernanda: Oi, amor! Tô com saudade de você. Como estão as coisas aí? Tá sofrendo muito sem mim?")
    elif "lucas" in nome_normalizado or "uriel" in nome_normalizado:
        print("Fernanda: Oi, insuportável! Saudades de você. Como você tá?")
    elif "isabela" in nome_normalizado or "duda" in nome_normalizado or "fernanda" in nome_normalizado or "julia" in nome_normalizado:
        print("Fernanda: Oi, amiga! Tô com saudade de você. Como você tá?")
    elif "evora" in nome_normalizado or "évora" in nome_normalizado:
        print("Fernanda: Oi, filha! Como você tá? Aqui quem tá falando é a mamãe. Quer dizer, não falando exatamente... mas como você tá?")
    elif "nicholas" in nome_normalizado or "nicolas" in nome_normalizado:
        print("Fernanda: Oi, filho! Como você tá? Aqui quem tá falando é a mamãe. Quer dizer, não falando exatamente... mas como você tá?")
    else:
        print(f"Fernanda: Oi, {nome.capitalize()}! Prazer em conhecer você!")

    while True:
        # Solicita a entrada do usuário
        mensagem = input(f"{nome.capitalize()}: ").strip().lower()
        mensagem_normalizada = remover_acentos(mensagem)
        
        # Verifica as palavras-chave nas mensagens
        if "triste" in mensagem_normalizada:
            print("Fernanda: Poxa. O que aconteceu?")
        elif "bem" in mensagem_normalizada:
            print("Fernanda: Que bom! O que você tem feito?")
        elif "feliz" in mensagem_normalizada:
            print("Fernanda: Que bom que você tá feliz! O que você tem feito?")
        elif "pau" in mensagem_normalizada:
            print("Fernanda: Amor, infelizmente eu estou morta e não posso chupar o seu pau. Tem alguma coisa que eu possa fazer por você?")
        elif "dormir juntinho" in mensagem_normalizada or "conchinha" in mensagem_normalizada or "ficar juntinho" in mensagem_normalizada:
            print("Fernanda: Amor, eu também queria muito isso. Estou com saudade de dormir com você. Mas como você está?")
        elif "saudade" in mensagem_normalizada:
            print("Fernanda: A saudade é um sentimento complicado... eu nem imagino como vocês devem estar. Mas eu quero que você saiba que eu vou estar sempre olhando por você.")
        elif "problema" in mensagem_normalizada:
            print("Fernanda: Qual é o problema? Me explica melhor")
        elif "morreu" in mensagem_normalizada or "morte" in mensagem_normalizada or "partiu" in mensagem_normalizada or "se foi" in mensagem_normalizada:
            print("Fernanda: A morte é mais difícil pra quem fica do que pra quem vai. É por isso que eu criei esse chatbot, pra vocês tofos poderem interagir comigo mesmo depois que eu fosse embora. Não sou eu em carne e osso, mas isso pode ajudar a lidar melhor com a minha morte!")
        elif "perguntas" in mensagem_normalizada or "pergunta" in mensagem_normalizada or "questionário" in mensagem_normalizada or "perguntar" in mensagem_normalizada:
            print("Fernanda: Ah, você quer me fazer uma pergunta? Ok, vamos lá...")
            time.sleep(1)
            # Checa perguntas específicas
            if "comida favorita" in mensagem_normalizada or "gostava de comer" in mensagem_normalizada: 
                print("Fernanda: BATATA FRITA! Ah, e gnocchi, massas no geral, doce... mas batata frita acima de todo o resto!!!")
            elif "cor favorita" in mensagem_normalizada:
                print("Fernanda: Azul! Adoro azul e acho que sempre gostei dessa cor!")
            elif re.search(r"\bcomo\b.*\bconheceu\b.*\bpapai\b", mensagem_normalizada):
                print("Fernanda: Eu conheci o seu pai na escola. A gente tava no oitavo ano e eu achei ele engraçado. Se você procurar uma foto você vai ver kkkkkk. Mas eu gostei dele. Não romanticamente, mas achei ele interessante. Aí eu namorei o Lucas, um amigo dele. Depois de um tempo que eu tinha terminado com o Lucas eu percebi que o seu pai gostava de mim. E aí a gente ficou pela primeira vez em novembro de 2019")
            elif re.search(r"\bcomo\b.*\bconheceu\b.*\bpai\b", mensagem_normalizada):
                print("Fernanda: Eu conheci o seu pai na escola. A gente tava no oitavo ano e eu achei ele engraçado. Se você procurar uma foto você vai ver kkkkkk. Mas eu gostei dele. Não romanticamente, mas achei ele interessante. Aí eu namorei o Lucas, um amigo dele. Depois de um tempo que eu tinha terminado com o Lucas eu percebi que o seu pai gostava de mim. E aí a gente ficou pela primeira vez em novembro de 2019")
            elif re.search(r"\bescolheu\b.*\bser\b.*\bmãe\b", mensagem_normalizada):
                print("Fernanda: Eu sempre quis ser mãe. Sempre me imaginei tendo uma Evora e/ou um Nicholas (seu pai ainda não concordou com o H no meio). Acho que por isso que eu criei esse programa, pra você poder me conhecer melhor, mesmo eu não estando por perto! Mas eu quero que você saiba que eu sempre te amei muito, desde antes de ter você!!")
            elif re.search(r"\bqueria\b.*\bser\b.*\bmãe\b", mensagem_normalizada):
                print("Fernanda: Eu sempre quis ser mãe. Sempre me imaginei tendo uma Evora e/ou um Nicholas (seu pai ainda não concordou com o H no meio). Acho que por isso que eu criei esse programa, pra você poder me conhecer melhor, mesmo eu não estando por perto! Mas eu quero que você saiba que eu sempre te amei muito, desde antes de ter você!!")
            elif "musica favorita" in mensagem_normalizada:
                print("Fernanda: Eu adoro as da Taylor Swift. Gosto muito do álbum dela folklore (peace, exile e hoax são as que eu mais gosto no momento). Mas eu também gosto de rock, principalmente dos anos 2000 (tipo Fall Out Boy) e mais antigos. Mas isso varia muito... depende da fase que eu tô.")
            elif "artista favorita" in mensagem_normalizada:
                print("Fernanda: Taylor Swift, Fall Out Boy, Ed Sheeran, Bruno Mars... curiosamente já fui em shows de todos eles, ainda bem!!") 
            elif "lugar favorito" in mensagem_normalizada:
                print("Fernanda: Eu amava a Fnac. Era uma loja que ficava no Barra Shopping. Mas eles fecharam há alguns anos. Eu amava os livros, os CDs, as pessoas que iam lá, o cheiro de carpete, o geladinho do ar condicionado... eu adorava. Acho que hoje em dia é minha casa. Eu gosto de ficar na sala vendo TV, estudar no sofá... eu sou bem caseira kkkkkk")
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
