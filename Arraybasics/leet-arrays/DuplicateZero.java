import java.util.*;
public class DuplicateZero {
    public static void main(String[] args) {

        int[] arr = {1,0,2,3,0,4,5,0};
        int pos = 0 ;
        int i = 0 ;
        int[] dest = new int[arr.length];
        while( i < arr.length && pos < arr.length){
            dest[i] = arr[pos];
            i++;
            if (arr[pos] == 0 && i < arr.length) {
                dest[i] = 0;
                i++;
            }
            pos++;
        }
        for( int j = 0 ; j < arr.length ; j++){
            arr[j] = dest[j];
        }
        System.out.println(Arrays.toString(dest));

    }
    
}
