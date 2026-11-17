print("Welcome to Wizo - Prompt Engineering Project!")

def improve_prompt(prompt):
    improved = (
        "You are a helpful AI assistant.\n"
        f"Task: {prompt}\n"
        "Provide a clear, detailed, step-by-step explanation.\n"
        "Include a practical example."
    )
    return improved


user_prompt = input("Enter your prompt: ")

result = improve_prompt(user_prompt)

print("\n--- Improved Prompt ---")
print(result)