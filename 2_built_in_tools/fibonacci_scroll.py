#!/usr/bin/env python3
"""
🔮 The Fibonacci Scroll - A Magical Number Sequence Generator
Created by Kiro the Grey Hat

This scroll contains ancient wisdom for generating the mystical Fibonacci sequence.
Each number holds the power of the two that came before it.
"""

def fibonacci_spell(n):
    """
    Conjures the first n numbers of the Fibonacci sequence.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
        
    Returns:
        list: The first n Fibonacci numbers
        
    Raises:
        ValueError: If n is not a positive integer
    """
    # Validate the magical parameter
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The spell requires a positive integer, young apprentice!")
    
    # Handle the simplest cases
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Initialize the magical sequence
    sequence = [0, 1]
    
    # Cast the iterative spell to generate remaining numbers
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    
    return sequence

def display_fibonacci_scroll(numbers):
    """
    Displays the Fibonacci sequence in a mystical format.
    
    Args:
        numbers (list): The Fibonacci sequence to display
    """
    print("✨" + "="*50 + "✨")
    print("🔮 THE FIBONACCI SCROLL HAS BEEN UNFURLED! 🔮")
    print("✨" + "="*50 + "✨")
    print()
    
    for i, num in enumerate(numbers):
        print(f"📜 Position {i+1:2d}: {num:>8d} ✨")
    
    print()
    print("🌟 The ancient pattern reveals itself! 🌟")
    print(f"📊 Sum of all numbers: {sum(numbers)}")
    print("✨" + "="*50 + "✨")

# Main spell execution
if __name__ == "__main__":
    try:
        # Cast the spell for the first 10 Fibonacci numbers
        magical_numbers = fibonacci_spell(10)
        
        # Display the results with mystical formatting
        display_fibonacci_scroll(magical_numbers)
        
        # Demonstrate the mathematical relationship
        print("\n🔍 Observing the magical pattern:")
        for i in range(2, len(magical_numbers)):
            a, b, c = magical_numbers[i-2], magical_numbers[i-1], magical_numbers[i]
            print(f"   {a} + {b} = {c}")
            
    except Exception as e:
        print(f"❌ The spell has failed: {e}")