import re;
import random;

max_digit = -1
target_len = -1

def read_game_parameters():
    
    while(True) :
        global max_digit
        global target_len
        ok = True
        
        print("Enter maximum target digit (1-9): ",end='')
        max_digit=int(input())
        if(not max_digit in range(1,9)) :
            print("Digit not in range\n")
            ok = False;

        if(ok):
            print("Enter number of  digit in target: ",end='')
            target_len=int(input())
            if(target_len < 1) :
                print("Target length must be at least 1\n")
                ok = False;

        if(ok):
            break
        
def extract_digits(string):
    """Extract a tuple of non-zero digits from a string
    return tuple of integers, or false if string does not comprise of digits"""
    
    #remove spaces
    string = string.replace(" ","")
    m = re.match(r"^[1-9]+$", string)
    if(m):
        return tuple(map(int, string))
    else:
        return False;

def read_guess():
    """"Read a guess """

    while(True) :
        print("Enter your guess (q to quit): ",end='')
    
        guess = input()
        if(guess.lower() == "q") :
            return False

        digits = extract_digits(guess)
        if(digits and len(digits) == target_len and
          max(digits) <= max_digit):
            return digits;
    
        print ("Guess must have %d digits in range 1 to %d"
            %(target_len, max_digit));

def random_guess() :
    guess = ()
    for i in range(0, target_len): 
        digit = random.randrange(1,max_digit+1)
        guess += (digit,)

    return guess;

def count_bulls(guess, target):
    target_iter = iter(target)
    bulls = 0;
    for g in guess :
        t = target_iter.__next__(); # why __next__? rather than next()?

        if(g == t) :
            bulls = bulls+1
        
    return bulls;

def count_raw_cows(guess, target):
    # bulls are included in count of 'raw' cows
    count = 0
    for digit in set(guess): # use set to get unique elements
        gc = guess.count(digit)
        tc = target.count(digit)
        count += min(gc, tc)

    return count;

def score(guess, target):
    bulls = count_bulls(guess, target)
    raw_cows = count_raw_cows(guess, target)
        
    return (bulls,raw_cows-bulls)


def guess_string(guess) :
    string = ""
    for digit in guess :
        string += (str(digit) + " ")

    return string[:-1]

def print_history(history):
    for (guess,bulls,cows) in history:
        print("%s: %d bulls %d cows" % (guess_string(guess),bulls,cows))
        
def play():

    history = []   
    target = random_guess()
    game_in_play = True;
    while(game_in_play) :
        guess = read_guess()
        if(guess) :
            (bulls,cows) = score(guess,target)
            history.append((guess, bulls, cows))
            print_history(history);
            
            if(bulls == target_len) :
                print("Solved in %d guess" % len(history))
                game_in_play = False


        else:
            print("Target was ",end="")
            for d in target :
                print(d,end="");
            print()
            game_in_play = False; 


read_game_parameters()
while(True) :
    play()

    print("Play again - same parameters [y/n]? ",end='')
    yn = input().lower();
    if(not yn == 'y') :
        break;

            
        
    
    
    



