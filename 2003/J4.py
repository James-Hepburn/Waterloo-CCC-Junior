def get_syllable (word):
  word = word.lower()
  syllable = ""
  found_vowel = False
  for i in word:
    if i in "aeiou":
      found_vowel = True
      syllable = i
    elif found_vowel:
      syllable += i
  if not found_vowel:
    return word
  return syllable
      
def identify_poem ():
  line1 = get_syllable (input().split()[-1])
  line2 = get_syllable (input().split()[-1])
  line3 = get_syllable (input().split()[-1])
  line4 = get_syllable (input().split()[-1])
  if line1 == line2 == line3 == line4:
    return "perfect"
  elif line1 == line2 and line3 == line4:
    return "even"
  elif line1 == line3 and line2 == line4:
    return "cross"
  elif line1 == line4 and line2 == line3:
    return "shell"
  return "free"

N = int (input())

for i in range (N):
  print (identify_poem ())
