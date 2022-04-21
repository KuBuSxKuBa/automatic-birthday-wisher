import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit,
                             QInputDialog, QFileDialog, QMessageBox,
                             QGridLayout, QLabel, QPushButton, QFrame)
import sys
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import Qt
import sys
BACKGROUND_COLOR = "#A8D8EA"
BLUE = "rgb(94, 136, 252)"
# if people_amount == 1:
#     x_button = QtWidgets.QPushButton(self)
#     x_button.setStyleSheet(
#         f"background-color: #E0115F; color: #ffffff; order-style: outset; padding: 5px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
#     x_button.move(700, 630 + 5)
#     x_button.setText("X")
#     x_button.resize(20, 20)
#     x_button.clicked.connect(self.set_index_0)
#     self.labels_names.append(x_button)
# elif people_amount == 2:
#     x_button = QtWidgets.QPushButton(self)
#     x_button.setStyleSheet(
#         f"background-color: #E0115F; color: #ffffff; order-style: outset; padding: 5px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
#     x_button.move(700, 630 + 5)
#     x_button.setText("X")
#     x_button.resize(20, 20)
#     x_button.clicked.connect(self.set_index_0)
#     self.labels_names.append(x_button)
#
#     x_button2 = QtWidgets.QPushButton(self)
#     x_button2.setStyleSheet(
#         f"background-color: #E0115F; color: #ffffff; order-style: outset; padding: 5px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
#     x_button2.move(700, 680 + 5)
#     x_button2.setText("X")
#     x_button2.resize(20, 20)
#     x_button2.clicked.connect(self.set_index_1)
#     self.labels_names.append(x_button2)
# else:
#     x_button = QtWidgets.QPushButton(self)
#     x_button.setStyleSheet(
#         f"background-color: #E0115F; color: #ffffff; order-style: outset; padding: 5px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
#     x_button.move(700, 630 + 5)
#     x_button.setText("X")
#     x_button.resize(20, 20)
#     x_button.clicked.connect(self.set_index_0)
#     self.labels_names.append(x_button)
#
#     x_button2 = QtWidgets.QPushButton(self)
#     x_button2.setStyleSheet(
#         f"background-color: #E0115F; color: #ffffff; order-style: outset; padding: 5px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
#     x_button2.move(700, 680 + 5)
#     x_button2.setText("X")
#     x_button2.resize(20, 20)
#     x_button2.clicked.connect(self.set_index_1)
#     self.labels_names.append(x_button2)
#
#     x_button3 = QtWidgets.QPushButton(self)
#     x_button3.setStyleSheet(
#         f"background-color: #E0115F; color: #ffffff; order-style: outset; padding: 5px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
#     x_button3.move(700, 720 + 5)
#     x_button3.setText("X")
#     x_button3.resize(20, 20)
#     x_button3.clicked.connect(self.set_index_2)
#     self.labels_names.append(x_button3)

# def delete_birthday(self):
#     print(self.last_clicked_button)
#     with open("data.txt", "r") as file:
#         data = file.readlines()
#         del data[self.last_clicked_button]
#         with open("data.txt", "w") as file2:
#             file2.writelines(data)
#     print("done")
#     time.sleep(4)
#     print("set whiteboard")
#     self.set_whiteboard()
#
#
# def set_index_0(self):
#     self.last_clicked_button = 0
#     self.delete_birthday()
#
#
# def set_index_1(self):
#     self.last_clicked_button = 1
#     self.delete_birthday()
#
#
# def set_index_2(self):
#     self.last_clicked_button = 2
#     self.delete_birthday()














class PeopleList(QWidget):
    def __init__(self):
        super(PeopleList,self).__init__()
        self.setGeometry(400, 25, 900, 850)
        self.setStyleSheet(f"background-color: {BLUE};")
        self.InitUI()

    def InitUI(self):
        STARTING_Y = 100
        self.labels_names = []
        with open("data.txt", "r") as file:
            data = file.readlines()
            if len(data) == 0:
                self.white_box.setText("To add new person click the button!\n(New person will be added after you re-open application)")
            else:
                with open("data.txt", "r") as file:
                    data = file.readlines()
                    if len(data) != 0:
                        for i in data[:3]:
                            if i != "":
                                i = i.replace(":", " ")
                                whole_data = i.split()
                                name = whole_data[3]
                                email = whole_data[0]
                                month = whole_data[1]
                                day = whole_data[2]
                                # print(whole_data)

                                self.email_label = QLabel(f"{email}", self)
                                self.email_label.setStyleSheet(
                                    f"background-color: {BACKGROUND_COLOR}; color: #000000; order-style: outset; padding: 5px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
                                self.email_label.resize(300, self.email_label.height())
                                self.email_label.move(150, STARTING_Y)
                                self.labels_names.append(self.email_label)


                                self.month_label = QLabel(f"{month}", self)
                                self.month_label.setStyleSheet(
                                    f"background-color: {BACKGROUND_COLOR}; color: #000000; order-style: outset; padding: 5px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
                                self.month_label.move(450, STARTING_Y)
                                self.labels_names.append(self.month_label)


                                self.day_label = QLabel(f"{day}", self)
                                self.day_label.setStyleSheet(
                                    f"background-color: {BACKGROUND_COLOR}; color: #000000; order-style: outset; padding: 5px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
                                self.day_label.move(600, STARTING_Y)
                                self.labels_names.append(self.day_label)
                                STARTING_Y += 50



if __name__=="__main__":
    app = QApplication(sys.argv)
    myshow = PeopleList()
    myshow.setWindowTitle("People List")
    myshow.show()
    sys.exit(app.exec_())
