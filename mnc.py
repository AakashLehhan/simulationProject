

global mx, my
import pygame

def mc():
    
    #initilise the pygame
    pygame.init()
    #create the screen
    screen=pygame.display.set_mode((800,600))
    #Title
    pygame.display.set_caption("Missionary and Cannibal")
    #Players
    player1Img=pygame.image.load('icons/devil.png')
    player2Img=pygame.image.load('icons/devil.png')
    player3Img=pygame.image.load('icons/devil.png')
    player4Img=pygame.image.load('icons/jesus.png')
    player5Img=pygame.image.load('icons/jesus.png')
    player6Img=pygame.image.load('icons/jesus.png')

    boatImg=pygame.image.load('icons/boat.png')
    riverImg=pygame.image.load('icons/river2.png')
    riverImg2=pygame.image.load('icons/river2.png')
    riverImg3=pygame.image.load('icons/river2.png')
    undoImg=pygame.image.load('icons/undo1.png')
    gameoverImg=pygame.image.load('icons/game-over.png')
    restartImg=pygame.image.load('icons/restart.png')
    goalImg=pygame.image.load('icons/goal.png')
    def game():
        #initial values of players
        global mx, my
        player1X,player1Y=150,300
        player2X,player2Y=200,300
        player3X,player3Y=250,300
        player4X,player4Y=150,350
        player5X,player5Y=200,350
        player6X,player6Y=250,350

        boatX,boatY=280,410
        countrd,countld=0,3
        countrm,countlm=0,3


        def player1(x,y):
            screen.blit(player1Img,(x,y))
        def player2(x,y):
            screen.blit(player2Img,(x,y))
        def player3(x,y):
            screen.blit(player3Img,(x,y))
        def player4(x,y):
            screen.blit(player4Img,(x,y))
        def player5(x,y):
            screen.blit(player5Img,(x,y))
        def player6(x,y):
            screen.blit(player6Img,(x,y))
        def boat(x,y):
            screen.blit(boatImg,(x,y))
        def gameover(x,y):
            screen.blit(gameoverImg,(x,y))
        def restart(x,y):
            screen.blit(restartImg,(x,y))
        def winner(x,y):
            screen.blit(goalImg,(x,y))



        #game loop
        sit=True
        while sit :

            screen.fill((255,153,204))
            screen.blit(riverImg,(100,-100))
            screen.blit(riverImg2,(120,-100))
            screen.blit(riverImg3,(147,-100))

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sit=False
                if event.type==pygame.MOUSEBUTTONDOWN:

                    mx,my=pygame.mouse.get_pos()
                    print(mx,my)

                    if boatX==280:
                        if mx>=140 and mx<=170 and my>=290 and my<=330:
                            if (player2X==300 or player3X==300 or player4X==300 or player5X==300 or player6X==300) and (player2X==350 or player3X==350 or player4X==350 or player5X==350 or player6X==350):
                                player1X,player1Y=150,300

                            elif player2X==300 or player3X==300 or player4X==300 or player5X==300 or player6X==300  :
                                player1X,player1Y=350,400

                            else:
                                player1X,player1Y=300,400


                        if mx>=190 and mx<=220 and my>=290 and my<=330:
                            if (player1X==300 or player3X==300 or player4X==300 or player5X==300 or player6X==300) and (player1X==350 or player3X==350 or player4X==350 or player5X==350 or player6X==350):
                                player2X,player2Y=200,300
                            elif player1X==300 or player3X==300 or player4X==300 or player5X==300 or player6X==300 :
                                player2X,player2Y=350,400
                            else:
                                player2X,player2Y=300,400


                        if mx>=240 and mx<=270 and my>=290 and my<=330:
                            if (player1X==300 or player2X==300 or player4X==300 or player5X==300 or player6X==300) and (player1X==350 or player2X==350  or player4X==350 or player5X==350 or player6X==350):
                                player3X,player3Y=250,300
                            elif player1X==300 or player2X==300 or player4X==300 or player5X==300 or player6X==300:
                                player3X,player3Y=350,400
                            else:
                                player3X,player3Y=300,400

                        if mx>=145 and mx<=177 and my>=350 and my<=385:
                            if (player1X==300 or player2X==300 or player3X==300 or player5X==300 or player6X==300) and (player1X==350 or player2X==350 or player3X==350 or player5X==350 or player6X==350):
                                player4X,player4Y=150,350
                            elif player1X==300 or player2X==300 or player3X==300 or player5X==300 or player6X==300:
                                player4X,player4Y=350,400

                            else:
                                player4X,player4Y=300,400

                        if mx>=195 and mx<=227 and my>=350 and my<=385:
                            if (player1X==300 or player2X==300 or player3X==300 or player4X==300 or player6X==300) and (player1X==350 or player2X==350 or player3X==350 or player4X==350 or player6X==350):
                                player5X,player5Y=200,350
                            elif player1X==300 or player2X==300 or player3X==300 or player4X==300 or player6X==300:
                                player5X,player5Y=350,400
                            else:
                                player5X,player5Y=300,400

                        if mx>=245 and mx<=277 and my>=350 and my<=385:
                            if (player1X==300 or player2X==300 or player3X==300 or player4X==300 or player5X==300) and (player1X==350 or player2X==350 or player3X==350 or player5X==350 or player6X==350):
                                player6X,player6Y=250,350
                            elif player1X==300 or player2X==300 or player3X==300 or player4X==300 or player5X==300:
                                player6X,player6Y=350,400
                            else:
                                player6X,player6Y=300,400

                    if boatX==480 and boatY==361:
                        if mx>=545 and mx<=575 and my>=275 and my<=300:
                            if (player2X==500 or player3X==500 or player4X==500 or player5X==500 or player6X==500) and (player2X==545 or player3X==545 or player4X==545 or player5X==545 or player6X==545):
                                player1X,player1Y=550,275

                            elif player2X==500 or player3X==500 or player4X==500 or player5X==500 or player6X==500  :
                                player1X,player1Y=545,350

                            else:
                                player1X,player1Y=500,350

                        if mx>=580 and mx<=605 and my>=275 and my<=300:
                            if (player1X==500 or player3X==500 or player4X==500 or player5X==500 or player6X==500) and (player1X==545 or player3X==545 or player4X==545 or player5X==545 or player6X==545):
                                player2X,player2Y=580,275
                            elif player1X==500 or player3X==500 or player4X==500 or player5X==500 or player6X==500 :
                                player2X,player2Y=545,350
                            else:
                                player2X,player2Y=500,350

                        if mx>=610 and mx<=635 and my>=275 and my<=300:
                            if (player1X==500 or player2X==500 or player4X==500 or player5X==500 or player6X==500) and (player1X==545 or player2X==545  or player4X==545 or player5X==545 or player6X==545):
                                player3X,player3Y=610,275
                            elif player1X==500 or player2X==500 or player4X==500 or player5X==500 or player6X==500:
                                player3X,player3Y=545,350
                            else:
                                player3X,player3Y=500,350

                        if mx>=640 and mx<=675 and my>=315 and my<=350:
                            if (player1X==500 or player2X==500 or player3X==500 or player5X==500 or player6X==500) and (player1X==545 or player2X==545 or player3X==545 or player5X==545 or player6X==545):
                                player4X,player4Y=640,315
                            elif player1X==500 or player2X==500 or player3X==500 or player5X==500 or player6X==500:
                                player4X,player4Y=545,350
                            else:
                                player4X,player4Y=500,350

                        if mx>=676 and mx<=710 and my>=315 and my<=350:
                            if (player1X==500 or player2X==500 or player3X==500 or player4X==500 or player6X==500) and (player1X==545 or player2X==545 or player3X==545 or player4X==545 or player6X==545):
                                player5X,player5Y=677,315
                            elif player1X==500 or player2X==500 or player3X==500 or player4X==500 or player6X==500:
                                player5X,player5Y=545,350
                            else:
                                player5X,player5Y=500,350


                        if mx>=712 and mx<=740 and my>=315 and my<=350:
                            if (player1X==500 or player2X==500 or player3X==500 or player4X==500 or player5X==500) and (player1X==545 or player2X==545 or player3X==545 or player5X==545 or player6X==545):
                                player6X,player6Y=714,315
                            elif player1X==500 or player2X==500 or player3X==500 or player4X==500 or player5X==500:
                                player6X,player6Y=545,350
                            else:
                                player6X,player6Y=500,350


                if event.type==pygame.MOUSEBUTTONUP:
                    nx,ny=pygame.mouse.get_pos()
                    print(nx,ny)
                    if mx>=275 and mx<=440 and my>=410 and my<=470 and nx>=600 and nx<=800:

                        if player1X==300 or player1X==350:
                            player1Y=275
                            player1X=550
                            countrd=countrd+1
                            countld=countld-1
                            boatX,boatY=480,361
                        if player2X==300 or player2X==350:
                            player2Y=275
                            player2X=580
                            countrd=countrd+1
                            countld=countld-1
                            boatX,boatY=480,361
                        if player3X==300 or player3X==350:
                            player3Y=275
                            player3X=610
                            countrd=countrd+1
                            countld=countld-1
                            boatX,boatY=480,361
                        if player4X==300 or player4X==350:
                            player4Y=315
                            player4X=640
                            countrm=countrm+1
                            countlm=countlm-1
                            boatX,boatY=480,361
                        if player5X==300 or player5X==350:
                            player5Y=315
                            player5X=677
                            countrm=countrm+1
                            countlm=countlm-1
                            boatX,boatY=480,361
                        if player6X==300 or player6X==350 :
                            player6Y=315
                            player6X=714
                            countrm=countrm+1
                            countlm=countlm-1
                            boatX,boatY=480,361


                    if mx>=480 and mx<=635 and my>=365 and my<=417 and nx>=0 and nx<=270 :

                        if player1X==500 or player1X==545:
                            player1X,player1Y=150,300
                            countld=countld+1
                            countrd=countrd-1
                            boatX,boatY=280,410
                        if player2X==500 or player2X==545:
                            player2X,player2Y=200,300
                            countld=countld+1
                            countrd=countrd-1
                            boatX,boatY=280,410
                        if player3X==500 or player3X==545:
                            player3X,player3Y=250,300
                            countld=countld+1
                            countrd=countrd-1
                            boatX,boatY=280,410
                        if player4X==500 or player4X==545:
                            player4X,player4Y=150,350
                            countlm=countlm+1
                            countrm=countrm-1
                            boatX,boatY=280,410
                        if player5X==500 or player5X==545:
                            player5X,player5Y=200,350
                            countlm=countlm+1
                            countrm=countrm-1
                            boatX,boatY=280,410
                        if player6X==500 or player6X==545:
                            player6X,player6Y=250,350
                            countlm=countlm+1
                            countrm=countrm-1
                            boatX,boatY=280,410

            boat(boatX,boatY)
            player1(player1X,player1Y)
            player2(player2X,player2Y)
            player3(player3X,player3Y)
            player4(player4X,player4Y)
            player5(player5X,player5Y)
            player6(player6X,player6Y)
            if countrm==3 and countrd==3:
                screen.fill((0,0,255))
                winner(140,40)
                restart(385,500)
                if mx>=380 and mx<=440 and my>=500 and my<=552:
                    game()
                    break

            if countld>countlm and countlm>0:
                screen.fill((255,0,0))
                gameover(140,40)
                restart(385,500)
                if mx>=380 and mx<=440 and my>=500 and my<=552:
                    game()
                    break
            if countrd>countrm and countrm>0:
                screen.fill((255,0,0))
                gameover(140,40)
                restart(385,500)
                if mx>=380 and mx<=440 and my>=500 and my<=552:
                    game()
                    break

            pygame.display.update()
    game()
