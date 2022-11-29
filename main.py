import sys, cv2
import cvlib as cv
import numpy as np 
from PySide6.QtGui import QAction, QImage, QPixmap, QIcon
from PySide6.QtWidgets import (QApplication,QWidget, QLabel, 
QMainWindow, QHBoxLayout, QVBoxLayout, 
QPushButton, QFileDialog, QToolBar, QStatusBar, QMessageBox)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Photoshop")
        self.setWindowIcon(QIcon('./icons/editor2.png'))
        self.initUI()

#내부 UI
    def initUI(self):
        #toolbar-기능
        open_file = QAction(QIcon('./icons/open4.png'),"파일 열기", self)
        open_file.setStatusTip("파일 열기")
        open_file.triggered.connect(self.show_file_dialog)

        save_file = QAction(QIcon('./icons/save4.png'), "저장", self)
        save_file.setStatusTip("저장")
        save_file.triggered.connect(self.save_file)

        clear_label = QAction(QIcon('./icons/delete2.png'), "작업 전체 취소", self)
        clear_label.setStatusTip("작업 전체 취소")
        clear_label.triggered.connect(self.clear_label)

        exit = QAction(QIcon('./icons/close.png'), "나가기", self)
        exit.setStatusTip("나가기")
        exit.triggered.connect(self.exit_window)

        self.statusBar()

        #toolbar 메뉴 추가
        toolbar = self.addToolBar('openfile')
        toolbar.addAction(open_file)
        toolbar.setStyleSheet("background-color: #E8EAED;") 
        toolbar = self.addToolBar('save_file')
        toolbar.addAction(save_file)
        toolbar.setStyleSheet("background-color: #E8EAED;")
        toolbar = self.addToolBar('clear_label')
        toolbar.setStyleSheet("background-color: #E8EAED;")
        toolbar.addAction(clear_label)
        toolbar.setStyleSheet("background-color: #E8EAED;")
        toolbar = self.addToolBar('exit')
        toolbar.addAction(exit)
        toolbar.setStyleSheet("background-color: #E8EAED;")
        

        #메인화면 레이아웃
        main_layout = QHBoxLayout()

        #사이드바 메뉴버튼
        sidebar = QVBoxLayout()
        sidebar.setContentsMargins(20, 100, 50, 100) #sidebar 마진 설정 #왼, 위, 오, 아
        button1 = QPushButton("회전(90)")
        button1.setFixedHeight(50) #버튼 높이 고정
        button2 = QPushButton("회전(-90)")
        button2.setFixedHeight(50)
        button3 = QPushButton("좌우반전")
        button3.setFixedHeight(50)
        button4 = QPushButton("상하반전")
        button4.setFixedHeight(50)
        # #사이드바 메뉴-기능 연결
        button1.clicked.connect(self.rotation_clock) 
        button2.clicked.connect(self.rotation_counter)
        button3.clicked.connect(self.flip)
        button4.clicked.connect(self.flip_v)
        # #사이드바에 메뉴버튼 추가(위젯)
        sidebar.addWidget(button1)
        sidebar.addWidget(button2)
        sidebar.addWidget(button3)
        sidebar.addWidget(button4)

        main_layout.addLayout(sidebar)

        #----- 기능 ------
        #파일
        #파일 열기
        show_file_dialog = QAction(QIcon('./icons/folder.png'), "파일 열기", self)
        show_file_dialog.setShortcut('Ctrl+o')
        show_file_dialog.setStatusTip("파일 열기")
        show_file_dialog.triggered.connect(self.show_file_dialog)

        #저장
        save_file = QAction(QIcon('./icons/save.png'),"저장",self)
        save_file.setShortcut('Ctrl+s')
        save_file.setStatusTip("저장")
        save_file.triggered.connect(self.save_file)

        #작업 취소
        clear_label = QAction(QIcon('./icons/delete.png'),"작업 취소", self)
        clear_label.setShortcut('Ctrl+F4')
        clear_label.setStatusTip("작업 취소")
        clear_label.triggered.connect(self.clear_label)

        #나가기
        exit_window = QAction(QIcon('./icons/close1.png'),"나가기", self)
        exit_window.setShortcut('Alt+F4')
        exit_window.setStatusTip("나가기")
        exit_window.triggered.connect(self.exit_window)

        #기본 편집
        #확대
        bigger = QAction(QIcon('./icons/zoom.png'),"확대", self) #버튼 이름
        bigger.setStatusTip("확대") #setStatusTip : 커서를 올려뒀을 때 나오는 설명창
        bigger.triggered.connect(self.bigger) #연결할 기능

        #축소
        smaller  = QAction(QIcon('./icons/zoom-out.png'),"축소", self) 
        smaller.setStatusTip("축소") 
        smaller.triggered.connect(self.smaller) 

        #회전-시계방향
        rotation_clock  = QAction(QIcon('./icons/rotate_clock.png'),"시계 방향 회전", self)
        rotation_clock.setShortcut('Ctrl+r')
        rotation_clock.setStatusTip("시계 방향 회전")
        rotation_clock.triggered.connect(self.rotation_clock)

        #회전-반시계방향
        rotation_counter = QAction(QIcon('./icons/rotate_counter.png'),"반시계 방향 회전", self)
        rotation_counter.setShortcut('ctrl+l')
        rotation_counter.setStatusTip("반시계 방향 회전")
        rotation_counter.triggered.connect(self.rotation_counter)

        #좌우반전
        flip  = QAction(QIcon('./icons/flip.png'),"좌우반전", self)
        flip.setStatusTip("좌우반전")
        flip.triggered.connect(self.flip)

        #상하반전
        flip_v  = QAction(QIcon('./icons/flip_v.png'),"상하반전", self)
        flip_v.setStatusTip("상하반전")
        flip_v.triggered.connect(self.flip_v)

        #자르기
        crop = QAction(QIcon('./icons/crop.png'),"자르기", self) 
        crop.setStatusTip("자르기")
        crop.triggered.connect(self.crop) 

        #원형으로 자르기
        circle_cut = QAction(QIcon('./icons/circle.png'),"원형 자르기", self)
        circle_cut.setStatusTip("원형 자르기")
        circle_cut.triggered.connect(self.circle_cut)


        #이미지
        #볼록렌즈
        convex = QAction("볼록렌즈", self)
        convex.setStatusTip("볼록렌즈")
        convex.triggered.connect(self.convex)

        #오목렌즈
        concave = QAction("오목렌즈", self)
        concave.setStatusTip("오목렌즈")
        concave.triggered.connect(self.concave)

        #모자이크
        mosaic = QAction("모자이크", self)
        mosaic.setStatusTip("모자이크")
        mosaic.triggered.connect(self.mosaic)

    
        #색상
        #명암 조절
        contrast = QAction("명암 조절", self)
        contrast.setStatusTip("명암 조절")
        contrast.triggered.connect(self.contrast)

        #밝기 조절
        bright = QAction("밝게", self)
        bright.setStatusTip("밝게")
        bright.triggered.connect(self.bright) 

        #어둡게
        darkness = QAction("어둡게", self)
        darkness.setStatusTip("어둡게")
        darkness.triggered.connect(self.darkness)

        #색상반전
        color_inversion = QAction("색상 반전", self)
        color_inversion.setStatusTip("색상 반전")
        color_inversion.triggered.connect(self.color_inversion)

        #역상
        corlor_reverse = QAction("역상", self)
        corlor_reverse.setStatusTip("역상")
        corlor_reverse.triggered.connect(self.corlor_reverse)

        #흑백
        gray_scale = QAction("흑백", self)
        gray_scale.setStatusTip("흑백")
        gray_scale.triggered.connect(self.gray_scale)


        #필터
        #샤픈
        sharpen = QAction("샤픈", self)
        sharpen.setStatusTip("sharpen")
        sharpen.triggered.connect(self.sharpen)

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

        #---드랍메뉴 추가---
        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()
        menu.setStyleSheet("background-color: #F5F5F5;")
        file_menu0 = menu.addMenu("&파일")
        file_menu0.addAction(show_file_dialog)
        file_menu0.addAction(save_file)
        file_menu0.addAction(clear_label)
        file_menu0.addAction(exit_window)

        file_menu1 = menu.addMenu("&기본 편집") #메뉴바에 메뉴 추가
        file_menu1.addAction(bigger)
        file_menu1.addAction(smaller)
        separator = QAction(self) #분할선 추가
        separator.setSeparator(True)
        file_menu1.addAction(separator)
        file_menu1.addAction(rotation_clock)
        file_menu1.addAction(rotation_counter)
        file_menu1.addAction(flip)
        file_menu1.addAction(flip_v)
        separator = QAction(self)#분할선 추가
        separator.setSeparator(True)
        file_menu1.addAction(separator)
        file_menu1.addAction(crop)
        file_menu1.addAction(circle_cut)

        file_menu2 = menu.addMenu("&이미지 왜곡")
        file_menu2.addAction(convex)
        file_menu2.addAction(concave)
        file_menu2.addAction(mosaic)

        file_menu3 = menu.addMenu("&명암과 색상")
        file_menu3.addAction(bright)
        file_menu3.addAction(darkness)
        file_menu3.addAction(contrast)
        separator = QAction(self)
        separator.setSeparator(True)
        file_menu3.addAction(separator)
        file_menu3.addAction(color_inversion)
        file_menu3.addAction(corlor_reverse)
        file_menu3.addAction(gray_scale)

        file_menu4 = menu.addMenu("&필터")
        file_menu4.addAction(sharpen)
        file_menu4.addAction(blur)
        file_menu4.addAction(gaussian_blur)
        file_menu4.addAction(median_blur)
        file_menu4.addAction(bilateral_filter)
        separator = QAction(self)
        separator.setSeparator(True)
        file_menu4.addAction(separator)
        file_menu4.addAction(roberts_filter)
        file_menu4.addAction(sobel_filter)
        
        
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
        global file_name
        file_name = QFileDialog.getOpenFileName(self, "이미지 열기", "./")
        print(file_name)
        self.image = cv2.imread(file_name[0]) #튜플 형태: 파일 주소

        global update
        update = self.image

        h, w, _ = self.image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(self.image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter) #이미지 중앙정렬
        pixmap = QPixmap(image)
        self.label1.setPixmap(pixmap)
    
    #작업 취소
    def clear_label(self, event):
        global update
        reply = QMessageBox.question(self, 'Message', '작업을 취소하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.label2.clear()
            update = self.image
        else:
            event.ignore()

        
    #나가기
    def exit_window(self, event):
        reply = QMessageBox.question(self, 'Message', '창을 닫으시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            event.ignore()

    #저장
    def save_file(self):
        global update
        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        cv2.imwrite(filename,update)
        QMessageBox.information(self, "저장 성공!", "이미지를 성공적으로 저장하였습니다.", QMessageBox.Ok)
        print("저장")


    #확대
    def bigger(self):
        global update
        h, w, _ = self.image.shape
        update = cv2.resize(update, None,  None, 2, 2, cv2.INTER_CUBIC)
        
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("확대")
    
    #축소
    def smaller(self):
        global update
        update= cv2.pyrDown(update) #이미지 2배로 축소

        h, w, _ = update.shape
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

        print("축소")
    
    #회전(시계방향)
    def rotation_clock(self): 
        global update
        update = cv2.rotate(update, cv2.ROTATE_90_CLOCKWISE)
        h, w, _ = update.shape
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

        print("시계방향 회전")
    
    #회전(반시계방향)
    def rotation_counter(self):
        global update
        update = cv2.rotate(update, cv2.ROTATE_90_COUNTERCLOCKWISE)
        h, w, _ = update.shape
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

        print("반시계방향 회전")
    
    #좌우반전
    def flip(self):
        global update
        
        update = cv2.flip(update, 1) #1은 좌우반전을 의미
        h, w, _ = update.shape #높이 너비 채널

        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("좌우반전")

    #상하반전
    def flip_v(self):
        global update
        update = cv2.flip(update, 0) #0은 상하반전 의미
        h, w, _ = update.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("상하반전")

    #자르기
    def crop(self):
        global update
        update = update[100:600, 200:700].copy()
        h, w, _ = update.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("자르기")

    #원형 자르기
    def circle_cut(self):
        global update
        h, w = update.shape[:2]
        mask = np.zeros_like(update)
        cv2.circle(mask, (int(w/2), int(w/2)), int(w/2), (255, 255, 255), -1)
        update = cv2.bitwise_and(update, mask)

        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("원형 자르기")

    #볼록렌즈
    def convex(self):
        global update
        h, w = update.shape[:2]
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

        update = cv2.remap(update, mapx, mapy, cv2.INTER_LINEAR) #재매핑

        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("볼록렌즈")

    #오목렌즈
    def concave(self):
        global update
        h, w = update.shape[:2]
        exp = 0.5
        scale = 1
        mapy, mapx = np.indices((h, w), dtype=np.float32)

        mapx = 2 * mapx / (w - 1) -1
        mapy = 2 * mapy / (h - 1) -1

        r, theta = cv2.cartToPolar(mapx, mapy) #직교좌표를 극좌표로 변환
        r[r < scale] = r[r < scale] ** exp 

        mapx, mapy = cv2.polarToCart(r, theta) #극좌표를 직교좌표로 변환
        mapx = ((mapx + 1) * w - 1) /2 #좌상단으로 복귀
        mapy = ((mapy + 1) * h - 1) / 2 

        update = cv2.remap(update, mapx, mapy, cv2.INTER_LINEAR) #재매핑

        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("오목렌즈")

    #모자이크
    def mosaic(self):
        global update
        QMessageBox.information(self, "CHECK", "영역 지정 후 ENTER버튼을 눌러주세요", QMessageBox.Ok)
        x, y, width, height = cv2.selectROI("위치", update, False)
        mosaic_loc = update[y : y+height, x : x + width ]
        mosaic_loc = cv2.blur(mosaic_loc, (50, 50))
        update[y : y+height, x : x + width] = mosaic_loc
        cv2.destroyAllWindows()
        
        h, w = update.shape[:2]
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("모자이크")

    #명암 조절    
    def contrast(self):
        global update
        alpha = 1 #기울기
        update = np.clip(((1 + alpha)*update - 128*alpha), 0, 255).astype(np.uint8)

        h, w, _ = update.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("명암 조절")

    #밝게
    def bright(self):
        global update
        val = 100
        array = np.full(update.shape, (val, val, val), dtype=np.uint8)
        update = cv2.add(update, array)
        h, w, _ = update.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("밝게")

    #어둡게
    def darkness(self):
        global update
        val = 100
        array = np.full(update.shape, (val, val, val), dtype=np.uint8)
        update = cv2.subtract(update, array)
        h, w, _ = update.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("어둡게")

    #색상 반전
    def color_inversion(self):
        global update
        h, w, _ = update.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_BGR888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("색상 반전")

    #역상
    def corlor_reverse(self):
        global update
        update = cv2.bitwise_not(update)
        h, w, _ = update.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("역상")

    #흑백
    def gray_scale(self):
        global update
        update = cv2.cvtColor(update, cv2.COLOR_RGB2GRAY)
        h, w = update.shape #높이 너비 채널
        bytes_per_line = 1 * w #흑백은 1차원 이미지
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("흑백")

    #샤픈
    def sharpen(self):
        global update
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        update = cv2.filter2D(update, -1, kernel)
        h, w, _ = update.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("sharpen")

    #블러
    def blur(self):
        global update
        kernel = np.full((5, 5), 0.04)
        update = cv2.filter2D(update, -1, kernel)

        h, w, _ = update.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("블러")

    #가우시안 블러
    def gaussian_blur(self):
        global update
        kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) * (1/ 16)
        update = cv2.filter2D(update, -1, kernel)

        h, w, _ = update.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("가우시안 블러")

    #미디언 블러링
    def median_blur(self):
        global update
        update = cv2.medianBlur(update, 5)

        h, w, _ = update.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("미디언 블러링")

    #바이래터럴 필터
    def bilateral_filter(self):
        global update
        update = cv2.bilateralFilter(update, 5, 75, 75)

        h, w, _ = update.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("바이래터널 필터")

    #로버츠 교차 필터
    def roberts_filter(self):
        global update
        gx_kernel = np.array([[1, 0],[0, -1]]) #x축의 경계만 나옴
        gy_kernel = np.array([[0, 1],[-1, 0]]) #y축의 경계만 나옴

        edge_gx = cv2.filter2D(update, -1, gx_kernel)
        edge_gy = cv2.filter2D(update, -1, gy_kernel)

        update = edge_gx + edge_gy

        h, w, _ = update.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        
        print("로버츠 교차 필터")

    #소벨 필터
    def sobel_filter(self):
        global update
        gx_kernel = np.array([[-1, 0, 1],[-2, 0, 2], [-1, 0, 1]]) 
        gy_kernel = np.array([[-1, -2, -1],[0, 0, 0], [1, 2, 1]]) 

        edge_gx = cv2.filter2D(update, -1, gx_kernel)
        edge_gy = cv2.filter2D(update, -1, gy_kernel)

        update = edge_gx + edge_gy

        h, w, _ = update.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(update.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        print("소벨 필터")



#창 보이기
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())