import java.util.*;

public class PS2751_2 {

    public static void quickSort(int[] arr, int start, int end) {
        if(start >= end) return;
        int pivot = start;
        int left = start + 1;
        int right = end;
        while(left <= right) {
            while(left <= end && arr[left] <= arr[pivot]) left++;
            while(right > start && arr[right] >= arr[pivot]) right--;
            if(left > right) {
                int temp = arr[pivot];
                arr[pivot] = arr[right];
                arr[right] = temp;
            }
            else {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
            }
        }
        quickSort(arr, start, right - 1);
        quickSort(arr, right + 1, end);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }

        quickSort(arr, 0, n-1);

        for(int i=0; i<n; i++) {
            System.out.println(arr[i]);
        }
    }
}
