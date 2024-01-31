def main():
    main_input = input("What time is it? ").strip()
    convert(main_input)

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    
    new_minute = round(float(minutes / 60), 2)
    formatted_minute = round(new_minute * 60, 1)
    
    if 7 <= hours < 8 and 0 <= formatted_minute < 60 or hours == 8 and formatted_minute == 0:
        print("Breakfast Time")
    elif 12 <= hours < 13 and 0 <= formatted_minute < 60 or hours == 13 and formatted_minute == 0:
        print("Lunch Time")
    elif 18 <= hours < 19 and 0 <= formatted_minute < 60 or hours == 19 and formatted_minute == 0:
        print("Dinner Time")
    else:
        print()        
    

if __name__ == "__main__":
    main()