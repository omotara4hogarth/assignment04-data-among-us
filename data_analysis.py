import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def read_dataset(path):
    music_lifestyle_df = pd.read_csv(path)
    print(music_lifestyle_df)
    return(music_lifestyle_df)

def normalise_dataset(df):
    #Normalise hobbies and weekend_activities using the categories outlined here: https://owaves.com/faqs/what-are-the-activity-categories/

    #Normalising 'home' to the first string (in most cases this is a city)

    #Normalising postcode to the zone (drop all characters including and after the first number)

    #Create a list from the social_media responses by creating a new list item at each comma

    #


    pass

def main():
    dataset_path = r"C:\Users\Omotara Edu\CTAClasses\Creative Code\Assignment04_DataAmongUs\data\music_and_lifestyle_data.csv"
    read_dataset(dataset_path)
    pass

if __name__ == '__main__':
    main()