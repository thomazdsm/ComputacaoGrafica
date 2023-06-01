# ESCOLHA UMA DAS FIGURAS 3D CRIADAS E FAÇA DUAS DAS SEGUINTES OPERAÇÕES: TRANSLAÇÃO, ROTAÇÃO, MUDANÇA DE ESCALA
# Comandos:
# Escala: Botões I, O (Efeito semelhanto ao Zoom In/Out)
# Translação: Setas e Botões Q e E (Zoom In/Out)
# Rotação: Botões W, A, S, D, Z, C

import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Função para criar um cubo com faces coloridas
def cube():
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )
    faces = (
        (0, 1, 2, 3),  # Face frontal
        (3, 2, 7, 6),  # Face traseira
        (6, 7, 5, 4),  # Face direita
        (4, 5, 1, 0),  # Face esquerda
        (1, 5, 7, 2),  # Face superior
        (4, 0, 3, 6)   # Face inferior
    )
    colors = (
        (1, 0, 0),  # Vermelho
        (0, 1, 0),  # Verde
        (0, 0, 1),  # Azul
        (1, 1, 0),  # Amarelo
        (1, 0, 1),  # Magenta
        (0, 1, 1)   # Ciano
    )

    glBegin(GL_QUADS)
    for face, color in zip(faces, colors):
        glColor3fv(color)
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    # Inicialização do Pygame
    pygame.init()

    # Configuração da janela e viewport
    width, height = 800, 600
    display = (width, height)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Inicialização do OpenGL
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (width / height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    # Variáveis para as operações de transformação
    translation_x = 0.0
    translation_y = 0.0
    translation_z = 0.0
    rotation_x = 0.0
    rotation_y = 0.0
    rotation_z = 0.0
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
                elif event.key == K_q:
                    translation_z += 0.1
                elif event.key == K_e:
                    translation_z -= 0.1
                elif event.key == K_a:
                    rotation_y += 5
                elif event.key == K_d:
                    rotation_y -= 5
                elif event.key == K_w:
                    rotation_x += 5
                elif event.key == K_s:
                    rotation_x -= 5
                elif event.key == K_z:
                    rotation_z += 5
                elif event.key == K_c:
                    rotation_z -= 5
                elif event.key == K_i:
                    scale_factor += 0.1
                elif event.key == K_o:
                    scale_factor -= 0.1

        # Limpeza do buffer e redefinição da matriz de modelo-visão
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Aplicação das transformações no cubo
        glTranslatef(translation_x, translation_y, translation_z)
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)
        glRotatef(rotation_z, 0, 0, 1)
        glScalef(scale_factor, scale_factor, scale_factor)

        # Desenho do cubo
        cube()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
