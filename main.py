from signal import signal, SIGINT
from spotipy.oauth2 import SpotifyClientCredentials
import random, time, pandas, csv, spotipy

"""
Singnal and SIGINIT are used to handle CTRL-C and SIGINT, and exit gracefully.
"""

import os, external_modules

def handler(signal_received, frame):
    # Handling any cleanup here
    print('\nCTRL-C or SIGINT detected. Exiting gracefully...')
    exit(0)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

### Login menu ###
while True:
    signal(SIGINT, handler)
    clear_console()
    print("\033[1\033[92mWelcome to the Music Quiz:\033[00m\033[0m")
    choice = input("""
Enter '\033[1mlogin\033[0m' to log in as a user
Enter '\033[1madd\033[0m' to add users
Enter '\033[1mquit\033[0m' to exit the program
>>> """)
    if choice == 'add':
        user_username = input('Enter a username you want to have: ')
        user_password = input('Enter your password you wish to have: ')
        external_modules.add_user_csv(user_username, user_password)
        break
    elif choice == 'login':
        while True:
            clear_console()
            entered_username = input('Enter a username: ')
            read_header, read_rows = external_modules.reading_data_csv('players.csv')
            row_to_check = 0
            for row in range(len(read_rows)):
                if entered_username in read_rows[row]:
                    row_to_check = row
                else:
                    continue
            entered_password = input(f'Enter the password for {entered_username}: ')
            if entered_password in read_rows[row_to_check]:
                print('Logged in succesfully')
                time.sleep(0.5)
                break
            else:
                print('Incorrect details')
                time.sleep(0.5)
                continue

        temp = input('\nPress ENTER to continue\n')
        break
    elif choice == 'exit':
        print('Exiting...')
        exit(0)
    else:
        break

### Main menu ###
while True:
    signal(SIGINT, handler)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1\033[92mWelcome to the Music Quiz:\033[00m\033[0m")
    choice = input("""
Enter '\033[1madd\033[0m' to add custom songs to the quiz
Enter '\033[1mplay\033[0m' to play the quiz (with own songs)
Enter '\033[1mspotify\033[0m' to play the quiz (with spotify songs)
Enter '\033[1mquit\033[0m' to exit the program
>>> """)
    if choice == 'quit':
        os._exit
    elif choice == "add":
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
    elif choice == "spotify":
        url = "https://open.spotify.com/playlist/4OIVU71yO7SzyGrh0ils2i?si=06ca21db2ef54760"

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
        temp = input("Press ENTER to start the quiz\n")
        points = 0
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
            if guess == names[random_number]:
                print("\033[1mCorrect!\033[00m")
                points += 3
            elif guess == "finish":
                break            
            else:
                print("\033[1mWrong!\033[00m")
                print("One more chance...")
                guess = input(">>> ")
                if guess == names[random_number]:
                    print("\033[1mCorrect!\033[00m")
                    points += 1
                elif guess == "finish":
                    break
                else:
                    print("No points for you!")
                    continue
        print("\033[1mYou scored " + str(points) + " points!\033[00m")
        temp = input("Press ENTER to return to the main menu\n")
        # external_modules.writing_data_csv('players.csv', [player, points], ['player', 'points'])
