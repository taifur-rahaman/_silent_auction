import replit

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
    for dict in bidders:
        if dict["bid_amount"] > max_bid:
            max_bid = dict["bid_amount"]
            max_bidder = dict["name"]
    print('''                 
`YMM'   `MM'                     `7MMF'     A     `7MF'db             
  VMA   ,V                         `MA     ,MA     ,V                 
   VMA ,V ,pW"Wq.`7MM  `7MM         VM:   ,VVM:   ,V `7MM `7MMpMMMb.  
    VMMP 6W'   `Wb MM    MM          MM.  M' MM.  M'   MM   MM    MM  
     MM  8M     M8 MM    MM          `MM A'  `MM A'    MM   MM    MM  
     MM  YA.   ,A9 MM    MM           :MM;    :MM;     MM   MM    MM  
   .JMML. `Ybmd9'  `Mbod"YML.          VF      VF    .JMML.JMML  JMML.                   ''')
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
