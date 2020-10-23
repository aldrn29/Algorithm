#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> v;

long long result = 0;

void bubbleSort(int n, vector<int>& v) {

	int swap = 0;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n - i - 1; j++)
		{
			if (v[j] > v[j + 1]) {
				int temp;
				temp = v[j];
				v[j] = v[j + 1];
				v[j + 1] = temp;

				result++;
			}
		}
	}
}

void mergeSort(vector<int>& v, int start, int end) 
{
	int left = start;
	int mid = (start + end) / 2;
	int right = mid + 1;

	vector<int> sorted;

	if (start >= end) return;

	mergeSort(v, start, mid);
	mergeSort(v, mid + 1, end);

	// 작은 순서대로 삽입
	while (left <= mid && right <= end) 
	{
		if (v[left] <= v[right]) {
			sorted.push_back(v[left]);
			left++;
		}
		else {
			sorted.push_back(v[right]);
			right++;
			result += mid - left + 1;
		}
	}

	// 남은 데이터 삽입
	while (left <= mid) {
		sorted.push_back(v[left]);
		left++;
	}
	while (right <= end) {
		sorted.push_back(v[right]);
		right++;
	}

	// 정렬된 데이터 삽입
	for (int i = start, j = 0; i <= end; ++i, ++j) {
		v[i] = sorted[j];
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;
	v.resize(n);

	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}

	//bubbleSort(n, v);
	mergeSort(v, 0, n - 1);
	cout << result;

	/*
	for (int i = 0; i < n; i++) {
		cout << v[i];
	}
	*/

	return 0;
}