#include <iostream>
using namespace std;

int px[4] = { 1, 1, 2, 2 };
int py[4] = { 2, -2, 1, -1 };
int v = 1;

int main()
{
	int n, m;
	cin >> n >> m;

	int x = 1;
	int y = 0;
	bool cons = false;

	while (true)
	{
		for (int i = 0; i < 4; i++)
		{
			// 이동할 수 있다면
			if (x + px[i] < n && y + py[i] < m && x + px[i] >= 0 && y + py[i] >= 0)
			{
				v++;
				x += px[i];
				y += py[i];
			}
			if (v > 4) { // 이동제약 걸렸을 때
				cons = true;
				v = 1;
				break;
			}
		}

		// 이동 제약 걸렸을 때는 모든 이동경로 포함하여
		if (cons)
		{
			for (int i = 0; i < 4; i++)
			{
				if (x + px[i] < n && y + py[i] < m && x + px[i] >= 0 && y + py[i] >= 0)
				{
					v++;
					x += px[i];
					y += py[i];
				}
			}
			break;
		}

		// 체스판을 넘어갈 때
		if (x >= n || y >= m)
			break;
	}

	cout << v;
	return 0;
}