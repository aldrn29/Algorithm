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
			// �̵��� �� �ִٸ�
			if (x + px[i] < n && y + py[i] < m && x + px[i] >= 0 && y + py[i] >= 0)
			{
				v++;
				x += px[i];
				y += py[i];
			}
			if (v > 4) { // �̵����� �ɷ��� ��
				cons = true;
				v = 1;
				break;
			}
		}

		// �̵� ���� �ɷ��� ���� ��� �̵���� �����Ͽ�
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

		// ü������ �Ѿ ��
		if (x >= n || y >= m)
			break;
	}

	cout << v;
	return 0;
}