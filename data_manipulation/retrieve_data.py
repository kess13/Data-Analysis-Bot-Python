import pandas as pd

def retrieve_data() -> []:
    """
    this function retrieves the data from the Excel file
    which will be used to create the graph using matplotlib
    :return: array of objects
    """
    df = pd.read_excel('result.xlsx')

    users_data = []

    for index, row in df.iterrows():
        user = row['User']
        weight = row['Weight']
        ppl = row['Price per liter']
        liters = row['Liters']
        miles_driven = row['Miles driven']
        date = row['Date']

        users_data.append({
            'user': user,
            'weight': weight,
            'ppl': ppl,
            'liters': liters,
            'miles_driven': miles_driven,
            'date': date
        })

    return users_data
