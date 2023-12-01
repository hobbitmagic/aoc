file = open("input.txt", "r")

def check_number(line, position):
  words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  for p in range(len(words)):
    if line.find(words[p], position, len(words[p])+position) != -1:
      return p+1
  return -1

total = 0
for line in file:
  line = line.strip()
  first_number = None
  second_number = None
  for i in range(len(line)):
    char = line[i]
    if char.isdigit():
      second_number = char
      if first_number is None:
        first_number = char
    else:
      word = check_number(line, i)
      if word > 0:
        # print("Found: " + str(word) + " at position " + str(i))
        second_number = word
        if first_number is None:
          first_number = word
  number = str(first_number)  + str(second_number)
  number = int(number)
  print(number)
  total += number 
print(total)

file.close()

