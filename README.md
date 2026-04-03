# NBA Stats Scraper

Scrapes the NBA.com stats leaderboard and exports player stats to CSV using BeautifulSoup.

## What It Does

Pulls the top 5 players from each of the 9 stat categories on the NBA stats page (points, rebounds, assists, etc.) and saves them to a CSV file with category headers.

## How It Works

1. Requests the NBA.com/stats page
2. Parses the HTML with BeautifulSoup
3. Extracts player names and stat values from the leaderboard cards
4. Organises them by category
5. Writes to `nba_stats.csv`

## Usage
```
python main.py
```

## Requirements
```
pip install requests beautifulsoup4
```
