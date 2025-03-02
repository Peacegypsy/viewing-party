def create_movie(title, genre, rating):
    m = dict();
    m['title'] = title
    m['genre'] = genre
    m['rating'] = rating
    if m['title'] and m['genre'] and m['rating']:
        return m
    
def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if title in movie['title']:
            user_data['watchlist'].remove(movie)
            add_to_watched(user_data, movie)
            return user_data
    return user_data
    
def get_watched_avg_rating(user_data):
    if len(user_data['watched']) < 1:
        return 0.0
    movie_rating_total = 0
    for movie in user_data['watched']:
        movie_rating_total += movie['rating']
    return movie_rating_total / len(user_data['watched'])    

def get_most_watched_genre(user_data):
    movie_genre_dictionary = {}
    if len(user_data['watched']) < 1:
        return None
    for movie in user_data['watched']:
        if movie['genre'] not in movie_genre_dictionary.keys():
            movie_genre_dictionary[movie['genre']] = 1 

        else:
            movie_genre_dictionary[movie['genre']] += 1

    most_watched = sorted(movie_genre_dictionary, key=movie_genre_dictionary.get)
    return most_watched[-1]  
   
def get_unique_watched(user_data):
    user_movie_list = []
    friends_movie_list = []
    unique_list = []
    for movie in user_data['watched']:
        user_movie_list.append(movie['title'])

    for friend in user_data['friends']:
        for title in friend['watched']:
            friends_movie_list.append(title['title'])

    for m in user_movie_list:
        if m not in friends_movie_list:
            unique_list.append({'title': m })

    return unique_list


def get_friends_unique_watched(user_data):
    user_movie_list = []
    friends_movie_list = []
    unique_list = []
    for movie in user_data['watched']:
        user_movie_list.append(movie['title'])

    for friend in user_data['friends']:
        for title in friend['watched']:
            friends_movie_list.append(title['title'])
            
    for m in friends_movie_list:
        if m not in user_movie_list:
            if {'title': m } not in unique_list:
                unique_list.append({'title': m })
            else:
                continue
            
    return unique_list

def get_available_recs(user_data):
    recommended_movies = []
    user_subscriptions = user_data['subscriptions']
    user_watched = user_data['watched']
    potential_list = []
    
    for item in (user_data['friends']):
        for i in item['watched']:
            potential_list.append(i)
                
    for item in potential_list:
        if item['host'] in user_subscriptions:
            if item not in recommended_movies:
                recommended_movies.append(item)

    return recommended_movies

def get_new_rec_by_genre(user_data):
    recs_by_genre_list = []
    potential_list = []      
    genre_to_find = get_most_watched_genre(user_data)

    for item in (user_data['friends']):
        for i in item['watched']:
            potential_list.append(i)
    for movie in potential_list:
        if movie['genre'] == genre_to_find:
            recs_by_genre_list.append(movie)
    return recs_by_genre_list

def get_rec_from_favorites(user_data):
    user_fav_movies = []
    recommended_movies = []
    friends_movie_list = []
    # potential_movies = get_friends_unique_watched(user_data)
    for movie in user_data['favorites']:
        user_fav_movies.append(movie)
    
    for friend in user_data['friends']:
        for title in friend['watched']:
            friends_movie_list.append(title['title'])
        
    for movie in user_fav_movies:
        if movie['title'] not in friends_movie_list:
            recommended_movies.append(movie)
    
    return recommended_movies