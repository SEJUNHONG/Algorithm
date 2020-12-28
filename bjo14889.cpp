#include <iostream>
#include <cmath>
using namespace std;

int match[20][20];
bool visited[20];
int N;
int answer = 10000;

void solution(int cnt, int cur) {
	if (cnt == N / 2) {
		int result1 = 0;
		int result2 = 0;
		for (int i = 0; i < N; i++) {
			for (int j = i + 1; j < N; j++) {
				if (visited[i] && visited[j]) {
					result1 += (match[i][j] + match[j][i]);
				}
				else if (!visited[i] && !visited[j]) {
					result2 += (match[i][j] + match[j][i]);
				}
			}
		}
		answer = __min(answer, abs(result1 - result2));
	}
	for (int i = 0; i < N; i++) {
		if (visited[i] == false && i > cur) {
			visited[i] = true;
			solution(cnt + 1, i);
			visited[i] = false;
		}
	}
}

int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> match[i][j];
		}
	}
	solution(0, -1);
	cout << answer << endl;
	system("pause");
}