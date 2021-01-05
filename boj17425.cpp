#include <iostream>
using namespace std;

int main() {
	int T, N;
	cin >> T;
	for (int a = 0; a < T; a++) {
		int gx = 0;
		cin >> N;
		for (int i = 0; i < N + 1; i++) {
			for (int j = i; j > 0; j--) {
				if (i%j == 0){
					gx = gx + j;
				}
			}
		}
		cout << gx;
	}
	system("pause");
	return 0;
}