def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    max_length = 6
    min_length = 2
    banned_list = [".", " ", ",", "?", ";", ":", "\"", "'", "-", "[", "]", "{", "}", "(", ")", "!", "<", ">", "/", "*", "&", "#", "\\", "~", "@", "^", "|"]
    
    for i in banned_list:
        if min_length <= len(s) <= max_length and i not in s:
            character_plate = s[:min_length].casefold()
            if character_plate.isalpha() and i not in character_plate:
                number_plate = s[min_length:len(s)].casefold()
                if number_plate[-1].isdigit() and number_plate[0] != "0" and i not in number_plate:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
        
main()