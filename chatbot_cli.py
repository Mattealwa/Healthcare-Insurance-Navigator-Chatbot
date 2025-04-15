from gemini import model, insurance_data

def get_user_input():
    print("--------------------------------------------------------")
    print("Hey! Let’s find you the perfect health insurance plan.")
    print("--------------------------------------------------------")
    age = input("1. How old are you? ")
    condition = input("2. Do you have any medical conditions (e.g., diabetes)? ")
    budget = input("3. What's your monthly premium budget (₹)? ")

    return age.strip(), condition.strip().lower(), budget.strip()

def build_prompt(age, condition, budget):
    prompt = f"""
You're a health insurance expert chatbot.
Based on the following data: {insurance_data},
recommend the best plan for a {age}-year-old with {condition}, under ₹{budget}/month.
Be detailed, compare if needed, and make it beginner-friendly.
"""
    return prompt

def main():
    print("chatbot_cli.py started")
    age, condition, budget = get_user_input()
    prompt = build_prompt(age, condition, budget)
    
    print("Sending prompt...")
    response = model.generate_content(prompt)
    print("Response:\n")
    print(response.text)

if __name__ == "__main__":
    main()
