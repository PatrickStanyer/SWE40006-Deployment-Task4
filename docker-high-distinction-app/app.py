import datetime
import time

def main():
    print("Starting Task 4.4 High Distinction Container...")
    for i in range(5):
        print(f"Iteration {i+1} at {datetime.datetime.now()}")
        time.sleep(2)
    print("Task 4.4 execution complete!")

if __name__ == "__main__":
    main()
