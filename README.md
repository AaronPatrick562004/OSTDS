# assgn_1_Corona
# Corona-Data-Analytics
This project is a web-based dashboard for analyzing and visualizing COVID-19 data. It utilizes Django for the web framework and Seaborn for creating data visualizations. The dashboard provides several key insights into COVID-19 statistics for the US.

**Features:**
- **Case Fatality Ratio Distribution:** Visualizes the distribution of the case fatality ratio.

- **Correlation Matrix:** Shows the correlation between different numerical variables.

- **Confirmed Cases by Province/State:** Displays the number of confirmed cases per province/state.

- **Recovery Rates by Province/State:** Illustrates the recovery rates per province/state.

- **Active Cases Trends Over Time:** Tracks the trends of active cases over time.

**Requirements:**
To run this project locally, you'll need the following installed:

Django>=3.0 </br>
pandas>=1.0 </br>
matplotlib>=3.0 </br>
seaborn>=0.10 </br>
pillow>=7.0 </br>
numpy>=1.18 </br>
requests>=2.0 </br>
 

```bash
You can install the dependencies by running:
pip install -r requirements.txt
```

 

# assgn_2_jupyter
# La Liga Match Data Scraper & Statistics Tracker
## Overview
This project scrapes football match data from the [FBref](https://fbref.com/en/comps/12/schedule/La-Liga-Scores-and-Fixtures) website for La Liga and analyzes the match results, including scores, team performances, and trends over different seasons.

The scraper gathers key match details like:
- Date and time
- Home and away teams
- Expected Goals (xG)
- Score
- Attendance
- Venue
- Referee information
- Match report links

It then processes the data and generates a visual representation of match results, such as home wins, away wins, and draws.

## Project Files:
- `scraper.py`: Main Python script that scrapes data from the website.
- `la_liga_match_data.json`: The JSON file containing the scraped match data.
- `README.md`: This file that explains the project.
- `requirements.txt`: A list of required Python packages.

## Requirements:
You can install the necessary dependencies by running:
```bash
pip install -r requirements.txt
