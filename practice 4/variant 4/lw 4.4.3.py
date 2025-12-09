question = "Как твои дела? "
answer = input(question).strip().lower()

good_responses = ["хорошо", "нормально", "я отлично, супер гуд"]
bad_responses = ["плохо", "не хорошо", "..."]

if answer in good_responses:
    print("😊")
elif answer in bad_responses:
    print("😔")
else:
    print("😐")