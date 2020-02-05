class_list=['Amy','Bod','Cathy','David']
def main():
    print("Welcome to the student checker!")   
    while True:
        name=input("Please give me the name of a student (enter 'q' to quit)")
        if name == "q":
            print ("Goodbye")
            break         
        while name not in class_list:
            print ("No,that student is not in the class")
            name=input("Please give me the name of a student (enter 'q' to quit)")
        print ("Yes,that student is enrolled in the calss")
if __name__== "__main__":
    main()
