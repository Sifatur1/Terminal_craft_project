import json

# Load questions from JSON file
with open("questions.json") as f:
    questions = json.load(f)

score = 0

print("===== Terminal Quiz Game =====\n")

for q in questions:
    print(q["question"])
    
    # Show options
    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")
    
    # Get user answer
    while True:
        try:
            ans = int(input("Your answer: "))
            if 1 <= ans <= 4:
                break
            else:
                print("Enter number between 1-4")
        except:
            print("Invalid input")

    # Check answer
    if ans == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        correct = q["options"][q["answer"] - 1]
        print(f"❌ Wrong! Correct answer: {correct}\n")

print("===== Game Over =====")
print(f"Your Score: {score}/{len(questions)}")