def main():
    main_input = input("camelCase: ").strip()
    camel_case(main_input)
    
    
def camel_case(the_input):
    for i in range (len(the_input)):
        while the_input[i].isupper():
            lowercase = the_input[i].lower()
            the_input = the_input[:i] + '_' + lowercase + the_input[i + 1:]
            
    print(f"snake_case: {the_input}", end="")


main()