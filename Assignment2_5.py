'''Write a program which accept one number for user and check whether number is prime or not.
Input : 5 Output : It is Prime Number'''
def ChekPrime(no):
    if(no==0):
        print("please enter the no");
        return 0;
    for i in range(2,no+1):
        if(no%i==0):
            break;
    return i;
        
def main():
    no=int(input("enter the number="));
    ans=ChekPrime(no);
    if(ans==no):
        print("It is Prime Number");
    else:
        print("It is not Prime Number");
if (__name__=="__main__"):
    main();