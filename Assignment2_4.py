'''Write a program which accept one number form user and return addition of its factors.
Input : 12 Output : 16 (1+2+3+4+6)'''
def Factors(no):
    if(no==0):
        print("please enter the no");
        return 0;
    ans=0;
    for i in range(1,no):
        if(no%i==0):
            ans=ans+i;
    return ans;
def main():
    no=int(input("enter the number="));
    ans=Factors(no);
    print("factors is =",ans);
if (__name__=="__main__"):
    main();