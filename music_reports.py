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
    genre_list = [line[-2] for line in albums]
    if genre not in genre_list:
        raise ValueError ("Wrong genre")

    genre_in_list = -2
    return sorted([line for line in albums if genre == line[genre_in_list]], key = itemgetter(-3))


def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """

    max_lenght_of_album = 0
    for line in albums:
        s = float(line[-1].replace(":", "."))
        if s > max_lenght_of_album:
            max_lenght_of_album = s

    max_lenght_of_album = str(max_lenght_of_album).replace(".", ":")
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
    max_total_time = 0
    for line in albums:
        index = line[-1].index(":")
        minutes = int(line[-1][:index])
        seconds = int(line[-1][index+1:])
        max_total_time += (minutes *60)+seconds
    max_time = float('%.2f' % float(max_total_time/60))

    return max_time
   

def get_genre_stats(genre):
    genre_in_list = -2
    genre_stats = {}
    for line in genre: 
        if line[genre_in_list] in genre_stats.keys():
            genre_stats[line[genre_in_list]] +=1
        else:
            genre_stats[line[genre_in_list]] = 1
    return genre_stats

def get_last_oldest(albums):
    
    year = 2
    min_year = min([int(line[year]) for line in albums])

    return max([line for line in albums if min_year == int(line[year])])

def get_last_oldest_of_genre(albums, genre):
    
    year = 2
    genre_in_list = -2
    oldest_of_genre = (sorted([line for line in albums if genre == line[genre_in_list]], key = itemgetter(2)))
    return oldest_of_genre[0]

   
