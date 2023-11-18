import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

def read_dataset(path):
    '''Takes the path of a dataset csv file as input, and returns it read as a Pandas dataframe'''
    music_lifestyle_df = pd.read_csv(path)
    #print(music_lifestyle_df)
    return(music_lifestyle_df)

def normalise_dataset(df):
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
        responders_tastes[responder] = responders_tastes[responder].split(",")
    
    print(responders_tastes)

    #Call genre_query function

    #Get rid of all original music columns in the dataframe and replace with a new one, music_taste, 


    pass

def genre_query(id):
    '''Query a Spotify ID and return a list of its corresponding genres'''

    pass

def main():
    #Hobbies and weekend_activities were manually normalised using the categories outlined here: https://owaves.com/faqs/what-are-the-activity-categories/
    #Music-related columns were also normalised manually, first by converting responders' song choices to their corresponding artists, then getting their IDs from the Spotify web app
    dataset_path = r"C:\Users\Omotara Edu\CTAClasses\Creative Code\Assignment04_DataAmongUs\data\music_and_lifestyle_data.csv"
    df = read_dataset(dataset_path)
    normalise_dataset(df)
    pass

if __name__ == '__main__':
    main()