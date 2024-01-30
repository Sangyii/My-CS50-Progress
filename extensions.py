def main():
    main_input = input("File name: ").strip()
    extension(main_input)
    
    
def extension(name = "application/octet-stream"):
    
    if '.gif' in name.casefold():
        print("image" , "gif", sep="/")
    elif '.jpg' in name.casefold():
        print("image" , "jpg", sep="/")
    elif '.jpeg' in name.casefold():
        print("image" , "jpeg", sep="/")
    elif '.png' in name.casefold():
        print("image" , "png", sep="/")
    elif '.pdf' in name.casefold():
        print("application" , "pdf", sep="/")
    elif '.txt' in name.casefold():
        print("text" , "txt", sep="/")
    elif '.zip' in name.casefold():
        print("application" , "zip", sep="/")                    
    else:
        print("application/octet-stream")
    
    
main()