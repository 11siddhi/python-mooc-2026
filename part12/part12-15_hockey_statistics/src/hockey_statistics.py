# Write your solution here
import json

class HockeyStats:
  def __init__(self, filename: str):
    self.data = self.__open_file(filename)
  
  def __open_file(self, json_file):
    with open(json_file) as my_file:
      data = my_file.read()
    return json.loads(data)
  
  def _get_players(self):
    return {player["name"]: n for n, player in enumerate(self.data)}

  def __get_players_teams(self):
    return {player["name"]: player["team"] for player in self.data}
  
  def __get_players_country(self):
    return {player["name"]: player["nationality"] for player in self.data}

  def __sort_by_points(self, players_list: list=None):
    def points_order(player):
      return (player["goals"] + player["assists"], player["goals"])
    if players_list is None:
      players_data = self.data
    else:
      players_data = [player for player in self.data if player["name"] in players_list]
    return sorted(players_data, key=points_order, reverse=True)

  def __sort_by_goals(self, players_list: list=None):
    def goals_order(player):
      return (-player["goals"], player["games"])
    if players_list is None:
      players_data = self.data
    else:
      players_data = [player for player in self.data if player["name"] in players_list]
    return sorted(players_data, key=goals_order)

  def __format_print(self, player_num):
    player = self.data[player_num]
    print(f"{player['name']:20} {player['team']:4} {player['goals']:2} + {player['assists']:2} = {player['goals'] + player['assists']:>3}")

  def search_player(self, name: str):
    player_dict = self._get_players()
    if name not in player_dict:
      return None
    self.__format_print(player_dict[name])

  def all_teams(self):
    teams_dict = self.__get_players_teams()
    return sorted(set((teams_dict.values())))
  
  def all_countries(self):
    countries_dict = self.__get_players_country()
    return sorted(set(countries_dict.values()))

  def players_from_team(self, team_name):
    teams_dict = self.__get_players_teams()
    if team_name not in teams_dict.values():
      return None
    players = [player for player, team in teams_dict.items() if team == team_name]
    orderd_players = self.__sort_by_points(players)
    for player in orderd_players:
      self.search_player(player["name"])
  
  def players_from_country(self, country_name):
    countries_dict = self.__get_players_country()
    if country_name not in countries_dict.values():
      return None
    players = [player for player, team in countries_dict.items() if team == country_name]
    orderd_players = self.__sort_by_points(players)
    for player in orderd_players:
      self.search_player(player["name"])

  def most_points(self, num: int):
    sorted_players = self.__sort_by_points()
    for i, player in enumerate(sorted_players):
      if i == num:
        break
      self.search_player(player["name"])
    
  def most_goals(self, num: int):
    sorted_players = self.__sort_by_goals()
    for i, player in enumerate(sorted_players):
      if i == num:
        break
      self.search_player(player["name"])

# Main application
class HockeyStatsApplication:
  def __init__(self):
    self.__filename = self.__get_filename()
    self.__hockey_stats = HockeyStats(self.__filename)

  def __help(self):
    commands = """
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals"""
    print(commands)

  def __get_filename(self):
    filename = input("file name: ")
    return filename

  def __print_total_players(self):
    total_players = len(self.__hockey_stats._get_players())
    print(f"read the data of {total_players} players")

  def execute(self):
    self.__print_total_players()
    print("")
    self.__help()

    while True:
      print("")
      cmd = input("command: ")
      if cmd == "0":
        break
      elif cmd == "1":
        pname = input("name: ")
        self.__hockey_stats.search_player(pname)

      elif cmd == "2":
        teams = self.__hockey_stats.all_teams()
        for team in teams:
          print(team)

      elif cmd == "3":
        countries = self.__hockey_stats.all_countries()
        for country in countries:
          print(country)

      elif cmd == "4":
        team_name = input("team: ")
        print("")
        self.__hockey_stats.players_from_team(team_name)

      elif cmd == "5":
        country_name = input("country: ")
        print("")
        self.__hockey_stats.players_from_country(country_name)

      elif cmd == "6":
        num = int(input("how many: "))
        print("")
        self.__hockey_stats.most_points(num)

      elif cmd == "7":
        num = int(input("how many: "))
        print("")
        self.__hockey_stats.most_goals(num)

      else:
        self.__help()


app = HockeyStatsApplication()
app.execute()