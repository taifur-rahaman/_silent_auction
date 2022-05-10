import replit
import art

print("Welcome to the Silent Auction\n")
bidders = []  # it's a global bidders list


def bidder(name, bid, bidders):
    temp = {}
    temp["name"] = name
    temp["bid_amount"] = bid
    return bidders.append(temp)


def highest_bid(bidders):
    replit.clear()
    max_bid = 0
    text = "Winner is"
    for dict in bidders:
        if dict["bid_amount"] > max_bid:
            max_bid = dict["bid_amount"]
            max_bidder = dict["name"]
    print(art.text2art(f"{text : ^30}\n") + art.text2art(f"{max_bidder : ^45}"))
    print(f"{max_bidder} won by bidding {max_bid}")


while True:
    name = input("Enter your name: ")
    bid = float(input("Enter the bid amount: "))
    bidder(name, bid, bidders)
    replit.clear()
    choice = int(input("Is there anyone else?\n1. Yes\n2. No\nEnter your Choice: "))
    if choice == 1:
        replit.clear()
        continue
    elif choice == 2:
        print("Thank you for your bid.")
        break

highest_bid(bidders)
