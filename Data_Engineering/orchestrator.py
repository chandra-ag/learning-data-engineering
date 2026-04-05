import schedule
import time
import subprocess
import sys

def run_weather_pipeline():
    print(f"\n[{time.strftime('%Y-%m-%d %H:%M:%S')}] 🚀 Triggering Weather Pipeline...")
    
    try:
        # This tells Python to run your pipeline script exactly as if you typed it in the terminal
        result = subprocess.run([sys.executable,'D:\Dev\Data_Engineering\weather_pipeline.py' ], capture_output=True, text=True)
        
        # Print the output of the pipeline
        print(result.stdout)
        
        if result.returncode == 0:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [SUCCESS] Pipeline execution successful.")
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [ERROR] Pipeline failed.")
            print(result.stderr)
            
    except Exception as e:
        print(f"Failed to execute script: {e}")

# --- THE SCHEDULE ---
# For testing right now, let's schedule it to run every 10 seconds.
schedule.every(10).seconds.do(run_weather_pipeline)

# In the real world, you would use this line instead:
# schedule.every().day.at("06:00").do(run_weather_pipeline)

print("⏱️ Orchestrator started. Waiting for the next scheduled run... (Press Ctrl+C to stop)")

# This infinite loop keeps the script alive in the background to check the time
while True:
    schedule.run_pending()
    time.sleep(1)