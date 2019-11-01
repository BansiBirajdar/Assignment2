'''Write a program which accept one number from user and return its factorial.
    Input : 5 Output : 120'''
def Factorial(no):
    if(no<0):
        no=-no
    if(no==0):
        return 1
    ans=1
    for i in range(1,no+1):
        ans=ans*i
    return ans

def main():
    no=int(input("enter the number="))
    ans=Factorial(no)
    print("factorial is =",ans)
    
if (__name__=="__main__"):
    main()