#include <iostream>
using namespace std;

int p[1000001][2];
int v[1000001][2];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t, n;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cin >> n;
		int result = n;
		
		for (int j = 1; j <= n; j++)
		{
			cin >> p[j][0] >> p[j][1];

			v[p[j][0]][0] = p[j][0];
			v[p[j][0]][1] = p[j][1];
		}
		
		//3 2		1 4
		//1 4		2 3
		//4 1	=>	3 2
		//2 3		4 1
		//5 5		5 5

		for (int j = 1; j < n; j++)
		{
			if (v[j][0] < v[j + 1][0] && v[j][1] < v[j + 1][1])
				result--;
		}

		cout << result << endl;
	}

	return 0;
}