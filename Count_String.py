def countCharacter(str):
    count=0
    for i in range(0,len(str)):
        if(str[i]==' '):
            continue
        count=count+1
    print(f"Number Of Characters is {count}")

def countWords(str):
    lst=str.split()
    print(f"Number of Words are {len(lst)}")

def countLines(str):
    lines=str.split("\n")
    print(f"Number of Lines : {len(lines)}")

file=input("Enter File Name\n")
try:
    with open(file) as f1:
       data = f1.read()
       countLines(data)
       countWords(data)
       countCharacter(data)
except FileNotFoundError:
    print("File Not Found")
