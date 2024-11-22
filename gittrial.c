/* 
calculating sum and average of floats

Damisola Talabi

10/10/2023

*/
#include <stdio.h>

int main()
{
    float num1 =0;
    float num2 =0;
    float num3 =0;
    float sum = 0;
    float average = 0;


    printf("Enter your first decimal number\n");
    scanf("%f",&num1);

    printf("Enter your second decimal number\n");
    scanf("%f",&num2);

    printf("Enter your third decimal number\n");
    scanf("%f",&num3);

     //sum adds the three numbers
    sum = num1 + num2 + num3;

    //average is the sum divided by the total
    average= sum/3;


    printf("The sum of the three numbers is %.3f",sum);
    printf("\nThe average of the three numbers is %.3f",average);
    
    return 0;

}