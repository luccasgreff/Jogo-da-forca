import random as rd

temas = ["musicas do eminem", "musicas do the weeknd", "musicas do coldplay"]
musicas_eminem = ["therealslimshady", "withoutme", "tillicollapse", "loseyourself", "rapgod"]
musicas_theweeknd = ["starboy", "blindinglights", "saveyourtears", "calloutmyname", "falsealarm"]
musicas_coldplay = ["vivalavida", "hymnfortheweekend", "thescientist", "fixyou", "yellow"]
erros = 0
limite = 7
letras_escolhidas = []

print("Seja bem vindo ao jogo da forca! Você deve acertar a palavra sorteada para vencer o jogo!\n")
print("Regras:")
print("1 - Você tentará uma letra por vez.")
print("2 - Acertando uma das letras, ela será colocada na palavra para te auxiliar até o final.")
print("3 - Caso erre, você perde uma chance. ATENÇÃO, você tem no máximo 7 chances.")
print("4 - As letras devem ser digitadas minúsculas, e não é necessário digitar a letra com acento.\n")

tema_escolhido = input("Escolha um destes temas: musicas do eminem, musicas do the weeknd ou musicas do coldplay: ")

while tema_escolhido not in temas:
    print("Esse tema não está disponível.")
    tema_escolhido = input("Escolha um destes temas: musicas do eminem, musicas do the weeknd ou musicas do coldplay: ")

if tema_escolhido == "musicas do eminem":
    sorteio = rd.choice(musicas_eminem)
elif tema_escolhido == "musicas do the weeknd":
    sorteio = rd.choice(musicas_theweeknd)
else:
    sorteio = rd.choice(musicas_coldplay)


progresso = ["_"] * len(sorteio)

while erros < limite and '' .join(progresso) != sorteio:
    letra = input("\n\nDigite uma letra: ")
    while letra in letras_escolhidas:
        print("Essa letra já foi digitada!")
        letra = input("Digite novamente: ")

    letras_escolhidas.append(letra)

    if letra in sorteio:
        print("\nACERTOU!")
        for i in range(len(sorteio)):
            if letra == sorteio[i]:
                progresso[i] = letra
    else:
        print("\nERROU!")
        erros = erros + 1

    print(progresso)
    print("Você errou", erros, "vez(s)", "e ainda possuí", limite - erros, "tentativa(s)")
    print("Letras que você já tentou: ")
    for i in letras_escolhidas:
        print(i, end=" ")

if erros == limite:
  print("\n\nVocê perdeu, acabaram suas tentativas...")
else:
  print("\n\nVocê ganhou, parabéns!!")

print("\nA palavra era", sorteio)