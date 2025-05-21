#!/usr/bin/env python3
import pyautogui
import time
import sys
from pynput.mouse import Listener

# Default values
DEFAULT_DELAY = 0.8  # Default delay between clicks in seconds
DEFAULT_REPETITIONS = 10  # Default number of repetitions
DEFAULT_CLICK_POSITIONS = 3  # Default number of click positions

def get_click_position(num_positions=DEFAULT_CLICK_POSITIONS):
    """
    Records a series of mouse click positions on the screen.

    This function waits for the user to click on the screen to record the coordinates
    of each click. It continues until the required number of positions is recorded.

    For each position, it creates a mouse listener that records the x, y coordinates
    when the mouse button is pressed. After each click, there's a small delay before
    waiting for the next click.

    Args:
        num_positions (int): Number of click positions to record. Defaults to DEFAULT_CLICK_POSITIONS.

    Returns:
        list: A list of tuples, where each tuple contains the (x, y) coordinates of a click position.
    """
    pos = []

    print("\nINSTRUCTIONS:")
    print("- Click on the locations you want to automate")
    print("- You can cancel at any time by pressing Ctrl+C")
    print(f"- You need to record {num_positions} positions\n")

    try:
        while len(pos) < num_positions:
            print(f"Click on the screen to record position {len(pos) + 1} of {num_positions}...")
            
            def on_click(x, y, button, pressed):
                if pressed:
                    pos.append((x, y))
                    print(f"Position recorded: ({x}, {y})")
                    return False

            with Listener(on_click=on_click) as listener:
                listener.join()

            time.sleep(0.5)
            
        return pos
    except KeyboardInterrupt:
        print("\nRecording canceled by user.")
        if pos:
            print(f"Recorded {len(pos)} positions so far. Proceeding with these positions.")
            return pos
        else:
            print("No positions recorded. Exiting program.")
            sys.exit(0)

def get_repetitions():
    """Get the number of repetitions from user input."""
    while True:
        try:
            user_input = input("\nEnter repetitions (number or 'inf' for infinite loop): ")
            if user_input.lower() in ('inf', 'infinite', 'none'):
                return None
            repetitions = int(user_input)
            if repetitions <= 0:
                print("Please enter a positive number or 'inf' for infinite loop.")
                continue
            return repetitions
        except ValueError:
            print("Invalid input. Please enter a number or 'inf'.")

def get_delay():
    """Get the delay between clicks from user input."""
    while True:
        try:
            user_input = input("\nEnter delay between clicks in seconds (0.5 very fast, 0.8 ~ 1.0 average)\n"
                             "or press Enter for default (0.8): ")
            if user_input == "":
                print(f"Using default delay: {DEFAULT_DELAY} seconds.")
                return DEFAULT_DELAY
            
            delay = float(user_input)
            if delay <= 0:
                print("Delay must be greater than 0. Please try again.")
                continue
            return delay
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def click_loop(click_points, repeat_times, delay):
    """
    Executes the automated clicking sequence.
    
    Args:
        click_points (list): List of (x, y) coordinates to click
        repeat_times (int or None): Number of repetitions, None for infinite
        delay (float): Time delay between clicks in seconds
    """
    count = 0
    try:
        print(f"\nStarting click sequence with {len(click_points)} positions.")
        print("Move mouse to top-left corner (0,0) to stop at any time.")
        
        while repeat_times is None or count < repeat_times:
            if repeat_times is None:
                print(f"Executing loop {count + 1} (infinite)...")
            else:
                print(f"Executing loop {count + 1} of {repeat_times}...")
                
            for i, (x, y) in enumerate(click_points):
                pyautogui.click(x, y)
                if i < len(click_points) - 1:  # Don't sleep after the last click in a cycle
                    time.sleep(delay)
            
            count += 1
            
            # Add a small pause between cycles
            if repeat_times is None or count < repeat_times:
                time.sleep(delay)
                
    except pyautogui.FailSafeException:
        print("\nFail-safe triggered! Program stopped.")
    except KeyboardInterrupt:
        print("\nProgram manually interrupted by user.")
    finally:
        print(f"\nCompleted {count} cycles.")

def main():
    """Main program function."""
    print("\n=== Click N Repeat - Automated Mouse Clicker ===")
    
    try:
        # Step 1: Get click positions
        click_points = get_click_position()
        
        # Step 2: Get repetition settings
        repeat_times = get_repetitions()
        
        # Step 3: Get delay settings
        delay = get_delay()
        
        # Step 4: Enable fail-safe mode
        pyautogui.FAILSAFE = True  # Move mouse to (0,0) to stop
        
        # Step 5: Countdown before starting
        print("\nPreparing to start in 3 seconds...")
        print("You can move to your target window now.")
        for i in range(3, 0, -1):
            print(f"{i}...")
            time.sleep(1)
            
        # Step 6: Execute click loop
        click_loop(click_points, repeat_times, delay)
        
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        return 1
        
    return 0

if __name__ == "__main__":
    sys.exit(main())
