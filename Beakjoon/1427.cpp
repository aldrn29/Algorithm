#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

//bool desc(int a, int b) {
//	return a > b;
//}

int main()
{

	int n;
	vector<int> v;

	cin >> n; 
	
	while (n != 0) 
	{
		int temp = n % 10;
		v.push_back(temp);
		n /= 10; 
	} 

	sort(v.begin(), v.end(), greater<int>()); //desc
	
	for (int i = 0; i < v.size(); i++) {
		cout << v[i];
	}
	return 0;
}