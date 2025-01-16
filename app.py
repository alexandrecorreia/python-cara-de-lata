
import sys
import os
import time
import random
import gtts
import re
from playsound import playsound
import threading

class Robot():

    know_peoples = [
        {'name': 'Fulano', 'phrase' : ' ainda bem que vc voltou ' }
    ]

    def __init__(self):
        self.clear_screen()


    def clear_screen(self):
        name_os = sys.platform.lower()

        if name_os == 'linux':
            os.system('clear')


    def face(self):
        return f"\nCara de Lata\n" + "#" * 40 + '''

            +----------+
            |  +    +  |
            |    ^     |
            |   %%%%   |
            +----------+
                |  |
            +----------+
            |          |
            +          +
            |----------|
              ||    ||
             ----  ----
        ''' + "\n" + "#" * 40

    def mouthing(self):

        prompt = input("Digite seu nome : ")
        prompt = "Bem-vindo " + prompt

        if len(self.know_peoples):
            for p in self.know_peoples:
                if re.search(p['name'], prompt, re.IGNORECASE):
                    prompt = prompt + p['phrase']

        self.talking(prompt)

        for i in range( ( len(prompt)-2 ) ):
            change = random.randint(0,3)
            mouth = "----"
            mouth = "  " + mouth[:change] + self.change_character() + mouth[change+1:] + "  "
            self.clear_screen()
            print(self.face().replace("  %%%%  ", mouth ))
            time.sleep(0.11)

        self.clear_screen()
        print( self.face().replace("  %%%%  ","  ----  "))

    def change_character(self):
        characteres = ['@', 'o' , 'O']
        return random.choice(characteres)

    def talking(self, speak):
        fala = gtts.gTTS(speak, lang="pt-br")
        fala.save('frase.mp3')

        # Criar uma thread para tocar o áudio em paralelo com a animação
        audio_thread = threading.Thread(target=playsound, args=('frase.mp3',))
        audio_thread.start()


    def load(self):
        print( self.face().replace("  %%%%  ","  ----  "))
        self.mouthing()


robot = Robot()

robot.load()