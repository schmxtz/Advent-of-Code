/* 
Input: String containing instructions
Output: Sum of all mul(X,Y) instructions
Example:
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Output: (2*4 + 5*5 + 11*8 + 8*5) = 161
*/

#include <stdio.h>

int main() {
  FILE *file_ptr;
  file_ptr = fopen("./data/day3.txt", "r");

  fclose(file_ptr);

  return 0;
}