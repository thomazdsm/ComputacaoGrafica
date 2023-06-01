# CRIE 5 DIFERENTES FIGURAS GEOMÉTRICAS 2D (QUADRADO, TRIÂNGULO, ETC) E APRESENTE-AS EM UMA MESMA TELA COM CORES DISTINTAS
import math
import pygame
from pygame.locals import *
from OpenGL.GL import *

def main():
    # Inicialização do Pygame
    pygame.init()

    # Configuração da tela
    width, height = 1000, 300
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

    # Configuração da viewport
    glViewport(0, 0, width, height)

    # Configuração da projeção
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Limpar a tela
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Desenhar quadrado
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)  # Vermelho
        glVertex2f(100, 100)
        glVertex2f(200, 100)
        glVertex2f(200, 200)
        glVertex2f(100, 200)
        glEnd()

        # Desenhar triângulo
        glBegin(GL_TRIANGLES)
        glColor3f(0.0, 1.0, 0.0)  # Verde
        glVertex2f(300, 100)
        glVertex2f(400, 100)
        glVertex2f(350, 200)
        glEnd()

        # Desenhar círculo
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.0, 0.0, 1.0)  # Azul
        glVertex2f(500, 150)
        radius = 50
        num_segments = 100
        for i in range(num_segments + 1):
            theta = 2.0 * 3.1415926 * float(i) / float(num_segments)
            x = radius * math.cos(theta) + 500
            y = radius * math.sin(theta) + 150
            glVertex2f(x, y)
        glEnd()

        # Desenhar retângulo
        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 0.0)  # Amarelo
        glVertex2f(600, 100)
        glVertex2f(700, 100)
        glVertex2f(700, 200)
        glVertex2f(600, 200)
        glEnd()

        # Desenhar Losango
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 1.0)  # Magenta
        glVertex2f(850, 100)
        glVertex2f(800, 150)
        glVertex2f(850, 200)
        glVertex2f(900, 150)
        glEnd()

        # Atualizar a tela
        pygame.display.flip()

if __name__ == '__main__':
    main()