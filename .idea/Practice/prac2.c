#include<stdio.h>
int main(){
  int n, i, number[100];
  float cgpa[100], chrs[100], f_cgpa;
  printf("Enter the number of courses: ");
  scanf("%d", &n);
  for(i=1; i<=n; i++){
    printf("Enter the final mark of course number %d: ",i);
    scanf("%d",&number[i]);
    printf("Enter the credit hour of %d: ",i);
    scanf("%f",&chrs[i]);
  }
  f_cgpa=(cgpa*chrs)/n;
  printf("CGPA: %f",fcgpa);

  return 0;
}
