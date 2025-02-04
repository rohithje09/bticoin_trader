import requests
import pandas as pd

def fetch_bitcoin_options():
    # Endpoint to fetch Bitcoin options data from Deribit
    url = "https://www.deribit.com/api/v2/public/get_instruments"
    params = {"currency": "BTC", "kind": "option"}
    response = requests.get(url, params=params)
    data = response.json()

    # Extract the relevant options data
    options_data = data['result']

    # Convert to a DataFrame
    options_df = pd.DataFrame(options_data)

    # Display the data or save it to a CSV
    options_df.to_csv('bitcoin_options_data.csv', index=False)
    return options_df

if __name__ == '__main__':
    fetch_bitcoin_options()
