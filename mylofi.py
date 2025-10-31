import tkinter
import pygame

# WINDOW CODE:
# # Creates a window
window = tkinter.Tk()
# # Adds the name at the top of the window
window.title("MyLoFi")
# # Dimensions of the window and background colour
window.geometry('500x570')
window.configure(bg='#f3dfc6')

# NAME CODE:
# # Bracket window means that everything occurs within the window aka its master/home
# # Pack to place widgets, used throughout project, makes it responsive unlike grid
# # # pady means padding-yaxis, provides room above and below label
name_label = tkinter.Label(window, text="MyLoFi*", bg="#f3dfc6", fg="#d6a5b3", font=('Lofi * Lifestyle', 60))
name_label.pack(pady=15) 

# DESCRIPTION CODE:
# # Little instruction label
name_label = tkinter.Label(window, text="Tick which elements you want in your lofi track!", bg="#f3dfc6", fg="#8a6aaf", font=('Lofi * Lifestyle', 18))
name_label.pack(pady=5)

# PIANO CHORDS CHECKBOX:
# # set variable meas future code can reset it through on value and off value
var1=tkinter.IntVar()
checkbox = tkinter.Checkbutton (window, text="Piano Chords", variable=var1, onvalue=1, offvalue=0, bg="#f3dfc6", fg="#bc8ab2", font=('Lofi * Lifestyle', 18))
checkbox.pack()

# BASS CHECKBOX:
var2=tkinter.IntVar()
checkbox = tkinter.Checkbutton (window, text="Bass", variable=var2, onvalue=1, offvalue=0, bg="#f3dfc6", fg="#bc8ab2", font=('Lofi * Lifestyle', 18))
checkbox.pack()

# DRUMS CHECKBOX:
var3=tkinter.IntVar()
checkbox = tkinter.Checkbutton (window, text="Drums", variable=var3, onvalue=1, offvalue=0, bg="#f3dfc6", fg="#bc8ab2", font=('Lofi * Lifestyle', 18))
checkbox.pack()

# HIGH HAT CHECKBOX:
var4=tkinter.IntVar()
checkbox = tkinter.Checkbutton (window, text="High Hat", variable=var4, onvalue=1, offvalue=0, bg="#f3dfc6", fg="#bc8ab2", font=('Lofi * Lifestyle', 18))
checkbox.pack()

# PIANO MELODY CHECKBOX:
var5=tkinter.IntVar()
checkbox = tkinter.Checkbutton (window, text="Piano Melody", variable=var5, onvalue=1, offvalue=0, bg="#f3dfc6", fg="#bc8ab2", font=('Lofi * Lifestyle', 18))
checkbox.pack()

# CAFE CHATTER CHECKBOX:
var6=tkinter.IntVar()
checkbox = tkinter.Checkbutton (window, text="Cafe Chatter", variable=var6, onvalue=1, offvalue=0, bg="#f3dfc6", fg="#bc8ab2", font=('Lofi * Lifestyle', 18))
checkbox.pack()

# VINYL CRACKLE CHECKBOX:
var7=tkinter.IntVar()
checkbox = tkinter.Checkbutton (window, text="Vinyl Crackle", variable=var7, onvalue=1, offvalue=0, bg="#f3dfc6", fg="#bc8ab2", font=('Lofi * Lifestyle', 18))
checkbox.pack()

# PLAY BUTTON COMMAND:
def start():
    # Paths to individual audio files
    file1 = "/Users/kaylyn/Desktop/lofitrack/pianochords.mp3"
    file2 = "/Users/kaylyn/Desktop/lofitrack/bass.mp3"
    file3 = "/Users/kaylyn/Desktop/lofitrack/drums.mp3"
    file4 = "/Users/kaylyn/Desktop/lofitrack/highhat.mp3"
    file5 = "/Users/kaylyn/Desktop/lofitrack/pianomelody.mp3"
    file6 = "/Users/kaylyn/Desktop/lofitrack/cafechatter.mp3"
    file7 = "/Users/kaylyn/Desktop/lofitrack/vinylcrackle.mp3"
    
    # Initialise pygame mixer
    pygame.mixer.init()

    # Load sounds and attaches them to the name 'sound_'
    sound1 = pygame.mixer.Sound(file1)
    sound2 = pygame.mixer.Sound(file2)
    sound3 = pygame.mixer.Sound(file3)
    sound4 = pygame.mixer.Sound(file4)
    sound5 = pygame.mixer.Sound(file5)
    sound6 = pygame.mixer.Sound(file6)
    sound7 = pygame.mixer.Sound(file7)

    # IF STATEMENT:
    # # If the certain variable e.g. var1=pianochords, is =1, which as stated previously is the onvalue, it will play sound1 which is the piano chords file
    # # Loop is set to -1 which means it will play infinitely 
    if var1.get()==1:
        channel1 = sound1.play(loops=-1)
    if var2.get()==1:
        channel1 = sound2.play(loops=-1)
    if var3.get()==1:
        channel1 = sound3.play(loops=-1)
    if var4.get()==1:
        channel1 = sound4.play(loops=-1)
    if var5.get()==1:
        channel1 = sound5.play(loops=-1)
    if var6.get()==1:
        channel1 = sound6.play(loops=-1)
    if var7.get()==1:
        channel1 = sound7.play(loops=-1)

    # Prints text in terminal
    print("Playing track... Press Stop button to stop playing.")

# STOP BUTTON COMMAND:
# # Defines the command written in the button further down
# # Stops the track and prints text in terminal
def stop():
    pygame.mixer.stop()
    print("Playback stopped.")

# SELECT ALL COMMAND:
# # sets the variable (checkboxes) to 1, which means onvalue, therefore, all boxes are checked
def select_all():
    var1.set(1)
    var2.set(1)
    var3.set(1)
    var4.set(1)
    var5.set(1)
    var6.set(1)
    var7.set(1)

# DESELECT ALL COMMAND:
# # sets the variable (checkboxes) to 0, which means offvalue, therefore, all boxes are blank
def deselect_all():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)

# PLAY BUTTON CODE:
play_button = tkinter.Button(window, text="Play", font=('Lofi * Lifestyle', 20), fg='#8a6aaf', command=start)
play_button.pack(pady=20)

# STOP BUTTON CODE:
stop_button = tkinter.Button(window, text="Stop", font=('Lofi * Lifestyle', 20), fg='#8a6aaf', command=stop)
stop_button.pack()

# SELECT ALL BUTTON CODE:
select_all_button = tkinter.Button(window, text="Select All", font=('Lofi * Lifestyle', 20), fg='#8a6aaf', command=select_all)
select_all_button.pack(pady=20)

# DESELECT ALL BUTTON CODE:
deselect_all_button = tkinter.Button(window, text="Deselect All", font=('Lofi * Lifestyle', 20), fg='#8a6aaf', command=deselect_all)
deselect_all_button.pack()

# Infinite loop so the app is being executed
# Nothing can be executed after it, hence why it's the last line
window.mainloop()