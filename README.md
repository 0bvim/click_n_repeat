# Click N Repeat

An automated mouse clicking utility that lets you record multiple click positions and then automatically clicks them in sequence.

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
- PyAutoGUI
- pynput

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

2. The program will ask you to record click positions:
   - You'll be prompted to click on the screen to record each position
   - By default, the program records 3 click positions
   - After each click, the coordinates will be displayed in the console

3. Enter the number of repetitions:
   - Enter a number for a finite number of repetitions
   - Enter 'None' for an infinite loop

4. Enter the delay between clicks in seconds:
   - 0.5 is very fast
   - 0.8-1.0 is average speed
   - Press Enter to use the default value (0.8 seconds)

5. After a 3-second countdown, the program will start clicking at the recorded positions in sequence

## Safety Feature

The program includes a fail-safe mechanism:
- To stop the automation at any point, move your mouse cursor to the top-left corner of the screen (position 0, 0)
- This will immediately terminate the program

## Customization

You can modify the default settings by changing these constants at the beginning of the script:
- `DEFAULT_DELAY`: Default time between clicks (in seconds)
- `DEFAULT_REPETITIONS`: Default number of repetition cycles
- `DEFAULT_CLICK_POSITIONS`: Default number of click positions to record

## Limitations

- The program is designed for basic repetitive clicking tasks
- For complex automation scenarios, consider more advanced solutions
- Performance may vary depending on your system specifications

## License

This project is open source and available under the MIT License.
