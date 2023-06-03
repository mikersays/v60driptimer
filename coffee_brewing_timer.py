import time

def countdown(duration):
    while duration > 0:
        minutes, seconds = divmod(duration, 60)
        timeformat = f"{minutes:02d}:{seconds:02d}"
        print(timeformat, end="\r")
        time.sleep(1)
        duration -= 1

def start_stopwatch():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        timeformat = f"{minutes:02d}:{seconds:02d}"
        print(timeformat, end="\r")
        time.sleep(1)

def brew_coffee():
    steps = [
        (10, "1. Pour 50 g of water"),
        (5, "2. Swirl"),
        (30, "3. Wait"),
        (15, "4. Pour 50 g of water"),
        (10, "5. Wait"),
        (10, "6. Pour 50 g of water"),
        (10, "7. Wait"),
        (10, "8. Pour 50 g of water"),
        (10, "9. Wait"),
        (10, "10. Pour 50 g of water"),
        (5, "11. Swirl"),
        (3, "12. Stop")
    ]

    input("Press Enter/Return to begin the coffee brewing procedure...")

    for duration, step in steps:
        print(step)
        countdown(duration)

brew_coffee()
print("Coffee brewing procedure completed.")
exit()
