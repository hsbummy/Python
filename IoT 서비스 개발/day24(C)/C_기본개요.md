# 수업개요



1. C의 기본 = > IoT를 위한 기능
   * 개발환경 작성
   * visual studio 이용방법
   * 표준입출력
   * c언어를 이용해서 프로그램 작성하기
   * 데이터 타입
   * 연산자
   * 기본제어문
   * 함수
   * 메모리와 포인터





1. 아두이노 제어 => 기본장비제어, 통신(I2C, 블루투스, wifi, 웹서버 통신)
2. 라즈베리파이 => os 설치, 장비제어
3. MQTT => IoT에서 발생하는 데이터 수집 제어, 모니터링 시스템
4. 웹서버 연동 => 데이터베이스, RestAPI
5. 안드로이드 => 코틀린



# 1강

* 소스코드 작성 (xxx.c) > 컴파일러를 이용하여 컴파일 > 오브젝트 코드(xxx.obj), 생성 , ex)라이브러리 코드 >(링커) >  실행파일(xxx.exe)

```c
#include <stdio.h>

//한 줄 주석문 달기

/*
여러줄 주석문
*/
int main()
{
	printf("hello\n world\n");
	return 7;
}
```



[실습 1]

강사메일 : heaves@hanmail.net

- iot 폴더에 myc 폴더를 생성하고 mysol 솔루션 생성
- firstPro 프로젝트를 만들고 c 로 변환
- 템플릿 생성: MyTemplate
- SecondPro프로젝트 생성(템플릿으로)
- exam01.c 작성
  - 이름과 이메일을 출력하는 프로그램을 작성
  - 다른행에 출력하고 문자열 출력하는 함수는 한 번만 사용하기



```c
#include <stdio.h>


/*메인함수
입력(매개변수-void)
출력(리턴값 - int)

시작함수 안에 함수를 부르고 그 안에 또 다른 함수를 부를 수 있다
*/
int main(void) // main 함수(caller) > 매개변수(call) printf함수(callee)를 부르고 다시 (return) > main 함수
{
	/* 프로그램에서 표현하고 싶은 내용을 정의*/
}
```





* 변수의 타입을 설정하는 이유 : 메모리 할당



```c
#include <stdio.h>


/*메인함수
입력(매개변수-void)
출력(리턴값 - int)

시작함수 안에 함수를 부르고 그 안에 또 다른 함수를 부를 수 있다
*/
int main(void) // main 함수(caller) > 매개변수(call) printf함수(callee)를 부르고 다시 (return) > main 함수
{
	/* 프로그램에서 표현하고 싶은 내용을 정의*/
	int num1;
	int num2;
	int a;

	num1 = 100;
	num2 = 200;
	a = num1 + num2;

	printf("연산 결과 : %i", a);
	return 0;
}


int main(void) // main 함수(caller) > 매개변수(call) printf함수(callee)를 부르고 다시 (return) > main 함수
{
	/* 프로그램에서 표현하고 싶은 내용을 정의*/
	//int num1;
	//int num2;
	//int result;
	int num1 = 100, num2 = 200, result;

	/*num1 = 100;
	num2 = 200;*/
	result = num1 + num2;

	printf("변수 num1 = %i, 변수 num2 = %d\n", num1, num2);
	printf("연산 결과 : %i", result);
	return 0;
}
```



* 디버그 : 코드 검사, 메모리 누수 관리



* 예제 
  * c파일을 추가하고 파일명은 exam02.c
  * 숫자를 입력받아 입력받은 숫자에 100 곱한 결과를 출력하기
* 출력형태
  * 입력값:  200
  * 연산결과 : 20000

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main()
{
	int num = 0;
	printf("값을 입력하세요:");
	scanf("%d", &num);
	printf("연산결과 : %d", num * 100);
	return 0;
}
```



* if loop

```c
#include <stdio.h>


int main(void)
{
	int num = 0;
	if (num >= 0) {
		printf("good\n");
	}
	else {
		printf("not good\n");
	}
	printf("fuck\n");
}


#include <stdio.h>

//매개변수 없고, 리턴값도 없는 함수의 정의
void display(void)
{
	printf("ok\n");
	return;
}

int main(void)
{
	int num = 0;
	if (num >= 0) {
		//조건이 만족했을 때 실행할 블럭
		printf("good\n");
	}
	else {
		//조건이 만족하지 않을 때 실행할 문장
		printf("not good\n");
	}
	//printf("fuck\n");
	//printf("fuck\n");
	//printf("fuck\n");
	//printf("fuck\n");
	//printf("fuck\n");
	display();
	return 0;
}
```



* 함수의 사용

```c
#include <stdio.h>

//1. 매개변수 없고 리턴값이 없는 함수
//2. 매개변수 있고, 리턴값이 있는 함수
int add(int num1, int num2)
{
	int result = num1 + num2;
	//매개변수를 연산한 결과를 리턴
	return result;
}
int main(void)
{
	int result = 0;
	result = add(100, 200);
	printf("연산결과 : %d", result);
}
```



[실습3]

- exam03.c 작성하기
  - 함수로 작업
  - 요금 계산하기
  - 기본요금 : 10000원
  - 청소년(20세미만) : 기본요금의 30% 할인
  - 요금계산하는 로직은 함수로 처리하고 main 함수에서 호출하여 작업

* 출력형태
  * 16 > 입력 : 기본요금 7000원 입니다.
  * 22 > 입력 : 기본요금은 10000원 입니다.

```c
내가 작성한 예제
int main()
{
	int age = 0;
	int charge = 10000;
	printf("나이를 입력하세요\n");
	scanf("%d", &age);
	if (age > 20)
	{
		printf("기본요금 %d 원 입니다.", charge);
	}
	else {
		printf("기본요금 %d 원 입니다.", charge - 3000);
	}
	return 0;
}    
    

강사님이 작성한 예제
    
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int calc(int age)
{
	int price = 0;
	if (age < 20)
	{
		price = 10000 * 0.7;
	}
	else {
		price = 10000;
	}
	return price;
}





int main(void)
{
	int age = 0, result = 0;
	printf("나이 : ");
	scanf("%d", &age);
	result = calc(age);
	printf("기본요금은 %d 원 입니다.", result);
	return 0;
}
```

