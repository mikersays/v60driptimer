import time

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"

def countdown(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(format_time(remaining_time), end="\r")
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

    print("Coffee brewing procedure completed.")

brew_coffee()
