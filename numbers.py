def main():
    coins = [ "H"] *1000 
    print(coins)
    transversing_numb = 0 
    while True:
        i = transversing_numb 
        while i<=99:
            if coins[i]=="H":
                coins[i] = "T"
            else:
                coins[i] = "H"
            i+=transversing_numb
            i+=1
       transversing_numb+=1 
        if transversing_numb == 3:
            break
    print(coins)




    return

if __name__ == "__main__":
    main()
