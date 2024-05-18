city_rainfall = {}
def rain_fall():
    while True:
        city = input('Enter city name: ').strip()
        if not city:
            break

        rainfall = input('Enter rainfall: ').strip()
        if rainfall.isdigit():
            rainfall = int(rainfall)
        else:
            print('Rainfall should be a number, try again.')
            continue

        if city in city_rainfall:
            city_rainfall[city] += rainfall
        else:
            city_rainfall[city] = rainfall
    for city, rainfall in city_rainfall.items():
        print(f'{city}: {rainfall}')

if __name__ == '__main__':
    rain_fall()  