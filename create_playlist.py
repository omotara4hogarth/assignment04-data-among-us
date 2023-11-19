from dotenv import load_dotenv
from requests import post, get
from data_processing import get_spotify_token, get_auth_header
import os, base64, json

def create_playlist(header, user_id):
    '''Create a Spotify playlist'''
    header["Content-Type"] = "application/json"
    print(header)
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    body = {"name": "CTA2 Playlist",
            "description": "CTA2 on decks",
            "public": False}
    result = post(url, headers=header, data=body)
    json_result = json.loads(result.content)
    print(json_result)
    playlist_id = ''
    return playlist_id

def genre_query(id, header):
    '''Search Spotify genres and add corresponding songs to a playlist'''
    url = f"https://api.spotify.com/v1/artists/{id}"
    

    result = get(url, headers=header)
    json_result = json.loads(result.content)

    genres = json_result["genres"]
    return genres, result

def main():
    token = get_spotify_token()
    user_id = 'pseudo2014'
    header = get_auth_header(token)
    #create_playlist(header, user_id)
    pass

if __name__ == '__main__':
    main()