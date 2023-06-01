# CRIE 3 DIFERENTES FIGURAS GEOMÉTRICAS 3D (CUBO, ESFERA, ETC) E APRESENTE-AS EM UMA MESMA TELA COM CORES DISTINTAS

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

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
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
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
    for face in faces:
        color_index = faces.index(face)
        glColor3fv(colors[color_index])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def tetrahedron():
    vertices = (
        (1, 1, 1),
        (1, -1, -1),
        (-1, -1, 1),
        (-1, 1, -1)
    )
    faces = (
        (0, 1, 2),
        (0, 2, 3),
        (0, 3, 1),
        (1, 3, 2)
    )
    colors = (
        (1, 0, 0),  # Vermelho
        (0, 1, 0),  # Verde
        (0, 0, 1),  # Azul
        (1, 1, 0)   # Amarelo
    )
    glBegin(GL_TRIANGLES)
    for face in faces:
        color_index = faces.index(face)
        glColor3fv(colors[color_index])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def sphere():
    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL)
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluSphere(quadric, 1, 32, 32)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glOrtho(-6, 6, -6, 6, 0.1, 50.0)  # Ajuste os parâmetros de projeção conforme necessário
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -15.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(-4.0, 0.0, 0.0)
        cube()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-1.5, 0.0, 0.0)
        tetrahedron()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(1.5, 0.0, 0.0)
        sphere()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
