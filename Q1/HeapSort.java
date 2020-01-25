

import java.io.BufferedReader;
import java.io.File;
import java.util.Scanner;

public class HeapSort {
    public static void swap(long[] heap, int first, int second){
        long tmp = heap[first];
        heap[first] = heap[second];
        heap[second] = tmp;
    }
    public static void heapify(long[] heap, int root, int end){
        int large = root;
        int leftChild = root*2 + 1;
        int rightChild = root*2 + 2;

        if(leftChild < end && heap[leftChild] > heap[large])
            large = leftChild;
        if(rightChild < end && heap[rightChild] > heap[large])
            large = rightChild;
        if(large != root){
            swap(heap, large, root);
            heapify(heap, large, end);
        }
    }

    public static void heapSort(long[] heap){
        for(int i = heap.length / 2 - 1; i >= 0; --i){
            heapify(heap, i, heap.length);
        }
        for(int i = heap.length - 1; i > 0; --i){
            swap(heap, i, 0);
            heapify(heap, 0, i);
        }
    }
    public static void main(String[] args) throws Exception{
        // write your code here
        File file = new File(args[0]);
        Scanner sc = new Scanner(file);
        int len = sc.nextInt();
        long[] nums = new long[len];
        for(int i = 0; i < len; ++i){
            nums[i] = sc.nextLong();
        }
        heapSort(nums);
        for(long num : nums){
            System.out.print(num + " ");
        }

    }
}
