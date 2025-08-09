import subprocess
import os
import datetime

# Define the output file path
current_time = datetime.datetime.now().strftime("%H_%M_%S")
ImageName = f"photo_{current_time}.jpg"

# The command to be executed
# -c 0 specifies the back camera. You can change it to 1 for the front camera if available.

def CaptureImage(FileName=ImageName):
    command = ["termux-camera-photo", "-c", "0", FileName]
    """Takes a picture using the termux-camera-photo command."""
    print("Attempting to take a picture...")
    try:
        # Execute the command(Termux specific)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"Successfully took picture and saved it to {FileName}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return ImageName

