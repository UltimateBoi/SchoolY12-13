import base64

def encode(data):
    return base64.b64encode(data)
def decode(data):
    return base64.b64decode(data)

def main():
    # Main menu for encode decode construct
    print("1. Encode\n2, Decode\n3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        data = input("Enter data to encode: ")
        encoded_data = encode(data.encode())
        print(f"Encoded data: {encoded_data}")
    elif choice == '2':
        data = input("Enter data to decode: ")
        decoded_data = decode(data.encode())
        print(f"Decoded data: {decoded_data.decode()}")
    elif choice == '3':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()