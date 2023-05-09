def get_suit (start, end, cards):
  suit = []
  start_index = cards.index (start)
  end_index = cards.index (end)
  for i in range (start_index + 1, end_index):
    suit.append (cards[i])
  return suit

def get_points (suit, values):
  points = 0
  for i in suit:
    if i in values:
      points += values[i]
  if len (suit) in values:
    points += values[len (suit)]
  return points 

cards = input()

clubs = get_suit ("C", "D", cards)
diamonds = get_suit ("D", "H", cards)
hearts = get_suit ("H", "S", cards)
spades = get_suit ("S", "*", cards + "*")

values = {"A":4, "K":3, "Q":2, "J":1, 0:3, 1:2, 2:1}

c_points = get_points (clubs, values)
d_points = get_points (diamonds, values)
h_points = get_points (hearts, values)
s_points = get_points (spades, values)
total = c_points + d_points + h_points + s_points

print ("Cards Dealt Points")
print ("Clubs " + " ".join (clubs) + " " + str (c_points))
print ("Diamonds " + " ".join (diamonds) + " " + str (d_points))
print ("Hearts " + " ".join (hearts) + " " + str (h_points))
print ("Spades " + " ".join (spades) + " " + str (s_points))
print ("Total " + str (total))
