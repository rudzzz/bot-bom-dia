import telebot

api_key = "5322079975:AAHMxgbpl6BxXS-Ib0ab7h_mH3uOgmnYXJo"

bot = telebot.TeleBot(api_key)

@bot.message_handler(commands=["mensagem1"])
def mensagem1(mensagem):
    bot.send_message(mensagem.chat.id, """
Bom dia, meus queridos amigos!
Que cada instante de hoje
Seja inesquecível de tão bom.

Que a alegria acompanhe a todos
E os passos que derem hoje sejam
Seguros e a caminho da felicidade.

Sejam felizes com o que já têm,
Mas nunca deixem de lutar por mais.
Tenham um ótimo dia, amigos!
    """)

@bot.message_handler(commands=["mensagem2"])
def mensagem2(mensagem):
    bot.send_message(mensagem.chat.id, "Bom dia! Você é uma pessoa muito especial para mim e é por isto que hoje te envio esse desejo de um dia maravilhoso")

@bot.message_handler(commands=["mensagem3"])
def mensagem3(mensagem):
    bot.send_message(mensagem.chat.id, "Um dia alegre e repleto de boas energias: é o que eu desejo para você hoje!")

@bot.message_handler(commands=["mensagem4"])
def mensagem4(mensagem):
    bot.send_message(mensagem.chat.id, "Hoje não faltará energia positiva nem sorrisos no seu rosto. Tenha um dia maravilhoso!")

@bot.message_handler(commands=["mensagem5"])
def mensagem5(mensagem):
    bot.send_message(mensagem.chat.id, """
Bom dia com todo o meu carinho, meu anjo! Por ter você na minha vida, sou constantemente relembrado de quanto sou abençoado.
Sou um homem completo por ter meu anjo ao meu lado. Você tem a estranha capacidade de me rejuvenescer e de me fazer sentir novamente criança. O mundo é muito melhor quando compartilhado com você.
Te amo e te adoro! Um beijo gigante de bom dia!
    """)

@bot.message_handler(commands=["mensagem6"])
def mensagem6(mensagem):
    bot.send_message(mensagem.chat.id, """
Hoje comece seu dia
Com a consciência que este será
O mais importante da sua vida.
Tudo que ficou para trás já não importa.
É hora de lutar pela sua felicidade
E pela realização dos seus sonhos.
Aconteça o que acontecer, pense sempre
Positivo, e tenha um bom dia!
    """)

@bot.message_handler(commands=["mensagem7"])
def mensagem7(mensagem):
    bot.send_message(mensagem.chat.id, "Bom dia! Ao acordar inspire esperança e positividade, e seja qual for a realidade que enfrentar, com certeza será mais fácil de levar. Pois um coração otimista e positivo consegue tudo, e ainda vai iluminando os que encontra pelo caminho. Então hoje saia espalhando sua luz positiva e tenha um ótimo dia!")

@bot.message_handler(commands=["mensagem8"])
def mensagem8(mensagem):
    bot.send_message(mensagem.chat.id, """
Bom dia! O tempo é o nosso bem mais precioso, pois cada minuto que se perde, não pode ser recuperado.
Por isso, não perca mais tempo, salte da cama e procure aproveitar o dia ao máximo. A vida é para ser vivida.
Tenha um ótimo dia!
    """)

@bot.message_handler(commands=["mensagem9"])
def mensagem9(mensagem):
    bot.send_message(mensagem.chat.id, """
Mais um dia começando, dando os primeiros passos através da luz que ofusca a lua! Uma nova hipótese de melhorar sua vida. De melhorar a vida dos que se cruzam com você!
Uma nova chance de dar gargalhada, de abraçar a alegria. Uma nova chance de ser feliz, querida amiga! Tenha um bom dia. Que a jornada de hoje seja memorável e que provoque em você sensações bem positivas.
    """)

@bot.message_handler(commands=["mensagem10"])
def mensagem10(mensagem):
    bot.send_message(mensagem.chat.id, """
Todos os dias são dias mágicos onde tudo pode acontecer e nada é igual ou será parecido sequer. É por isso que devemos desfrutar de todos os instantes que recebemos da vida. Bom dia!
Que o sol seja o foco da sua atenção, mas também a lua mais tarde ou os olhares perdidos na rua. Ou até mesmo aquele sorriso que você nunca deu importância. Viva! Viva e celebre intensamente cada momento do dia.
    """)

@bot.message_handler(commands=["sair"])
def sair(mensagem):
    bot.send_message(mensagem.chat.id, "Obrigado por testar o bot!")


def verifica(mensagem):
    return True

@bot.message_handler(func=verifica)
def resposta_padrao(mensagem):
    texto_menu = """
Mensagens de Bom Dia!
Escolha uma opção :
     /mensagem1 - Mensagem 1
     /mensagem2 - Mensagem 2
     /mensagem3 - Mensagem 3
     /mensagem4 - Mensagem 4
     /mensagem5 - Mensagem 5
     /mensagem6 - Mensagem 6
     /mensagem7 - Mensagem 7
     /mensagem8 - Mensagem 8
     /mensagem9 - Mensagem 9
     /mensagem10 - Mensagem 10
     /sair - Sair do bot
     """
    bot.reply_to(mensagem, texto_menu)

bot.polling()