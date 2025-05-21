import pyautogui
import time
from pynput.mouse import Listener

# Default values
DEFAULT_DELAY = 0.8  # Default delay between clicks in seconds
DEFAULT_REPETITIONS = 10  # Default number of repetitions
DEFAULT_CLICK_POSITIONS = 3 # Default number of click positions

def get_click_position():
    """
    Records a series of mouse click positions on the screen.

    This function waits for the user to click on the screen to record the coordinates
    of each click. It continues until the required number of positions (defined by
    DEFAULT_CLICK_POSITIONS) is recorded.

    For each position, it creates a mouse listener that records the x, y coordinates
    when the mouse button is pressed. After each click, there's a small delay before
    waiting for the next click.

    Returns:
        list: A list of tuples, where each tuple contains the (x, y) coordinates of a click position.
    """
    pos = []

    while len(pos) < DEFAULT_CLICK_POSITIONS:
        print(f"Click on the screen to record position {len(pos) + 1} of {DEFAULT_CLICK_POSITIONS}.")
        def on_click(x, y, button, pressed):
            if pressed:
                pos.append((x, y))
                print(f"Position recorded: {x}, {y}")
                return False

        with Listener(on_click=on_click) as listener:
            listener.join()

        time.sleep(0.5)

    return pos

click_points = get_click_position()

# Number of repetitions (set to None for infinite loop)
repeat_times = int(input("Enter repetitions numbers or 'None' to infinity loop: "))  # or use: repeat_times = None

# Delay between each click (in seconds)
delay = input("Enter delay between clicks (in seconds) (0.5 very fast, 0.8 ~ 1.0 average): ")
if delay == "":
    print("Delay must be greater than 0. Setting to default value.")
    delay = DEFAULT_DELAY
else:
    delay = float(delay)

# Does not use FALSE in this case if you want to use the fail-safe feature
# To use the fail-safe feature, move the mouse to the top-left corner of the screen to stop the script (0, 0)
pyautogui.FAILSAFE = True  # Enable fail-safe mode

def click_loop():
    count = 0
    while repeat_times is None or count < repeat_times:
        for x, y in click_points:
            pyautogui.click(x, y)
            time.sleep(float(delay))
        count += 1

# Countdown before start to give you time to switch windows
print("Starting in 3 seconds...")
time.sleep(3)
click_loop()
