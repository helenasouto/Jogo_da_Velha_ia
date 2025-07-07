# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int):
        lista = []
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))

        # R1: Se vc ou oponente tiver duas marcações em sequencia, marcar o quadrado restante
        for emptySpot in lista:
            x, y = emptySpot

            #horizontal
            if sum(self.matriz[x]) == Tabuleiro.JOGADOR_0 * 2 or sum(self.matriz[x]) == Tabuleiro.JOGADOR_X * 2:
                return emptySpot

            #vertical 
            value = 0
            for i in range(0, 3):
                value = value + self.matriz[i][y]
            
            if value == Tabuleiro.JOGADOR_0 * 2 or value == Tabuleiro.JOGADOR_X * 2:
                return emptySpot
       
            # diagonal principal
            #(0,0), (1,1), (2,2) # x = y

            if x == y:
                value = 0

                for i in range(0, 3):
                    value = value + self.matriz[i][i]
    
                if value == Tabuleiro.JOGADOR_0 * 2 or value == Tabuleiro.JOGADOR_X * 2:
                    return emptySpot
                    
            
            # diagonal secundária
            # (0,2), (1,1), (2,0) #x + y = 2

            if x + y == 2:
                value = 0

                for i in range(0, 3):
                    value = value + self.matriz[i][2-i]
    
                if value == Tabuleiro.JOGADOR_0 * 2 or value == Tabuleiro.JOGADOR_X * 2:
                    return emptySpot
                
        # R2: Se houver uma jogada que crie duas sequencias de duas marcacoes faça
      
        for emptySpot in lista:
            x, y = emptySpot
            ameacas = 0  # Contador de ameaças criadas

            # Linha horizontal
            if sum(self.matriz[x]) + Tabuleiro.JOGADOR_0 == 2 * Tabuleiro.JOGADOR_0:
                ameacas += 1
            #vertical
            if sum(self.matriz[i][y] for i in range(0, 3)) + Tabuleiro.JOGADOR_0 == 2 * Tabuleiro.JOGADOR_0:
                ameacas += 1
            # Diagonal principal 
            if x == y and sum(self.matriz[i][i] for i in range(0, 3)) + Tabuleiro.JOGADOR_0 == 2 * Tabuleiro.JOGADOR_0:
                ameacas += 1
            # Diagonal secundária 
            if x + y == 2 and sum(self.matriz[i][2-i] for i in range(0, 3)) + Tabuleiro.JOGADOR_0 == 2 * Tabuleiro.JOGADOR_0:
                ameacas += 1

            if ameacas >= 2:
                return emptySpot
        
    # R3: Se o quadrado central estiver livre, marque          
        if self.matriz [1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # R4: Se oponente tiver marcado um dos cantos, marque o canto oposto

        if self.matriz [0][0] == Tabuleiro.JOGADOR_X and self.matriz [2][2] == Tabuleiro.DESCONHECIDO:
            return (2,2)
        if self.matriz [0][2] == Tabuleiro.JOGADOR_X and self.matriz [2][0] == Tabuleiro.DESCONHECIDO:
            return (2, 0)
        if self.matriz [2][0] == Tabuleiro.JOGADOR_X and self.matriz [0][2] == Tabuleiro.DESCONHECIDO:
            return (0,2)
        if self.matriz [2][2] == Tabuleiro.JOGADOR_X and self.matriz [0][0] == Tabuleiro.DESCONHECIDO:
            return (0, 0)
        
        # R5: Se houver um canto vazio, marque

        lista_de_cantos = [(0, 0), (2, 2), (0, 2), (2,0)]
        cantos_vazios = []

        for c in lista_de_cantos:
            if self.matriz [c[0]][c[1]] == Tabuleiro.DESCONHECIDO:
                cantos_vazios.append(c)
            
        if cantos_vazios:
            return cantos_vazios[randint(0, len(cantos_vazios)-1)]

        # R6: Marque arbitrariamente um quadrado vazio
        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
           return None
        
    