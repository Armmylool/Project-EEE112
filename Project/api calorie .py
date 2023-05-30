import requests

url = 'https://api.calorieninjas.com/v1/nutrition?query='
user_input = input('What do you want to eat: ')
response = requests.get(url + user_input, headers={'X-Api-Key': '/nj5rHE+RtwdIlzmHgDitA==XuMT6lysDbY4Zmlb'})

if response.status_code == requests.codes.ok:
    data = response.json()
    if 'items' in data and len(data['items']) > 0:
        item = data['items'][0]
        serving_size = item['serving_size_g']
        calories = item['calories']
        sugar = item['sugar_g']
        fat = item['fat_total_g']
        sodium = item['sodium_mg']
        carbohydrate = item['carbohydrates_total_g']
        
        print(f"Food: {user_input}")
        print(f"Serving Size: {serving_size}g")
        print(f"Calories per Serving: {calories}")
        print(f"Sugar per Serving: {sugar}g")
        print(f"Fat per Serving: {fat}g")
        print(f"Sodium per Serving: {sodium}mg")
        print(f"Carbohydrate per Serving: {carbohydrate}g")
    else:
        print("No information available for the specified food.")
else:
    print("English only")