#include<stdio.h>
int main(){
  int n=0, i=0;
  float number[100]={0}, cgpa[100]={0}, chrs[100]={0}, sum_t[100]={0}, f_cgpa=0, sum=0, t_hrs=0;
  printf("Enter the number of courses: ");
  scanf("%d", &n);
  for(i=1; i<=n; i++){
    printf("Enter the final mark of course number %d: ",i);
    scanf("%f",&number[i]);

    if ((number[i]>=60) && (number[i]<=66)){
      cgpa[i]=1.0;
    }
    else if ((number[i]>=67) && (number[i]<=69)) {
      cgpa[i]=1.30;
    }
    else if ((number[i]>=70) && (number[i]<=72)) {
      cgpa[i]=1.70;
    }
    else if ((number[i]>=73) && (number[i]<=76)) {
      cgpa[i]=2.00;
    }
    else if ((number[i]>=77) && (number[i]<=79)) {
      cgpa[i]=2.30;
    }
    else if ((number[i]>=80) && (number[i]<=82)) {
      cgpa[i]=2.70;
    }
    else if ((number[i]>=83) && (number[i]<=86)) {
      cgpa[i]=3.00;
    }
    else if ((number[i]>=87) && (number[i]<=89)) {
      cgpa[i]=3.30;
    }
    else if ((number[i]>=90) && (number[i]<=92)) {
      cgpa[i]=3.70;
    }
    else if ((number[i]>=93) && (number[i]<=100)) {
      cgpa[i]=4.00;
    }
    else if ((number[i]>=0) && (number[i]<=59)) {
      cgpa[i]=0.00;
    }
    else{
      printf("Invalid mark input\n");
    }
    printf("Enter the credit hour of %d: ",i);
    scanf("%f",&chrs[i]);
    sum_t[i]=cgpa[i]*chrs[i];
    sum+=sum_t[i];
    t_hrs+=chrs[i];
  }
  f_cgpa=sum/t_hrs;
  printf("CGPA: %.2f",f_cgpa);

  return 0;
}
