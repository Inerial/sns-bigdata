/* �ۼ��� : �����
12/27   HW1 : ���� ���� ������ ����ϴ� ���α׷��� �ۼ��Ͻÿ�*/

#include <stdio.h>
void printAge(int n);
void printHeight(double m);

int main()
{
	char name[300] = "�����";
	int age = 24;
	double height = 183.3;

	printf("���� : %s\n", name);
	printAge(age);
	printHeight(height);

	return 0;
}
void printAge(int n)
{
	printf("���� : %d\n", n);
	return;
}
void printHeight(double m)
{
	printf("���� : %lf\n", m);
	return;
}