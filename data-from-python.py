

# Open the CSV file
with open("data.csv", "r") as file:
    lines = file.readlines()
    # Extract the data from the lines 
    data = []
    for line in lines:
        values = line.strip().split(",")
        data.append(values)
for row in data[:5]:
    print(row)

    
#output:
# ['name', 'age', 'city']
# ['Alice', '24', 'NewYork']
# ['John', '32', 'Los Angeles']
# ['Micheal', '44', 'Chicago']
