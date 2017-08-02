# NOT TYLER'S CODE

def answer(xs):
  negative_numbers = []
  positive_numbers = []
  for item in xs:
    if int(item) < 0:
      negative_numbers.append(int(item))
      continue
    positive_numbers.append(int(item))



  if len(negative_numbers) % 2 != 0:
    negative_numbers = sorted(negative_numbers)[:-1]

  all_numbers = positive_numbers + negative_numbers
  power = 1
  for number in all_numbers:
    if number == 0:
      continue
    power = power * number

  return str(power)