def main():
    my_input = input("What is the answer to the great question of life, the universe, and everything? ")
    thinking(my_input)
    
    
def thinking(inputs):
        if inputs == "42" or inputs == "forty two" or inputs == "forty-two":
            print("Yes")
        else:
            print("No")

main()