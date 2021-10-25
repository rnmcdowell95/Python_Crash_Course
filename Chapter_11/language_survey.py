#Ryan McDowell
#10/24/2021
#Practicing with the test class I just made.

from survey import AnonymousSurvey

# Define a question, and create a survey.

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#Show the question, store the responses to the question.
my_survey.show_question()

print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#Show the survey results
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()