import time

def speed_typing_test():
    text = "The quick brown fox jumps over the lazy dog."
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")
    start_time = time.time()
    user_input = input(f"Type the following text:\n{text}\n")
    end_time = time.time()
    
    correct_chars = 0
    for i in range(min(len(text), len(user_input))):
        if text[i] == user_input[i]:
            correct_chars += 1
    
    accuracy = (correct_chars / len(text)) * 100
    elapsed_time = end_time - start_time
    words_per_minute = (len(user_input) / 5) / (elapsed_time / 60)
    
    print("\nResults:")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Words per minute: {words_per_minute:.2f} WPM")

if __name__ == "__main__":
    speed_typing_test()
