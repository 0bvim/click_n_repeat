# Click N Repeat

An automated mouse clicking utility that lets you record multiple click positions and then automatically clicks them in sequence, perfect for automating repetitive tasks.

## Description

Click N Repeat is a Python application that automates repetitive mouse clicking tasks. It allows users to:
- Record multiple click positions on the screen
- Automatically click these positions in sequence
- Specify the number of repetition cycles
- Control the delay between clicks

This tool is particularly useful for tasks requiring repetitive clicking in the same sequence, such as:
- Data entry
- Testing UI interfaces
- Simple game automation
- Repetitive form submissions

## Requirements

- Python 3.6+
- PyAutoGUI (for automated mouse control)
- pynput (for capturing mouse input)

## Installation

1. Clone or download this repository to your machine
2. Install the required packages:

```
pip install -r requirements.txt
```

Or install them directly:

```
pip install pyautogui==0.9.54 pynput==1.8.1
```

## Usage

1. Run the script:

```
python3 script.py
```

On Windows, you may use:
```
python script.py
```

2. The program will ask you to record click positions:
   - You'll be prompted to click on the screen to record each position
   - By default, the program records 3 click positions
   - After each click, the coordinates will be displayed in the console

3. Enter the number of repetitions:
   - Enter a number for a finite number of repetitions
   - Enter 'inf' or 'infinite' for an infinite loop
   - The program will validate your input to ensure it's a positive number or infinity

4. Enter the delay between clicks in seconds:
   - 0.5 is very fast
   - 0.8-1.0 is average speed
   - Press Enter to use the default value (0.8 seconds)
   - The program will validate that the delay is greater than zero

5. After a 3-second countdown, the program will start clicking at the recorded positions in sequence
   - The console will display which loop iteration is currently executing
   - For infinite loops, it will show the current iteration number

## Safety Features

The program includes multiple safety mechanisms:

1. **Fail-safe mechanism**:
   - To stop the automation at any point, move your mouse cursor to the top-left corner of the screen (position 0, 0)
   - This will immediately terminate the program

2. **Keyboard interrupt**:
   - Press Ctrl+C in the terminal/command prompt to stop the program
   - Works during both position recording and clicking phases

3. **Error handling**:
   - The program validates all user inputs to prevent crashes
   - If position recording is interrupted, you can proceed with the positions already recorded

## Customization

You can modify the default settings by changing these constants at the beginning of the script:
- `DEFAULT_DELAY`: Default time between clicks (in seconds)
- `DEFAULT_REPETITIONS`: Default number of repetition cycles
- `DEFAULT_CLICK_POSITIONS`: Default number of click positions to record

Advanced users can modify the script to add features like:
- Custom key combinations for stopping the automation
- Variable delays between different click positions
- Saving and loading click patterns from files
- Adding keyboard input automation alongside mouse clicks

## Limitations

- The program is designed for basic repetitive clicking tasks
- For complex automation scenarios, consider more advanced solutions
- Performance may vary depending on your system specifications
- The automation works best on stable UIs that don't change position between executions
- Some applications or games may have anti-bot measures that detect automated clicking

## License

This project is open source and available under the MIT License.

## Troubleshooting

**Q: The clicks aren't happening at the right positions**
- Make sure your screen resolution hasn't changed since recording positions
- Ensure the target window is in the same position as during recording
- Try using a longer delay to ensure the application has time to respond

**Q: The program crashes when I enter repetitions**
- Make sure you're entering a valid number or 'inf'
- Check that you have the required Python packages installed

**Q: How can I stop an infinite loop?**
- Move your mouse to the top-left corner of the screen (0,0) coordinates
- Alternatively, press Ctrl+C in the terminal window running the script
