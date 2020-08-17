# Mad Libs is pretty much a random story that can be made. There are blanks words which can be anything.
# A noun, adjective, verb, pronoun, etc, it can be anything
# It will be randomly generated

# Using the establish variables and creating them for a random generator
# Input function is the key
# Input function lets the user type in whatever value they want to type in
# Value must be a string of course

name = input("Enter a name: ")
characteristics = input("Enter a characteristic: ")
goal = input("Enter a goal: ")
feeling = input("Enter a feeling: ")

# Come up with Mad Libs story
# For the story itself must use concatenation of strings

print("There once was a man named " + name)
print("He is an " + characteristics + " person")
print("His goal in life is to " + goal)
print("I " + feeling + " this person")

# A MadLibs Example using a template from google

adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
pluralnoun1 = input("Enter a plural noun: ")
femaleperson = input("Enter the name of a female: ")
adjective2 = input("Enter an adjective: ")
clothing = input("Enter what clothes the person is wearing: ")
noun2 = input("Enter a noun: ")
city = input("Enter a city: ")
pluralnoun2 = input("Enter a plural noun: ")
adjective3 = input("Enter an adjective: ")
body1 = input("Enter part of the body: ")
Letters = input("Enter letters of the alphabet: ")
Celebrity = input("Enter a celebrity: ")
pluralnoun3 = input("Enter a plural noun: ")
adjective4 = input("Enter an adjective: ")
place = input("Enter a place: ")
body2 = input("Enter part of the body: ")
adjective5 = input("Enter an adjective: ")
adjective6 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
pluralnoun4 = input("Enter a plural noun: ")
number = input("Enter a number: ")

print("There are many " +adjective1+ " ways to chose a/an " +noun1+ "to read.")
print(" First, you could ask for recommendations with your friends and " + pluralnoun1)
print(" Just don't ask Aunt " +femaleperson+ " -she only reads " +adjective2+ " books with " + clothing)
print(" -ripping goddesses on cover. If your friends and family are no help, try checking out the " + noun2)
print(" Review in The " + city+ " Times. If the " + pluralnoun2 + " featured there are too " + adjective3)
print(" for your taste, try something a little more low- " +body1+ ", like " +Letters)
print(": The " +Celebrity+ " Magazine, or " +pluralnoun3+ " Magazine.")
print(" You could also choose a book the " +adjective4+ " -fashioned way.")
print(" Head your way to the local library or " +place+ " and browse the shelves until something catches")
print(" your " +body2+ ". Or, you could save yourself a whole lot of " +adjective5)
print(" trouble and log on to www.bookish.com, the " +adjective6+ " new website to " + verb)
print(" for books! With all the time you'll save not having to search for " +pluralnoun4+ " you can read " +number)
print(" more books!")