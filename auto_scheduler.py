import schedule
import time
import subprocess

# Function to run a script
def run_script(script_name):
    try:
        print(f"Running {script_name}...")
        subprocess.run(["python", script_name], check=True)
        print(f"{script_name} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}: {e}")

# Scheduling the scripts
schedule.every().day.at("09:00").do(run_script, script_name="p2.py")
schedule.every().day.at("12:00").do(run_script, script_name="p4.py")
schedule.every().day.at("15:00").do(run_script, script_name="p5.py")
schedule.every().day.at("18:00").do(run_script, script_name="p6.py")

# Loop to keep the scheduler running
print("Auto-scheduler started. Waiting for the next scheduled task...")
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute