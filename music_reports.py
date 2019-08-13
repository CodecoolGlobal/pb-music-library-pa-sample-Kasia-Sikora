from file_handling import *
from operator import itemgetter


def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    genre_list = [line[-2] for line in albums] # create a list of avalable genres in albums

    if genre not in genre_list: # rise an error if genre not in albums 
        raise ValueError ("Wrong genre")

    genre_in_list = -2 # index of genre in every line in for loop under 

    # list of genre albums sorted by year
    return sorted([line for line in albums if genre == line[genre_in_list]], key = itemgetter(2)) 


def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    max_lenght_of_album = 0

    # get max lenght of albums
    for line in albums:
        s = float(line[-1].replace(":", "."))
        if s > max_lenght_of_album:
            max_lenght_of_album = s

    max_lenght_of_album = str(max_lenght_of_album).replace(".", ":")
        
    # get album with longest play time
    for line in albums: 
        if max_lenght_of_album in line:
            return line


def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    sum_of_time = 0

    # for loot to sum play time of every album
    for line in albums:
        index = line[-1].index(":")
        minutes = int(line[-1][:index])
        seconds = int(line[-1][index+1:])
        sum_of_time += (minutes *60)+seconds
    
    # round to 2 decimals
    total_time = float('%.2f' % float(sum_of_time/60))

    return total_time
   

def get_genre_stats(genre):

    genre_in_list = -2 # number of genre index in lines
    genre_stats = {}

    # add to dictionary genre keys 
    for line in genre: 
        if line[genre_in_list] in genre_stats.keys():
            genre_stats[line[genre_in_list]] +=1
        else:
            genre_stats[line[genre_in_list]] = 1

    return genre_stats


def get_last_oldest(albums):
    
    year = 2
    min_year = min([int(line[year]) for line in albums]) # get minimum year in albums

    last_oldest_album = [line for line in albums if min_year == int(line[year])] # create a list of oldest albums

    return last_oldest_album[-1]


def get_last_oldest_of_genre(albums, genre):
    
    genre_list = [line[-2] for line in albums] # list of available genres in albums

    if genre not in genre_list: # rise an error if genre not in genre list
        raise ValueError ("Wrong genre")

    year = 2
    genre_in_list = -2

    #sort albums of specific genre by oldest year
    oldest_of_genre = sorted([line for line in albums if genre == line[genre_in_list]], key = itemgetter(2))

    return oldest_of_genre[0]

   
