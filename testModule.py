def cubeRoot(n):
    #n = float(input("Enter number to find cuberoot of: "))
    epsilon = 0.001
    counter = 0
    low = 0
    high = n 
    guess = (high+low)/2.0


    if abs(n) > 1:
        while abs(abs(guess)**3 - abs(n)) >= epsilon:
            if abs(guess)**3 < n:
                low = guess
            else:
                high = guess
        
            guess = (high+low)/2.0
            counter += 1
        print("number of iteration:",counter)
        print("Cuberoot of ",n,"is",guess)

    if abs(n) < 1:
        low = n
        high = 1
        guess = (high+low)/2.0

        while abs (abs(guess)**3 - abs(n)) >= epsilon:
            if n > 0:
                if guess**3 < n:
                    low = guess
                else:
                    high = guess

                guess = (high+low)/2.0
                counter += 1
            else:
                low = -1
                high = n
                if guess ** 3 > n:
                    high = guess
                else:
                    low = guess
                guess = (low + high) / 2.0
                counter+= 1
        print(counter)
        print("The cube root of",n,"is closest to:",guess)




def squareRoot(n):
    #n = float(input("Enter number to find square root of: "))
    epsilon = 0.001
    counter = 0
    low = 0
    high = n 
    guess = (high+low)/2.0


    if abs(n) > 1:
        while abs(abs(guess)**2 - abs(n)) >= epsilon:
            if abs(guess)**2 < n:
                low = guess
            else:
                high = guess
        
            guess = (high+low)/2.0
            counter += 1
        print("number of iteration:",counter)
        print("square root of ",n,"is",guess)

    if abs(n) < 1:
        low = n
        high = 1
        guess = (high+low)/2.0

        while abs (abs(guess)**2 - abs(n)) >= epsilon:
            if n > 0:
                if guess**2 < n:
                    low = guess
                else:
                    high = guess

                guess = (high+low)/2.0
                counter += 1
            else:
                low = -1
                high = n
                if guess ** 2 > n:
                    high = guess
                else:
                    low = guess
                guess = (low + high) / 2.0
                counter+= 1
        print(counter)
        print("The square root of",n,"is closest to:",guess)
