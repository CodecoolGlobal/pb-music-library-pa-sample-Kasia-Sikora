from music_reports import *
from display import *
from file_handling import *
"""
The main program should use functions from music_reports and display modules
"""

def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    menu_commands = ["Get albums by genre", "Display longest album", "Display total albums lenght", "Show genre statse", "Display oldest album", "Display oldest album by genre"]
    print_program_menu(menu_commands)
    albums = import_data()

    while True: 
        user_input = int(input("\nEnter number of menu: "))
        if user_input == 1:
            print_command_result(menu_commands[user_input-1])
            genre = input("Enter genre: \n")
            print_albums_list(get_albums_by_genre(albums, genre))
        elif user_input == 2:
            print_command_result(menu_commands[user_input-1])
            get_longest_album(albums)
        elif user_input == 3:
            print_command_result(menu_commands[user_input-1])
            get_total_albums_length(albums)
        elif user_input == 4:
            print_command_result(menu_commands[user_input-1])
            get_genre_stats(albums)
        elif user_input == 5:
            print_command_result(menu_commands[user_input-1])
            get_last_oldest(albums)
        elif user_input == 6:
            print_command_result(menu_commands[user_input-1])
            genre = input("Enter genre: \n")
            get_last_oldest_of_genre(albums, genre)
        else:
            break




if __name__ == '__main__':
    main()
