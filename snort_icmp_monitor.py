import time
import os

# Path to Snort's alert file (Check your specific config location)
LOG_FILE = '/var/log/snort/alert' 

def follow(thefile):
    """Generator that yields new lines in a file"""
    thefile.seek(0, os.SEEK_END)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == "__main__":
    print(f"Watching {LOG_FILE} for intrusions...")
    try:
        with open(LOG_FILE, 'r') as logfile:
            for line in follow(logfile):
                if "ICMP Ping Detected" in line:
                    print("\n[!!!] ALERT: PING SCAN DETECTED [!!!]")
                    print(f"Raw Log: {line.strip()}")
                    # Add code here to block IP via firewall (ufw/iptables)
    except FileNotFoundError:
        print("Log file not found. Run Snort first!")
