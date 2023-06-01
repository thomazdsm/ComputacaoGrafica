# ESCOLHA UMA DAS FIGURAS 2D CRIADAS E FAÇA AS TRÊS SEGUINTES OPERAÇÕES: TRANSLAÇÃO, ROTAÇÃO E MUDANÇA DE ESCALA;
# Botões W,A,S,D > Rotação e Escala
# Setas (cima, baixo, esquerda e direita) > Translação

import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Função para criar uma figura geométrica 2D
def create_2d_figure(vertices, color):
    glBegin(GL_POLYGON)
    glColor3fv(color)
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()

def main():
    # Inicialização do Pygame
    pygame.init()

    # Configuração da janela e viewport
    width, height = 800, 600
    display = (width, height)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Inicialização do OpenGL
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    # Definição das figuras geométricas 2D
    square_vertices = [(-0.5, -0.5), (-0.5, 0.5), (0.5, 0.5), (0.5, -0.5)]

    # Variáveis para as operações de transformação
    translation_x = 0.0
    translation_y = 0.0
    rotation_angle = 0.0
    scale_factor = 1.0
    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Detecção dos comandos do teclado
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    translation_x -= 0.1
                elif event.key == K_RIGHT:
                    translation_x += 0.1
                elif event.key == K_UP:
                    translation_y += 0.1
                elif event.key == K_DOWN:
                    translation_y -= 0.1
                elif event.key == K_a:
                    rotation_angle += 5
                elif event.key == K_d:
                    rotation_angle -= 5
                elif event.key == K_w:
                    scale_factor += 0.1
                elif event.key == K_s:
                    scale_factor -= 0.1

        # Limpeza do buffer e redefinição da matriz de modelo-visão
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Aplicação das transformações na figura escolhida
        glTranslatef(translation_x, translation_y, 0.0)
        glRotatef(rotation_angle, 0.0, 0.0, 1.0)
        glScalef(scale_factor, scale_factor, scale_factor)

        # Criação das figuras geométricas 2D
        create_2d_figure(square_vertices, (1, 0, 0))  # Quadrado vermelho

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()