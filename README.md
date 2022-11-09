![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=300&section=header&text=Simple%20Photoshop&fontSize=90&animation=fadeIn&fontAlignY=38&desc=computer%20vision&descAlignY=51&descAlign=62)

<p align='center'> IT융합공학과 2020101012 김소희 </p>
<div align='center'> 
        <img src = "https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white"/>
        <img src = "https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white"/>
        <img src = "https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white"/>
</div>

## 기능 개요
| 기능 | 기능 설명 |
| ------ |----------- |
| **🔴파일** |  |
| 파일 열기 | 파일 열기 |
| 작업 취소 | 진행중인 작업을 전부 취소 |
| 나가기 | 포토샵 앱 종료 |
| **🟠기본 편집** | |
| 확대 | 사진을 2배 확대 |
| 축소 | 사진을 2배 축소 |
| 회전(시계방향) | 사진을 시계방향으로 회전 |
| 회전(반시계방향) | 사진을 반시계방향으로 회전 |
| 좌우반전 | 사진을 좌우반전 |
| 상하반전 | 사진을 상하반전 |
| 자르기 | 사진을 [100:600, 200:700] 크기로 자름 |
| 축소 | 사진을 2배 축소 |
| 원형 자르기 | 사진을 원형으로 자르고 이외 부분은 검정색으로 처리 |
| **🟡이미지 왜곡** |  |
| 볼록렌즈 | 사진 중앙을 중심으로 볼록렌즈 효과 |
| 오목렌즈 | 사진 중앙을 중심으로 오목렌즈 효과 |
| **🟢색상** |  |
| 밝게 | 사진 밝기를 밝게 조절 |
| 어둡게 | 사진 밝기를 어둡게 조절 |
| 색상 반전 | RGB이미지를 BGR로 출력 |
| 역상 | bitwise not연산을 통해 이미지 값을 반대로 바꿈 |
| 흑백 | 사진을 흑백처리 |
| **🔵필터** |  |
| 샤픈 | 사진에 sharpen 필터 처리 |
| 블러 | 사진을 흐리게(blur) 처리 |
| 가우시안 블러 | 3x3커널의 가우시안 블러, 값을 1/16형태로 계산하여 처리하여 노이즈 제거 |
| 미디언 블러링 | kernel 픽셀 값 중 중앙 값을 선택하여 잡음 제거 |
| 바이래터널 필터 | 가우시안 필터와 경계필터를 결합하여 경계는 유지하며 노이즈 제거 |
| 로버츠 교차 필터 | 사선 경계 검출 |
| 소벨 필터 | x축, y축, 대각선 방향의 경계 검출 |

## 기능 설명

#### 1. 원형자르기
- 사진을 원형으로 자르고 이외 부분은 검정색으로 처리
![원형자르기](https://user-images.githubusercontent.com/111819641/200733614-9b57f70a-9be5-466b-8bc8-1666051463ac.png)

#### 2. 오목렌즈
- 사진 중앙을 중심으로 오목렌즈 효과
![오목렌즈](https://user-images.githubusercontent.com/111819641/200733675-fa4e388f-f1f9-4701-9acb-aa4604ea7b67.png)

#### 3. 역상
- bitwise not연산을 통해 이미지 값을 반대로 바꿈
![역상](https://user-images.githubusercontent.com/111819641/200733710-76ab3031-49d4-434f-b9e4-f5ce54ad8760.png)

#### 4. 미디언블러링
- kernel 픽셀 값 중 중앙 값을 선택하여 잡음 제거
![미디언 블러링](https://user-images.githubusercontent.com/111819641/200733737-f67a1b62-84b0-4f14-8313-95e5703f414c.png)

#### 5. 소벨필터
- x축, y축, 대각선 방향의 경계 검출
![소벨필터](https://user-images.githubusercontent.com/111819641/200733759-639bc29f-060a-4d22-a8ee-67f4de41e8e3.png)
