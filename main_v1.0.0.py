import datetime
import pygame
import math

pygame.init()

Size = (800,600)
app = True
fps = 30

backGrndClr = (0,8,131)

Screen = pygame.display.set_mode(Size,0,32)

Icon = pygame.image.load('res/icon.png')

pygame.display.set_caption('Chronometer: The Ultimate Time Teller')
pygame.display.set_icon(Icon)

clock = pygame.time.Clock()

clockBase = pygame.transform.scale(pygame.image.load('res/ClockFace1.png').convert(),(400,400))

def game():

    app = True
    
    while app:
        Now = datetime.datetime.now()

        #time variables
        timeArray = [Now.hour, Now.minute, Now.second]
        
        hr1 = timeArray[0]//10
        hr2 = timeArray[0]%10
        min1 = timeArray[1]//10
        min2 = timeArray[1]%10
        sec1 = timeArray[2]//10
        sec2 = timeArray[2]%10

        #clockArmLogic
        ArmLngths = (80,100,125)

        clck12 = dict(zip(range(12),range(0,360,30)))
        clck60 = dict(zip(range(60),range(0,360,6)))
        
        def clockPos(clockDict, clckHand, Rad):
            x = 400 + Rad * math.cos(math.radians(clockDict[clckHand%12]) - math.pi/2)
            y = Size[1]*2/5 + Rad * math.sin(math.radians(clockDict[clckHand%12]) - math.pi/2)
            return [x,y]
        
        def secPos(clockDict, clckHand, Rad):
            x = 400 + Rad * math.cos(math.radians(clockDict[clckHand]) - math.pi/2)
            y = Size[1]*2/5 + Rad * math.sin(math.radians(clockDict[clckHand]) - math.pi/2)
            return [x,y]

        #images

        hour1 = pygame.transform.scale(pygame.image.load(f'res/digits/red/{hr1}.png').convert(),(64,96))
        hour2 = pygame.transform.scale(pygame.image.load(f'res/digits/red/{hr2}.png').convert(),(64,96))
        minute1 = pygame.transform.scale(pygame.image.load(f'res/digits/green/{min1}.png').convert(),(64,96))
        minute2 = pygame.transform.scale(pygame.image.load(f'res/digits/green/{min2}.png').convert(),(64,96))
        second1 = pygame.transform.scale(pygame.image.load(f'res/digits/blue/{sec1}.png').convert(),(64,96))
        second2 = pygame.transform.scale(pygame.image.load(f'res/digits/blue/{sec2}.png').convert(),(64,96))
        
        colon = pygame.transform.scale(pygame.image.load(f'res/colonW.png').convert(),(16,96))

        Screen.fill(backGrndClr)
        
        #time
        Screen.blit(hour1,((Size[0]/2)-(64*3)-(16*1),Size[1]*4/5))
        Screen.blit(hour2,((Size[0]/2)-(64*2)-(16*1),Size[1]*4/5))
        Screen.blit(minute1,((Size[0]/2)-(64*1),Size[1]*4/5))
        Screen.blit(minute2,((Size[0]/2),Size[1]*4/5))
        Screen.blit(second1,((Size[0]/2)+(64*1)+(16*1),Size[1]*4/5))
        Screen.blit(second2,((Size[0]/2)+(64*2)+(16*1),Size[1]*4/5))

        Screen.blit(colon,((Size[0]/2)-(64*1)-(16*1),Size[1]*4/5))
        Screen.blit(colon,((Size[0]/2)+(64*1),Size[1]*4/5))

        Screen.blit(clockBase,((Size[0]/2)-200,(Size[1]*2/5)-200))

        #clockHands: hour, min, sec
        pygame.draw.line(Screen,(255,0,0),(400,Size[1]*2/5),clockPos(clck12,timeArray[0],ArmLngths[0]),9)#h
        pygame.draw.line(Screen,(0,255,0),(400,Size[1]*2/5),secPos(clck60,timeArray[1],ArmLngths[1]),6)#m
        pygame.draw.line(Screen,(0,0,255),(400,Size[1]*2/5),secPos(clck60,timeArray[2],ArmLngths[2]),3)#s
        
        #centerpiece
        pygame.draw.circle(Screen,(0,0,0),(400,Size[1]*2/5),10)
        
        pygame.display.update()
        clock.tick(fps)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    app = False
                    pygame.quit()
                    
game()
