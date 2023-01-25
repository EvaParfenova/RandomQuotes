import random

quotes = [
    "Life is 10% what happens to you and 90% how you react to it.",
    "Positive anything is better than negative nothing.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do.",
    "The way to get started is to quit talking and begin doing.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle."
]

def generate_random_quote():
    return random.choice(quotes)

if __name__ == '__main__':
    print(generate_random_quote())
