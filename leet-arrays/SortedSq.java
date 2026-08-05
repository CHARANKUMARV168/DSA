//leetcode 
import java.util.*;
public class SortedSq {
    public static void main(String[] args) {
       int[] arr = {-4,-1,0,3,10};
       int[] arr1 = {-7,-3,2,3,11};
       sortedsq1(arr);
       sortedsq2(arr1);
    }
    public static void sortedsq1(int [] arr){
        int N = arr.length ;
        int l = 0;
        int r = arr.length-1 ;
        int [] res = new int[arr.length];

        for ( int i = N-1 ; i >= 0 ; i --){
            if ( Math.abs(arr[l]) > Math.abs(arr[r]) ){
                res[i] = arr[l]* arr[l];
                l++;
            }else{
                res[i] = arr[r] * arr[r];
                r--;
            }
        }
        for ( int i = 0 ; i < arr.length ; i++){
            arr[i] = res[i] ;
        }
        System.out.println(Arrays.toString(arr));
    }
    public static void sortedsq2( int [] arr){
        int [] res = new int[arr.length];
        for ( int i = 0 ; i < arr.length ; i++){
            res[i] = arr[i]*arr[i];
        }
        Arrays.sort(res);
        System.out.println(Arrays.toString(res));
    }
}
