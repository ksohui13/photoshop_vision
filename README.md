![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=300&section=header&text=Simple%20Photoshop&fontSize=90&animation=fadeIn&fontAlignY=38&desc=computer%20vision&descAlignY=51&descAlign=62)

<p align='center'> IT융합공학과 2020101012 김소희 </p>

## 사용한 기술
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)

## 기능 개요
| 기능 | 기능 설명 |
| ------ |----------- |
| **파일** |  |
| 파일 열기 | 파일 열기 |
| 작업 취소 | 진행중인 작업을 전부 취소 |
| 나가기 | 포토샵 앱 종료 |
| **기본 편집** | |
| 확대 | 사진을 2배 확대 |
| 축소 | 사진을 2배 축소 |
| 회전(시계방향) | 사진을 시계방향으로 회전 |
| 회전(반시계방향) | 사진을 반시계방향으로 회전 |
| 좌우반전 | 사진을 좌우반전 |
| 상하반전 | 사진을 상하반전 |
| 자르기 | 사진을 [100:600, 200:700] 크기로 자름 |
| 축소 | 사진을 2배 축소 |
| 원형 자르기 | 사진을 원형으로 자르고 이외 부분은 검정색으로 처리 |
| **이미지** |  |
| 렌즈 왜곡 | 사진 중앙을 중심으로 렌즈 왜곡 |
| **색상** |  |
| 밝게 | 사진 밝기를 밝게 조절 |
| 어둡게 | 사진 밝기를 어둡게 조절 |
| 색상 반전 | RGB이미지를 BGR로 출력 |
| 역상 | bitwise not연산을 통해 이미지 값을 반대로 바꿈 |
| 흑백 | 사진을 흑백처리 |
| **필터** |  |
| 샤픈 | 사진에 sharpen 필터 처리 |
| 블러 | 사진을 흐리게(blur) 처리 |
| 가우시안 블러 | 3x3커널의 가우시안 블러, 값을 1/16형태로 계산하여 처리하여 노이즈 제거 |
| 미디언 블러링 | kernel 픽셀 값 중 중앙 값을 선택하여 잡음 제거 |
| 바이래터널 필터 | 가우시안 필터와 경계필터를 결합하여 경계는 유지하며 노이즈 제거 |
| 로버츠 교차 필터 | 사선 경계 검출 |
| 소벨 필터 | x축, y축, 대각선 방향의 경계 검출 |

## 기술 상세 설명
<p>파일 열기</p>

``` python3
def show_file_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, "이미지 열기", "./")
        print(file_name)
        self.image = cv2.imread(file_name[0]) #튜플 형태: 파일 주소
        h, w, _ = self.image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(self.image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label1.setPixmap(pixmap)
```
