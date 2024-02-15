import requests
import json


API_KEY = 'your_steam_api_key'
STEAM_ID = 'your_steam_id'
ignored_steam_ids = ['123456789', '123456789']  # Replace this with actual Steam IDs to not delete
base_url = f'https://api.steampowered.com/ISteamUser/GetFriendList/v1/?key={API_KEY}&steamid={STEAM_ID}&relationship=friend'

def delete_friend(friend_id):
    if friend_id in ignored_steam_ids:
        print(f'Friend with ID {friend_id} is ignored and will not be removed.')
        return
    url = f'https://api.steampowered.com/ISteamUser/RemoveFriend/v1/?key={API_KEY}&steamid={STEAM_ID}&friendsteamid={friend_id}'
    response = requests.post(url)
    if response.status_code == 200:
        print(f'Friend with ID {friend_id} has been removed.')
    else:
        print(f'Error removing friend with ID {friend_id}. Response: {response.status_code} {response.reason}')

def main():
    global STEAM_ID
    global API_KEY

    response = requests.get(base_url)
    if response.status_code == 200:
        friends_list = json.loads(response.text)['friendslist']['friends']
        for friend in friends_list:
            friend_id = friend['steamid']
            delete_friend(friend_id)
    else:
        print(f'Error fetching friends list. Response: {response.status_code} {response.reason}')

if __name__ == '__main__':
    main()
