def main():
    my_list = list[input('enter number list')]
    
    

    while True:
        print("\nCurrent List:", my_list)
        print("Options:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Edit item")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            item = input("Enter item to add: ")
            my_list.append(item)
            print(f"Added '{item}' to the list.")
        
        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in my_list:
                my_list.remove(item)
                print(f"Removed '{item}' from the list.")
            else:
                print(f"'{item}' not found in the list.")
        
        elif choice == '3':
            index = int(input("Enter the index of the item to edit (0 to {}): ".format(len(my_list) - 1)))
            if 0 <= index < len(my_list):
                new_item = input("Enter new item: ")
                my_list[index] = new_item
                print(f"Item at index {index} updated to '{new_item}'.")
            else:
                print("Invalid index.")
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
