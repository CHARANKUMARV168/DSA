//leetcode 1295 : Given an array nums of integers, return how many of them contain an even number of digits.


public class EvenDigits {
    public static void main(String[] args) {
        //int [] arr = {12,345,2,6,7896};
        int [] arr1 = {555,901,482,1771};
        int evenCount = 0 ;
        for (int num : arr1){
            if(isEven(num)){
                evenCount = evenCount + 1;
            }
        }
        System.out.println(evenCount);
    }
    public static boolean isEven(int num){
        int divCount = 0 ;
        while ( num != 0 ){
            num = num/10;
            divCount = divCount + 1;
        }
        return divCount % 2 == 0 ;
    }

    public static boolean isEven1(int num){
        String str = String.valueOf(num);
        return str.length()%2 == 0 ;
    }
}
