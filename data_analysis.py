import pandas as pd
import matplotlib, os, base64, json
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from requests import post, get

def read_dataset(path):
    '''Takes the path of a dataset csv file as input, and returns it read as a Pandas dataframe'''
    music_lifestyle_df = pd.read_csv(path)
    return(music_lifestyle_df)

def normalise_dataset(df):
    '''Normalise all unstandardised data in the dataset ('home', 'london_address', 'social_media' and all music related columns)'''
    clean_music_lifestyle_df = df

    #Normalising 'home' to the first string (in most cases this is a city)
    for row in clean_music_lifestyle_df.home:
        clean_music_lifestyle_df.replace(row, row.split(",")[0], inplace = True)

    #Normalising postcode to the zone (drop all characters including and after the first number)
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    for row in clean_music_lifestyle_df.london_address:
        for char in row[0:3]:
            if char in numbers:
                clean_music_lifestyle_df.replace(row,row.split(char)[0], inplace = True)

    #Create a list from the social_media responses by creating a new list item at each comma
    music_columns = ["turn_up_artist","boogie_artist","sad_artist","commute_artist"]
    responders_tastes = {}
    col_idx = 0
    for column in music_columns:
        i = 0
        for row in clean_music_lifestyle_df[column]:
            if col_idx == 0:
                responders_tastes[i] = str(row)
            else:
                responders_tastes[i] = responders_tastes[i] + "," + str(row)
            i += 1
        col_idx += 1

    for responder in responders_tastes:
        responders_tastes[responder] = responders_tastes[responder].replace(" ", "").split(",")
    
    #Call genre_query function on each list item in the responders_tastes dictionary, and replace the list with a new list of all genres

    for responder in responders_tastes:
        responders_genres = []
        for artist_id in responders_tastes[responder]:
            if artist_id != 'nan' and type(artist_id) != None:
                try:
                    genre_list = genre_query(artist_id)[0]
                except:
                    KeyError
                for genre in genre_list:
                    if genre not in responders_genres:
                        responders_genres.append(genre)
        responders_tastes[responder] = responders_genres

    #Get rid of all original music columns in the dataframe and replace with a new one, music_taste, 
    clean_music_lifestyle_df.drop(columns=music_columns, inplace=True)
    genre_df = pd.DataFrame(index=responders_tastes, columns=['music_taste'])
    for key in responders_tastes:
        genre_df['music_taste'][key] = responders_tastes[key]

    clean_music_lifestyle_df = pd.concat([clean_music_lifestyle_df, genre_df], axis=1)
    return clean_music_lifestyle_df

def get_spotify_token():
    '''Generate a Spotify API token'''
    load_dotenv()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    spot_headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    spot_data = {"grant_type": "client_credentials"}
    result = post(url, headers=spot_headers, data=spot_data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]

    return token

def get_auth_header(token):
    '''Given a token, construct the template header for a Spotify API request'''
    return {"Authorization": "Bearer " + token}

def genre_query(id):
    '''Query a Spotify ID and return a list of its corresponding genres'''
    url = f"https://api.spotify.com/v1/artists/{id}"
    token = get_spotify_token()
    header = get_auth_header(token)

    result = get(url, headers=header)
    json_result = json.loads(result.content)

    genres = json_result["genres"]
    return genres, result

def main():
    #Hobbies and weekend_activities were manually normalised using the categories outlined here: https://owaves.com/faqs/what-are-the-activity-categories/
    #Music-related columns were also normalised manually, first by converting responders' song choices to their corresponding artists, then getting their IDs from the Spotify web app
    dataset_path = r"C:\Users\Omotara Edu\CTAClasses\Creative Code\Assignment04_DataAmongUs\data\music_and_lifestyle_data.csv"
    df = read_dataset(dataset_path)
    normalise_dataset(df)
    pass

if __name__ == '__main__':
    main()