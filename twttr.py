def main():
    user_input = input("Input: ").strip()
    vowels(user_input)
    
def vowels(main_input):
    vowel_list = ["a", "i", "u", "e", "o"]
    for j in vowel_list:
        main_input = main_input.casefold().replace(j, "")
            
    print(f"Output: {main_input}", end="")
    
    
if __name__ == "__main__":
    main()