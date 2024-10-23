# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from OMPython import ModelicaSystem
import matplotlib.pyplot as plt
import csv


from Ui_login import Ui_MainWindow
from Ui_phm_functionchoose import Ui_Phmfunction
from Ui_main import Ui_Main
from Ui_motor import Ui_Motor
from Ui_shaft import Ui_Shaft
from Ui_load import Ui_Load
from Ui_shaftspeed_control import Ui_Shaftspeed_control
from Ui_load_control import Ui_Load_control
from Ui_testbearing import Ui_Testbearing
from Ui_testbearing_ball import Ui_Testbearing_ball
from Ui_testbearing_raceway import Ui_Testbearing_raceway
from Ui_simulationoptions import Ui_Simulationoptions


class MainWindow_login(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    username_init='123'
    password_init='222'
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow_login, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_signin.clicked.connect(self.pushButton_signin_clicked)
        self.pushButton_quit.clicked.connect(QCoreApplication.quit)
        self.username='111'
        self.possword='111'
        
    
    def paintEvent(self, event):# set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./picture/background.jpg")
        painter.drawPixmap(self.rect(), pixmap)
        
    @pyqtSlot()
    def pushButton_signin_clicked(self):
        self.username=self.lineEdit_username.text()  
        self.possword=self.lineEdit_password.text() 
        if self.username_init==self.username and self.password_init==self.possword:#密码正确，进入软件窗口
            self.close()
            phmInterface.show() 
        else:
            QMessageBox.warning(self,"Warning","Username or the password is incorrect!",QMessageBox.Ok)

class PHMInterface(QDialog, Ui_Phmfunction):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(PHMInterface, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_dynamicmodel.clicked.connect(self.pushButton_dynamicmodel_clicked)
        #self.pushButton_cnn.clicked.connect(self.pushButton_cnn_clicked)
        self.pushButton_back.clicked.connect(self.pushButton_back_clicked)
        
        
        #self.cnnfunctionsInterface=CNNfunctionsInterface()
        
    def paintEvent(self, event):# set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./picture/6.jpg")
        painter.drawPixmap(self.rect(), pixmap)
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self,'Warning',"Are you sure to quit the appication?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    @pyqtSlot()
    def pushButton_dynamicmodel_clicked(self):
        self.hide()
        MainInterface.show() 
        
    @pyqtSlot()
    def pushButton_cnn_clicked(self):
        self.hide()
        self.cnnfunctionsInterface.show()
        
    @pyqtSlot()
    def pushButton_back_clicked(self):
        self.hide()
        Login.show()


class MainInterface(QDialog, Ui_Main):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainInterface, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_Motor.clicked.connect(self.pushButton_Motor_clicked)
        self.pushButton_Shaft.clicked.connect(self.pushButton_Shaft_clicked)
        self.pushButton_Load.clicked.connect(self.pushButton_Load_clicked)
        self.pushButton_shaftspeed_control.clicked.connect(self.pushButton_shaftspeed_control_clicked)
        self.pushButton_Testbearing.clicked.connect(self.pushButton_Testbearing_clicked)
        self.pushButton_Load_control.clicked.connect(self.pushButton_Load_control_clicked)
        self.pushButton_simulate.clicked.connect(self.pushButton_simulate_clicked)
        self.pushButton_back.clicked.connect(self.pushButton_back_clicked)
        
        #subinterface
        self.motorInterface=MotorInterface()
        self.shaftInterface=ShaftInterface()
        self.loadInterface=LoadInterface()
        self.shaftspeedcontrolInterface=ShaftspeedcontrolInterface()
        self.loadcontrolInterface=LoadcontrolInterface()
        self.testbearingInterface=TestbearingInterface()
        self.simulationoptionsInterface=SimulationoptionsInterface()
        
        #simulationoptions
        self.simulation_starttime='0'
        self.simulation_stoptime='10'
        self.simulation_stepsize='0.001'
        self.simulation_tolerance='0.000001'
        
        #default motor parameter
        self.motor_IM='0.01'
        self.motor_CM='0.1'
        self.motor_Kt='0.01'
        self.motor_Ke='0.01'
        self.motor_R='1'
        self.motor_L='0.5'
        
        #default shaft parameter
        self.shaft_Dp='0.03932'
        self.shaft_Db='0.00794'
        self.shaft_G='79000000000'
        self.shaft_l='1'
        
        #default load parameter
        self.load_Ap='0.001526'
        self.load_Vt='0.1072'
        self.load_Mt='2.5'
        self.load_Bp='0.000032'
        self.load_be ='700000000'
        self.load_Kp='1'
        
        #default shaft speed control parameters:
        self.shaftspeedcontrol_k_KM='100' #对应modelica模型中的参数KM
        self.shaftspeedcontrol_Ti_TIM='0.5'#对应modelica模型中的参数TIM
        self.shaftspeedcontrol_Td_TDM='0'#对应modelica模型中的参数TDM
        self.shaftspeedcontrol_Nd_1='10'
        self.shaftspeedcontrol_fs_command='10'
        
        #default load control parameters:
        self.loadcontrol_k_KH='0.08' #对应modelica模型中的参数KH
        self.loadcontrol_Ti_TIH='800'#对应modelica模型中的参数TIH
        self.loadcontrol_Td_TDH='0'#对应modelica模型中的参数TDH
        self.loadcontrol_Nd='10'
        self.loadcontrol_Fr_command='-30000'
        
        #default bearing parameter
        #material parameters
        self.bearing_ms ='3.2638'
        self.bearing_ks= '74200000'
        self.bearing_cs = '1376.8'
        self.bearing_mp = '6.638'
        self.bearing_kp = '15100000'
        self.bearing_cp = '2210.7'
        self.bearing_mr = '1'
        self.bearing_kr = '8882600000'
        self.bearing_cr = '9424.8'
        #design parameters
        self.bearing_nb = '9'
        self.bearing_Dp= '0.03932'
        self.bearing_Db = '0.00794'
        self.bearing_phi_slip = '0.01'
        self.bearing_mut = '0'
        self.bearing_kb = '18900000000'
        self.bearing_c = '0'
        self.bearing_alpha = '0'
        #defect parameters:
        #defecttype: 0 healthy  1-raceway: race=1 outer, race=2 inner 2-ball
        self.defect_type='0'
        #default raceway defect parameters:
        self.raceway_race='1' #1 for outer,2 for inner
        self.raceway_B='0.001'
        self.raceway_H='0.0006'
        self.raceway_L  ='0.0003'
        self.raceway_lambda='0.2'
        self.raceway_phi_d='0'
        #default ball defect parameters:
        self.ball_ball='3'#3 for ball
        self.ball_k='4'
        self.ball_w='0.003'
        self.ball_phi_s_ini='0'
    
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self,'Warning',"Are you sure to quit the appication?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    @pyqtSlot()
    def pushButton_Motor_clicked(self):
        self.motorInterface.exec()
    
    @pyqtSlot()
    def pushButton_Shaft_clicked(self):
        self.shaftInterface.exec()
    
    @pyqtSlot()
    def pushButton_Load_clicked(self):
        self.loadInterface.exec()
    
    @pyqtSlot()
    def pushButton_shaftspeed_control_clicked(self):
        self.shaftspeedcontrolInterface.exec()
        
    @pyqtSlot()
    def pushButton_Testbearing_clicked(self):
        self.testbearingInterface.exec()
        
    @pyqtSlot()
    def pushButton_Load_control_clicked(self):
        self.loadcontrolInterface.exec()
    
    @pyqtSlot()
    def pushButton_simulate_clicked(self):
        self.hide()
        self.simulationoptionsInterface.show()
    
    @pyqtSlot()
    def pushButton_back_clicked(self):
        self.hide()
        phmInterface.show()
        
        
class MotorInterface(QDialog, Ui_Motor):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MotorInterface, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton_confirm.clicked.connect(self.pushButton_confirm_clicked)

#press mouse，move the dialog        
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            #self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
    
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
        
    def closeEvent(self, event):
        self.close()
        MainInterface.show() 
   
# set background_img 
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./picture/2.jpg")
        painter.drawPixmap(self.rect(), pixmap)
        
    @pyqtSlot()
    def pushButton_confirm_clicked(self):
        self.get_motor_parameter()
        self.close()
        MainInterface.show() 
    
    
    def get_motor_parameter(self):
        if self.lineEdit_motor_IM.text() !='' :
            MainInterface.motor_IM = self.lineEdit_motor_IM.text()
        if self.lineEdit_motor_CM.text() !='' :
            MainInterface.motor_CM= self.lineEdit_motor_CM.text()
        if self.lineEdit_motor_Kt.text() !='' :
            MainInterface.motor_Kt = self.lineEdit_motor_Kt.text()
        if self.lineEdit_motor_Ke.text() !='' :
            MainInterface.motor_Ke = self.lineEdit_motor_Ke.text()
        if self.lineEdit_motor_R.text() !='' :
            MainInterface.motor_R = self.lineEdit_motor_R.text()
        if self.lineEdit_motor_L.text() !='' :
            MainInterface.motor_L = self.lineEdit_motor_L.text()
        
class ShaftInterface(QDialog, Ui_Shaft):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ShaftInterface, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton_confirm.clicked.connect(self.pushButton_confirm_clicked)
    
    #press mouse，move the dialog        
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            #self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
    
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
    
    def closeEvent(self, event):
        self.close()
        MainInterface.show() 
        
    def paintEvent(self, event):# set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./picture/2.jpg")
        painter.drawPixmap(self.rect(), pixmap)
    
    @pyqtSlot()
    def pushButton_confirm_clicked(self):
        self.get_shaft_parameter()
        self.close()
        MainInterface.show() 
    
    def get_shaft_parameter(self):
        if self.lineEdit_shaft_Dp.text() !='' :
            MainInterface.shaft_Dp = self.lineEdit_shaft_Dp.text()
        if self.lineEdit_shaft_Db.text() !='' :
            MainInterface.shaft_Db= self.lineEdit_shaft_Db.text()
        if self.lineEdit_shaft_G.text() !='' :
            MainInterface.shaft_G = self.lineEdit_shaft_G.text()
        if self.lineEdit_shaft_l.text() !='' :
            MainInterface.shaft_l = self.lineEdit_shaft_l.text()\
            
class LoadInterface(QDialog, Ui_Load):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(LoadInterface, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton_confirm.clicked.connect(self.pushButton_confirm_clicked)
    
    #press mouse，move the dialog        
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            #self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
    
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
    
    def closeEvent(self, event):
        self.close()
        MainInterface.show() 
    
    def paintEvent(self, event):# set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./picture/2.jpg")
        painter.drawPixmap(self.rect(), pixmap)
        
    @pyqtSlot()
    def pushButton_confirm_clicked(self):
        self.get_load_parameter()
        self.close()
        MainInterface.show() 
    
    def get_load_parameter(self):
        if self.lineEdit_load_Ap.text() !='' :
            MainInterface.load_Ap = self.lineEdit_load_Ap.text()
        if self.lineEdit_load_Vt.text() !='' :
            MainInterface.load_Vt= self.lineEdit_load_Vt.text()
        if self.lineEdit_load_Mt.text() !='' :
            MainInterface.load_Mt = self.lineEdit_load_Mt.text()
        if self.lineEdit_load_Bp.text() !='' :
            MainInterface.load_Bp = self.lineEdit_load_Bp.text()
        if self.lineEdit_load_be.text() !='' :
            MainInterface.load_be = self.lineEdit_load_be.text()
        if self.lineEdit_load_Kp.text() !='' :
            MainInterface.load_Kp = self.lineEdit_load_Kp.text()

class ShaftspeedcontrolInterface(QDialog, Ui_Shaftspeed_control):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ShaftspeedcontrolInterface, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton_confirm.clicked.connect(self.pushButton_confirm_clicked)
    
    #press mouse，move the dialog        
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            #self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
    
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
    
    def closeEvent(self, event):
        self.close()
        MainInterface.show() 
        
    def paintEvent(self, event):# set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./picture/2.jpg")
        painter.drawPixmap(self.rect(), pixmap)
    
    @pyqtSlot()
    def pushButton_confirm_clicked(self):
        self.get_shaftspeedcontrol_parameter()
        self.close()
        MainInterface.show() 
    
    def get_shaftspeedcontrol_parameter(self): 
        if self.lineEdit_shaftspeedcontrol_k_KM.text() !='' :
            MainInterface.shaftspeedcontrol_k_KM = self.lineEdit_shaftspeedcontrol_k_KM.text()
        if self.lineEdit_shaftspeedcontrol_Ti_TIM.text() !='' :
            MainInterface.shaftspeedcontrol_Ti_TIM= self.lineEdit_shaftspeedcontrol_Ti_TIM.text()
        if self.lineEdit_shaftspeedcontrol_Td_TDM.text() !='' :
            MainInterface.shaftspeedcontrol_Td_TDM= self.lineEdit_shaftspeedcontrol_Td_TDM.text()
        if self.lineEdit_shaftspeedcontrol_Nd_1.text() !='' :
            MainInterface.shaftspeedcontrol_Nd_1= self.lineEdit_shaftspeedcontrol_Nd_1.text()
        if self.lineEdit_shaftspeedcontrol_fs_command.text() !='' :
            MainInterface.shaftspeedcontrol_fs_command= self.lineEdit_shaftspeedcontrol_fs_command.text()

class LoadcontrolInterface(QDialog, Ui_Load_control):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(LoadcontrolInterface, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton_confirm.clicked.connect(self.pushButton_confirm_clicked)
    
    #press mouse，move the dialog        
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            #self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
    
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
    
    
    def closeEvent(self, event):
        self.close()
        MainInterface.show()
        
    def paintEvent(self, event):# set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./picture/2.jpg")
        painter.drawPixmap(self.rect(), pixmap)
    
    @pyqtSlot()
    def pushButton_confirm_clicked(self):
        self.get_loadcontrol_parameter()
        self.close()
        MainInterface.show() 
        
    def get_loadcontrol_parameter(self): 
        if self.lineEdit_loadcontrol_k_KH.text() !='' :
            MainInterface.loadcontrol_k_KH = self.lineEdit_loadcontrol_k_KH.text()
        if self.lineEdit_loadcontrol_Ti_TIH.text() !='' :
            MainInterface.loadcontrol_Ti_TIH= self.lineEdit_loadcontrol_Ti_TIH.text()
        if self.lineEdit_loadcontrol_Td_TDH.text() !='' :
            MainInterface.loadcontrol_Td_TDH= self.lineEdit_loadcontrol_Td_TDH.text()
        if self.lineEdit_loadcontrol_Nd.text() !='' :
            MainInterface.loadcontrol_Nd= self.lineEdit_loadcontrol_Nd.text()
        if self.lineEdit_loadcontrol_Fr_command.text() !='' :
            MainInterface.loadcontrol_Fr_command= self.lineEdit_loadcontrol_Fr_command.text()

class TestbearingInterface(QDialog, Ui_Testbearing):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(TestbearingInterface, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton_confirm.clicked.connect(self.pushButton_confirm_clicked)
        self.pushButton_finish.clicked.connect(self.pushButton_finish_clicked)
        self.comboBox.currentIndexChanged.connect(self.Defecttype_confirm)
        
        self.testbearing_ballInterface=Testbearing_ballInterface()
        self.testbearing_racewayInterface=Testbearing_racewayInterface()
        
        self.interface_ball_race='0' # paramter for choosing ball or race interface
       
    #press mouse，move the dialog        
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            #self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
    
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
        
    def closeEvent(self, event):
        self.close()
        MainInterface.show()
    
    def paintEvent(self, event):# set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./picture/2.jpg")
        painter.drawPixmap(self.rect(), pixmap)
        
    def get_bearing_parameter(self):
        #material parameters
        if self.lineEdit_bearing_ms.text() !='' :
            MainInterface.bearing_ms = self.lineEdit_bearing_ms.text()
        if self.lineEdit_bearing_ks.text() !='' :
            MainInterface.bearing_ks= self.lineEdit_bearing_ks.text()
        if self.lineEdit_bearing_cs.text() !='' :
            MainInterface.bearing_cs = self.lineEdit_bearing_cs.text()
        if self.lineEdit_bearing_mp.text() !='' :
            MainInterface.bearing_mp = self.lineEdit_bearing_mp.text()
        if self.lineEdit_bearing_kp.text() !='' :
            MainInterface.bearing_kp = self.lineEdit_bearing_kp.text()
        if self.lineEdit_bearing_cp.text() !='' :
            MainInterface.bearing_cp = self.lineEdit_bearing_cp.text()
        if self.lineEdit_bearing_mr.text() !='' :
            MainInterface.bearing_mr = self.lineEdit_bearing_mr.text()
        if self.lineEdit_bearing_kr.text() !='' :
            MainInterface.bearing_kr = self.lineEdit_bearing_kr.text()
        if self.lineEdit_bearing_cr.text() !='' :
            MainInterface.bearing_cr = self.lineEdit_bearing_cr.text()
        #design parameters
        if self.lineEdit_bearing_nb.text() !='' :
            MainInterface.bearing_nb = self.lineEdit_bearing_nb.text()
        if self.lineEdit_bearing_Dp.text() !='' :
            MainInterface.bearing_Dp= self.lineEdit_bearing_Dp.text()
        if self.lineEdit_bearing_Db.text() !='' :
            MainInterface.bearing_Db = self.lineEdit_bearing_Db.text()
        if self.lineEdit_bearing_phi_slip.text() !='' :
            MainInterface.bearing_phi_slip = self.lineEdit_bearing_phi_slip.text()
        if self.lineEdit_bearing_mut.text() !='' :
            MainInterface.bearing_mut = self.lineEdit_bearing_mut.text()
        if self.lineEdit_bearing_kb.text() !='' :
            MainInterface.bearing_kb = self.lineEdit_bearing_kb.text()
        if self.lineEdit_bearing_c.text() !='' :
            MainInterface.bearing_c = self.lineEdit_bearing_c.text()
        if self.lineEdit_bearing_alpha.text() !='' :
            MainInterface.bearing_alpha = self.lineEdit_bearing_alpha.text()
    
    @pyqtSlot()
    def Defecttype_confirm(self):
        if self.comboBox.currentText()=='Healthy':
            MainInterface.defect_type='0' 
            self.interface_ball_race='0'
            
        elif self.comboBox.currentText()=='RaceWay':
            MainInterface.defect_type='1' 
            self.interface_ball_race='1'
            
        elif self.comboBox.currentText()=='Ball':
            MainInterface.defect_type='2' 
            self.interface_ball_race='2'
            
    
    @pyqtSlot()
    def pushButton_confirm_clicked(self):
        self.get_bearing_parameter()
        QMessageBox.information(self,"Information","The configuration of parameters are completed!Please choose defect type next!",QMessageBox.Ok) 
        
      
    @pyqtSlot()
    def pushButton_finish_clicked(self):
        self.close()
        if self.interface_ball_race=='1':
            self.testbearing_racewayInterface.exec()
        elif self.interface_ball_race=='2':
            self.testbearing_ballInterface.exec()
        else:
            pass

class Testbearing_ballInterface(QDialog, Ui_Testbearing_ball):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Testbearing_ballInterface, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton_confirm.clicked.connect(self.pushButton_confirm_clicked)
    
    #press mouse，move the dialog        
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            #self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
    
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
    
    def closeEvent(self, event):
        self.close()
        MainInterface.show()
    
    def paintEvent(self, event):# set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./picture/2.jpg")
        painter.drawPixmap(self.rect(), pixmap)
    
    def get_ball_parameter(self): 
        if self.lineEdit_ball_ball.text() !='' :
            MainInterface.ball_ball = self.lineEdit_ball_ball.text()
        if self.lineEdit_ball_k.text() !='' :
            MainInterface.ball_k= self.lineEdit_ball_k.text()
        if self.lineEdit_ball_w.text() !='' :
            MainInterface.ball_w= self.lineEdit_ball_w.text()
        if self.lineEdit_ball_phi_s_ini.text() !='' :
            MainInterface.ball_phi_s_ini= self.lineEdit_ball_phi_s_ini.text()
    
    @pyqtSlot()
    def pushButton_confirm_clicked(self):
        self.get_ball_parameter()
        self.close()
        MainInterface.show() 

class Testbearing_racewayInterface(QDialog, Ui_Testbearing_raceway):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Testbearing_racewayInterface, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton_confirm.clicked.connect(self.pushButton_confirm_clicked)
    
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            #self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
    
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
        
    def closeEvent(self, event):
        self.close()
        MainInterface.show()
        
    def paintEvent(self, event):# set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./picture/2.jpg")
        painter.drawPixmap(self.rect(), pixmap)
    
    def get_raceway_parameter(self):
        #material parameters
        if self.lineEdit_raceway_race.text() !='' :
            MainInterface.raceway_race = self.lineEdit_raceway_race.text()
        if self.lineEdit_raceway_B.text() !='' :
            MainInterface.raceway_B= self.lineEdit_raceway_B.text()
        if self.lineEdit_raceway_H.text() !='' :
            MainInterface.raceway_H= self.lineEdit_raceway_H.text()
        if self.lineEdit_raceway_L.text() !='' :
            MainInterface.raceway_L = self.lineEdit_raceway_L.text()
        if self.lineEdit_raceway_lambda.text() !='' :
            MainInterface.raceway_lambda= self.lineEdit_raceway_lambda.text()
        if self.lineEdit_raceway_phi_d.text() !='' :
            MainInterface.raceway_phi_d = self.lineEdit_raceway_phi_d.text()
    
    @pyqtSlot()
    def pushButton_confirm_clicked(self):
        self.get_raceway_parameter()
        self.close()
        MainInterface.show() 

class SimulationoptionsInterface(QDialog, Ui_Simulationoptions):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SimulationoptionsInterface, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton_run.clicked.connect(self.pushButton_run_clicked)
        self.pushButton_back.clicked.connect(self.pushButton_back_clicked)
        
    def closeEvent(self, event):
        self.close()
        MainInterface.show()   
    
    def paintEvent(self, event):# set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./picture/2.jpg")
        painter.drawPixmap(self.rect(), pixmap)
    
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            #self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
    
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
    
    def get_simulation_options(self):
        #material parameters
        if self.lineEdit_simulation_starttime.text() !='' :
            MainInterface.simulation_starttime = self.lineEdit_simulation_starttime.text()
        else:
            MainInterface.simulation_starttime = '0'
        
        if self.lineEdit_simulation_stoptime.text() !='' :
            MainInterface.simulation_stoptime= self.lineEdit_simulation_stoptime.text()
        else:
            MainInterface.simulation_stoptime = '10'
            
        if self.lineEdit_simulation_stepsize.text() !='' :
            MainInterface.simulation_stepsize= self.lineEdit_simulation_stepsize.text()
        else:
            MainInterface.simulation_stepsize = '0.001'
            
        if self.lineEdit_simulation_tolerance.text() !='' :
            MainInterface.simulation_tolerance = self.lineEdit_simulation_tolerance.text()
        else:
            MainInterface.simulation_tolerance = '0.000006'
        
    @pyqtSlot()
    def pushButton_run_clicked(self):
        self.get_simulation_options()

        base_path = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_path, 'model', 'VirtualBearingTestBench.mo')
        m = ModelicaSystem(model_path, 'Library.VirtualBench_layout_v1')
        
        #SimulationOptions
        m.setSimulationOptions(["startTime=%s"%(float(MainInterface.simulation_starttime)),"stopTime=%s"%(float(MainInterface.simulation_stoptime)),"tolerance=%s"%(float(MainInterface.simulation_tolerance)),"stepSize=%s"%(float(MainInterface.simulation_stepsize)),"solver=dassl",])
        
        #defecttype选择
        m.setInputs("defecttype=%s"%(str(MainInterface.defect_type)))
        
        #motor参数配置
        m.setParameters("IM=%s"%(str(MainInterface.motor_IM)))
        m.setParameters("CM=%s"%(str(MainInterface.motor_CM)))
        m.setParameters("Kt=%s"%(str(MainInterface.motor_Kt)))
        m.setParameters("Ke=%s"%(str(MainInterface.motor_Ke)))
        m.setParameters("R=%s"%(str(MainInterface.motor_R)))
        m.setParameters("L_m=%s"%(str(MainInterface.motor_L)))
        
        #shaft参数配置
        m.setParameters("Dp_s=%s"%(str(MainInterface.shaft_Dp)))
        m.setParameters("Db_s=%s"%(str(MainInterface.shaft_Db)))
        m.setParameters("G=%s"%(str(MainInterface.shaft_G)))
        m.setParameters("l=%s"%(str(MainInterface.shaft_l)))
        
        #load参数配置
        m.setParameters("Ap=%s"%(str(MainInterface.load_Ap)))
        m.setParameters("Vt=%s"%(str(MainInterface.load_Vt)))
        m.setParameters("Mt=%s"%(str(MainInterface.load_Mt)))
        m.setParameters("Bp=%s"%(str(MainInterface.load_Bp)))
        m.setParameters("be=%s"%(str(MainInterface.load_be)))
        m.setParameters("Kp=%s"%(str(MainInterface.load_Kp)))
        
        #testbearing基本参数配置
        #material parameters
        m.setParameters("ms=%s"%(str(MainInterface.bearing_ms)))
        m.setParameters("ks=%s"%(str(MainInterface.bearing_ks)))
        m.setParameters("cs=%s"%(str(MainInterface.bearing_cs)))
        m.setParameters("mp=%s"%(str(MainInterface.bearing_mp)))
        m.setParameters("kp=%s"%(str(MainInterface.bearing_kp)))
        m.setParameters("cp=%s"%(str(MainInterface.bearing_cp)))
        m.setParameters("mr=%s"%(str(MainInterface.bearing_mr)))
        m.setParameters("kr=%s"%(str(MainInterface.bearing_kr)))
        m.setParameters("cr=%s"%(str(MainInterface.bearing_cr)))
        #design parameters
        #m.setParameters("nb=%s"%(str(MainInterface.bearing_nb)))    #nb改写不了
        m.setParameters("Dp=%s"%(str(MainInterface.bearing_Dp)))
        m.setParameters("Db=%s"%(str(MainInterface.bearing_Db)))
        m.setParameters("phi_slip=%s"%(str(MainInterface.bearing_phi_slip)))
        m.setParameters("mut=%s"%(str(MainInterface.bearing_mut)))
        m.setParameters("kb=%s"%(str(MainInterface.bearing_kb)))
        m.setParameters("c=%s"%(str(MainInterface.bearing_c)))
        m.setParameters("alpha=%s"%(str(MainInterface.bearing_alpha)))
        
        #raceway defect parameters:
        m.setParameters("race[1]=%s"%(str(MainInterface.raceway_race)))
        m.setParameters("B[1]=%s"%(str(MainInterface.raceway_B)))
        m.setParameters("H[1]=%s"%(str(MainInterface.raceway_H)))
        m.setParameters("L[1]=%s"%(str(MainInterface.raceway_L)))
        m.setParameters("lambda[1]=%s"%(str(MainInterface.raceway_lambda)))
        m.setParameters("phi_d[1]=%s"%(str(MainInterface.raceway_phi_d)))
        
        #ball defect parameters:
        m.setParameters("ball[1]=%s"%(str(MainInterface.ball_ball)))
        m.setParameters("k[1]=%s"%(str(MainInterface.ball_k)))
        m.setParameters("w[1]=%s"%(str(MainInterface.ball_w)))
        m.setParameters("phi_s_ini[1]=%s"%(str(MainInterface.ball_phi_s_ini)))
        
        #shaft speed control parameters:
        m.setParameters("KM=%s"%(str(MainInterface.shaftspeedcontrol_k_KM)))
        m.setParameters("TIM=%s"%(str(MainInterface.shaftspeedcontrol_Ti_TIM)))
        m.setParameters("TDM=%s"%(str(MainInterface.shaftspeedcontrol_Td_TDM)))
        m.setParameters("Nd_1=%s"%(str(MainInterface.shaftspeedcontrol_Nd_1)))
        m.setParameters("fs_command=%s"%(str(MainInterface.shaftspeedcontrol_fs_command)))
        
        #load control parameters:
        m.setParameters("KH=%s"%(str(MainInterface.loadcontrol_k_KH)))
        m.setParameters("TIH=%s"%(str(MainInterface.loadcontrol_Ti_TIH)))
        m.setParameters("TDH=%s"%(str(MainInterface.loadcontrol_Td_TDH)))
        m.setParameters("Nd=%s"%(str(MainInterface.loadcontrol_Nd)))
        m.setParameters("Fr_command=%s"%(str(MainInterface.loadcontrol_Fr_command)))
        
        #m.buildModel()
        m.simulate(simflags="-noEventEmit")
        '''
        parameters=m.getParameters()
        s1=pd.Series(parameters)
        data=pd.DataFrame(s1,columns={'Value'})
        pd.set_option('display.max_rows', None)  
        print(data)
        '''
        #plot acc_x according to time
        acc_x=m.getSolutions('acc_x')
        acc_x=acc_x[0]#注：getSolution返回是一个列表中嵌套列表的数据格式如[[1,2]],acc_x[0]即取出这个嵌套的列表，如不取出画图存在问题
        t=m.getSolutions('time')
        t=t[0]
        plt.plot(t,acc_x, 'r-', linewidth=0.5)
        plt.xlabel(r'Time (s)', fontsize=22)
        plt.ylabel(r'$\text{acc}_x$ (m/s$^2$)', fontsize=22)
        plt.tick_params(axis='both', labelsize=24)
        plt.show()
        plt.ion()
        
        
        label=["acc_x"]
        label1=["time"]
        #only save acc_x to csv
        '''
        data = list(map(lambda x:[x],acc_x))
        with open("acc_x.csv",'w',newline ='') as f:
            mywrite = csv.writer(f)
            mywrite.writerow(label)
            for i in data:
                mywrite.writerow(i)
        '''
        #save acc_x and time to csv
        with open('output.csv','wt', newline ='') as f:
            writer = csv.writer(f)
            writer.writerows(zip(label1,label))
            writer.writerows(zip(t,acc_x))
            
    @pyqtSlot()
    def pushButton_back_clicked(self):
        self.close()
        MainInterface.show() 
        

    
#Class for :Redirects console output to textEdit，used in CNN interface
class Stream(QtCore.QObject):
    
    newText = QtCore.pyqtSignal(str)
 
    def write(self, text):
        self.newText.emit(str(text))


    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    Login=MainWindow_login()
    MainInterface=MainInterface()
    phmInterface=PHMInterface()
    Login.show()
    sys.exit(app.exec_())

