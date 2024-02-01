def main():
    main_input = input(str("What time is it? ")).strip()
    convert(main_input)
    
    if "a.m." in main_input or "p.m." in main_input:
        hours, the_time = convert(main_input)
        hours, minutes = hours.split(".")
        hours = int(hours)
        minutes = int(minutes)
        the_time = str(the_time)
        
        if 7 <= hours < 8 and 0 <= minutes < 100 or hours == 8 and minutes == 0:
            if the_time == "am":
                print("Breakfast Time")
            else:
                print()
        elif hours == 12 and 0 <= minutes < 100 or hours == 1 and minutes == 0:
            if the_time == "pm":
                print("Lunch Time")
            else:
                print()
        elif hours == 6 and 0 <= minutes < 100 or hours == 7 and minutes == 0:
            if the_time == "pm":
                print("Dinner Time")
            else:
                print()
        else:
            print()     
    
    elif "a.m." not in main_input or "p.m." not in main_input:
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
    if "a.m." in time or "p.m." in time:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes, time_statement = minutes.replace(".", "").split()
        time_statement = str(time_statement)
        minutes = int(minutes)
    
        minutes = round(float(minutes / 60), 2)
        time_check = float(hours + minutes)
        return str(time_check), str(time_statement)
    
    elif "a.m." not in time or "p.m." not in time:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)
    
        minutes = round(float(minutes / 60), 2)
        time_check = float(hours + minutes)
        return str(time_check)
        

if __name__ == "__main__":
    main()