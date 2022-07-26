from signal import signal, SIGINT
import random

"""
Singnal and SIGINIT are used to handle CTRL-C and SIGINT, and exit gracefully.
"""

import os, external_modules

def handler(signal_received, frame):
    # Handling any cleanup here
    print('\nCTRL-C or SIGINT detected. Exiting gracefully...')
    exit(0)


### Main menu ###
while True:
    signal(SIGINT, handler)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1\033[92mWelcome to the Music Quiz:\033[00m\033[0m")
    choice = input("""
Enter '\033[1madd\033[0m' to add custom songs to the quiz
Enter '\033[1mplay\033[0m' to play the quiz
Enter '\033[1mquit\033[0m' to exit the program
>>> """)
    if choice == "add":
        # Add songs to the quiz
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[1\033[92mWelcome to the Music Quiz:\033[00m\033[0m")
        print("\033[1mAdd songs to the quiz:\033[00m")
        print("\033[1mEnter '\033[0mback\033[1m' to return to the main menu\033[0m")
        while True:
            song_name = input("Enter the name of the song: ")
            if song_name == "back":
                break
            artist_name = input("Enter the name of the artist: ")
            if artist_name == "back":
                break
            external_modules.writing_data_csv("quiz_songs.csv", [song_name, artist_name], ["song_name", "artist_name"])
            print("\033[1mSong added successfully!\033[00m")
            print("\033[1mEnter '\033[0mback\033[1m' to return to the main menu\033[0m")
    elif choice == "play":
        # Play the quiz
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[1\033[92mWelcome to the Music Quiz:\033[00m\033[0m")
        print("\033[1mPlay the quiz:\033[00m")
        print("\033[1mEnter '\033[0mback\033[1m' to return to the main menu\033[0m")
        read_header, read_rows = external_modules.reading_data_csv("quiz_songs.csv")
        names = []
        artists = []
        for i in range(len(read_rows)):
            name, artist = read_rows[i].split(",")
            names.append(name)
            artists.append(artist)
        # print(names)
        # print(artists)
        temp = input()
        while True:
            random_number = random.randint(0, len(names)-1)
            print("Artist: " + artists[random_number])
            print("Song [first letter(s)]: ", end=" ")
            if " " in names[random_number]:
                split_song = names[random_number].split(" ")
                for i in range(len(split_song)):
                    print(split_song[i][:1], end=" ")
            else:
                print(names[random_number][:1])
            guess = input(">>> ")
            if guess == "back":
                break
            if guess == names[random_number]:
                print("\033[1mCorrect!\033[00m")
            else:
                print("\033[1mWrong!\033[00m")

