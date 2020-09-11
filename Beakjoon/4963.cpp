#include <iostream>
using namespace std;

int w, h;
bool c[50][50];
int a[50][50];
int tx[8]		= { -1, -1, -1, 0, 0, 1, 1, 1 };
int ty[8]		= { -1, 0, 1, -1, 1, -1, 0, 1 };
int result		= 0;

void DFS(int x, int y)
{
	c[x][y] = true;

	for (int i = 0; i < 8; i++)
	{
		// 없는 땅인 경우 
		if (x + tx[i] < 0 || x + tx[i] > h - 1 || 
			y + ty[i] < 0 || y + ty[i] > w - 1)
			continue;

		// c[x-1][y-1]  c[x-1][y]  c[x-1][y+1]
		// c[x][y-1]               c[x][y+1]
		// c[x+1][y-1]  c[x+1][y]  c[x+1][y+1]

		// 근접한 곳이 땅이고, 안가본 곳이면 다시 탐색
		if (a[x + tx[i]][y + ty[i]] == 1 && c[x + tx[i]][y + ty[i]] == false)
			DFS(x + tx[i], y + ty[i]);
	}
}

int main()
{
	cin >> w >> h;

	while (w + h != 0)
	{
		// 초기화
		result = 0;
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				c[i][j] = false;
				a[i][j] = 0;
			}
		}

		// 입력
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				cin >> a[i][j];
			}
		}

		// 검사
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				// 땅이고 안가본 곳에서 검사 시작
				if (a[i][j] == 1 && c[i][j] == false)
				{
					DFS(i, j);
					result++;
				}
			}
		}
		
		cout << result << endl;
		cin >> w >> h;
	}

	return 0;
}