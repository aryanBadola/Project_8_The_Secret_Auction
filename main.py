from replit import clear
import art

print(art.logo)
print("Welcome to the Secret Auction Program")

bidders = {}
more_bidders = True


while more_bidders:
    name = input("What is your name ?: ")
    bid = int(input("What's your bid? $"))
    bidders[name] = bid
    bidders_left = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if bidders_left == "no":
        more_bidders = False
    clear()

max_bid = 0
max_bidder_name = ""
for key in bidders:
    if bidders[key] > max_bid:
        max_bid = bidders[key]
        max_bidder_name = key

print(f"The winner is {max_bidder_name} with a bid of ${max_bid}")


