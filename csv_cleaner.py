import csv

input_file = "data.csv"
output_file = "cleaned_data.csv"

rows = set()

with open(input_file, "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        rows.add(tuple(row))

with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)

    for row in rows:
        writer.writerow(row)

print("Duplicate rows removed. Cleaned file created.")