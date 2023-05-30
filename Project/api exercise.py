import requests

activity = 'skiing'
api_url = 'https://api.api-ninjas.com/v1/caloriesburned?activity={}'.format(activity)
response = requests.get(api_url, headers={'X-Api-Key': '/nj5rHE+RtwdIlzmHgDitA==25nG7trAOneV3LZy'})
if response.status_code == requests.codes.ok:
    with open('calories_data.txt', 'w') as file:
        data = response.json()
        for item in data:
            file.write(str(item) + '\n')
    print("Data saved successfully.")
else:
    print("Error:", response.status_code, response.text)
