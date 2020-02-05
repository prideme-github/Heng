def main ()
grades={'Student':'Grade'}
while True:
    name=input("Please give me the name if the student (q to quit):")
    if name == 'q':
        print("Okey,printing grades")
        for name,grade in grades.items():
            print('{name}:{grade}'.format(name=name,grade=grade))
        break
    grade=input("Please give me their grade:")
    grades[name]=grade
if __name__="__main__":
    main()