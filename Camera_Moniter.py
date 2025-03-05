#!/usr/bin/python3
# coding: utf-8

import sys
import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer

class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(20)

    def initUI(self):
        self.image_label = QLabel(self)
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)
        self.setWindowTitle('Camera App')
        self.setGeometry(100, 100, 100, 100)  # ウインドウのサイズを100x100に設定
        self.show()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (130, 100))  # フレームを200x200にリサイズ
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.image_label.setPixmap(QPixmap.fromImage(qt_image))

    def closeEvent(self, event):
        self.cap.release()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CameraApp()
    sys.exit(app.exec_())