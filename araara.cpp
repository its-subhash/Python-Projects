#include <iostream>
using namespace std;
int main(){
    const int length =4;
    int arr[length]= {1,2,3,4};
    
    double sum=0;

    for (int i=0; i< length; i++){
        sum += arr[i];
    }
    double mean= sum/length;
    
    cout <<"The mean value of given array is :"<< mean<< endl;

}
