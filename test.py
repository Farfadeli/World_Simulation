import random

if __name__ == "__main__" : 
    for e in range(100000):
        guess = random.random()
        if guess < 0.0006 :
            print(guess)