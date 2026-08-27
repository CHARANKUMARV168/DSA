//leetcode 485 : Given a binary array nums, return the maximum number of consecutive 1's in the array.

public class ConsecutiveOne {
    public static void main(String[] args) {
        //int[] arr = {1,1,0,1,1,1};
        int[] arr1 = {1,0,1,1,0,1};
        int maxcount = 0 ;
        int onecount = 0 ;

        for ( int num : arr1){
            if ( num == 1 ){
                onecount = onecount + 1 ;
            }else{
                maxcount = Math.max(maxcount, onecount);
                onecount = 0 ;
            }
        }

        System.out.println(Math.max(maxcount, onecount));
    }
    
}
