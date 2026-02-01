#This is code for a simple time clock
import time
import sys
import winsound

def play_tune():
    """Custom victory soundtrack"""
    notes = [
        (784, 150), (880, 150), (988, 200), (1047, 250),
        (988, 200), (880, 200), (784, 400), (1175, 500)
    ]
    for freq, dur in notes:
        winsound.Beep(freq, dur)
        time.sleep(0.03)

def countdown(time_sec):
    print("⏳ Timer started...\n")
    total = time_sec

    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = f"{mins:02d}:{secs:02d}"
        bar_length = 30
        filled_length = int(bar_length * (total - time_sec) / total)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)

        sys.stdout.write(f"\r⏱  {timeformat} |{bar}|")
        sys.stdout.flush()

        # Final 3-second warning beeps
        if time_sec <= 3:
            winsound.Beep(800 + time_sec * 100, 200)

        time.sleep(1)
        time_sec -=1

    print("\r⏱ 00:00 |██████████████████████████████|")
    print("\n🎶 Timer Ended — Enjoy your victory tune!\n")
    play_tune()

# Example: 2-second timer
countdown(5)



 
