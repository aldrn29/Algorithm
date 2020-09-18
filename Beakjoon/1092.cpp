#include <iostream>
#include <algorithm>
using namespace std;

int crane[1000000];
int box[1000000];

int main()
{
	int n, m;
	int v = 0;

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> crane[i];
	}

	cin >> m;
	for (int i = 0; i < m; i++)
	{
		cin >> box[i];
	}

	sort(crane, crane + n);
	sort(box, box + m);
	
	// 力老 公芭款 Box 八荤
	if (crane[n - 1] < box[m - 1]) {
		cout << "-1";
		return 0;
	}

	bool loop = true;
	while (loop)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = m - 1; j >= 0; j--)
			{
				if (box[j] == 0) continue;
				if (crane[i] >= box[j]) {
					box[j] = 0;
					break;
				}
			}
		}

		v++;
		loop = false;
		for (int i = 0; i < m; i++)
		{
			if (box[i] != 0) {
				loop = true;
				break;
			}
		}
	}
	
	cout << v;

	return 0;
}