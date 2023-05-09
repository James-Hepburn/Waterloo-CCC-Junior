p1_cards = []
p2_cards = []
cards = []

for i in range (26):
  p1_cards.append (input())
  p2_cards.append (input())
  cards.append (p1_cards[-1])
  cards.append (p2_cards[-1])
  
high_cards = ["ace", "king", "queen", "jack"]
p1 = 0
p2 = 0

for i in range (52):
  if i % 2 == 0:
    if p1_cards[i // 2] == "ace" and i <= 47:
      if cards[i+1] not in high_cards and cards[i+2] not in high_cards and cards[i+3] not in high_cards and cards[i+4] not in high_cards:
        print ("Player A scores 4 point(s).")
        p1 += 4
    elif p1_cards[i // 2] == "king" and i <= 48:
      if cards[i+1] not in high_cards and cards[i+2] not in high_cards and cards[i+3] not in high_cards:
        print ("Player A scores 3 point(s).")
        p1 += 3 
    elif p1_cards[i // 2] == "queen" and i <= 49:
      if cards[i+1] not in high_cards and cards[i+2] not in high_cards:
        print ("Player A scores 2 point(s).")
        p1 += 2 
    elif p1_cards[i // 2] == "jack" and i <= 50:
      if cards[i+1] not in high_cards:
        print ("Player A scores 1 point(s).")
        p1 += 1
  else:
    if p2_cards[i // 2] == "ace" and i <= 47:
      if cards[i+1] not in high_cards and cards[i+2] not in high_cards and cards[i+3] not in high_cards and cards[i+4] not in high_cards:
        print ("Player B scores 4 point(s).")
        p2 += 4
    elif p2_cards[i // 2] == "king" and i <= 48:
      if cards[i+1] not in high_cards and cards[i+2] not in high_cards and cards[i+3] not in high_cards:
        print ("Player B scores 3 point(s).")
        p2 += 3 
    elif p2_cards[i // 2] == "queen" and i <= 49:
      if cards[i+1] not in high_cards and cards[i+2] not in high_cards:
        print ("Player B scores 2 point(s).")
        p2 += 2 
    elif p2_cards[i // 2] == "jack" and i <= 50:
      if cards[i+1] not in high_cards:
        print ("Player B scores 1 point(s).")
        p2 += 1
  
print ("Player A:", p1, "point(s).") 
print ("Player B:", p2, "point(s).") 
