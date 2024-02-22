def main():
    coin_dues = 50
    dues(coin_dues)


def dues(coin_dues):
    while coin_dues > 0:
        print(f"Amount Due: {coin_dues}")
        amount = int(input("Insert Coin: "))
        coin_dues = coin_denomination(amount, coin_dues)
            
    if coin_dues == 0:
        print(f"Change Owed: {abs(coin_dues)}")
    elif coin_dues < 0:
        amount -= coin_dues
        print(f"Change Owed: {abs(coin_dues)}")    
    
    
def coin_denomination(amount, coin_dues):
    while amount == 25 or amount == 10 or amount == 5:
        coin_dues -= amount
        return int(coin_dues)
    return coin_dues
    
if __name__ == "__main__":
    main()