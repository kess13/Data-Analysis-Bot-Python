import matplotlib.pyplot as plt
from .retrieve_data import retrieve_data
from io import BytesIO
from pathlib import Path

def generate_graph():
    users = []
    users_data = []

    data = retrieve_data()

    # initialize array with usernames
    for user_data in data:
        users.append(user_data['user'])

    # array with user_data (everything except username)
    for user_data in data:
        users_data.append({
            'weight': user_data['weight'],
            'ppl': user_data['ppl'],
            'liters': user_data['liters'],
            'miles_driven': user_data['miles_driven'],
            'date': user_data['date']
        })

    oil_prices = []
    user_miles_driven = []

    # generate graph values
    for user_data in users_data:
        # generate price spend on oil
        price = user_data['ppl'] * user_data['liters']
        oil_prices.append(price)

        # append miles driven
        user_miles_driven.append(user_data['miles_driven'])

    plt.figure(figsize=(len(users)*2, 10))

    # create graph for oil prices
    plt.subplot(121)
    plt.title('Oil Prices')
    plt.bar(users, oil_prices)

    # create graph for user miles driven
    plt.subplot(122)
    plt.bar(users, user_miles_driven)
    plt.title('User miles driven')

    # save graph as .png file
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    file_path = Path("data.png")

    with file_path.open('wb') as file:
        file.write(buffer.getvalue())
        print("[*] Successfully generated graph and saved it as file.")

    return str(file_path)
