import sys
import cv2
from PySide6.QtGui import QAction, QImage, QPixmap
from PySide6.QtWidgets import (QApplication,QWidget, QLabel, 
QMainWindow, QHBoxLayout, QVBoxLayout, 
QPushButton, QFileDialog)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Photoshop")

        #메뉴바
        self.menu = self.menuBar()
        self.menu_file = self.menu.addMenu("파일")
        exit = QAction("나가기", self, triggered = qApp.quit)
        self.menu_file.addAction(exit)

        #메인화면 레이아웃
        main_layout = QHBoxLayout()

        #사이드바 메뉴버튼
        sidebar = QVBoxLayout()
        button1 = QPushButton("이미지 열기")
        button2 = QPushButton("좌우반전")
        button3 = QPushButton("새로고침")

        button1.clicked.connect(self.show_file_dialog) #버튼 기능 추가
        button2.clicked.connect(self.flip_image)
        button3.clicked.connect(self.clear_label)
        
        #사이드바에 메뉴버튼 추가(위젯)
        sidebar.addWidget(button1)
        sidebar.addWidget(button2)
        sidebar.addWidget(button3)

        main_layout.addLayout(sidebar)

        #사이드바 버튼 크기 고정
        self.label1 = QLabel(self)
        self.label1.setFixedSize(640, 480) #사이드바 제외 한 여백의 크기
        main_layout.addWidget(self.label1)

        self.label2 = QLabel(self)
        self.label2.setFixedSize(640, 480) 
        main_layout.addWidget(self.label2)

        widget = QWidget(self)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

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

    #좌우반전
    def flip_image(self):
        image = cv2.flip(self.image, 1) #1은 좌우반전을 의미
        h, w, _ = image.shape #높이 너비 채널
        bytes_per_line = 3 * w
        image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)


    #작업 취소
    def clear_label(self):
        self.label2.clear()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


        #기능이름
        # button_action = QAction("저장", self) 
        # button_action.setShortcut('Ctrl+S') 
        # button_action.setStatusTip("저장")
        # button_action.triggered.connect(self.toolbarButtonClick) 

        #기능이름
        # button_action = QAction("저장", self) 
        # button_action.setStatusTip("저장")
        # button_action.triggered.connect(self.toolbarButtonClick) 