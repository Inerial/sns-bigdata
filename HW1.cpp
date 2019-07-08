/* 작성자 : 김기태
12/27   HW1 : 나에 대한 정보를 출력하는 프로그램을 작성하시오*/

#include <stdio.h>
void printAge(int n);
void printHeight(double m);

int main()
{
	char name[300] = "김기태";
	int age = 24;
	double height = 183.3;

	printf("성명 : %s\n", name);
	printAge(age);
	printHeight(height);

	return 0;
}
void printAge(int n)
{
	printf("나이 : %d\n", n);
	return;
}
void printHeight(double m)
{
	printf("신장 : %lf\n", m);
	return;
}