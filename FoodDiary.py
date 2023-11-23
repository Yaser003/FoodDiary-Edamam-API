import requests

def get_nutritional_data(food_name, weight):
    app_id = '3c09bc7e'  # Edamam Application ID
    app_key = 'b018d8336a44b0d9a99527aa57f4d757'  # Edamam Application Key
    url = f"https://api.edamam.com/api/nutrition-data?app_id={app_id}&app_key={app_key}&ingr={weight}%20grams%20of%20{food_name}"
    
    response = requests.get(url)
    data = response.json()

    nutrients = data.get('totalNutrients', {})
    
    fat = nutrients.get('FAT', {}).get('quantity', 0)
    total_carbs = nutrients.get('CHOCDF', {}).get('quantity', 0)
    fiber = nutrients.get('FIBTG', {}).get('quantity', 0)
    sugar = nutrients.get('SUGAR', {}).get('quantity', 0)
    protein = nutrients.get('PROCNT', {}).get('quantity', 0)
    net_carbs = total_carbs - fiber

    return {
        'Fat (g)': fat,
        'Total Carbs (g)': total_carbs,
        'Fiber (g)': fiber,
        'Sugar (g)': sugar,
        'Net Carbs (g)': net_carbs,
        'Protein (g)': protein
    }

def main():
    food_name = input("Enter the name of the food: ")
    weight = input("Enter the weight of the food in grams: ")

    nutrition = get_nutritional_data(food_name, weight)

    print("\nNutritional Information:")
    for key, value in nutrition.items():
        print(f"{key}: {value:.2f} grams")

if __name__ == "__main__":
    main()
#test2

