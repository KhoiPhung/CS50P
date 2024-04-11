while True:
    try:
        fuel = input("Fraction: ")
        x, y = fuel.split('/')
        fraction = int(int(x) / int(y) * 100)
        if fraction <= 100:
            if fraction == 100:
                print("F")
            elif fraction < 1:
                print("E")
            else: 
                print(f"{fraction}%")
        else:
            continue            

    except (ValueError, ZeroDivisionError): 
        pass
    else:
        break