from pygame import mixer
import os
os.chdir("Stock")
mixer.init()
sl=os.listdir(os.getcwd())
#print(sl)

count=len(os.listdir(os.getcwd()))
counter=0
mixer.music.load(sl[0])

def pause():
    mixer.music.pause()

def play(counter):
    mixer.music.play()

print("\n\tWelcom to Python Music Player")
while True:
    print("""\n    \t\tYou can opt:

    0 -> Play
    1 -> Pause
    2 -> Unpause
    3 -> Stop
    4 -> Play Next
    5 -> Play Previous
    6 -> Show List
                     """)
    op=int(input("    What to do ? : "))

    if op==0:
        play(counter)
    if op==1:
        pause()
    if op==2:
        mixer.music.unpause()
    if op==3:
        mixer.music.stop()
        print("\nHope you enjoyed the music !!!\n")
        break

    if op==4:
        counter+=1
        if counter<count:
            mixer.music.load(sl[counter])
            play(counter)
        else:
            counter=0
            mixer.music.load(sl[counter])
            play(counter)

    if op==5:
        counter=counter-1
        if counter<0:
            counter=count-1
            mixer.music.load(sl[counter])
            play(counter)
        else:
            mixer.music.load(sl[counter])
            play(counter)

    if op==6:
        for i in range(len(sl)):
            print(sl[i]," --> ",i)
        print("For playing a specific song select the no.")
        n=int(input("Enter here: "))

        counter=n
        mixer.music.load(sl[n])
        play(n)
input()








































        

