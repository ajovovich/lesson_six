#Task 1: Command Parser

while True:
    help_desk = input("Select a phrase that you are looking for (help, issue, contact support)").lower()
    if help_desk == "help":
        print("We are here to help! I am just a chatbot, but I will help the best I can")
    if help_desk == "issue":
        print("What issue are you having? If I can help, I will, otherwise we will submit a ticket through this conversation")
        further_support = input("What are you having trouble with? (Login, performance, error code)").lower()
        if further_support == "login":
            print("User is having issues logging into their account")
        if further_support == "performance":
            print("User is experiencing unexpected performance issues for unknown reasons")
        if further_support == "error code":
            print("User is experiencing error code: 328")
    if help_desk == "contact support":
        print("Of course! Here is our support centers number - 111-222-3333")


    retry = input("Would you like to start over? (Yes/No)").lower()
    if retry != "yes":
        break       
