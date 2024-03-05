import random
import sys


#---> Funcion de preguntarle al user si quiere jugar
def askWannaPlay():  #--->Preguntar si se quiere jugar
  answer = input("¿Aceptas mi desafio? S/N -> ")

  if answer.upper() == "S":
    return True
  elif answer.upper() == "N":
    return False
  else:
    print("Por favor di 'S' o 'N' ⤜(▰_▰)⤏\n")
    return None


#---> Funcion de mostrar mensaje segun la respuesta anterior
def messageOfWannaPlay(accepted):
  if accepted:
    print("\n")
    print("¡Genial, empezemos con esto! ◥▶ ᗝ ◀◤\n")
  else:
    print("\n")
    print("Qué mal, algún día tendrás las agallas de enfrentarme ᕙ(▰෴  ▰)ᕗ\n")
    sys.exit()


#---> Funcion del Piedra, papel o tijera
def choiceOptions(n):
  options = ("Piedra", "Papel", "Tijera")
  playerChoice = input("Piedra, Papel o Tijera? -> ")

  playerChoice.lower()
  playerChoice.title()

  if playerChoice not in options:
    print("💀Elegiste mal💀")
    return None, None

  pcChoice = random.choice(options)

  print("\n")
  print(f"{n} eligio -> {playerChoice}")
  print(f"PC eligio -> {pcChoice}")
  print("\n")

  return playerChoice, pcChoice


#---> Funcion de jugar
def pptfunction(user, pc, uswins, pwins, n):
  if pc == user:
    print(f"{user} contra {pc} es empate!\n")
    print(f"Victorias: {n} -> {uswins}, PC -> {pwins}\n")
    return uswins, pwins
  elif user == "Tijera":
    if pc == "Papel":
      print(f"{n} gana, {user} le gana a {pc}!")
      uswins += 1
      print(f"Victorias: {n} -> {uswins}, PC -> {pwins}\n")
      return uswins, pwins
    else:
      print(f"PC gana, {pc} le gana a {user}!")
      pwins += 1
      print(f"Victorias: {n} -> {uswins}, PC -> {pwins}\n")
      return uswins, pwins
  elif user == "Papel":
    if pc == "Piedra":
      print(f"{n} gana, {user} le gana a {pc}!")
      uswins += 1
      print(f"Victorias: {n} -> {uswins}, PC -> {pwins}\n")
      return uswins, pwins
    else:
      print(f"PC gana, {pc} le gana a {user}!")
      pwins += 1
      print(f"Victorias: {n} -> {uswins}, PC -> {pwins}\n")
      return uswins, pwins
  elif user == "Piedra":
    if pc == "Tijera":
      print(f"{n} gana, {user} le gana a {pc}!")
      uswins += 1
      print(f"Victorias: {n} -> {uswins}, PC -> {pwins}\n")
      return uswins, pwins
    else:
      print(f"PC gana, {pc} le gana a {user}!")
      pwins += 1
      print(f"Victorias: {n} -> {uswins}, PC -> {pwins}\n")
      return uswins, pwins


def runGame():
  userWins = 0
  pcWins = 0

  rounds = 0

  # Inicio del programa
  print("\n")  # Decoración
  name = input("Hola humano, ¿cómo te llamas? -> ")  #Nombre del jugador
  print(f"Hola, {name}, te reto a Piedra, papel o tijera (⌐■_■)づ\n")

  wannaPlay = None
  while wannaPlay is None:
    wannaPlay = askWannaPlay()  # Elección de si o no jugar

  messageOfWannaPlay(wannaPlay)

  #---> Juego principal

  while True:
    rounds += 1
    print("*" * 85)
    print(f"{'~' * 36}>>>Ronda {rounds}<<<{'~' * 36}")
    print("*" * 85, "\n")

    pc, player = choiceOptions(name)

    userWins, pcWins = pptfunction(pc, player, userWins, pcWins, name)

    if userWins == 3:
      print("\n")
      print(f"{'~' * 15}>El ganador es {name}!<{'~' * 15}")
      print("\n")
      exit()
    elif pcWins == 3:
      print("\n")
      print(f"{'~' * 15}>El ganador es PC!<{'~' * 15}")
      print("\n")
      exit()


#-->Programa
runGame()
