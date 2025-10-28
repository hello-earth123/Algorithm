#include <iostream>
#include <string>
#include <array>
using namespace std;


int main() {
    string S;
    array<int, 26> word;
    word.fill(-1);
    bool char_in = false;
    int count = 0;

    cin >> S;

    for (char ch : S) {
        if (word[ch - 'a'] == -1 ) {
            word[ch - 'a'] = count;
        }
        count++;
    }
    
    for (int i = 0; i < 26; i++) {
        cout << word[i] << " ";
    }
}