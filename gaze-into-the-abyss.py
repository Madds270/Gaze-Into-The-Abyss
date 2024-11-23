# Write functions
def greeting():
    return 'Hello'

# Call functions
print(greeting())

# Import from Standard Library
import datetime
now = datetime.datetime.now()
print(now)

# Create and work with classes
class Greeting:
    def greet(self, name):
        return 'Hello ' + name

print(Greeting().greet('Madds'))


import time
import random

# Define some "abyssal thoughts"
abyss_thoughts = [
    "The void stares back at you.",
    "In the darkness, you see your own fears reflected.",
    "The deeper you look, the less you understand.",
    "The abyss whispers: 'Why do you seek meaning here?'",
    "Time loses meaning in the void.",
    "You find nothing... or is it everything?",
    "The infinite emptiness feels strangely familiar.",
    "The abyss shows you what you already knew."
]

# Function to gaze into the abyss
def gaze_into_the_abyss():
    print("\nGazing into the abyss...\n")
    try:
        while True:
            # Randomly select a thought from the abyss
            thought = random.choice(abyss_thoughts)
            print(f"🔮 {thought}")
            time.sleep(random.uniform(1.5, 3.5))  # Add a pause for dramatic effect
    except KeyboardInterrupt:
        print("\n\nYou pull back from the edge of the abyss... for now.")
        print("But its presence lingers in your mind.\n")

# Start the abyss-gazing experience
if __name__ == "__main__":
    gaze_into_the_abyss()
