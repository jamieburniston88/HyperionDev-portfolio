# Function to calculate the average radiation levels for each location in the data
def calculate_average(data_list):
    averages = []
    for location_data in data_list:
        location = location_data[0]
        radiation_levels = location_data[1:] # Extracting radiation levels for each location
        avg = sum(radiation_levels) / len(radiation_levels) # Calculating average
        averages.append((location, avg)) # Storing location and its average
    return averages


data =[
    ['city centre', 22, 19, 20, 31, 28],
    ['industrial zone', 35, 32, 30, 37, 40],
    ['residentail district', 15, 12, 18, 20, 14],
    ['rural outskirts', 9, 13, 16, 14, 7],
    ['downtown', 25, 18, 22, 21, 26]
]

# Continuous loop to take user input for new locations and their radiation levels
while True:
    try:
        # Getting location input from the user
        location = input("Enter new location (or 'stop' to finish): ")
        if location.lower() == 'stop':
            break # Break the loop if user inputs 'stop'
            
        try:
            # Getting radiation levels input from the user
            radiation_levels_input = input("Enter radiation levels separated by a space: ")
            if radiation_levels_input.lower() == 'stop':
                break
            radiation_levels = [int(level) for level in radiation_levels_input.split()] # Converting input to integers
            
            
            data.append([location] + radiation_levels)
            print("Updated data: ", data)
        
        except ValueError:
            print("Invalid input for radiation levels. Please enter numeric values.")
        
    except KeyboardInterrupt:
        print("\nOperation interrupted. Exiting...")
        break # Break the loop if user interrupts with KeyboardInterrupt (Ctrl+C)

    
    averages = calculate_average(data)
    
 # Creating a list with the averages and appending it to the final data   
for loc, avg in averages:
    print(f"Average radiation level in {loc}: {avg}")
    

    


