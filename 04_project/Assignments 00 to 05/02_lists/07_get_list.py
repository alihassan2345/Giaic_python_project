def main():
    list = []  
    
    while True:
        value = input("Enter a value: ")       
        if value == "": 
            break
        
        list.append(value)  

    print("Here's the list:", list)  


if __name__ == '__main__':
    main()