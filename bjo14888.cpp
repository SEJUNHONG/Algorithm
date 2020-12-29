#include <iostream>
using namespace std;

int N;
int num_list[11];
int operators[4];
int max_num = -99999;
int min_num = 99999;

void solution(int result, int idx) {
	if (idx == N) {
		if (result > max_num)
			max_num = result;
		if (result < min_num)
			min_num = result;
		return;
	}
	for (int i = 0; i < 4; i++) {
		if (operators[i] > 0) {
			operators[i]--;
			if (i == 0)
				solution(result + num_list[idx], idx + 1);
			else if (i == 1)
				solution(result - num_list[idx], idx + 1);
			else if (i == 2)
				solution(result * num_list[idx], idx + 1);
			else
				solution(result / num_list[idx], idx + 1);
			operators[i]++;
		}
	}
	return;
}

int main() {
	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> num_list[i];
	for (int i = 0; i < 4; i++)
		cin >> operators[i];
	solution(num_list[0], 1);
	cout << max_num << endl;
	cout << min_num;
	system("pause");
}