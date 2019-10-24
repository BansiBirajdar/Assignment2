'''Write a program which accept one number and display below pattern.
Input : 5
Output :
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5'''
def Display(no):
    if(no==0):
        print("please enter the no");
        return ;
    for i in range(1,no+1):
        for j in range(1,no+1):
            if(j<=i):
                print(j,end=" ");
        print("\n");
def main():
    no=int(input("enter the number="));
    Display(no);
if (__name__=="__main__"):
    main();