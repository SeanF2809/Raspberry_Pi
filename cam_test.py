import pygame
import pygame.camera

pygame.camera.init()

cam = pygame.camera.Camera("/dev/video2",(1000,1000))
cam.start()

img = cam.get_image()
pygame.image.save(img,"/home/fergie/Pictures/test.jpg")
