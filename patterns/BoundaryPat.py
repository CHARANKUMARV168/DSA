# for the empty space after printing the conditional stars print space in else 
# normal diagonal : i == j 
# cross diagonal : i+j == constant in terms of n 
'''
pattern 1 :
* * * * * * * * * 
*               * 
*               * 
*               * 
*               * 
*               * 
*               * 
*               * 
* * * * * * * * * 
'''
n = 9
for i in range( 1,n+1,1):
    for j in range( 1, n+1,1):
        if i == 1 or i == 9 or j == 1 or j == 9 :
            print("* ",end='')
        else :
            print("  ",end='')
    print()

'''
normal diagonal :  i == j 
* * * * * * * * * 
* *             * 
*   *           * 
*     *         * 
*       *       * 
*         *     * 
*           *   * 
*             * * 
* * * * * * * * * 
'''
n = 9
for i in range( 1,n+1,1):
    for j in range( 1, n+1,1):
        if i == 1 or i == 9 or j == 1 or j == 9 :
            print("* ",end='')
        elif i == j or j == i:
            print("* ",end='')
        else :
            print("  ",end='')
    print()
'''
pattern 2 : 
cross diagonal : i+j = constant value = {n+1}
Intrusion  : if n = 9 the constant value is {n+1}

* * * * * * * * * 
* *           * * 
*   *       *   * 
*     *   *     * 
*       *       * 
*     *   *     * 
*   *       *   * 
* *           * * 
* * * * * * * * *
'''

n = 9
for i in range( 1,n+1,1):
    for j in range( 1, n+1,1):
        if i == 1 or i == 9 or j == 1 or j == 9 :
            print("* ",end='')
        elif i == j or j == i or i+j == n+1:
            print("* ",end='')
        else :
            print("  ",end='')
    print()

'''
pattern 3 :

* * * * * * * * * 
* *     *     * * 
*   *   *   *   * 
*     * * *     * 
* * * * * * * * * 
*     * * *     * 
*   *   *   *   * 
* *     *     * * 
* * * * * * * * * 

'''
n = 9
for i in range( 1,n+1,1):
    for j in range( 1, n+1,1):
        if i == 1 or i == 9 or j == 1 or j == 9 :
            print("* ",end='')
        elif i == j or j == i or i+j == n+1:
            print("* ",end='')
        elif i == n//2+1 or j == n//2+1:
            print("* ",end='')
        else :
            print("  ",end='')

    print()
'''
pattern 4 :
*                 
* *               
*   *             
*     *           
*       *         
*         *       
*           *     
*             *   
* * * * * * * * * 
'''
n = 9 
for i in range(1,n+1,1):
    for j in range( 1, n+1 ,1):
        if i == j :
            print("* ",end='')
        elif j == 1 :
            print("* ",end='')
        elif i == n :
            print("* ",end='')
        else :
            print("  ",end='')
    print()

'''
pattern 5 :

* * * * * * * * * 
*             *   
*           *     
*         *       
*       *         
*     *           
*   *             
* *               
*   
'''
n = 9 
for i in range(1,n+1,1):
    for j in range( 1, n+1 ,1):
        if i == 1 :
            print("* ",end='')
        elif i+j == n+1 :
            print("* ",end='')
        elif j == 1 :
            print("* ",end='')
        else :
            print("  ",end='')
    print()

'''
pattern 6 :
                * 
              * * 
            *   * 
          *     * 
        *       * 
      *         * 
    *           * 
  *             * 
* * * * * * * * * 
'''
n = 9 
for i in range(1,n+1,1):
    for j in range( 1, n+1 ,1):
        if i == n :
            print("* ",end='')
        elif i+j == n+1 :
            print("* ",end='')
        elif j == n :
            print("* ",end='')
        else :
            print("  ",end='')
    print()

'''
pattern 7 : 
* * * * * * * * * 
  *           *   
    *       *     
      *   *       
        *         
      *   *       
    *       *     
  *           *   
* * * * * * * * * 
'''
n = 9 
for i in range(1,n+1,1):
    for j in range( 1, n+1 ,1):
        if i == j or (i+j == n+1) :
            print("* ",end='')
        elif i == 1 :
            print("* ",end='')
        elif i == n :
            print("* ",end='')
        else :
            print("  ",end='')
    print()
'''
pattern 8 : 
*               * 
* *           * * 
*   *       *   * 
*     *   *     * 
*       *       * 
*     *   *     * 
*   *       *   * 
* *           * * 
*               * 
'''
n = 9 
for i in range(1,n+1,1):
    for j in range( 1, n+1 ,1):
        if i == j or (i+j == n+1) :
            print("* ",end='')
        elif j == 1 :
            print("* ",end='')
        elif j == n :
            print("* ",end='')
        else :
            print("  ",end='')
    print()

'''
pattern 9 :
        *         
      *   *       
    *       *     
  *           *   
*               * 
  *           *   
    *       *     
      *   *       
        *         
'''
n = 9
for i in range(1,n+1,1):
    for j in range( 1, n+1 ,1):
        if i+j+4 == n+1 or i == j+4 or i+4 == j or i+j==n+5 :
            print("* ",end='')

        else :
            print("  ",end='')
    print()