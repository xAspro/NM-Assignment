#include<limits.h>
#include<float.h>
#include<iostream>
using namespace std;

int main()
{
	cout<<"Size of int: \t"<< sizeof(int)<<" bytes"<< endl;
	cout<<"Size of float: \t"<< sizeof(float)<<" bytes"<< endl;
	cout<<"Size of bool: \t"<< sizeof(bool)<<" bytes"<< endl;
	cout<<"Size of char: \t"<< sizeof(char)<<" bytes"<< endl;

	cout<<"\nMin value of int: \t"<< INT_MIN<<"\nMax value of int: \t"<<INT_MAX;
	cout<<"\nMin value of float: \t"<< FLT_MIN<<"\nMax value of float: \t"<<FLT_MAX;
	cout<<"\nMin value of long: \t"<< LONG_MIN<<"\nMax value of long int: \t"<<LONG_MAX;

	cout<<"\n";
}
