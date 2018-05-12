import csv

data =  [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("list.csv", "w") as csvtest:
    csv_writer = csv.writer(csvtest, delimiter=",")
    for datam in data:
       csv_writer.writerow(datam)
    csv_writer.writerow(["1","2","3"])
