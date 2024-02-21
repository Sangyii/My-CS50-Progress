def main():
    main_input = input("Expression: ").strip()
    interpreter(main_input)
    
    
def interpreter(final):
    x, y, z = final.split()
    x = int(x)
    z = int(z)
    
    match y:
        
        case "+":
            print(float(x + z))
        case "-":
            print(float(x - z))
        case "*":
            print(float(x * z))
        case "/":
            print(float(x / z))
        case _:
            print("Oops, error")
                
            return y
    
main()