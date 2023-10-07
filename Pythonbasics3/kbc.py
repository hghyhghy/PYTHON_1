questions = [
    [
        "Which programming language is used to make fb?",
        "Python",
        "Javascript",
        "pHp",
        "React",
        "None",
        4,
    ],
    [
        "Who is the current PM of india",
        "Manmohan Singh",
        "Rajiv Gandhi",
        "Narendra Modi ",
        "Ataj Vihari Vajpayee",
        "None",
        3,
    ],
    [
        "Which is the semi-highspeed  train now in India",
        "Rajdhani",
        "Shatabdi",
        "Gatiman",
        "Vande Bharat",
        "None",
        4,
    ],
    [
        "How Many teams are participating in CWC2023?",
        "Five ",
        "Ten",
        "Fifteen",
        "Eight",
        2,
    ],
]

# creating labels in kbc game


levels = [1000, 10000, 30000, 40000, 100000]


prize = 0

# running a for loop

for i in range(0, len(questions)):
    question = questions[i]

    print(f"Your Question for Rs.{levels[i]} ")

    print(f"Your Question is {question[0]}")

    print(f"a.{question[1]}                         b.{question[2]}")

    print(f"c.{question[3]}                          d.{question[4]}")

    print(f"e.{question[5]}")

    reply = int(input("\n Enter Your answer between 1-4 or enter 0 to quit:>>"))

    #     if reply == 0:
    #         prize = levels[i - 1]

    #         break

    if reply == question[-1]:
        print(f"Correct answer ! You have won Rs.{levels[i]}")

        print("Your total Prize  is ", (1000 + 10000 + +30000 + 40000))

        if i == 4:
            prize = 1000

        elif i == 9:
            prize = 40000

        elif i == 14:
            prize = 100000

    else:
        print("Wrong Answer!!")

        break
