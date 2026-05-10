import requests
from bs4 import BeautifulSoup
import csv

# URL of the website
url = "https://www.scrapethissite.com/pages/forms/"

# 1. Fetch the webpage
response = requests.get(url)

# 2. Create the soup object
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Locate all team containers
# Each team row is inside a <tr> tag
teams = soup.find_all('tr', class_='team')

# 4. Extract data and store it in a list
scraped_data = []

for team in teams:

    # Extract team name
    team_name = team.find('td', class_='name').text.strip()

    # Extract year
    year = team.find('td', class_='year').text.strip()

    # Extract wins
    wins = team.find('td', class_='wins').text.strip()

    # Extract losses
    losses = team.find('td', class_='losses').text.strip()

    # Extract OT losses
    ot_losses = team.find('td', class_='ot-losses').text.strip()

    # Extract win percentage
    win_pct = team.find('td', class_='pct').text.strip()

    # Extract goals for
    goals_for = team.find('td', class_='gf').text.strip()

    # Extract goals against
    goals_against = team.find('td', class_='ga').text.strip()

    # Extract goal difference
    goal_diff = team.find('td', class_='diff').text.strip()

    # Append data as dictionary
    scraped_data.append({
        'Team Name': team_name,
        'Year': year,
        'Wins': wins,
        'Losses': losses,
        'OT Losses': ot_losses,
        'Win %': win_pct,
        'Goals For': goals_for,
        'Goals Against': goals_against,
        'Goal Difference': goal_diff
    })

# 5. Save to CSV file
with open('hockey_teams_dataset.csv', 'w', encoding='utf-8', newline='') as file:

    fieldnames = [
        'Team Name',
        'Year',
        'Wins',
        'Losses',
        'OT Losses',
        'Win %',
        'Goals For',
        'Goals Against',
        'Goal Difference'
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(scraped_data)

print("Data scraped and saved successfully!")