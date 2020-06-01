#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> inclination(vector<int>& p1, vector<int>& p2) {
	vector<int> v(2);
	v[0] = p2[0] - p1[0];
	v[1] = p2[1] - p1[1];
	return v;
}

bool ccw(vector<int>& p1, vector<int>& p2, vector<int>& p3) {
	vector<int> v = inclination(p1, p2), u = inclination(p2, p3);
	if ((long long)v[0] * u[1] > (long long)v[1] * u[0])
		return true;
	return false;
}

int convex_hull(vector<vector<int>>& positions) {
	vector<vector<int> > convex;
	convex.reserve(positions.size());
	for (vector<int>& p3 : positions) {
		while (convex.size() >= 2) {
			int l = convex.size();
			vector<int>& p1 = convex[l - 2];
			vector<int>& p2 = convex[l - 1];
			if (ccw(p1, p2, p3))
				break;
			convex.pop_back();
		}
		convex.push_back(p3);
	}
	return convex.size();
}

bool compare(vector<int>& p1, vector<int>& p2) {
	if (p1[0] == p2[0]) return p1[1] < p2[1];
	return p1[0] < p2[0];
}

int main(void) 
{
	// 포로 수용소의 크기 N, 포로의 수 M이 주어졌을 때, 
	// 감시 권한이 있는 포로와 없는 포로의 수를 출력하는 프로그램을 작성하시오. 

	int N, M, answer = -2;
	vector<vector<int>> v;
	
	// 입력
	cin >> N >> M;

	v.resize(M, vector<int>(2));
	for (int i = 0; i < M; i++)
		cin >> v[i][0] >> v[i][1];
	sort(v.begin(), v.end(), compare);
	answer += convex_hull(v);

	reverse(v.begin(), v.end());
	answer += convex_hull(v);

	// 출력
	cout << endl;
	cout << answer << " " << M - answer << endl;
	return 0;
}