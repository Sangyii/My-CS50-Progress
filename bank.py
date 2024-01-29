def main():
    main_input = input("Greeting: ").strip()
    provoke(main_input)
    
    
def provoke(greet):
    if greet.casefold()[0] == 'h' and greet.casefold() == 'hello'.casefold() or 'hello' in greet.casefold():
        print("$0")
    elif greet.casefold()[0] == 'h':
        print("$20")
    else:
        print("$100")


main()