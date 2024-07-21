import requests
from bs4 import BeautifulSoup

website = "https://www.nba.com/stats"

access = requests.get(url=website)
html_doc = access.text

soup = BeautifulSoup(html_doc, 'html.parser')

player_stats_import = soup.find_all("a",{"class":"LeaderBoardPlayerCard_lbpcTableLink__MDNgL"})
all_player_stats = [x.getText() for x in player_stats_import]


titles_import = soup.find_all("h2", {"class": "LeaderBoardCard_lbcTitle___WI9J"})
titles = [i.getText() for i in titles_import]


all_section_stats = []
step = 0
while step < 9:
    step += 1
    section_stats = []
    i = 0
    while i < 10:
        section_stats.append(all_player_stats[i])
        i += 1
    all_section_stats.append(section_stats)
    del all_player_stats[0:10]
print(all_section_stats)




