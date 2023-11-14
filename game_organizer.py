import requests
import config

def make_game(player1=config.player1,player2=config.player2, template=config.templates, gameName="Title", description="A game"):
    # The API endpoint to communicate with
    url_post = "https://www.warzone.com/API/CreateGame"
    # request body
    new_data = \
        {
            "hostEmail": config.mail,
            "hostAPIToken": config.api_key,
            "templateID": template,
            "gameName": gameName,
            "personalMessage": description,
            "players": [
                {"token": player1, "team": "None"},
                {"token": player2, "team": "None"}
            ]
        }
    # A POST request to the API
    post_response = requests.post(url_post, json=new_data)
    # Print the response
    post_response_json = post_response.json()

    game_id = str(post_response_json['gameID'])
    return game_id

def check_game(id):
    url = 'https://www.warzone.com/API/GameFeed?GameID=' + id
    payload = 'Email=' + config.mail + '&APIToken=' + config.api_key
    headers = {
        'Content-Type': 'text/plain',
        'Cookie': config.cookie
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

current_games = []
new_game_id = make_game()
print("Game Created: ", new_game_id)
current_games.append(new_game_id)

check_game(current_games[0])