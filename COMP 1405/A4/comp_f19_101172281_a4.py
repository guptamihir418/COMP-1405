#Mihir Gupta
#student id - 101172281

	
import pygame
# asking for instructions
instructions = input("Do you want to read instructions or not? ")
if instructions in ["no", "No", "NO"]:
    print(" Start by adding your background image.")
#pending
else:
    print(" This program works by you to chose background image in .bmp and it will then ask the filename for the ghost pic you want to add. You have to then tell the center x and y co-ordinates for the ghost pic. This program then see the pxel for each of your ghost image, if the pixel is green it totally be ignored and if the pixel is not green for the ghost image it will average the values RGB values s as to give sem-transparent look for the ghost.")

  
  
#Asking for background image
image_of_bg = input("Enter the name of image you want in your background. ")
background_image = pygame.image.load(image_of_bg)
(height_bg, width_bg) = background_image.get_rect().size
surface = pygame.display.set_mode( (height_bg, width_bg) )
surface.blit( background_image, (0, 0) )
#Asking for ghost image
image_of_ghost = input("Enter the file name of the ghost you want to add in the background picture. ")
ghost_image = pygame.image.load(image_of_ghost)
(height_ghost, width_ghost) = ghost_image.get_rect().size

 
#asking for x and y co-ordinates to add ghost picture to add on background colour.
while True:
	x = int(input("Enter x co-ordinate where you want to centerize the ghost picture."))
	y = int(input("Enter y co-ordinate where you want to centerize the ghost picture."))
	# centerizing the ghost image on x and y
	xg=int(x-width_ghost/2)
	yg=int(y-height_ghost/2)
	yp=int(y+height_ghost/2)
	xp=int(x+width_ghost/2)
	if (yg) < 0 or (yg) > height_bg or (xg) < 0 or (xg) > width_bg:
#I was confused between if the ghost image have to be fully applied on the background or the partial image will also work. So the code of above is the code for partial imnage but I can also write the code for full image, bt it would make the co-ordinates selection more precise. Moreover there is nothing mentioned in the assignment specification about this.
		print("invalid values of X or Y or both.")
		invalid_input = input(" press enter to re-enter the X and Y values.")
         
                
	else:
		break
	
for i in range(0,height_ghost,1):
	for j in range(0,width_ghost,1):
		(r2,b2,g2,_) = background_image.get_at((i,j))
		(r,g,b,_) = ghost_image.get_at((i,j))

		if (r,g,b,_) != (0,255,0,_):
			setting_x_y = (x-(xg-i), y-(yg-j))
			red = (r+r2)//2
			green = (g+g2)//2
			blue = (b+b2)//2
			surface.set_at(setting_x_y, (red, green, blue))

pygame.display.update()
	
	 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
