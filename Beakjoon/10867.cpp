#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() 
{
	int number;
	cin >> number;

	vector<int> v; 
	vector<int> result;
	
	for (int i = 0; i < number; i++)
	{ 
		int n;
		cin >> n;
        v.push_back(n);
	} 

	sort(v.begin(), v.end());
	
	while (v.size() > 1)
	{
		if (v[0] == v[1]) {
			v.erase(v.begin());
		}
		else {
			result.push_back(v.front());
			v.erase(v.begin());
		}
	}
	
	result.push_back(v.front());
	for (int i = 0; i < result.size(); i++)
	{
		cout << result[i] << " ";
	} 

	return 0;

}