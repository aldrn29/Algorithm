#include <iostream>
#include <algorithm>

using namespace std;

int n, len;
int f[10000];

int main()
{
	cin >> n >> len;

	for (int i = 0; i < n; i++) 
	{
		cin >> f[i];
	}

	sort(f, f + n);

	for (int i = 0; i < n; i++) 
	{
		if (len < f[i]) break;
		len++;
	}

	cout << len;

	return 0;
}