import time
import serial
import re
import os
import socket

def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 80), timeout=5)
        return True
    except:
        return False

def renew_internet_connection():
    # Handle potential exceptions during serial communication
    try:
        os.system("echo 0e8d 7126 > /sys/bus/usb-serial/drivers/generic/new_id")
        time.sleep(1)
        with serial.Serial("/dev/ttyUSB2", 9600, timeout=2) as ser:
            ser.write(b"AT+CGDCONT=1,\"IPV4V6\",\"telstra.internet\",,0,0,0,0,0,0,0\r\n")
            ser.write(b"AT+CGACT=1,1\r\n")
            ser.write(b"AT+CGPADDR=1\r\n")
            read_val = ser.read(500).decode("utf-8")
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', read_val)

            if not ip:
                print("Failed to obtain IP address from cellular network.")
                return

            # print(f"\nifconfig eth2 down\nifconfig eth2 {ip[0]}\nifconfig eth2 up\nip route add default via {ip[0][:ip[0].rfind('.')]}.1 dev eth2\n")

            # Combine error handling and success messages
            if os.system(f"ifconfig eth2 down"):
                print("Error bringing down eth2 interface.")

            if os.system(f"ifconfig eth2 {ip[0]}"):
                print(f"Error configuring eth2 with IP {ip[0]}.")

            if os.system(f"ifconfig eth2 up"):
                print("Error bringing up eth2 interface.")

            if os.system(f"ip route add default via {ip[0][:ip[0].rfind('.')]}.1 dev eth2"):
                print(f"Error adding default route via {ip[0][:ip[0].rfind('.')]}.1.")

    except serial.SerialException as e:
        print(f"Error communicating with serial port: {e}")
    except Exception as e:
        print(f"Unexpected error during internet renewal: {e}")

if __name__ == "__main__":
    retry_count = 0
    while True:
        if check_internet_connection():
            time.sleep(60)
        else:
            retry_count += 1
            if retry_count > 50:
                print("Maximum retries reached. Attempting internet renewal...")
                break
            renew_internet_connection()
            time.sleep(10)
