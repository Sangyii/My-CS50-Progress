def main():
    user_input = input("Input: ").strip()
    vowels(user_input)
    
def vowels(main_input):
    vowel_list = ["a", "i", "u", "e", "o"]
    vowel_list_case = [j for j in vowel_list] + [j.upper() for j in vowel_list]
    for j in vowel_list_case:
        main_input = main_input.replace(j, "")
            
    print(f"Output: {main_input}", end="")
    
    
if __name__ == "__main__":
    main()