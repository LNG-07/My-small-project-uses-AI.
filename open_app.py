import subprocess
import webbrowser
import time

def open_workspace():
    print("🚀 Starting workspace...")

    # Replace the paths below with the applications on your machine
    # Note: Keep the r before the quotes to avoid system errors
    apps = [
        ""
    ]

    # Add the websites you frequently open while studying/working here
    urls = [
        ""
    ]

    # Open websites
    for url in urls:
        print(f"🌐 Opening: {url}")
        webbrowser.open(url)
        time.sleep(0.5)

    # Open applications
    for app in apps:
        try:
            print(f"💻 Opening: {app}")
            # start_new_session helps app run independently, script closes doesn't affect app
            subprocess.Popen(app, start_new_session=True)
            time.sleep(1) # Rest 1 second to prevent machine lag
        except FileNotFoundError:
            print(f"❌ File not found at: {app}")
        except Exception as e:
            print(f"⚠️ Error: {e}")

    print("\n✅ Everything is ready!")

if __name__ == "__main__":
    open_workspace()
