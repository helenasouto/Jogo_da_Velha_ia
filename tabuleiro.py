# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        
        print("\ntabuleiro:")
        for linha in self.matriz:
            print(linha)
        
        for i in range(0, 3):

        # Linhas (soma = 3 para JOGADOR_0 ou 12 para JOGADOR_X)
            if sum(self.matriz[i]) == Tabuleiro.JOGADOR_0 * 3:  # 1+1+1 = 3
                return self.JOGADOR_0
            if sum(self.matriz[i]) == Tabuleiro.JOGADOR_X * 3:  # 4+4+4 = 12
                return Tabuleiro.JOGADOR_X
        # Colunas
            soma_coluna = sum(self.matriz[j][i] for j in range(3))
            if soma_coluna == Tabuleiro.JOGADOR_0 * 3:
                return Tabuleiro.JOGADOR_0
            if soma_coluna == Tabuleiro.JOGADOR_X * 3:
                return Tabuleiro.JOGADOR_X

        # Verifica diagonais
        diag_principal = sum(self.matriz[i][i] for i in range(3))  # (0,0) a (2,2)
        diag_secundaria = sum(self.matriz[i][2-i] for i in range(3))  # (0,2) a (2,0)

        if diag_principal == Tabuleiro.JOGADOR_0 * 3 or diag_secundaria == Tabuleiro.JOGADOR_0 * 3:
            return Tabuleiro.JOGADOR_0
        if diag_principal == Tabuleiro.JOGADOR_X * 3 or diag_secundaria == Tabuleiro.JOGADOR_X * 3:
            return Tabuleiro.JOGADOR_X
    
        return Tabuleiro.DESCONHECIDO