# Coffee Brewing Procedure Timer

This Python script provides a countdown timer for a coffee brewing procedure according to [James Hoffman's 2022 V60 brewing technique](https://youtu.be/1oB1oDrDkHM). It allows you to time each step of the procedure and ensures accurate timing for a perfect cup of coffee.

## Prerequisites

- Python 3.x

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the Python script is saved.
3. Run the script using the following command:
    ```bash
    python3 coffee_brewing_timer.py
    ```
4. Press Enter/Return in the terminal to begin the coffee brewing procedure.
5. The script will display the current step of the procedure and the remaining time for each step.
6. After completing the coffee brewing procedure, the script will display a completion message.

## Coffee Brewing Procedure

The coffee brewing procedure is defined within the `brew_coffee` function in the Python script. The steps and their corresponding timings are as follows:

1. Pour 50 g of water (10 seconds)
2. Swirl (5 seconds)
3. Wait (30 seconds)
4. Pour 50 g of water (15 seconds)
5. Wait (10 seconds)
6. Pour 50 g of water (10 seconds)
7. Wait (10 seconds)
8. Pour 50 g of water (10 seconds)
9. Wait (10 seconds)
10. Pour 50 g of water (10 seconds)
11. Swirl (5 seconds)
12. Stop (3 seconds)

## Note

- The timer is implemented using the `countdown` function, which displays the remaining time for each step.
- The `start_stopwatch` function is not used in this script.
- Pressing Enter/Return at the beginning of the procedure starts the timer.

- The script will exit automatically after the coffee brewing procedure is completed.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and adapt the code to suit your specific coffee brewing procedure or add any additional features you may need.

Enjoy your perfect cup of coffee!
