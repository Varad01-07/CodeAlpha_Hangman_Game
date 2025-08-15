# Basic Rule-Based Chatbot
# CodeAlpha Internship Project - Task 4

def chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == 'hello' or user_input == 'hi':
            print("Chatbot: Hi there!")
        elif user_input == 'how are you':
            print("Chatbot: I'm just a program, but I'm functioning well! How about you?")
        elif user_input == 'what is your name':
            print("Chatbot: I'm CodeAlpha Bot, your simple chatbot assistant!")
        elif user_input == 'bye' or user_input == 'goodbye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif user_input == 'help':
            print("Chatbot: I can respond to greetings like 'hello', 'hi', 'how are you', 'what is your name', and 'bye'.")
        elif not user_input:
            print("Chatbot: Please type something...")
        else:
            print("Chatbot: I'm a simple bot. I don't understand that. Try 'hello' or 'how are you'.")

if __name__ == "__main__":
    chatbot()