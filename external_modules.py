import csv, random
from os.path import exists

def writing_data_csv(filename, data_to_write, header):
    """
    Function to write data to csv file
    Parameters: filename (string) - the name of the file to be read
                data_to_write (string) - the data to be written (or appended) to the file
    """
    file_exists = exists(filename)
    if file_exists is False:
        # Create a new file if it doesn't exist
        with open(filename, 'w+', newline="", encoding='utf-8') as writing_file:
            csvwriter1 = csv.writer(writing_file) # 1. create a csvwriter object
            csvwriter1.writerow(header) # 2. write the header, must be an array
            csvwriter1.writerow(data_to_write) # 3. write the rest of the data
            writing_file.close() # 4. close the file
    else:
        with open(filename, 'a', newline="", encoding='utf-8') as appending_file:
            csvwriter2 = csv.writer(appending_file) # 1. create a csvwriter object
            csvwriter2.writerow(data_to_write) # 2. write the row, without the header
            appending_file.close() # 3. close the file

def reading_data_csv(filename):
    """
    Reads the data from the csv file and returns a header and a list of rows (both as lists)
    Parameters: filename (string) - the name of the file to be read
    """
    with open(filename, 'r', encoding='utf-8') as read_file:
        content = read_file.readlines()
    read_header = content[:1]
    read_rows = content[1:]
    read_file.close()
    read_header[-1] = read_header[-1].strip()
    for i in range(len(read_rows)):
        read_rows[i] = read_rows[i].strip()
    return read_header, read_rows

def choosing_random_song():
    """
    Function to choose a random song from the csv file
    """
    read_header, read_rows = reading_data_csv("quiz_songs.csv")
    random_number = random.randint(0, len(read_rows)-1)
    return read_rows[random_number]

def add_user_csv(username, password):
    writing_data_csv('players.csv', [username, password, 0], ['usernames', 'passwords', 'scores'])

def check_username(filename, username_to_check):
    read_header, read_rows = reading_data_csv(filename)
    usernames = []
    for i in range(len(read_rows)):
        split_username = read_rows[i].split(',')
        usernames.append(split_username[0])
    if username_to_check in usernames:
        return True
    else:
        return False

def check_password(filename, password_to_check):
    read_header, read_rows = reading_data_csv(filename)
    passwords = []
    for i in range(len(read_rows)):
        split_username = read_rows[i].split(',')
        passwords.append(split_username[1])
    if password_to_check in passwords:
        return True
    else:
        return False
