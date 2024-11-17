import os

def shutdown():
    os.system("shutdown /s /t 1")
    print("System will shut down shortly.")

def restart():
    os.system("shutdown /r /t 1")
    print("System will restart shortly.")

def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    print("System will enter sleep mode.")

def sign_out():
    os.system("shutdown -l")
    print("Signed out of the system.")

def switch_user():
    os.system("tsdiscon")
    print("Switched user.")

def main():
    while True:
        print("\nSelect an option:")
        print("1. Shutdown")
        print("2. Restart")
        print("3. Sleep")
        print("4. Sign Out")
        print("5. Switch User")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            shutdown()
        elif choice == "2":
            restart()
        elif choice == "3":
            sleep()
        elif choice == "4":
            sign_out()
        elif choice == "5":
            switch_user()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
