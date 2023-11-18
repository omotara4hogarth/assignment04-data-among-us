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

    print(f"The most common music genres amongst CTA'ers in each London zone are the following:\n\n In East, we have {most_common_genre_per_london_zone['E']}.\n In West, {most_common_genre_per_london_zone['W']}.\n In North, {most_common_genre_per_london_zone['N']}.\n And in South, {most_common_genre_per_london_zone['S']}")

    #Which music genres are most common amongst people from different parts of the world?
    most_common_genre_worldwide = most_pop_genres_amongst_subset('home')

    print(most_common_genre_worldwide.keys())

    #Which music genres are most common amongst people with different hobbies/weekend_activities?

    #Which hobbies/weekend_activities have the most correlation with music taste? (Visualised using heatmap)

    #What about social_media against music_taste? (Heatmap)

    #Social_media against hobbies/weekend_activities? (Heatmap)
    pass

if __name__ == '__main__':
    main()