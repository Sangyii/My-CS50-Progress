def main():
    my_input = input("What is the answer to the great question of life, the universe, and everything? ").strip()
    thinking(my_input)
    
    
def thinking(inputs):
        if inputs == "42" or inputs.casefold() == "forty two" or inputs.casefold() == "forty-two":
            print("Yes")
        else:
            print("No")

main()