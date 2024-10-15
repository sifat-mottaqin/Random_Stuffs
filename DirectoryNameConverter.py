# A Lame Code to Convert the name of a Windows path directory into linux directory

while True:
    # Input Windows path
    windows_path = input("Enter the Windows path (or type 'e' to quit): ")

    # Check if the user wants to exit
    if windows_path.lower() == 'e':
        break

    # Convert the drive letter and path
    drive_letter = windows_path[0].lower()
    linux_path = f"/mnt/{drive_letter}" + windows_path[2:].replace('\\', '/')

    # Print the converted path
    print(f"Linux path: {linux_path}")

# Final message before exiting
print("Khela Shesh...")
