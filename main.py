import sys, cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageQt
from PySide6.QtGui import QAction, QImage, QPixmap, QPainter, QIcon
from PySide6.QtWidgets import (QApplication,QWidget, QLabel, 
QMainWindow, QHBoxLayout, QVBoxLayout, 
QPushButton, QFileDialog, QToolBar, QStatusBar, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Photoshop")
        self.initUI()

#내부 UI
    def initUI(self):
        #toolbar-기능
        open_file = QAction(QIcon('./icons/open_folder_color.png'),"파일 열기", self)
        open_file.setStatusTip("파일 열기")
        open_file.triggered.connect(self.show_file_dialog)

        save_file = QAction(QIcon('./icons/save_color.png'), "저장", self)
        save_file.setStatusTip("저장")
        save_file.triggered.connect(self.save_file)

        clear_label = QAction(QIcon('./icons/delete_file.png'), "작업 전체 취소", self)
        clear_label.setStatusTip("작업 전체 취소")
        clear_label.triggered.connect(self.clear_label)

        exit = QAction(QIcon('./icons/logout_color.png'), "나가기", self)
        exit.setStatusTip("나가기")
        exit.triggered.connect(qApp.quit)

        self.statusBar()

        #toolbar 메뉴 추가
        toolbar = self.addToolBar('openfile')
        toolbar.addAction(open_file)
        toolbar = self.addToolBar('save_file')
        toolbar.addAction(save_file)
        toolbar = self.addToolBar('clear_label')
        toolbar.addAction(clear_label)
        toolbar = self.addToolBar('exit')
        toolbar.addAction(exit)
        

        #메인화면 레이아웃
        main_layout = QHBoxLayout()

        #사이드바 메뉴버튼
        # sidebar = QVBoxLayout()
        # button1 = QPushButton("이미지 열기")
        # button2 = QPushButton("저장")
        # button3 = QPushButton("이전")
        # button4 = QPushButton("작업 취소")
        # button5 = QPushButton("나가기")
        # #사이드바 메뉴-기능 연결
        # button1.clicked.connect(self.show_file_dialog) 
        # button2.clicked.connect(self.save_file)
        # #이전 기능 추가 예정
        # button4.clicked.connect(self.clear_label)
        # button5.clicked.connect(qApp.quit)
        # #사이드바에 메뉴버튼 추가(위젯)
        # sidebar.addWidget(button1)
        # sidebar.addWidget(button2)
        # sidebar.addWidget(button3)
        # sidebar.addWidget(button4)
        # sidebar.addWidget(button5)

        # main_layout.addLayout(sidebar)

        #----- 기능 ------
        #기본 편집
        #확대
        bigger = QAction("확대", self) #버튼 이름
        bigger.setStatusTip("확대") #setStatusTip : 커서를 올려뒀을 때 나오는 설명창
        bigger.triggered.connect(self.bigger) #연결할 기능

        #축소
        smaller  = QAction("축소", self) 
        smaller.setStatusTip("축소") 
        smaller.triggered.connect(self.smaller) 

        #회전
        rotation  = QAction("회전", self)
        rotation.setShortcut('Ctrl+r')
        rotation.setStatusTip("회전")
        rotation.triggered.connect(self.rotation)

        #좌우반전
        lr_flip  = QAction("좌우반전", self)
        lr_flip.setStatusTip("좌우반전")
        lr_flip.triggered.connect(self.lr_flip)

        #상하반전
        ud_flip  = QAction("상하반전", self)
        ud_flip.setStatusTip("상하반전")
        ud_flip.triggered.connect(self.ud_flip)

        #자르기
        cut = QAction("자르기", self) 
        cut.setStatusTip("자르기")
        cut.triggered.connect(self.cut) 

        #원형으로 자르기
        circle_cut = QAction("원형 자르기", self)
        circle_cut.setStatusTip("원형 자르기")
        circle_cut.triggered.connect(self.circle_cut)


        #이미지
        #뒤틀리기
        twist = QAction("뒤틀리기", self)
        twist.setStatusTip("뒤틀리기")
        twist.triggered.connect(self.twist)

        #리퀴파이
        liquefy = QAction("리퀴파이", self)
        liquefy.setStatusTip("리퀴파이")
        liquefy.triggered.connect(self.liquefy)

        #렌즈 왜곡
        distortion = QAction("렌즈 왜곡", self)
        distortion.setStatusTip("렌즈 왜곡")
        distortion.triggered.connect(self.distortion)

        #모자이크
        mosaic = QAction("모자이크", self)
        mosaic.setStatusTip("모자이크")
        mosaic.triggered.connect(self.mosaic)

        #합성
        compose = QAction("합성", self)
        compose.setStatusTip("합성")
        compose.triggered.connect(self.compose)


        #색상
        #밝기 조절
        bright = QAction("밝기 조절", self)
        bright.setStatusTip("밝기 조절")
        bright.triggered.connect(self.bright) 

        #색상반전
        color_inversion = QAction("색상 반전", self)
        color_inversion.setStatusTip("색상 반전")
        color_inversion.triggered.connect(self.color_inversion)

        #흑백
        gray_scale = QAction("흑백", self)
        gray_scale.setStatusTip("흑백")
        gray_scale.triggered.connect(self.gray_scale)


        #필터
        #블러
        blur = QAction("블러", self)
        blur.setStatusTip("블러")
        blur.triggered.connect(self.blur)

        #가우시안 블러
        gaussian_blur = QAction("가우시안 블러", self)
        gaussian_blur.setStatusTip("가우시안 블러")
        gaussian_blur.triggered.connect(self.gaussian_blur)

        #미디언 블러링
        median_blur = QAction("미디언 블러링", self)
        median_blur.setStatusTip("미디언 블러링")
        median_blur.triggered.connect(self.median_blur)

        #바이래터널 필터
        bilateral_filter = QAction("바이래터널 필터", self)
        bilateral_filter.setStatusTip("바이래터널 필터")
        bilateral_filter.triggered.connect(self.bilateral_filter)

        #경계 필터
        #로버츠 교차 필터
        roberts_filter = QAction("로버츠 교차 필터", self)
        roberts_filter.setStatusTip("로버츠 교차 필터")
        roberts_filter.triggered.connect(self.roberts_filter)

        #소벨필터
        sobel_filter = QAction("소벨 필터", self)
        sobel_filter.setStatusTip("소벨 필터")
        sobel_filter.triggered.connect(self.sobel_filter)

        #캐니 엣지 필터
        canny_edge = QAction("캐니 엣지 필터", self)
        canny_edge.setStatusTip("캐니 엣지 필터")
        canny_edge.triggered.connect(self.canny_edge)

        #흑백필터
        #binary
        binary = QAction("binary", self)
        binary.setStatusTip("binary")
        binary.triggered.connect(self.binary)

        #binary_inv
        binary_inv = QAction("binary_inv", self)
        binary_inv.setStatusTip("binary inverse")
        binary_inv.triggered.connect(self.binary_inv)

        #trunc
        trunc = QAction("trunc", self)
        trunc.setStatusTip("trunc")
        trunc.triggered.connect(self.trunc)

        #tozero
        tozero = QAction("tozero", self)
        tozero.setStatusTip("tozero")
        tozero.triggered.connect(self.tozero)

        #tozero_inv
        tozero_inv = QAction("tozero_inv", self)
        tozero_inv.setStatusTip("tozero inverse")
        tozero_inv.triggered.connect(self.tozero_inv)


        #그리기
        #원그리기
        circle = QAction("원", self)
        circle.setStatusTip("원")
        circle.triggered.connect(self.circle)
        
        #사각형 그리기
        square = QAction("사각형", self)
        square.setStatusTip("사각형")
        square.triggered.connect(self.square)

        #삼각형 그리기
        triangle = QAction("삼각형", self)
        triangle.setStatusTip("삼각형")
        triangle.triggered.connect(self.triangle)

        #직선 그리기
        line = QAction("직선", self)
        line.setStatusTip("직선")
        line.triggered.connect(self.line)

        #브러쉬
        brush = QAction("브러쉬", self)
        brush.setStatusTip("브러쉬")
        brush.triggered.connect(self.brush)

        #선택
        select = QAction("선택", self)
        select.setStatusTip("선택")
        select.triggered.connect(self.select)


        #---드랍메뉴 추가---
        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()
        file_menu1 = menu.addMenu("&기본 편집") #메뉴바에 메뉴 추가
        file_menu1.addAction(bigger)
        file_menu1.addAction(smaller)
        #분할선 추가
        separator = QAction(self)
        separator.setSeparator(True)
        file_menu1.addAction(separator)
        file_menu1.addAction(rotation)
        file_menu1.addAction(lr_flip)
        file_menu1.addAction(ud_flip)
        separator = QAction(self)
        separator.setSeparator(True)
        file_menu1.addAction(separator)
        file_menu1.addAction(cut)
        file_menu1.addAction(circle_cut)

        file_menu2 = menu.addMenu("&이미지")
        file_menu2.addAction(twist)
        file_menu2.addAction(liquefy)
        file_menu2.addAction(distortion)
        file_menu2.addAction(mosaic)
        file_menu2.addAction(compose)

        file_menu3 = menu.addMenu("&선택")
        file_menu3.addAction(select)

        file_menu4 = menu.addMenu("&색상")
        file_menu4.addAction(bright)
        file_menu4.addAction(color_inversion)
        file_menu4.addAction(gray_scale)

        file_menu5 = menu.addMenu("&필터")
        file_menu5.addAction(blur)
        file_menu5.addAction(gaussian_blur)
        file_menu5.addAction(median_blur)
        file_menu5.addAction(bilateral_filter)
        separator = QAction(self)
        separator.setSeparator(True)
        file_menu5.addAction(separator)
        file_menu5.addAction(roberts_filter)
        file_menu5.addAction(sobel_filter)
        file_menu5.addAction(canny_edge)
        separator = QAction(self)
        separator.setSeparator(True)
        file_menu5.addAction(separator)
        file_menu5.addAction(binary)
        file_menu5.addAction(binary_inv)
        file_menu5.addAction(trunc)
        file_menu5.addAction(tozero)
        file_menu5.addAction(tozero_inv)

        # file_menu6 = menu.addMenu("&경계필터")
        # file_menu6.addAction(roberts_filter)
        # file_menu6.addAction(sobel_filter)
        # file_menu6.addAction(canny_edge)

        # file_menu7 = menu.addMenu("&그리기")
        # file_menu7.addAction(circle)
        # file_menu7.addAction(square)
        # file_menu7.addAction(triangle)
        # file_menu7.addAction(line)
        # file_menu7.addAction(brush)
        
        #메인 화면 구성
        self.label1 = QLabel(self)
        # self.label1.setFixedSize(640, 480) #사이즈 고정
        main_layout.addWidget(self.label1)

        self.label2 = QLabel(self)
        self.label2.setFixedSize(640, 480) 
        main_layout.addWidget(self.label2)

        widget = QWidget(self)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

#------기능 관련 함수 -----

    #파일 불러오기
    def show_file_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, "이미지 열기", "./")
        print(file_name)
        self.image = cv2.imread(file_name[0]) #튜플 형태: 파일 주소
        h, w, _ = self.image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(self.image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label1.setPixmap(pixmap)
    
    #작업 취소
    def clear_label(self):
        self.label2.clear()

    #저장
    def save_file(self):
        # save_file = QFileDialog.getSaveFileName(self, "Save Image", "","PNG Files (*.png);;JPG Files (*.jpeg *.jpg );;Bitmap Files (*.bmp);;\ GIF Files (*.gif)")
        # if save_file == "" : #이름을 입력하지 않은 경우
        #     return False
        # else: 
        #     save_imave = cv2.imread(self.label2[0])
        #     cv2.imwrite(save_file[0], save_imave)
        #     self.label2.setText(save_file[0])

        # if self.image is None == False: #만약 사진이 있다면 #무슨 레이어를 인식하는거지..?
        #     image_file, _ = QFileDialog.getSaveFileName(self, "Save Image", "","PNG Files (*.png);;JPG Files (*.jpeg *.jpg );;Bitmap Files (*.bmp);;\
        #             GIF Files (*.gif)" )
        #     if image_file and self.image is None == False:
        #         self.image.save(image_file)
        #     else:
        #         QMessageBox.information(self, "Error", "이미지를 저장 할 수 없습니다.", QMessageBox.Ok)
        # else:
        #     QMessageBox.information(self, "이미지 없음", "저장 할 이미지가 없습니다.", QMessageBox.Ok)
        print("저장")

    #확대
    def bigger(self):
        print("확대")
    
    #축소
    def smaller(self):
        print("축소")
    
    #회전
    def rotation(self): #수정중
        h, w, _ = self.image.shape
        d90 = 90.0 * np.pi / 180.0 #90도
        m90 = np.float32([
            [np.cos(d90), -1*np.sin(d90), h],
            [np.sin(d90), np.cos(d90), 0]
        ])
        r90 = cv2.warpAffine(self.image, m90, (h, w))

        bytes_per_line = 3 * w
        image = QImage(r90.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

        print("회전")
    
    #좌우반전
    def lr_flip(self):
        image = cv2.flip(self.image, 1) #1은 좌우반전을 의미
        h, w, _ = image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    
    def ud_flip(self):
        print("상하반전")

    def cut(self):
        print("자르기")

    def circle_cut(self): #수정중
        h, w = self.image.shape[:2]
        mask = np.zeros_like(self.image)
        cv2.circle(mask, (int(w/2), int(w/2)), int(w/2), (255, 255, 255), -1)
        image = cv2.bitwise_and(self.image, mask)

        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("원형 자르기")

    def twist(self):
        print("뒤틀리기")

    def liquefy(self):
        print("리퀴파이")

    def distortion(self):
        h, w = self.image.shape[:2]
        exp = 2
        scale = 1
        mapy, mapx = np.indices((h, w), dtype=np.float32)

        mapx = 2 * mapx / (w - 1) -1
        mapy = 2 * mapy / (h - 1) -1

        r, theta = cv2.cartToPolar(mapx, mapy) #직교좌표를 극좌표로 변환
        r[r < scale] = r[r < scale] ** exp 

        mapx, mapy = cv2.polarToCart(r, theta) #극좌표를 직교좌표로 변환
        mapx = ((mapx + 1) * w - 1) /2 #좌상단으로 복귀
        mapy = ((mapy + 1) * h - 1) / 2 

        image = cv2.remap(self.image, mapx, mapy, cv2.INTER_LINEAR) #재매핑

        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

        print("렌즈왜곡")

    def mosaic(self):
        print("모자이크")

    def compose(self):
        print("사진 합성")

    def select(self):
        print("배경 선택")

    def bright(self):
        print("밝기 조절")

    def color_inversion(self):
        h, w, _ = self.image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(self.image.data, w, h, bytes_per_line, QImage.Format_BGR888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("색상 반전")

    def gray_scale(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        h, w = image.shape #높이 너비 채널
        bytes_per_line = 1 * w #흑백은 1차원 이미지
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("흑백")

    def blur(self):
        kernel = np.full((5, 5), 0.04)
        image = cv2.filter2D(self.image, -1, kernel)

        h, w, _ = image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("블러")

    def gaussian_blur(self):
        kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) * (1/ 16)
        image = cv2.filter2D(self.image, -1, kernel)

        h, w, _ = image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("가우시안 블러")

    def median_blur(self):
        image = cv2.medianBlur(self.image, 5)

        h, w, _ = image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("미디언 블러링")

    def bilateral_filter(self):
        image = cv2.bilateralFilter(self.image, 5, 75, 75)

        h, w, _ = image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("바이래터널 필터")

    def roberts_filter(self):
        gx_kernel = np.array([[1, 0],[0, -1]]) #x축의 경계만 나옴
        gy_kernel = np.array([[0, 1],[-1, 0]]) #y축의 경계만 나옴

        edge_gx = cv2.filter2D(self.image, -1, gx_kernel)
        edge_gy = cv2.filter2D(self.image, -1, gy_kernel)

        image = edge_gx + edge_gy

        h, w, _ = image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        
        print("로버츠 교차 필터")

    def sobel_filter(self):
        gx_kernel = np.array([[-1, 0, 1],[-2, 0, 2], [-1, 0, 1]]) 
        gy_kernel = np.array([[-1, -2, -1],[0, 0, 0], [1, 2, 1]]) 

        edge_gx = cv2.filter2D(self.image, -1, gx_kernel)
        edge_gy = cv2.filter2D(self.image, -1, gy_kernel)

        image = edge_gx + edge_gy

        h, w, _ = image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("소벨 필터")

    def canny_edge(self): #수정중
        image = cv2.Canny(self.image, 50, 200)
        h, w, _ = image.shape #높이 너비 채널

        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("캐니 엣지 필터")

    #임계값은 150
    def binary(self): #수정중
        image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        bin_image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
        
        h, w = image.shape #높이 너비 채널
        bytes_per_line = 1 * w
        # bin_image = QImage(self.image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        bin_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
        pixmap = QPixmap(bin_image)
        self.label2.setPixmap(pixmap)
        print("binary")

    def binary_inv(self): #수정중
        image = cv2.threshold(self.image, 150, 255, cv2.THRESH_BINARY_INV)
        h, w, _ = image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("binary_inv")

    def trunc(self): #수정중
        image = cv2.threshold(self.image,150, 255, cv2.THRESH_TRUNC)
        h, w, _ = image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("trunc")

    def tozero(self): #수정중
        image = cv2.threshold(self.image, 150, 255, cv2.THRESH_TOZERO)
        h, w, _ = image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("tozero")
 
    def tozero_inv(self): #수정중
        image = cv2.threshold(self.image, 150, 255, cv2.THRESH_TOZERO_INV)
        h, w, _ = image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("tozero_inv")


    def circle(self):
        print("원")

    def square(self):
        print("사각형")

    def triangle(self):
        print("삼각형")
    
    def line(self):
        qp = QPainter()
        qp.begin(self)
        self.draw_line(qp)
        qp.end()
        print("직선 그리기")

    def brush(self):
        print("브러쉬")
    


#창 보이기
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())