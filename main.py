#!/usr/bin/env python3
"""
Screenshot Tool using pyscreenshot / pyautogui
Author: brainiacweb-tech
"""
import datetime, os, time

def take_screenshot(filename=None, delay=0, region=None):
    try:
        import pyautogui
    except ImportError:
        print("Install: pip install pyautogui"); return
    if not filename:
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{ts}.png"
    if delay > 0:
        print(f"Taking screenshot in {delay} second(s)...")
        time.sleep(delay)
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(filename)
    size = os.path.getsize(filename)
    print(f"Screenshot saved: {filename} ({size:,} bytes)")
    return filename

if __name__ == "__main__":
    print("=" * 42)
    print("        Screenshot Tool")
    print("=" * 42)
    print("1. Full screen screenshot")
    print("2. Delayed screenshot")
    print("3. Region screenshot")
    choice = input("Choice: ").strip()
    if choice == "1":
        take_screenshot()
    elif choice == "2":
        try: delay = int(input("Delay in seconds: "))
        except ValueError: delay = 3
        take_screenshot(delay=delay)
    elif choice == "3":
        try:
            x = int(input("X: ")); y = int(input("Y: "))
            w = int(input("Width: ")); h = int(input("Height: "))
            take_screenshot(region=(x, y, w, h))
        except ValueError:
            print("Invalid values.")
    else:
        print("Invalid choice.")
