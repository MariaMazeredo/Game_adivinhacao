import random
import os
import time  # Para adicionar um atraso

class GameAdivinhacao:
    def __init__(self):
        self.erros = 0
        self.sorteado = random.randrange(0, 100)

    def limpando_tela(self): 
        os.system('cls' if os.name == 'nt' else 'clear')

    def obter_um_palpite(self):
        return int(input("Digite o número escolhido: "))
    
    def verificacao_palpite(self, palpite):
        if self.sorteado > palpite:
            print("ERRO! O número é maior, tente outra vez")
            self.erros += 1
            return False
        elif self.sorteado < palpite:
            print("ERRO! O número é menor, tente novamente!")
            self.erros += 1
            return False
        else:
            return True
    
    def iniciar(self):
        while True:
            jogador = self.obter_um_palpite()
            if self.verificacao_palpite(jogador):
                break
            time.sleep(2)  # Atraso de 2 segundos para o jogador ver a mensagem
            self.limpando_tela()
        print(f"Número {jogador}, você acertou em {self.erros + 1} tentativas")

    def Menu(self):
        while True:
            self.limpando_tela()
            print("======== Jogo de Adivinhação ========")
            print("Press 1. Iniciar Jogo")
            print("Press 2. Sair")
            escolha = input("Escolha uma opção: ")
            if escolha == '1':
                self.erros = 0
                self.sorteado = random.randrange(0, 100)
                self.iniciar()
                input(" Pressione Enter para voltar ao menu ")
            elif escolha == '2':
                print("Obrigado por jogar!")
                break
            else:
                print("Opção inválida!")
                time.sleep(4)
   
if __name__ == "__main__":
    jogo = GameAdivinhacao()
    jogo.Menu()