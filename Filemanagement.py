def read_file(filename):
    try :
        with open(filename,"r") as f:
            content = f.read()
            print("/---File content---/")
            print(content)
    except FileNotFoundError:
        print("File Not Found")
    except Exception as e:
        print(f"Error:{e}")
def write_file(filename):
    try :
        with open(filename, "w") as f:
            text = input("enter a text to writein file:")
            f.write(text)
            print("Text written in the file succefully")
    except Exception as e:
        print(f"Error:{e}")
        
def append_file(filename):
    try:
        with open(filename,"a") as f:
            text = input("enter a text to append")
            f.write("\n"+text)
            print("Text is appended Successfully")
    except Exception as e:
        print(f"Error:{e}")
def search_keyword(filename, keyword):
    try:
        with open(filename,"r") as f:
            content = f.read()
            if keyword in content:
                print(f"{keyword} found in file")
            else:
                print(f"{keyword} is not found in filename")
    except FileNotFoundError:
        print("file is not found")
        
def count_of_words(filename):
    try:
        with open(filename, "r") as f:
            word = f.read().split()
            print(f"Total number of words {len(word)}")
    except FileNotFoundError:
        print("file not found")
        
def main():
    print("===File Management System===")
    while True:
        print("1.Read a file")
        print("2.Write a file")
        print("3.Append a file")
        print("4.Search a keyword in file")
        print("5.Count of words in file")
        print("6.Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            filename = input("Enter the filename to read: ")
            read_file(filename)
        elif choice == '2':
            filename = input("Enter the filename to write: ")
            write_file(filename)
        elif choice == '3':
            filename = input("Enter the filename to append: ")
            append_file(filename)
        elif choice == '4':
            filename = input("Enter the filename to search: ")
            keyword = input("Enter the keyword to search: ")
            search_keyword(filename, keyword)
        elif choice == '5':
            filename = input("Enter the filename to count words: ")
            count_of_words(filename)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()              
            