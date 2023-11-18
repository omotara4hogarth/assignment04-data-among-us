#from data_processing import normalise_dataset, read_dataset
import pandas as pd
import matplotlib.pyplot as plt
import ast

dataset_path = r"C:\Users\Omotara Edu\CTAClasses\Creative Code\Assignment04_DataAmongUs\data\prepared_music_lifestyle_data.csv"

music_and_lifestyle_df = pd.read_csv(dataset_path)

all_our_genres = []

#Overwrite values in music_taste column from str type, to list
music_and_lifestyle_df['music_taste'] = [ast.literal_eval(row_str) for row_str in music_and_lifestyle_df['music_taste']]

#Get a list of all our genres
for row in music_and_lifestyle_df['music_taste']:
    for each_genre in row:
        if each_genre not in all_our_genres:
            all_our_genres.append(each_genre)

def most_pop_genres_amongst_subset(subset_column):
    all_subset = []

    for subset_item in music_and_lifestyle_df[subset_column]:
        if subset_item not in all_subset:
            all_subset.append(subset_item)

    most_common_genre_per_subset_item = {}

    for subset_item in all_subset:
        recurrence_of_genres_here = {}
        subset_at_subset_item = music_and_lifestyle_df.loc[music_and_lifestyle_df[subset_column] == subset_item]
        for genre_list in subset_at_subset_item['music_taste']:
            for item in genre_list:
                if item in recurrence_of_genres_here:
                    recurrence_of_genres_here[item] += recurrence_of_genres_here[item]
                else:
                    recurrence_of_genres_here[item] = 1
        max_value = max(recurrence_of_genres_here.values())
        max_key = [key for key in recurrence_of_genres_here if recurrence_of_genres_here[key] == max_value]
        most_common_genre_per_subset_item[subset_item] = max_key

    return most_common_genre_per_subset_item

def main():

    #Which music genres are most common in the different areas of London?
    most_common_genre_per_london_zone = most_pop_genres_amongst_subset('london_address')

    print("\n\nThe most common music genres amongst CTA'ers in each London zone are the following:\n")
    for key in most_common_genre_per_london_zone: 
        print(f"In {key}, people tend to listen to {most_common_genre_per_london_zone[key]}.\n")

    #Which music genres are most common amongst people from different parts of the world?
    most_common_genre_worldwide = most_pop_genres_amongst_subset('home')

    print("\n\nThe most common genres amongst CTA'ers from different parts of the world are:\n")
    for key in most_common_genre_worldwide: 
        print(f"With people from {key}, their music taste tends to include these genres {most_common_genre_worldwide[key]}.\n")

    #Which music genres are most common amongst people with different hobbies/weekend_activities?
    all_hobbies = []

    for str_of_hobbies in music_and_lifestyle_df['hobbies_activities']:
        list_of_hobbies = str_of_hobbies.split(", ")
        for hobby in list_of_hobbies:
            if hobby not in all_hobbies:
                all_hobbies.append(hobby)

    most_common_genre_per_hobby = {}

    for hobby in all_hobbies:
        recurrence_of_genres_here = {}
        subset_with_hobby = music_and_lifestyle_df.loc[music_and_lifestyle_df['hobbies_activities'].str.contains(hobby) == True]
        for genre_list in subset_with_hobby['music_taste']:
            for item in genre_list:
                if item in recurrence_of_genres_here:
                    recurrence_of_genres_here[item] += recurrence_of_genres_here[item]
                else:
                    recurrence_of_genres_here[item] = 1
        max_value = max(recurrence_of_genres_here.values())
        max_key = [key for key in recurrence_of_genres_here if recurrence_of_genres_here[key] == max_value]
        most_common_genre_per_hobby[hobby] = max_key

    print("\n\nThe most common genres amongst CTA'ers with different hobbies are:\n")
    for key in most_common_genre_per_hobby: 
        print(f"Amongst people whose hobbies fall under the '{key}' category, their music taste tends to include these genres {most_common_genre_per_hobby[key]}.\n")

    #Get dataset mapping genre against hobbies
    data = []
    for genre in all_our_genres:
        genre_dict = {'genre': genre}
        hobby_count = 0
        subset_with_genre = music_and_lifestyle_df[music_and_lifestyle_df['music_taste'].apply(lambda x: genre in x)]
        for hobby in all_hobbies:
            subset_with_genre_and_hobby = subset_with_genre.loc[subset_with_genre['hobbies_activities'].str.contains(hobby) == True]
            #print(f"Subset who like {genre} and {hobby} is: {subset_with_genre_and_hobby}")
            hobby_count = subset_with_genre_and_hobby.shape[0]
            genre_dict[hobby] = hobby_count
        data.append(genre_dict)

    print(f"This is our data on hobbies and genre similarity {data}")
    #Which hobbies/weekend_activities have the most correlation with music taste? (Visualised using heatmap)

    #What about social_media against music_taste? (Heatmap)

    #Social_media against hobbies/weekend_activities? (Heatmap)
    pass

if __name__ == '__main__':
    main()