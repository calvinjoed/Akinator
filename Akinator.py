import os
import time
a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=0
point=0
while True:
    print("████▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀████")
    print("████░░░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░░░████")
    print("████░░░░║║║╠─║─║─║║║║║╠─░░░░████")
    print("████░░░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░░░████")
    print("████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄████")
    print("a.PLAY")
    print("b.HOW TO PLAY")

    x = input()
    if(x == 'a'):
        while True:
            print("Is it a Boy?")#Q1
            print("a.Yes")
            print("b.No")
            aa = input("Answer: ")
            if(aa =="a"):
                a = 100000
                break
            elif(aa =="b"):
                a = 0 
                break
            else:
                print("Can't Recognize Answer")
        while True:
            print("Is it an Alien?")#Q2
            print("a.Yes")
            print("b.No")
            bb = input("Answer: ")
            if(bb =="a"):
                b = 50000
                break
            elif(bb =="b"):
                b = 0
                break
            else:
                print("Can't Recognize Answer")
        while True:
            print("Is it an animal or have animal element?")#Q3
            print("a.Yes")
            print("b.No")
            cc = input("Answer: ")
            if(cc =="a"):
                c = 30000
                break
            elif(cc =="b"):
                c = 0
                break
            else:
                print("Can't Recognize Answer")
        #COLOR----------------------------------------------------------------------------------------------------
    
        while True:
            print("Does the main color RED?")#Q4-----RED-----
            print("a.Yes")
            print("b.No")
            dd = input("Answer: ")
            if(dd =="a"):
                d = 10000
                break
            elif(dd =="b"):
                d = 0
                while True:
                    print("Does the main color GREEN?")#Q5-----GREEN-----
                    print("a.Yes")
                    print("b.No")
                    ee = input("Answer: ")
                    if(ee =="a"):
                        e = 7000
                        break
                    elif(ee =="b"):
                        e = 0
                        while True:
                            print("Does the main color BLUE?")#Q6-----BLUE-----
                            print("a.Yes")
                            print("b.No")
                            ff = input("Answer: ")
                            if(ff =="a"):
                                f = 6000
                                break
                            elif(ff =="b"):
                                f = 0
                                while True:
                                    print("Does the main color GOLD?")#Q7-----GOLD-----
                                    print("a.Yes")
                                    print("b.No")
                                    gg = input("Answer: ")
                                    if(gg =="a"):
                                        g = 5000
                                        break
                                    elif(gg =="b"):
                                        g = 0
                                        while True:
                                            print("Does the main color BROWN?")#Q8-----BROWN-----
                                            print("a.Yes")
                                            print("b.No")
                                            hh = input("Answer: ")
                                            if(hh =="a"):
                                                h = 4000
                                                break
                                            elif(hh =="b"):
                                                h = 0
                                                while True:
                                                    print("Does the main color BLACK?")#Q9-----BLACK-----
                                                    print("a.Yes")
                                                    print("b.No")
                                                    ii = input("Answer: ")
                                                    if(ii =="a"):
                                                        i = 3000
                                                        break
                                                    elif(ii =="b"):
                                                        i = 0
                                                        while True:
                                                            print("Does the main color GREY?")#Q10-----GREY-----
                                                            print("a.Yes")
                                                            print("b.No")
                                                            jj = input("Answer: ")
                                                            if(jj =="a"):
                                                                j = 2000
                                                                break
                                                            elif(jj =="b"):
                                                                j = 0
                                                                while True:
                                                                    print("Does the main color WHITE?")#Q11-----WHITE-----
                                                                    print("a.Yes")
                                                                    print("b.No")
                                                                    kk = input("Answer: ")
                                                                    if(kk =="a"):
                                                                        k = 1000
                                                                        break
                                                                    elif(kk =="b"):
                                                                        k = 0
                                                                        break
                                                                    else:
                                                                        print("Can't Recognize Answer")
                                                                break
                                                            else:
                                                                print("Can't Recognize Answer")
                                                        break
                                                    else:
                                                        print("Can't Recognize Answer")
                                                break
                                            else:
                                                print("Can't Recognize Answer")
                                        break
                                    else:
                                        print("Can't Recognize Answer")
                                break
                            else:
                                print("Can't Recognize Answer")
                        break
                    else:
                        print("Can't Recognize Answer")
                break           
            else:
                print("Can't Recognize Answer")
        #-------------------------------------------------------------------------------------------------------------
        
        while True:
            print("Is it can Fly?")#Q12
            print("a.Yes")
            print("b.No")
            ll = input("Answer: ")
            if(ll =="a"):
                l = 500
                break
            elif(ll =="b"):
                l = 0
                break
            else:
                print("Can't Recognize Answer")
        #POWER--------------------------------------------------------------------------------------------------------
        while True:
            print("Does the main superpower magical?")#Q13-----MAGIC-----
            print("a.Yes")
            print("b.No")
            mm = input("Answer: ")
            if(mm =="a"):
                m = 30
                break
            elif(mm =="b"):
                m = 0
                while True:
                    print("Does it's using technology as a main power")#Q14-----TECH-----
                    print("a.Yes")
                    print("b.No")
                    nn = input("Answer: ")
                    if(nn =="a"):
                        n = 20
                        break
                    elif(nn =="b"):
                        n = 0
                        while True:
                            print("Does it's main power is physical ability?")#Q15-----PHYSIC-----
                            print("a.Yes")
                            print("b.No")
                            oo = input("Answer: ")
                            if(oo =="a"):
                                o = 10
                                break
                            elif(oo =="b"):
                                o = 0
                                break
                            else:
                                 print("Can't Recognize Answer")
                        break
                    else:
                        print("Can't Recognize Answer")
                break
            else:
                print("Can't Recognize Answer")
        #--------------------------------------------------------------------------------------------------------------
        #HAIR----------------------------------------------------------------------------------------------------------
        while True:
            print("Is the hair black?")#Q16
            print("a.Yes")
            print("b.No")
            pp = input("Answer: ")
            if(pp =="a"):
                p = 2
                break
            elif(pp =="b"):
                p = 0
                while True:
                    print("Is the hair blonde?")#Q17
                    print("a.Yes")
                    print("b.No")
                    qq = input("Answer: ")
                    if(qq =="a"):
                        q = 1
                        break
                    elif(qq =="b"):
                        q = 0
                        break
                    else:
                        print("Can't Recognize Answer")
                break
            else:
                print("Can't Recognize Answer")
        #----------------------------------------------------------------------------------------------------------------      
        point=a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q      
        print(point)
    
        if (point==3010):#1
            print("It's a Black Widow")

        elif (point==4022):#2
            print("It's a Shuri")

        elif (point==5012):#3
            print("It's a Okoye")

        elif (point==6531):#4
            print("It's a Captain Marvel")

        elif (point==10532):#5
            print("It's a Scarlet Witch")

        elif (point==33522):#6
            print("It's a Wasp")

        elif (point==51012):#7
            print("It's a Valkyrie")

        elif (point==56010):#8
            print("It's a Nebula")

        elif (point==57012):#9
            print("It's a Gamora")

        elif (point==87032):#10
            print("It's a Mantis")

        elif (point==102010):#11
            print("It's a Quicksilver")

        elif (point==102522):#12
            print("It's a War Machine")

        elif (point==103022):#13
            print("It's a Winter Soldier")

        elif (point==104032):#14
            print("It's a Wong")

        elif (point==106011):#15
            print("It's a Captain America")

        elif (point==106532):#16
            print("It's a Doctor Strange")

        elif (point==107012):#17
            print("It's a Hulk")

        elif (point==110521):#18
            print("It's a Star Lord")

        elif (point==110520):#19
            print("It's a Iron Man")
            
        elif (point==110530):#20
            print("It's a Vision")

        elif (point==132022):#21
            print("It's a Falcon")

        elif (point==133010):#22
            print("It's a Hawkeye")

        elif (point==133012):#23
            print("It's a Black Panther")

        elif (point==140010):#24
            print("It's a Spider Man")
        
        elif (point==140022):#25
            print("It's a Ant Man")

        elif (point==152031):#26
            print("It's a Thor")

        elif (point==154010):#27
            print("It's a Groot")

        elif (point==155032):#28
            print("It's a Heimdall")

        elif (point==156010):#29
            print("It's a Drax")

        elif (point==156020):#30
            print("It's a Yondu")

        elif (point==157032):#31
            print("It's a Loki")

        elif (point==184020):#32
            print("It's a Rocket Racoon")
        else:
            print("Can't Specify That")
            print("I guess..")
            if(point in range (3000,8000)):#----CHECK1----
                print("Black Widow?")
                print("a.Correct")
                print("b.No")
                cek1=input("Answer: ")
                if(cek1=='a'):
                    print("Yay!!!")
                    
                elif(cek1=='b'):
                    print("Shuri?")
                    print("a.Correct")
                    print("b.No")
                    cek1=input("Answer: ")
                    if(cek1=='a'):
                        print("Yay!!!")
                        
                    elif(cek1=='b'):
                        print("Okoye?")
                        print("a.Correct")
                        print("b.No")
                        cek1=input("Answer: ")
                        if(cek1=='a'):
                            print("Yay!!!")
                            
                        elif(cek1=='b'):
                            print("Captain Marvel?")
                            print("a.Correct")
                            print("b.No")
                            cek1=input("Answer: ")
                            if(cek1=='a'):
                                print("Yay!!!")
                                
                            elif(cek1=='b'):
                                print("Hero not Found :(")
                            else:
                                print('Cant Recognize Answer')
                        else:
                            print('Cant Recognize Answer')
                    else:
                        print('Cant Recognize Answer')
                else:
                    print('Cant Recognize Answer')
                        
            elif(point in range (8000,40000)):#----CHECK2----
                print("Scarlet Witch?")
                print("a.Correct")
                print("b.No")
                cek1=input("Answer: ")
                if(cek1=='a'):
                    print("Yay!!!")
                    
                elif(cek1=='b'):
                    print("Wasp?")
                    print("a.Correct")
                    print("b.No")
                    cek1=input("Answer: ")
                    if(cek1=='a'):
                        print("Yay!!!")
                        
                    elif(cek1=='b'):
                        print("Hero not Found :(")
                    else:
                        print('Cant Recognize Answer')
                else:
                    print('Cant Recognize Answer')
            
            elif(point in range (40000,70000)):#----CHECK3----
                print("Valkyrie?")
                print("a.Correct")
                print("b.No")
                cek1=input("Answer: ")
                if(cek1=='a'):
                    print("Yay!!!")
                    
                elif(cek1=='b'):
                    print("Nebula?")
                    print("a.Correct")
                    print("b.No")
                    cek1=input("Answer: ")
                    if(cek1=='a'):
                        print("Yay!!!")
                        
                    elif(cek1=='b'):
                        print("Gamora?")
                        print("a.Correct")
                        print("b.No")
                        cek1=input("Answer: ")
                        if(cek1=='a'):
                            print("Yay!!!")
                            
                        elif(cek1=='b'):
                            print("Hero not Found :(")
                        else:
                            print('Cant Recognize Answer')
                    else:
                        print('Cant Recognize Answer')
                else:
                    print('Cant Recognize Answer')

            elif(point in range (70000,100000)):#----CHECK4----    
                print("Mantis?")
                print("a.Correct")
                print("b.No")
                cek1=input("Answer: ")
                if(cek1=='a'):
                    print("Yay!!!")
                    
                elif(cek1=='b'):
                    print("Hero not Found :(")
                else:
                    print('Cant Recognize Answer')

            elif(point in range (100000,107000)):#----CHECK5----
                print("Quicksilver?")
                print("a.Correct")
                print("b.No")
                cek1=input("Answer: ")
                if(cek1=='a'):
                    print("Yay!!!")
                    
                elif(cek1=='b'):
                    print("War Machine?")
                    print("a.Correct")
                    print("b.No")
                    cek1=input("Answer: ")
                    if(cek1=='a'):
                        print("Yay!!!")
                        
                    elif(cek1=='b'):
                        print("Winter Soldier?")
                        print("a.Correct")
                        print("b.No")
                        cek1=input("Answer: ")
                        if(cek1=='a'):
                            print("Yay!!!")
                            
                        elif(cek1=='b'):
                            print("Wong?")
                            print("a.Correct")
                            print("b.No")
                            cek1=input("Answer: ")
                            if(cek1=='a'):
                                print("Yay!!!")
                                
                            elif(cek1=='b'):
                                print("Captain America?")
                                print("a.Correct")
                                print("b.No")
                                cek1=input("Answer: ")
                                if(cek1=='a'):
                                    print("Yay!!!")
                                    
                                elif(cek1=='b'):
                                    print("Doctor Strange?")
                                    print("a.Correct")
                                    print("b.No")
                                    cek1=input("Answer: ")
                                    if(cek1=='a'):
                                        print("Yay!!!")     

                                    elif(cek1=='b'):
                                        print('Hero not Found :(')
                                    else:
                                        print('Cant Recognize Answer')
                                else:
                                    print('Cant Recognize Answer')
                            else:
                                print('Cant Recognize Answer')
                        else:
                            print('Cant Recognize Answer')
                    else:
                        print('Cant Recognize Answer')
                else:
                    print('Cant Recognize Answer')

            elif(point in range (107000,110000)):#----CHECK5----    
                print("Hulk?")
                print("a.Correct")
                print("b.No")
                cek1=input("Answer: ")
                if(cek1=='a'):
                    print("Yay!!!")
                        
                elif(cek1=='b'):
                    print("Hero not Found :(")
                else:
                    print('Cant Recognize Answer')
            
            elif(point in range (110000,120000)):#----CHECK6----
                print("StarLord?")
                print("a.Correct")
                print("b.No")
                cek1=input("Answer: ")
                if(cek1=='a'):
                    print("Yay!!!")
                    
                elif(cek1=='b'):
                    print("Iron Man?")
                    print("a.Correct")
                    print("b.No")
                    cek1=input("Answer: ")
                    if(cek1=='a'):
                        print("Yay!!!")
                        
                    elif(cek1=='b'):
                        print("Vision?")
                        print("a.Correct")
                        print("b.No")
                        cek1=input("Answer: ")
                        if(cek1=='a'):
                            print("Yay!!!")
                            
                        elif(cek1=='b'):
                            print("Hero not Found :(")
                        else:
                            print('Cant Recognize Answer')
                    else:
                        print('Cant Recognize Answer')
                else:
                    print('Cant Recognize Answer')
            
            elif(point in range (130000,140000)):#----CHECK7----
                print("Falcon?")
                print("a.Correct")
                print("b.No")
                cek1=input("Answer: ")
                if(cek1=='a'):
                    print("Yay!!!")
                    
                elif(cek1=='b'):
                    print("Hawkeye?")
                    print("a.Correct")
                    print("b.No")
                    cek1=input("Answer: ")
                    if(cek1=='a'):
                        print("Yay!!!")
                        
                    elif(cek1=='Black Panther?'):
                        print("Gamora?")
                        print("a.Correct")
                        print("b.No")
                        cek1=input("Answer: ")
                        if(cek1=='a'):
                            print("Yay!!!")
                            
                        elif(cek1=='b'):
                            print("Hero not Found :(")
                        else:
                            print('Cant Recognize Answer')
                    else:
                        print('Cant Recognize Answer')
                else:
                    print('Cant Recognize Answer')
            
            elif(point in range (140000,150000)):#----CHECK8----
                print("Spider Man?")
                print("a.Correct")
                print("b.No")
                cek1=input("Answer: ")
                if(cek1=='a'):
                    print("Yay!!!")
                    
                elif(cek1=='b'):
                    print("Ant Man?")
                    print("a.Correct")
                    print("b.No")
                    cek1=input("Answer: ")
                    if(cek1=='a'):
                        print("Yay!!!")
                        
                    elif(cek1=='b'):
                        print("Hero not Found :(")
                    else:
                        print('Cant Recognize Answer')
                else:
                    print('Cant Recognize Answer')
            
            elif(point in range (150000,156000)):#----CHECK9----
                print("Thor?")
                print("a.Correct")
                print("b.No")
                cek1=input("Answer: ")
                if(cek1=='a'):
                    print("Yay!!!")
                    
                elif(cek1=='b'):
                    print("Groot?")
                    print("a.Correct")
                    print("b.No")
                    cek1=input("Answer: ")
                    if(cek1=='a'):
                        print("Yay!!!")
                        
                    elif(cek1=='Heimdall?'):
                        print("Gamora?")
                        print("a.Correct")
                        print("b.No")
                        cek1=input("Answer: ")
                        if(cek1=='a'):
                            print("Yay!!!")
                            
                        elif(cek1=='b'):
                            print("Hero not Found :(")
                        else:
                            print('Cant Recognize Answer')
                    else:
                        print('Cant Recognize Answer')
                else:
                    print('Cant Recognize Answer')
            
            elif(point in range (156000,170000)):#----CHECK10----
                print("Drax?")
                print("a.Correct")
                print("b.No")
                cek1=input("Answer: ")
                if(cek1=='a'):
                    print("Yay!!!")
                    
                elif(cek1=='b'):
                    print("Yondu?")
                    print("a.Correct")
                    print("b.No")
                    cek1=input("Answer: ")
                    if(cek1=='a'):
                        print("Yay!!!")
                        
                    elif(cek1=='Loki?'):
                        print("Gamora?")
                        print("a.Correct")
                        print("b.No")
                        cek1=input("Answer: ")
                        if(cek1=='a'):
                            print("Yay!!!")
                            
                        elif(cek1=='b'):
                            print("Hero not Found :(")
                        else:
                            print('Cant Recognize Answer')
                    else:
                        print('Cant Recognize Answer')
                else:
                    print('Cant Recognize Answer')

            elif(point in range (184020,200000)):#----CHECK11----    
                print("RocketRacoon?")
                print("a.Correct")
                print("b.No")
                cek1=input("Answer: ")
                if(cek1=='a'):
                    print("Yay!!!")
                            
                elif(cek1=='b'):
                    print("Hero not Found :(")
                else:
                    print('Cant Recognize Answer')

            else:
                print("Hero not Found :(")

        while True:
            print("Play Again?")
            print("a.Yes")
            print("b.No")
            play = input("Answer: ")
            if(play =="a"):
                os.system('cls')
                break        
            elif(play =="b"):
                break     
            else:
                print("Can't Recognize Answer")

        if(play =="b"):
            for i in range (0,10):
                os.system('cls')
                print(".O")
                print(".°")
                print("   ")
                print("   ")
                print("   ")
                print("   ")
                print("   ")
                print(".O")
                print(".°")
                time.sleep(0.02)
                os.system('cls')
                print(".O°o.")
                print(".°o.O.")
                print("         ")
                print("         ")
                print("         ")
                print("         ")
                print("         ")
                print(".O°o.")
                print(".°o.O.")
                time.sleep(0.02)
                os.system('cls')
                print(".O°o. .o°")
                print(".°o.O.o° ")
                print("         ")
                print("         ")
                print("         ")
                print("         ")
                print("         ")
                print(".O°o. .o°")
                print(".°o.O.o° ")
                time.sleep(0.02)
                os.system('cls')
                print(".O°o. .o°O____")
                print(".°o.O.o° ¯¯¯¯¯")
                print("         ░░░░░")
                print("         ░░░░░")
                print("         ░░░░░")
                print("         ░░░░░")
                print("         ░░░░░")
                print(".O°o. .o°O____")
                print(".°o.O.o° ¯¯¯¯¯")
                time.sleep(0.02)
                os.system('cls')
                print(".O°o. .o°O________")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯")
                print("         ░░░░░╔══╦")
                print("         ░░░░░╚╗╔╣")
                print("         ░░░░░░║║║")
                print("         ░░░░░░║║║")
                print("         ░░░░░░╚╝╚")
                print(".O°o. .o°O________")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯")
                time.sleep(0.02)
                os.system('cls')
                print(".O°o. .o°O____________")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯")
                print("         ░░░░░╔══╦╗░░░")
                print("         ░░░░░╚╗╔╣╚╦═╦")
                print("         ░░░░░░║║║║╠╝║")
                print("         ░░░░░░║║║║║║║")
                print("         ░░░░░░╚╝╚╩╩═╩")
                print(".O°o. .o°O____________")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯")
                time.sleep(0.02)
                os.system('cls')
                print(".O°o. .o°O________________")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                print("         ░░░░░╔══╦╗░░░░╔╗░")
                print("         ░░░░░╚╗╔╣╚╦═╦═╣║╔")
                print("         ░░░░░░║║║║╠╝║║║╠╝")
                print("         ░░░░░░║║║║║║║║║╔╗")
                print("         ░░░░░░╚╝╚╩╩═╩╩╩╝╚")
                print(".O°o. .o°O________________")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                time.sleep(0.02)
                os.system('cls')
                print(".O°o. .o°O_____________________")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                print("         ░░░░░╔══╦╗░░░░╔╗░░░░░░")
                print("         ░░░░░╚╗╔╣╚╦═╦═╣║╔╗░░░░")
                print("         ░░░░░░║║║║╠╝║║║╠╝║░░░░")
                print("         ░░░░░░║║║║║║║║║╔╗╣░░░░")
                print("         ░░░░░░╚╝╚╩╩═╩╩╩╝╚╝░░░░")
                print(".O°o. .o°O_____________________")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                time.sleep(0.02)
                os.system('cls')
                print(".O°o. .o°O_________________________")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                print("         ░░░░░╔══╦╗░░░░╔╗░░░░░░╔╗╔╗")
                print("         ░░░░░╚╗╔╣╚╦═╦═╣║╔╗░░░░║║║╠")
                print("         ░░░░░░║║║║╠╝║║║╠╝║░░░░║╚╝║")
                print("         ░░░░░░║║║║║║║║║╔╗╣░░░░╚╗╔╣")
                print("         ░░░░░░╚╝╚╩╩═╩╩╩╝╚╝░░░░░╚╝╚")
                print(".O°o. .o°O_________________________")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                time.sleep(0.02)
                os.system('cls')
                print(".O°o. .o°O____________________________")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                print("         ░░░░░╔══╦╗░░░░╔╗░░░░░░╔╗╔╗░░░")
                print("         ░░░░░╚╗╔╣╚╦═╦═╣║╔╗░░░░║║║╠═╦╦")
                print("         ░░░░░░║║║║╠╝║║║╠╝║░░░░║╚╝║║║║")
                print("         ░░░░░░║║║║║║║║║╔╗╣░░░░╚╗╔╣║║║")
                print("         ░░░░░░╚╝╚╩╩═╩╩╩╝╚╝░░░░░╚╝╚═╩═")
                print(".O°o. .o°O____________________________")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                time.sleep(0.02)
                os.system('cls')
                print(".O°o. .o°O________________________________O")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                print("         ░░░░░╔══╦╗░░░░╔╗░░░░░░╔╗╔╗░░░░░░░░")
                print("         ░░░░░╚╗╔╣╚╦═╦═╣║╔╗░░░░║║║╠═╦╦╗░░░░")
                print("         ░░░░░░║║║║╠╝║║║╠╝║░░░░║╚╝║║║║║░░░░")
                print("         ░░░░░░║║║║║║║║║╔╗╣░░░░╚╗╔╣║║║║░░░░")
                print("         ░░░░░░╚╝╚╩╩═╩╩╩╝╚╝░░░░░╚╝╚═╩═╝░░░░")
                print(".O°o. .o°O________________________________O")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                time.sleep(0.02)
                os.system('cls')
                print(".O°o. .o°O________________________________O")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                print("         ░░░░░╔══╦╗░░░░╔╗░░░░░░╔╗╔╗░░░░░░░░")
                print("         ░░░░░╚╗╔╣╚╦═╦═╣║╔╗░░░░║║║╠═╦╦╗░░░░")
                print("         ░░░░░░║║║║╠╝║║║╠╝║░░░░║╚╝║║║║║░░░░")
                print("         ░░░░░░║║║║║║║║║╔╗╣░░░░╚╗╔╣║║║║░░░░")
                print("         ░░░░░░╚╝╚╩╩═╩╩╩╝╚╝░░░░░╚╝╚═╩═╝░░░░")
                print(".O°o. .o°O________________________________O")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                time.sleep(0.02)
                os.system('cls')
                print(".O°o. .o°O________________________________O°o. .o°O.")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯.°o.O.o°")
                print("         ░░░░░╔══╦╗░░░░╔╗░░░░░░╔╗╔╗░░░░░░░░")
                print("         ░░░░░╚╗╔╣╚╦═╦═╣║╔╗░░░░║║║╠═╦╦╗░░░░")
                print("         ░░░░░░║║║║╠╝║║║╠╝║░░░░║╚╝║║║║║░░░░")
                print("         ░░░░░░║║║║║║║║║╔╗╣░░░░╚╗╔╣║║║║░░░░")
                print("         ░░░░░░╚╝╚╩╩═╩╩╩╝╚╝░░░░░╚╝╚═╩═╝░░░░")
                print(".O°o. .o°O________________________________O°o. .o°O.")
                print(".°o.O.o° ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯.°o.O.o°.")
                time.sleep(1)
            break
    
    elif(x == 'b'):
        print(".O°o. .o°O___________________________________________________O°o. .o°O.")
        print("1.Imagine about 1 random avengers superhero")
        print("2.Answer the question with YES or NO according to chosen hero")
        print(".O°o. .o°O___________________________________________________O°o. .o°O.")
        print("press ENTER to back")
        back = input()

    else:
        print("Sorry, there's no such option")
        print("Please Try again")