def fake_llama(prompt):
    return "LLaMA says: AI is intelligence shown by machines."

def fake_qwen(prompt):
    return "Qwen says: AI helps automate tasks and learning."

if __name__ == "__main__":
    user_input = input("Ask something: ")

    print("\nLLaMA Response:\n", fake_llama(user_input))
    print("\nQwen Response:\n", fake_qwen(user_input))