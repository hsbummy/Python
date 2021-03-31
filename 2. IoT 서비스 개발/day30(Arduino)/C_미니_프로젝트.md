# C 미니 프로젝트



## 주차 관리 프로그램



```c
#include <stdio.h>


int ParkingMenu(void);
void InParking(int(*parr)[10], int floor, int num1);
void NowParking(int (*parr)[10]);
void CheckParking(int(*parr)[10]);
int Parkingarr[3][10];
int main()
{
	
	int (*parr)[10] = Parkingarr;
	int menuIndex = 0;
	

	while ((menuIndex = ParkingMenu()) != 0)
	{
		switch (menuIndex)
		{
		case 1:
			
			printf("1. 주차\n");
			
			int num1 = 0;
			printf("주차할 차번 입력(숫자 4자리) : ");
			scanf_s("%d", &num1);
			InParking(parr, 0, num1);
			break;
		case 2:
			printf("2. 출차\n");
			//OutParking();
			break;
		case 3:
			printf("3. 주차현황 출력\n");
			NowParking(parr);
			break;
		case 4:
			printf("4. 층별 빈 주차 공간 확인하기\n");
			CheckParking(parr);
			break;
		default:
			printf("잘못선택\n");
			break;
		}
	}
	printf("종료");
	return 0;
}


int ParkingMenu(void)
{
	int inputValue = 0;
	printf("--------------주차관리시스템---------------\n\n");
	printf("1. 주차\t2. 출차\t3. 주차현황 출력\t4. 층별 빈 주차 공간 확인하기\t0. 종료\n");
	printf("번호 선택 : ");
	scanf_s("%d", &inputValue);
	return inputValue;
}

void InParking(int(*parr)[10], int floor, int num1)
{
	int num2, num3, num4;
	printf("다른층 0, 취소 -1 : ");
	scanf_s("%d", &num2);
	if (num2 == 0)
	{
		printf("층 수를 입력하세요 : ");
		scanf_s("%d", &num3);
		printf("주차할 장소를 입력하세요\n");
		InParking(parr, num3-1, num1);
	}
	else if (num2 == -1)
	{
		printf("취소\n");
	}
	else
	{	
		parr[floor][num2-1] = num1;
	}
	
}


void NowParking(int(*parr)[10])
{
	for (int i = 0; i < 3; i++)
	{
		printf("-------------------------------B%d층-------------------------------\n\n", i+1);
		for (int j = 0; j < 10; j++)
		{
			printf("%d\t", *(parr[i] + j));
		}
		printf("\n\n");
	}
}

void CheckParking(int(*parr)[10])
{
	int check;
	printf("층을 입력하세요(B1층 = 1, B2층 = 2, B3층 = 3 : ");
	scanf_s("%d", &check);
	if (check == 1)
	{
		printf("-----------------B1층---------------\n\n");
		for (int i = 0; i < 10; i++)
		{
			
			printf("%d\t", parr[0][i]);
		}
		printf("\n");
	}
	else if(check == 2)
	{
		printf("-----------------B2층---------------\n\n");
		for (int i = 0; i < 10; i++)
		{
			
			printf("%d\t", parr[1][i]);
		}
		printf("\n");
	}
	else
	{
		printf("-----------------B3층---------------\n\n");
		for (int i = 0; i < 10; i++)
		{
			
			printf("%d\t", parr[2][i]);
		}
		printf("\n");
	}
}
```



