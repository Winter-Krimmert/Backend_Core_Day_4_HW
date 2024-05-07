# Lesson 5
# Python Functions
# 1. The Calculator Problem

# create a function for each of the arithmetic operations


# task 2 #implement user input to receive numbers and an operation choice.

number_1 = float(input("input a number: "))
number_2 = float(input("input a second number: "))
op = input("please input a math operator (either (+, -, *, /) ")

if op == '+':
    print(number_1 + number_2)  

elif op == '-':
    print(number_1 - number_2)

# Task 3 #ensure your program can handle division by zero
elif op == '/':
    if number_2 == 0 :
        print("Cannot divide by zero.")
    else: 
        print(number_1 / number_2)

elif op == '*':
    print(number_1 * number_2)


#The Shopping List Maker
shopping_cart = []
bagged_items = []

def add_item(cart):
    item = input("What would you like to add to your cart? ").lower() #lowercases the string
    if item not in cart:
        cart.append(item)
    else:
        print(f"{item} is already in your cart!")

def remove_item(cart):
    item = input("Which item would you like to remove from your cart?").lower()
    try:
        cart.remove(item)
    except ValueError:
        print(f"{item} is not in your cart, you can't remove something that doesn't exist!")

def bag_item(cart, bag): 
    item = input("Which item would you like to bag?").lower()
    try:      
        cart.remove(item)
        bag.append(item)
    except ValueError:
        print("That item is not in your cart...")

def view_items(cart, bag):
    response = input("Would you like to check your cart or your bag? ").lower()
    if response == "cart":
        print("Here are your items!")
        for item in cart:
            print(item)
    elif response == "bag":
        print("Here are your purchased items: ")
        for item in bag:
            print(item)
    else:
        print("please enter a valid response!")             


def run(cart,bag):
    while True:
        response = input("What would you like to do? add/remove/purchase/view/quit: ").lower()
        if response == "add":
            add_item(cart)
            print(cart)
        elif response == "remove":
            remove_item(cart)
            print(cart)
        elif response == "purchase":
            bag_item(cart, bag)
            print("Your purchased items: ")
            for item in bag:
                print(item)
        elif response == "view":
            view_items(cart, bag)

        elif response == "quit":
            for item in cart:
                print(item)
            for purchased_item in bag:
                print(purchased_item)
            break
        else:
            print("Please enter a valid response")


run(shopping_cart, bagged_items)



# Lesson 6: Python Strings

# Product Review Analysis


python_reviews = [ "This product is really good. I'm impressed with its quality.",
                   "The performance of this product is excellent. Highly recommended!",
                     "I had a bad experience with this product. It didn't meet my expectations.", 
                     "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."
                ]
upper_case_reviews = []
review_words = ["good", "excellent", "bad", "poor"]
for sentence in python_reviews:
    for word in review_words:
        sentence = sentence.replace(word, word.upper())
        sentence = sentence.replace(word.title(), word.upper())
    upper_case_reviews.append(sentence)
    print(sentence)
    
print(upper_case_reviews)
# 


# Product Review Analysis
# Sentiment Tally
# develop a function that tallies the number of positive and negative words in each review.
# Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.




positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!","I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

def pos_and_neg_count():
    number_of_positive = 0
    number_of_negative = 0
    for sentence in python_reviews:
        for word in sentence.split():
            word = word.replace(".", "")
            if word.lower() in positive_words:
                number_of_positive += 1
    print(f"The number of positive words in python reviews is {number_of_positive}.")

    for sentence in python_reviews:
        for word in sentence.split():
            word = word.replace(".", "")
            if word.lower() in negative_words:
                number_of_positive += 1
    print(f"The number of negative words in python reviews is {number_of_negative}.")

pos_and_neg_count()



# Task 3
python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!","I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
reviews = " ".join(python_reviews)

i = 30
for sentence in python_reviews:
    i = 30
    while sentence[i] != " ":
        i += 1
    sliced_review = sentence[:i] + "..."
    print(sliced_review)




    # User Input Data Processor
# Task 1: Input Length Validator Write a script that checks the length of the user's first name and last name.
# Both should be at least 2 characters long. If not, print an error message.

print("Let's get you info!")
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
while True:
    
    if len(first_name) >= 2:
        print("First name recorded successfully!")
        if len(last_name) >= 2:
            print("Last name recorded successfully!")
            break
        else:
            print("Last name must be at least 2 characters long!")
            last_name = input("Please enter your last name: ")
    else:
        print("First name must be at least 2 characters long!")
        first_name = input("Please enter your first name: ")
        
print(f"Your name has been recorded as {first_name} {last_name}! Thank you!")