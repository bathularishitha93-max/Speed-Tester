import time
import random

paragraphs = [
    "Python is a powerful programming language used for web development data science artificial intelligence and automation.",
    "Practice typing every day to improve your speed accuracy and confidence while working on computers.",
    "Success comes from consistent practice hard work and learning from mistakes every single day.",
    "Artificial intelligence and machine learning are transforming industries around the world with innovative solutions.",
    "Programming helps students develop logical thinking problem solving skills and creativity."
]

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()

    correct = 0

    for i in range(min(len(original_words), len(typed_words))):
        if original_words[i] == typed_words[i]:
            correct += 1

    if len(original_words) == 0:
        return 0

    return (correct / len(original_words)) * 100


def typing_test():
    print("=" * 60)
    print("            PYTHON TYPING SPEED TESTER")
    print("=" * 60)

    while True:
        paragraph = random.choice(paragraphs)

        print("\nType the following paragraph exactly:\n")
        print(paragraph)

        input("\nPress Enter to start...")

        start_time = time.time()

        typed_text = input("\nStart Typing:\n")

        end_time = time.time()

        time_taken = end_time - start_time

        words = len(typed_text.split())

        wpm = (words / time_taken) * 60 if time_taken > 0 else 0

        accuracy = calculate_accuracy(paragraph, typed_text)

        print("\n" + "=" * 40)
        print("RESULT")
        print("=" * 40)
        print(f"Time Taken : {time_taken:.2f} seconds")
        print(f"Words Typed: {words}")
        print(f"Typing Speed: {wpm:.2f} WPM")
        print(f"Accuracy: {accuracy:.2f}%")

        if accuracy >= 95:
            print("Performance: Excellent")
        elif accuracy >= 80:
            print("Performance: Good")
        elif accuracy >= 60:
            print("Performance: Average")
        else:
            print("Performance: Needs Improvement")

        choice = input("\nDo you want to try again? (yes/no): ").lower()

        if choice != "yes":
            print("\nThank you for using the Typing Speed Tester!")
            break


typing_test()