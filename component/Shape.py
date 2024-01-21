import pygame

class Shape:

    def __init__(self, center = (0, 0), radius = 0, verticeAmount = 360, color = pygame.Color((255, 255, 255))):
        self.center = center
        self.radius = radius
        self.color = color
        self.verticeAmount = verticeAmount

    def generateVertices(self, center, verticeAmount):#TO-DO
        pass