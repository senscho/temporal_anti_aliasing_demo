
import pygame

pygame.init()
screen = pygame.display.set_mode([300, 300])
pygame.display.set_caption('Rotating image example')
clock = pygame.time.Clock()

img = pygame.transform.scale(pygame.image.load('wheel.png').convert(),(300,300))
img_rect = img.get_rect(center = screen.get_rect().center)

rot_img = []
rot_img_rect = []
for degree in range(360):
    rot_img.append(pygame.transform.rotate(img, degree))
    rot_img_rect.append(rot_img[degree].get_rect(center = img_rect.center))

blk_img = []
for intensity in range(256):
    black_img = pygame.Surface(img.get_size())
    blk_color = (intensity,intensity,intensity)
    black_img.fill( blk_color )
    blk_img.append(black_img)


font = pygame.font.Font(None, 24)


degree = 0
degree_delta = 0

n_avg = 1

text = font.render('speed: {0:3d}, avg: {1:2d}'.format(degree_delta,n_avg), 0,(255,255,0))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key==27: done = True
            if event.key==1073741906: degree_delta += 1
            if event.key==1073741905: degree_delta -= 1
            if event.key==48: degree_delta =0
            if event.key==1073741899: degree_delta += 10
            if event.key==1073741902: degree_delta -= 10
            if event.key==1073741904: n_avg -= 1
            if event.key==1073741903: n_avg += 1
            
            n_avg = max(n_avg,1)
            n_avg = min(n_avg,10)

            text = font.render('speed: {0:3d}, avg: {1:2d}'.format(degree_delta,n_avg), 0,(255,255,0))
            # print(event.key)

    screen.fill((0, 0, 0))
    

    for n in range(n_avg):
        idx = (degree - n) % 360
        work_img = blk_img[ int(255/n_avg) ].copy()
        work_img.blit(rot_img[idx], rot_img_rect[idx], special_flags=pygame.BLEND_MULT)
        screen.blit(work_img, (0,0),special_flags=pygame.BLEND_ADD)
    
    screen.blit(text,(5,5))

    pygame.display.flip()

    clock.tick(12)
    degree = (degree + degree_delta) % 360

pygame.quit()