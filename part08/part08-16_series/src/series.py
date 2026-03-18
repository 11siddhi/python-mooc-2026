# Write your solution here:
class Series:
  def __init__(self, title: str, seasons: int, genre: list):
    self.title = title
    self.seasons = seasons
    self.genre = genre 
    self.rates_list = []
    self.avg_rate = 0
  
  def __str__(self):
    about_series = f"{self.title} ({self.seasons} seasons)"
    genre_str = "genres: " + ", ".join(self.genre)
    if self.rates_list:
      total_reviews = len(self.rates_list)
      rate = f"{total_reviews} ratings, average {self.avg_rate:.1f} points"
    else:
      rate = "no ratings"
    return f"{about_series}\n{genre_str}\n{rate}"
  
  # adding reviews
  def rate(self, rating: int):
    self.rates_list.append(rating)
    self.avg_rate = sum(self.rates_list) / len(self.rates_list)

# Searching for series 
def minimum_grade(rating: float, series_list: list):
  result = []
  for series in series_list:
    if series.avg_rate >= rating:
      result.append(series)
  return result

def includes_genre(genre: str, series_list: list):
  result = []
  for series in series_list:
    if genre in series.genre:
      result.append(series) 
  return result
    

if __name__ == "__main__":
  s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
  s1.rate(0)
  s2 = Series("South Park", 24, ["Animation", "Comedy"])

  s3 = Series("Friends", 10, ["Romance", "Comedy"])

  series_list = [s1, s2, s3]

  print(s1.rates_list)
  print("a minimum grade of 4.5:")
  for series in minimum_grade(0, series_list):
    print(series.title)

  print("genre Comedy:")
  for series in includes_genre("Comedy", series_list):
    print(series.title)