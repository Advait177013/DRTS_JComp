import os
import time
from playsound import playsound
import SongPlayers
import LyricPlayers
from multiprocessing import Process

if __name__ == "__main__":
    while(1):
        os.system('cls')
        print("Welcome to Improv Karaoke\nWe have a selection of songs available for you")
        extensions=[".wav", ".mp3"]
        file_list=[]
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
            p1=Process(target=SongPlayers.playExitlude)
            p2=Process(target=LyricPlayers.playExitlude)
        elif(sgname=='OceanMan.mp3'):
            p1=Process(target=SongPlayers.playOcean)
            p2=Process(target=LyricPlayers.playOcean)
        elif(sgname=='RickRoll.mp3'):
            p1=Process(target=SongPlayers.playRick)
            p2=Process(target=LyricPlayers.playRick)
        elif(sgname=='LoseYourself.mp3'):
            p1=Process(target=SongPlayers.playLoseYourself)
            p2=Process(target=LyricPlayers.playLoseYourself)
        elif(sgname=='CountryRoads.mp3'):
            p1=Process(target=SongPlayers.playCountry)
            p2=Process(target=LyricPlayers.playCountry)

        p1.start()
        p2.start()
        input("\nPress any key to terminate\n")
        p1.terminate()
        p2.terminate()
