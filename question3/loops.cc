#include<iostream>
using namespace std;

int cubes(int n)
{
	int sum=0;

	for(int i=1;i<=n;i++)
	{
		sum+=i*i*i;
	}

	return sum;
}

int main()
{
	int a=cubes(40);
	cout<<"Sum of 1st 40 cubes is "<<a;

	int b=cubes(10);
	cout<<"\nSum of 1st 10 cubes is "<<b;

	cout<<"\nTherefore the sum of 30 cubes from 11 is "<< (a-b)<<endl;
}
