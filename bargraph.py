from matplotlib import pyplot as plt
from IPython.display import clear_output

ratings, num_ratings = [1, 2, 3, 4, 5], [0, 0, 0, 0, 0]

n = True
while n:
    
    x = True
    while x:
        
        rating = input("What would you rate this movie (1-5)? ")
    
        if rating == '1':
            num_ratings[0] += 1
            clear_output()
            x = False
        
        elif rating == '2':
            num_ratings[1] += 1
            clear_output()
            x = False
        
        elif rating == '3':
            num_ratings[2] += 1
            clear_output()
            x = False
        
        elif rating == '4':
            num_ratings[3] += 1
            clear_output()
            x = False
        
        elif rating == '5':
            num_ratings[4] += 1
            clear_output()
            x = False
        
        else:
            print("That is not a number or is not a number between 1 through 5!")
    
    y = True
    while y != False:
        ask_again = input("Is there another user that would like to review (y/n) ")
    
        if ask_again == 'y':
            clear_output()
            x = True
            y = False
        
        elif ask_again == 'n':
            clear_output()
            n = False
            y = False
        
        else:
            print("That is not an option.")
            
plt.bar(ratings, num_ratings)

plt.title("Movie Ratings", fontsize=24)
plt.xlabel("Ratings", fontsize=16)
plt.ylabel("# of Ratings", fontsize=16)

plt.show()