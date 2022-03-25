import csv

rows = []

with open("data.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
planet_data_rows = rows[1:]

below_44 = ['Stars have less than 44 light years distance']
above_44 = ['Stars have greater than 44 light years distance']

for planet_data in planet_data_rows:
  distance = float(planet_data[2])
  if distance < 44:
    below_44.append(planet_data[1])
  elif distance > 44:
    above_44.append(planet_data[1])

f = open("star_distances.csv", "w")

for i in range(len(below_44)):
    f.write("{} , {}\n".format(below_44[i], above_44[i]))

f.close()