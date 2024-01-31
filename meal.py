def main():
    main_input = input("What time is it? ").strip()
    convert(main_input)
    
    hours, minutes = convert(main_input).split(".")
    hours = int(hours)
    minutes = int(minutes)
    
    if 7 <= hours < 8 and 0 <= minutes < 100 or hours == 8 and minutes == 0:
        print("Breakfast Time")
    elif 12 <= hours < 13 and 0 <= minutes < 100 or hours == 13 and minutes == 0:
        print("Lunch Time")
    elif 18 <= hours < 19 and 0 <= minutes < 100 or hours == 19 and minutes == 0:
        print("Dinner Time")
    else:
        print()       
    

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    
    minutes = round(float(minutes / 60), 2)
    time_check = float(hours + minutes)
    
    return str(time_check)
    

if __name__ == "__main__":
    main()