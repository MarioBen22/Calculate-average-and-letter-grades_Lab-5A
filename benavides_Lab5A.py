# Mario Benavides
# Program Status - Complete
# Input 5 numeric scores, calculate the average, and
# display the letter grade based on the average.

scores = 5

# defining the main function
def main():
    score1 = int(input('Enter score #1 in range 1-100: ')) # input for score 1
    while score1 > 100: # input validation
        score1 = int(input('Error: Re-enter score #1 in range 1-100: '))

    score2 = int(input('Enter score #2 in range 1-100: ')) # input for score 2
    while score2 > 100: # input validation
        score2 = int(input('Error: Re-enter score #2 in range 1-100: '))

    score3 = int(input('Enter score #3 in range 1-100: ')) # input for score 3
    while score3 > 100: # input validation
        score3 = int(input('Error: Re-enter score #3 in range 1-100: '))

    score4 = int(input('Enter score #4 in range 1-100: ')) # input for score 4
    while score4 > 100: # input validation
        score4 = int(input('Error: Re-enter score #4 in range 1-100: '))

    score5 = int(input('Enter score #5 in range 1-100: ')) # input for score 5
    while score5 > 100: # input validation
        score5 = int(input('Error: Re-enter score #5 in range 1-100: '))
 
    average = (score1 + score2 + score3 + score4 + score5) / scores # calculating the average   
    determine_grade(average) # passing the argument to determine_grade()

# defining the determine grade function    
def determine_grade(average):
    if average >= 90:
        print('Your average is', format(average, ',.2f'), 'which is a(n)', 'A.')
    elif average >= 80:
        print('Your average is', format(average, ',.2f'), 'which is a(n)', 'B.')
    elif average >= 70:
        print('Your average is', format(average, ',.2f'), 'which is a(n)', 'C.')
    elif average >= 60:
        print('Your average is', format(average, ',.2f'), 'which is a(n)', 'D.')
    else:
        print('Your average is', format(average, ',.2f'), 'which is a(n)', 'F.')
        
main() # call the main function to begin
