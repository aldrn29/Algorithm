#include <iostream>

using namespace std;

int cal(int kg)
{
	if (kg < 3) return -1;

	if (kg % 5 == 0) {
		return kg / 5;
	}

	for (int i = 0; i < 1000; i++)
	{
		for (int j = 0; j < 1000; j++)
		{
			if (kg == 3 * i + 5 * j)
			{
				return i + j;
			}
		}
	}

	if (kg % 3 == 0) {
		return kg / 3;
	}
	
	return -1;
}

int main()
{
	int kg; //n=3~5000
	cin >> kg;

	cout << cal(kg);

	return 0;
}