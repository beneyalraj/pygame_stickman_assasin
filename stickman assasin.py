import pygame
from tkinter import filedialog
from tkinter import *
 
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)
pygame.init()
screen = pygame.display.set_mode((600,500))
image = pygame.image.load(root.filename)
screen.blit(image,(100,150))
pygame.display.update()
picture = pygame.image.load(filename)
picture = pygame.transform.scale(picture, (1280, 720))