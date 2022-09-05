
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!

print("WELCOME TO YOUR MADLIB!")
print("You will be asked to enter various words - please be creative!")

city = input("Please enter a city (real or fictional): ")
nickname = input("Please enter a nickname you might give someone: ")
animal = input("Please enter an animal: ")
celebrity_name = input("Please enter a celebrity's name: ")
food = input("Please enter a food item in plural form (ex. apples): ")
past_tense_verb = input("Please enter a verb in past tense (ex. swam): ")
whole_number = input("Please enter a whole number: ")
noun = input("Please enter a noun: ")
household_item = input("Please enter a household item: ")
object = input("Please enter an object: ")

print(f"Once upon a time, there was a kingdom called {city}. The ruler of {city} was Princess Esmerelda, but the townsfolk called her {nickname}. {nickname} loved all animals, but her favorite was her pet {animal} named {celebrity_name} who loved to eat {food}. One day, {nickname} went to the barn to feed {celebrity_name}, but all the {food} was gone! She {past_tense_verb} to the nearest witch, who said that if {celebrity_name} went {whole_number} hours without {food}, then he would turn into a {noun}! In a panic, {nickname} went to her father, King {household_item} and begged him for money. The King knew his daughter was spoiled, and so he agreed to give her the money if she cleaned the {object}. {nickname} refused, and {celebrity_name} turned into a {noun}. Guess she didn't care that much after all. The End.")

































# --------------------------------------------------
# Partial solution
























# name = input("Name:")
# color = input("color:")
# num = input("Number:")

# print(f"{name} wore {color} shoes while they counted to {num}")