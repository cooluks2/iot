# Kotlin 개발환경 구축

**OpenJDK 설치**

-   https://jdk.java.net/java-se-ri/13

    -   Windows 10 x64 Java Development Kit 다운로드
    -   C:\jdk-13로 압축 해제

-   `JAVA_HOME` 환경 변수 추가

    -   값: `C:\jdk-13`

        ![image-20201015150901738](00_Kotlin_개발환경_구축.assets/image-20201015150901738.png)  

-   PATH 환경변수에 값 추가
    -   `C:\jdk-13\bin`

<br>

**Kotlin 컴파일러 설치**

-   https://kotlinlang.org/docs/tutorials/command-line.html

    ![image-20201015151308385](00_Kotlin_개발환경_구축.assets/image-20201015151308385.png)    

    

    ![image-20201015151326440](00_Kotlin_개발환경_구축.assets/image-20201015151326440.png)  

-   PATH 환경 변수 값 추가
    -   C:\kotlinc\bin

<br>

**확인**

-   \> `java --version`
-   \> `kotlinc -version`

![image-20201015151811969](00_Kotlin_개발환경_구축.assets/image-20201015151811969.png)  

<br>

**Vscode Kotlin 확장팩 설치**

-   Kotlin language

![image-20201015151914541](00_Kotlin_개발환경_구축.assets/image-20201015151914541.png)  