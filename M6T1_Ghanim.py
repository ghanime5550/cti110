# CTI-110
# Converts kilometers to miles
# Eihab Ghanim
# 10/26/2017

# Converting kilometers to miles.
CONVERSION_FACTOR = 0.6214

# The distance in kilometers.
def main():
    kilometers = float (input('Enter a distance in kilometers: '))
    show_miles(kilometers)

def show_miles (km):
    miles = km * CONVERSION_FACTOR
    # Display the miles
    print(km, 'kilometers equales',miles, 'miles.')

main()
