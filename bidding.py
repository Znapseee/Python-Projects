# Part 1: Create a function that determines the highest bidder within the dictionary
# Part 2: Create a loop that continues bidding as the bidder presses yes and halt when the user presses no

print("""
  _________ __                 __     __________.__    .___  .___.__                
 /   _____//  |______ ________/  |_   \______   \__| __| _/__| _/|__| ____    ____  
 \_____  \\   __\__  \\_  __ \   __\   |    |  _/  |/ __ |/ __ | |  |/    \  / ___\ 
 /        \|  |  / __ \|  | \/|  |     |    |   \  / /_/ / /_/ | |  |   |  \/ /_/  >
/_______  /|__| (____  /__|   |__|     |______  /__\____ \____ | |__|___|  /\___  / 
        \/           \/                       \/        \/    \/         \//_____/  

""")

# Creating a function to determine who is the highest bidder
def highest_bidder(bidding_dict):
    bidder = max(bidding_dict, key=bidding_dict.get)
    print(f"The highest bidder is {bidder} with an amount of PHP {bidding_dict[bidder]}")


# Creating the loop for bidders
bids =  {}
continue_bidding = True

while continue_bidding:
    name = str(input("Enter the name of the bidder: ")).title()
    amount = int(input("Enter the amount of bid: PHP "))
    bids[name] = amount
    is_continue = input("Enter YES if you want to bid again and NO if not \n").lower()

    if is_continue == 'no':
        continue_bidding = False
        highest_bidder(bids)
    elif is_continue == 'yes':
        print("\n" * 20)






