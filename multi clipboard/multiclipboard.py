import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"


def saved_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data

    except:
            return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        saved_data(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load":
        key = input("enter a key:")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard.")

    elif command == "list":
        print(data)

    else:
        print("unknown command")
else:
    print("please pass exactly one command.")


