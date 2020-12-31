#include <iostream>
#include <vector>
using namespace std;

int N, K, answer;
int A[201];
bool Belt[101];

void rotate(){
    for(int i=N-1; i>0; i--){
        if(Belt[i]){
            Belt[i+1]=true;
            Belt[i]=false;
        }
    }
    Belt[N]=false;

    int temp=A[2*N];
    for(int i=2*N; i>1; i--){
        A[i]=A[i-1];
    }
    A[1]=temp;
}

void robot(){
    for(int i=N-1; i>0; i--){
        if(Belt[i] && !Belt[i+1] && A[i+1]>0){
            Belt[i+1]=true;
            Belt[i]=false;
            A[i+1]--;
        }
    }
    Belt[N]=false;
}

int count(){
    int cnt=0;
    for (int i=1; i<=2*N; i++){
        if(A[i]==0){
            cnt++;
        }
    }
    return cnt;
}

int main(){
    cin>>N>>K;
    for (int i =1; i<=2*N; i++){
        cin>>A[i];
    }
    answer=0;
    while(true){
        rotate();
        robot();
        if(!Belt[1] && A[1]>0){
            Belt[1]=true;
            A[1]--;
        }
        answer++;
        if (count()>=K){
            break;
        }
    }
    cout<<answer;
	system("pause");
    return 0;
}