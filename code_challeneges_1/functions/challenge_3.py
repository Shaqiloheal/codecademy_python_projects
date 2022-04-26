"""Create a function called win_percentage() that takes two parameters named wins and losses.
This function should return out the total percentage of games won by a team based on these two numbers."""

def win_percentage(wins, losses):
  total_games = wins + losses
  win_percentage = (wins / total_games) * 100
  return win_percentage
  
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100