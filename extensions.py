def main():
    main_input = input("File name: ").strip()
    extension(main_input)
    
    
def extension(name = "application/octet-stream"):
    
    if name.casefold().endswith(".gif"):
        print("image", "gif", sep="/")
    elif name.casefold().endswith(".jpg" or ".jpeg"):
        print("image", "jpeg", sep="/")
    elif name.casefold().endswith(".png"):
        print("image", "png", sep="/")
    elif name.casefold().endswith(".pdf"):
        print("application" , "pdf", sep="/")
    elif '.txt' in name.casefold():
        print("text" , "plain", sep="/")
    elif '.zip' in name.casefold():
        print("application" , "zip", sep="/")                    
    else:
        print("application/octet-stream")
    
    
main()
