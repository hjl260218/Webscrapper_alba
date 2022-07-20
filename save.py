import csv

def save(brand,jobs):
    file = open(f"{brand}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for job in jobs:
      writer.writerow(list(job.values()))
    return
  


  