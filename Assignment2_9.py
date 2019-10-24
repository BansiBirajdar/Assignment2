'''Write a program which accept number from user and return number of digits in that number.
Input : 5187934 Output : 7'''
icnt=None;
def CountDigit(no):
    global icnt;
    print (icnt);
    if(no==0):
        #print("Please enter the number ");
        return icnt;
    else:
        icnt+=1;
        CountDigit(no//10);
'''def CountDigit(no):
    if(no==0):
        print("Please enter the number");
        return 0;
    icnt=0;
    while no!=0:
        icnt+=1;
        no=no//10;
    return icnt; '''      

def main():
    no=int(input("Enter the number=="))
    ans=CountDigit(no);
    print("Count of digits =",ans);

if (__name__=="__main__"):
    main();