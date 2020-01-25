#include<iostream>
#include <bits/stdc++.h> 



void merge(long*list, int left, int mid, int right){
	int i = left, j = mid+1, idx = 0;
	long*tmp = new long[right - left + 1];

	while(i <= mid && j <= right){
		if(list[i] < list[j]){
			tmp[idx++] = list[i++];
		}else{
			tmp[idx++] = list[j++];
		}
	}


	while(i <= mid) tmp[idx++] = list[i++];
	while(j <= right) tmp[idx++] = list[j++];


	for(idx = 0, i = left; i <= right; ++i, ++idx){
		list[i] = tmp[idx];
	}

	delete[] tmp;

}
void mergeSort(long* list, int left, int right){
	if(left < right){
		int mid = left + (right - left)/2;
		mergeSort(list, left, mid);
		mergeSort(list, mid+1, right);
		merge(list, left, mid, right);
	}
}

int main(){
	
	int n;
	std::cin >> n;
	long* list = new long[n];
	for(int i = 0; i < n; ++i){
		std::cin >> list[i];
	}
	mergeSort(list, 0, n - 1);
	for(int i = 0; i < n; ++i){
		std::cout << list[i] << " ";	
	}
	std::cout << "\n";
	delete[] list;
	return 0;
}


