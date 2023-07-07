#include<iostream>
using namespace std;
int main()
{
    int x,y,temp;
    cout<<"enter your dividend: "<<endl;
    cin>>x;
    cout<<"enter your divisor: "<<endl;
    cin>>y;
    try
    {
        if(y==0)
        {
            throw (y);
        }
        else
        {
            temp=x/y;
            cout<<"quotient= "<<temp;
        }
    }
    catch(int y)
    {
       cout<<"cant divide by zero: ";
    }
}