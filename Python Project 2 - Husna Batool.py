#Project 2: Daily Digest CLI
#Using Random Joke API
import requests
from datetime import datetime

# API URL
API_URL = "https://official-joke-api.appspot.com/random_joke"

#Function to fetch joke from API
def fetch_joke():
    try:
        response = requests.get(API_URL)

        #Check if request is successful
        response.raise_for_status()

        #Convert JSON response into Python dictionary
        joke = response.json()

        return joke
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")
        return None
    except requests.exceptions.HTTPError:
        print("Error: API request failed.")
        return None
    except requests.exceptions.RequestException as e:
        print("An unexpected error occurred:", e)
        return None

#Function to display joke
def display_joke(joke):

    print("\n Daily Digest")

    print("API Name : Random Joke API")
    print("Date     :", datetime.now().strftime("%d-%m-%Y"))
    print()
    print("Setup    :", joke["setup"])
    print("Punchline:", joke["punchline"])

#Function to save report into file
def save_report(joke):

    current_date = datetime.now().strftime("%d-%m-%Y")

    with open("daily_report.txt", "w") as file:

        file.write("========== DAILY REPORT ==========\n\n")
        file.write(f"Current Date : {current_date}\n")
        file.write("API Name     : Random Joke API\n\n")
        file.write("Retrieved Information\n")
        file.write("-------------------------\n")
        file.write(f"Setup     : {joke['setup']}\n")
        file.write(f"Punchline : {joke['punchline']}\n")
    print("\nReport saved successfully as 'daily_report.txt'")
    
def main():
    joke = fetch_joke()

    if joke:
        display_joke(joke)
        save_report(joke)
    else:
        print("Could not retrieve data.")

#Program Starts Here
if __name__ == "__main__":
    main()