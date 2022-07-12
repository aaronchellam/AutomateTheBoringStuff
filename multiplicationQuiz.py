import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # Pick two random numbers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = f'Q{questionNumber+1}) {num1} x {num2} = '

    try:
        # Right answers are handled by allowRegexes
        # Wrong answers are handled by blockRegexes
        # There is a limit of 3 answers and a timeout after 8 secs
        pyip.inputStr(prompt, allowRegexes=[f'^{num1*num2}$'],
                              blockRegexes=[('.*', 'Incorrect!')],
                              limit=3, timeout=8
                      )

    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This else block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1


    time.sleep(1)  # Brief pause to let user see result.

print(f'Score: {correctAnswers} / {numberOfQuestions}')

