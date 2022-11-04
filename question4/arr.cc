#include<iostream>

#include<cstdlib>
using namespace std;

void prnt(int n, int a[])
{
        for(int i=0;i<n;i++)
        {
                cout<<a[i]<<"  ";
        }
        cout<<endl;
}

void arr(int n, int a[])
{
	int max=52; //Its like a set of cards
	srand(time(0));
	
	for(int i=0;i<n;i++)
	{
		a[i]=rand()%max+1;		//so it runs from 1 to 52
	}
	cout<<"Random array:\t\t(taking it till 52 like cards, if needed this number can be changed or removed)"<<endl;
	prnt(n,a);
	
}

void sort(int n, int a[]) //bubble sort
{

	int temp=0;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n-1-i;j++)
		{
			if(a[j]>a[j+1])
			{
				temp=a[j];
				a[j]=a[j+1];
				a[j+1]=temp;
			}
		}
	}
	cout<<"Sorted array:\t\t(this is where taking that 52 is helpful, we can see the numbers clearly, else its too big in general)"<<endl;
	prnt(n,a);
}

/*void prnt(int n, int a[])
{
	for(int i=0;i<n;i++)
	{
                cout<<a[i]<<"  ";
        }
	cout<<endl;
}*/

void prog(int n)
{
	int a[n];
	arr(n,a);
	sort(n,a);
}

int main()
{
	prog(20);
}
