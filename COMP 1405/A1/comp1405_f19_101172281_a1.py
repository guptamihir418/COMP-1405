import pygame
pygame.display.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("house_101172281") 
win.fill((0, 0, 90))

pygame.draw.rect(win, (255, 255, 0), (0, 0, 500, 250))
pygame.draw.rect(win, (0, 255, 0), (0, 250, 500, 250))

pygame.draw.rect(win, (111, 89, 87), (190, 300, 20, 30))


pygame.draw.polygon(win, (255,105,180), [(125, 150), (50, 250), (175, 275)])
pygame.draw.polygon(win, (50, 100, 120), [(175, 275), (175, 450), (50, 425), (50, 250)])  
pygame.draw.polygon(win, (255, 100, 6), [(175, 275), (375, 225), (375, 400), (175, 450)])
pygame.draw.polygon(win, (139,69,19), [(125, 150), (325, 100), (375, 225), (175, 275)])

pygame.draw.rect(win, (40,50,60), (75, 350, 70, 75))
pygame.draw.circle(win, (240, 255, 255), (79, 390), (5))

pygame.draw.polygon(win, (139,69,19), [(225, 75), (275, 50), (275, 125), (225, 125)])
pygame.draw.ellipse(win, (10, 10, 10), (250, 50, 10,20))
pygame.draw.circle(win, (10, 10, 10), (235, 40), (5))
pygame.draw.circle(win, (10, 10, 10), (230, 50), (5))

pygame.draw.circle(win, (169,169,169), (270, 345), (40))

pygame.draw.line(win, (0, 0, 0), (234, 358), (308, 330))
pygame.draw.line(win, (0, 0, 0), (286, 380), (256, 310))

pygame.draw.rect(win, (20,30,30), [425, 275, 50, 125])
pygame.draw.polygon(win, (34,139,34) , [[400, 275], [500, 275], [450, 200]])
pygame.draw.polygon(win, (34,139,34), [[415,225], [485, 225], [450, 150]])




pygame.display.update()
pygame.time.delay(3000)

pygame.image.save(win, ("house_101172281.bmp"))

