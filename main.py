import subprocess
import time
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit,
                             QInputDialog, QFileDialog, QMessageBox,
                             QGridLayout, QLabel, QPushButton, QFrame)
from inputdialog import InputDialog
import datetime as dt
from people_list import PeopleList
BACKGROUND_COLOR = "#A8D8EA"
BLUE = "rgb(94, 136, 252)"

class MainWindow(QMainWindow):



    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(400, 25, 900, 850)
        self.setWindowTitle("Automatic birthday wisher")

        try:
            with open("userdata.txt", "r") as file:
                data = file.readlines()
                # print(data)
        except FileNotFoundError:
                self.msg = QMessageBox()
                self.msg.setWindowTitle("Fill data!")
                self.msg.setText("You have to input your e-mail address and password\nWe promise it\'s safe.")
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.exec_()
                self.user_email, self.done1 = QtWidgets.QInputDialog.getText(
                    self, 'E-mail input', 'Enter your E-mail:')
                self.user_password, self.done2 = QtWidgets.QInputDialog.getText(
                    self, 'Password input', 'Enter your Password:')
                if self.done1 and self.done2:
                    self.thanks_message = QMessageBox()
                    self.thanks_message.setWindowTitle("Thanks!")
                    self.thanks_message.setText("Thanks for trusting us!\nData that you provided is stored ONLY on your computer!\nIn order to work you have to turn 2fa google off.")
                    self.thanks_message.setIcon(QMessageBox.Information)
                    self.thanks_message.exec_()
                    with open("userdata.txt", "w") as file:
                        file.write(f"{self.user_email}:{self.user_password}")
        self.initUI()
        self.check_for_birthdays()
    def initUI(self):
        self.setStyleSheet(f"background-color: {BLUE};")
        self.image = QPixmap('birthday.png')

        self.imagelabel = QtWidgets.QLabel(self)
        self.imagelabel.setPixmap(self.image)
        self.imagelabel.resize(self.image.width(),
                          self.image.height())
        self.imagelabel.move(30 , self.imagelabel.y() + 10)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.resize(150,50)
        self.b1.setStyleSheet(f"background-color: {BACKGROUND_COLOR}; color: #000000; order-style: outset; padding: 2px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8;")
        # self.b1.setStyleSheet("QPushButton::hover"
        #                      "{"
        #                      "background-color : lightgreen;"
        #                      "}")
        self.b1.move(350,520)
        self.b1.setText("Add new person!")
        self.b1.clicked.connect(self.take_inputs)

        self.set_whiteboard()

        self.emailname = QLabel("E-Mail", self)
        self.emailname.setStyleSheet(
            f"background-color: {BACKGROUND_COLOR}; color: #000000; order-style: outset; padding: 2px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
        self.emailname.move(250, 580)

        # self.people_name = QLabel("Name", self)
        # self.people_name.setStyleSheet(
        #     f"background-color: {BACKGROUND_COLOR}; color: #000000; order-style: outset; padding: 2px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
        # self.people_name.move(150, 580)

        self.people_month = QLabel("Month", self)
        self.people_month.setStyleSheet(
            f"background-color: {BACKGROUND_COLOR}; color: #000000; order-style: outset; padding: 2px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
        self.people_month.move(450, 580)

        self.people_day = QLabel("Day", self)
        self.people_day.setStyleSheet(
            f"background-color: {BACKGROUND_COLOR}; color: #000000; order-style: outset; padding: 2px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
        self.people_day.move(600, 580)



    def take_inputs(self):
        with open("data.txt", "r") as file:
            data = file.readlines()
            if len(data) < 16:
                self.myshow = InputDialog()
                self.myshow.setWindowTitle("Enter Details")
                self.myshow.show()
            else:
                self.msg = QMessageBox()
                self.msg.setWindowTitle("No more space!")
                self.msg.setText("Current limit is 16 people.\nWe are sorry.")
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.exec_()

    def check_for_birthdays(self):
        self.birthday_people = []
        now = dt.datetime.now()
        today_day = now.day
        today_month = now.month
        with open("data.txt" , "r") as file:
            data = file.readlines()
            for i in data:
                if i != "":
                    i = i.replace(":", " ")
                    clear_data = i.split()
                    if int(clear_data[1]) == today_month and int(clear_data[2]) == today_day:
                        self.birthday_people.append(clear_data)
                    # self.birthday_people = [i for i in data if int(clear_data[1]) == today_month]
            if len(self.birthday_people) > 0:
                import smtplib
                with open("userdata.txt", "r") as file:
                    data = file.readlines()
                    for i in data:
                        i = i.replace(":", " ")
                        clear_user_data = i.split()
                    self.user_email = clear_user_data[0]
                    self.user_password = clear_user_data[1]
                    print(self.user_password, self.user_email)
                index = 0
                for i in self.birthday_people:
                    sender = self.user_email
                    receiver = self.birthday_people[index][0]
                    print(f"Sending to: {receiver}")
                    print(f"Sending from: {sender}")
                    password = self.user_password
                    subject = "Happy birthday!"
                    body = "Wishing you the best!"

                    message = f"Subject:Happy Birthday!\n\nWishing the best!"

                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    try:
                        server.login(sender, password)
                        print("Logged in...")
                        server.sendmail(sender, receiver, message)
                        print("Email has been sent!")
                        index += 1

                    except smtplib.SMTPAuthenticationError:
                        print("unable to sign in")
                        index += 1
            print(f"bth people: {self.birthday_people}")

    def see_more(self):
        self.more_people_list = PeopleList()
        self.more_people_list.setWindowTitle("People List")
        self.more_people_list.show()

    def set_whiteboard(self):
        self.labels_names = []
        WHITEBOARD_STARTING_Y = 625
        self.white_box = QLabel("⠀", self)
        self.white_box.setStyleSheet(
            f"background-color: {BACKGROUND_COLOR}; color: #000000; order-style: outset; padding: 2px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
        self.white_box.resize(700, 200)
        self.white_box.move(100, 600)
        self.labels_names.append(self.white_box)

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
                                self.email_label.move(150, WHITEBOARD_STARTING_Y)
                                self.labels_names.append(self.email_label)


                                self.month_label = QLabel(f"{month}", self)
                                self.month_label.setStyleSheet(
                                    f"background-color: {BACKGROUND_COLOR}; color: #000000; order-style: outset; padding: 5px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
                                self.month_label.move(450, WHITEBOARD_STARTING_Y)
                                self.labels_names.append(self.month_label)


                                self.day_label = QLabel(f"{day}", self)
                                self.day_label.setStyleSheet(
                                    f"background-color: {BACKGROUND_COLOR}; color: #000000; order-style: outset; padding: 5px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
                                self.day_label.move(600, WHITEBOARD_STARTING_Y)
                                self.labels_names.append(self.day_label)
                                WHITEBOARD_STARTING_Y += 50
                                if len(data) > 3:
                                    self.more_button = QtWidgets.QPushButton(self)
                                    self.more_button.resize(150,50)
                                    self.more_button.setStyleSheet(
                                        f"background-color: {BACKGROUND_COLOR}; color: #000000; order-style: outset; padding: 2px ; font: bold 15px ; border-width: 6px ; border-radius: 10px ; border-color: #2752B8; qproperty-alignment: AlignCenter")
                                    self.more_button.move(350, 775)
                                    self.more_button.setText("See more!")
                                    self.more_button.clicked.connect(self.see_more)
                                    self.labels_names.append(self.more_button)


def window():
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())

window()
