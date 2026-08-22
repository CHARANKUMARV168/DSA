//leetcode 88 : You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

import java.util.Arrays;

public class MergeSorted {
    public static void main(String[] args){
        int[] nums1 = {1,2,3,0,0,0};
        int[] nums2 = {2,5,6};
        int m = 3;
        int n = 3;
        merge(nums1,m,nums2,n);

    }
    public static void merge1(int[] nums1, int m, int[] nums2, int n){
        for (int i = 0 ; i < n ; i++){
            nums1[i+m] = nums2[i];
        }
        Arrays.sort(nums1);
        System.out.println(Arrays.toString(nums1));

    }
    public static void merge2(int[] nums1, int m, int[] nums2, int n){
        int[] nums1copy = new int[m];
        for ( int i = 0 ; i < m ; i++){
            nums1copy[i] = nums1[i] ;
        }
        int p1 = 0 ;
        int p2 = 0 ;
        for ( int p = 0 ; p < m + n ; p++ ){
            if( p2 >= n || (p1 < m && nums1copy[p1] < nums2[p2]) ){
               nums1[p] = nums1copy[p1];
               p1++;
            }else{
                nums1[p] = nums2[p2];
                p2++;
            }

        }
        System.out.println(Arrays.toString(nums1));
    }

    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int l = 0 ;
        int i = 0 ;
        while( i < nums1.length ){
            if( nums1[i] == 0 && l < n){
                nums1[i] = nums2[l];
                l++;
                i++;
            }else{
                i++;
            }
        }
        Arrays.sort(nums1);
        System.out.println(Arrays.toString(nums1));
    }
    
}
