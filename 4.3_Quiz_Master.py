'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
correct = 0
total=0
print()
print("Star Wars Pop Quiz!")
print()


question = str(input("What is Baby Yoda's real name? ==> "))
print()
if question.lower() == "grogu":
    print("Correct!")
    correct+=1
    total+=1
else:
    print("Wrong! The correct answer is Grogu.")
    total+=1
print()


question = str(input("Who is Palpatine's granddaughter? ==> "))
print()
if question.lower() == "rey":
    print("Correct!")
    correct+=1
    total+=1
else:
    print("Wrong! The correct answer is Rey.")
    total+=1
print()


question = str(input("Who was Anakin Skywalker's Padawan? ==> "))
print()
if question.lower() == "ahsoka" or question.lower() == "ahsoka tano":
    print("Correct!")
    correct+=1
    total+=1
else:
    print("Wrong! The correct answer is Ahsoka Tano.")
    total+=1
print()


question = str(input("What is Mando's true name? ==> "))
print()
if question.lower() == "din djarin":
    print("Correct!")
    correct+=1
    total+=1
else:
    print("Wrong! The correct answer is Din Djarin.")
    total+=1
print()


print("What body part did Luke Skywalker lose in his fight with Darth Vader?")
print()
print("A: His Right Leg")
print("B: His Left Arm")
print("C: His Right Hand")
print()
question = str(input("Choose a Letter ==> "))
print()
if question.lower() == "c":
    print("Correct!")
    correct+=1
    total+=1
else:
    print("Wrong! The correct choice is C.")
    total+=1
print()


print("What did Jar Jar Binks end up owing Qui-Gon Jinn after being rescued during the invasion of Naboo?")
print()
print("A: An honor debt")
print("B: Bongo")
print("C: A trip to Otoh Gunga")
print()
question = str(input("Choose a Letter ==> "))
print()
if question.lower() == "a":
    print("Correct!")
    correct+=1
    total+=1
else:
    print("Wrong! The correct choice is A.")
    total+=1
print()


print("What is Chewbacca’s weapon of choice?")
print()
print("A: Blaster rifle")
print("B: Bowcaster")
print("C: Metal club")
print()
question = str(input("Choose a Letter ==> "))
print()
if question.lower() == "b":
    print("Correct!")
    correct+=1
    total+=1
else:
    print("Wrong! The correct choice is B.")
    total+=1
print()


question = str(input("If the mass of an object is 65 and the acceleration is 15 squared what is the force of the object? ==> "))
print()
if question == "975":
    print("Correct!")
    correct+=1
    total+=1
else:
    print("Wrong! The correct answer is 975.")
    total+=1
print()


question = str(input("If the force of an object is 609 and the mass of the object is 60 what is the acceleration of the object? ==> "))
print()
if question == "10.15":
    print("Correct!")
    correct+=1
    total+=1
else:
    print("Wrong! The correct answer is 10.15.")
    total+=1
print()


question = str(input("If the mass of an object is 5912 and the acceleration of the object is 9 what is the force of the object? ==> "))
print()
if question == "53208" or question == "53,208":
    print("Correct!")
    correct+=1
    total+=1
else:
    print("Wrong! The correct answer is 53,208")
    total+=1
print()



grade = correct/total*100

if grade >= 92:
    letter="A"
elif grade >= 90:
    letter="A-"
elif grade >= 88:
    letter="B+"
elif grade >= 82:
    letter="B"
elif grade >= 80:
    letter="B-"
elif grade >= 78:
    letter="C+"
elif grade >= 72:
    letter="C"
elif grade >= 70:
    letter="C-"
elif grade >= 65:
    letter="D"
else:
    letter="F"
    print("You need to learn more about Star Wars!")

print("Your overall grade is:", grade,"% ",letter)

