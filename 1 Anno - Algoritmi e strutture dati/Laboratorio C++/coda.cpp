#include <iostream>
#include <queue>

using namespace std;
/*Usa la libreria queue nativa di c++
*/

int main(){

    queue<int> queue;
    queue.push(10);
    queue.push(20);
    queue.push(30);
    queue.push(40);
    cout<<queue.size()<<endl;;

    while (!queue.empty()) {
        int front = queue.front();
        cout << front <<endl;
        queue.pop();
    }
    return 0;
}

