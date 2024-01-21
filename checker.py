import json
import time
from datetime import datetime, timedelta

from message import send_message

NIKO = "+17788141068"


def check():
    while True:
        with open("initiated.json", "r") as f:
            dat = json.loads(f.read())
        if dat["initiated"]:
            print("ini")
            with open("running.json", "r") as f:
                tt = json.loads(f.read())
            current_timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            current_timestamp = datetime.strptime(
                current_timestamp_str, "%Y-%m-%d %H:%M:%S"
            )
            saved_timestamp = datetime.strptime(tt["timestamp"], "%Y-%m-%d %H:%M:%S")

            time_difference = (current_timestamp - saved_timestamp).total_seconds() / 60
            if time_difference > 0.8:
                print(
                    f"Time difference is greater than 0.8 minute: {time_difference:.2f} minutes"
                )
                send_message("Your Kayo crashed or was force closed", NIKO)
                break
            else:
                print(
                    f"Time difference is less than or equal to 1 minute: {time_difference:.2f} minutes"
                )
        time.sleep(15)


if __name__ == "__main__":
    check()
