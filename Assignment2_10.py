'''Write a program which accept number from user and return addition of digits in that number.
Input : 5187934 Output : 37'''

'''def DigitSum(no):
    if(no==0):
        print("Please enter the number ");
        return 0 ;
    d=0;
    sum=0;
    while(no!=0):
        d=no%10;
        sum+=d;
        no=no//10;
    return sum;'''
#by using recursive funcation
def DigitSum(no):
    if(no==0):
        print("Please enter the number ");
        return 0 ;
    else:
        return (no%10)+DigitSum(no//10);
    

def main():
    no=int(input("Enter the number=="))
    ans=DigitSum(no);
    print("Addition of digits =",ans);

if (__name__=="__main__"):
    main();