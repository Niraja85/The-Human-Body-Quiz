"""
A welcome statement for starting the quiz and if the user
says no, the game quits, and if chooses yes to play the game, 
questions are displayed.
"""
print("Welcome to Fun facts about the Human Body Quiz")
ans = input("Are you ready to play?\n").lower()

if ans != "yes":
    quit()

score = 0    

""" Creating variables from q1 to q10 which includes questions and choices,
that will act as key in dictionary named questions.
"""

q1 = """ Because its cells has mitochondria,which of your muscles never tires?
a. Tongue
b. Triceps
c. Heart
d. Gluteus Maximus
"""
q2 = """ The paper-thin tympanic membrane can be found in what body part?
a. Ear
b. Colon
c. Lungs
d. Throat
"""
q3 = """ Which of these body parts has the most bones?
a. Rib-cage
b. Foot
c. Skull
d. Hand
"""
q4 = """ Where are red blood cells created?
a. Brain
b. Heart
c. Spleen
d. Bones
"""
q5 = """ Which of these body parts continue to get bigger with age?
a. Ear
b. Thumb
c. Spine
d. Femur
"""
q6 = """ The funny bone is actually what type of body-part?
a. Nerve
b. Muscle
c. Bone
d. Organ
"""
q7 = """ How many bones are there in human body?
a. 260
b. 206
c. 150
d. 200
"""
q8 = """ What does mucus do?
a. Filters out harmful bacteria.
b. Helps in smell
c. Helps your lungs take in oxygen
d. Stops your nose from collapsing
"""
q9 = """ The most common eye color in the world is:
a. Brown
b. Blue
c. Green
d. Hazel
"""
q10 = """ How many muscles do you use when you talk?
a. 45
b. 55
c. 72
d. 87
"""

"""
Created a dictionary with q1 to q10 as 'key' and correct answer as 'value'
"""
questions = {
    q1: "c",
    q2: "a",
    q3: "d",
    q4: "d",
    q5: "a",
    q6: "a",
    q7: "b",
    q8: "a",
    q9: "a",
    q10: "c"
}

"""
Creating a for loop to iterate the question and its correct answers.
"""
for question in questions:
    print(question)
    """
    The skip variable moves on to the next question,
    without giving any score.
    """
    skip = input("Do you want to skip the question? (yes/no):\n")
    if skip == "yes":
        continue

    answer = input("Enter the correct answer a/b/c/d: \n")
    if answer == questions[question]:
        print("Correct Answer. You get 10 points!")
        score = score + 10
        print("The current score is:", score)
    else:
        print("Incorrect Answer.")
    """
    The quit variable when chosen, stops the quiz 
    and the we come out of the for loop.
    """    
    quit = input("Do you want to quit the quiz? (yes/no):\n")
    if quit == "yes":
        break    

print("The Final Score is:", score)        
