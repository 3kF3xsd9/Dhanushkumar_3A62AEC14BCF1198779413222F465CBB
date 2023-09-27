class Player:
  def play(self):
    print("The Player is playing Cricket")
class Batsman(Player):
  def play(self):
   print("The Batsman is Batting")
class Bowler(Player):
  def play(self):
   print("The Bowler is Bowling")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()
