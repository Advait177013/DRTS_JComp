import os
import time
from playsound import playsound
import Lyrics
from multiprocessing import Process

#if __name__ == "__main__":
#def sound():
#    playsound('OceanMan.mp3')

if __name__ == "__main__":
    #p = Process(target=sound)
    #p.start()
    #input("test : ")
    #p.terminate()
    #input("wow : ")
    while(1):
        os.system('cls')
        print("Welcome to Improv Karaoke\nWe have a selection of songs available for you")
        extensions=[".wav", ".mp3"]
        file_list=[]
        print("pid is "+str(os.getpid()))
        for path, dirs, files in os.walk('.'):
            for filename in files:
                if any(ext in filename for ext in extensions):
                    file_list.append(os.path.join(filename))
        counter=1
        for file in file_list:
            print("\t"+str(counter)+" : "+file)
            counter+=1
        x=input("select the file you want by entering a number : ")
        x=int(x)
        x-=1
        sgname = file_list[x]
        print("Now playing : "+sgname)
        if(sgname=='Exitlude.mp3'):
            p1=Process(target=Lyrics.playExitlude)
            p1.start()
            input("\nPress any key to terminate\n")
            p1.terminate()
        elif(sgname=='OceanMan.mp3'):
            p1=Process(target=Lyrics.playOcean)
            p1.start()
            input("\nPress any key to terminate\n")
            p1.terminate()
