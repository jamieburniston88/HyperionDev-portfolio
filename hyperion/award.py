#def defines function in the code
def calculate_triathlon_time():
#float converts the specified value into a floating point number
#Input times for the swimming, cycling and running
    Swim_time = float(input("Enter swimming time(minutes): "))
    cycle_time = float(input("Enter cycling time(minutes): "))
    run_time = float(input("Enter running time(minutes): "))
    
    #calculate total time
    total_time = Swim_time + cycle_time + run_time
    #return function exits the function and returns a value
    return total_time
# program looks through the conditions and returns an outcome  
def determine_award(total_time):
    if total_time <= 100:
        return "provincial Colours"
    elif 100 < total_time <= 105:
        return "Provincial Half Colours"
    elif 105 < total_time <= 110:
        return "Provincial Scroll"
    else:
        return "No Award"
#The dunbar name helps python assign a different value depending on how its containing script executes
if __name__=="__main__":
    print("Welcome to the Triathlon Awards Calculator!")
    triathlon_time = calculate_triathlon_time()
    award = determine_award(triathlon_time)
    print(f"The total time taken for the triathlon is: {triathlon_time}minutes")
    print(f"The award for this participant is: {award}")