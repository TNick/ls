# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transformation_calc.ui'
#
# Created: Mon Nov 17 09:47:00 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TransformationCalcDialog(object):
    def setupUi(self, TransformationCalcDialog):
        TransformationCalcDialog.setObjectName(_fromUtf8("TransformationCalcDialog"))
        TransformationCalcDialog.resize(821, 476)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TransformationCalcDialog.sizePolicy().hasHeightForWidth())
        TransformationCalcDialog.setSizePolicy(sizePolicy)
        TransformationCalcDialog.setWindowTitle(QtGui.QApplication.translate("TransformationCalcDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.Layers_GroupBox = QtGui.QGroupBox(TransformationCalcDialog)
        self.Layers_GroupBox.setGeometry(QtCore.QRect(10, 10, 181, 251))
        self.Layers_GroupBox.setTitle(QtGui.QApplication.translate("TransformationCalcDialog", "Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.Layers_GroupBox.setObjectName(_fromUtf8("Layers_GroupBox"))
        self.comboBox = QtGui.QComboBox(self.Layers_GroupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 50, 161, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.Layer1_ToolButton = QtGui.QToolButton(self.Layers_GroupBox)
        self.Layer1_ToolButton.setGeometry(QtCore.QRect(120, 90, 51, 20))
        self.Layer1_ToolButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.Layer1_ToolButton.setObjectName(_fromUtf8("Layer1_ToolButton"))
        self.comboBox_2 = QtGui.QComboBox(self.Layers_GroupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 160, 161, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.Layer2_ToolButton = QtGui.QToolButton(self.Layers_GroupBox)
        self.Layer2_ToolButton.setGeometry(QtCore.QRect(120, 200, 51, 19))
        self.Layer2_ToolButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.Layer2_ToolButton.setObjectName(_fromUtf8("Layer2_ToolButton"))
        self.Layer1_Label = QtGui.QLabel(self.Layers_GroupBox)
        self.Layer1_Label.setGeometry(QtCore.QRect(10, 30, 151, 16))
        self.Layer1_Label.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Layer 1", None, QtGui.QApplication.UnicodeUTF8))
        self.Layer1_Label.setObjectName(_fromUtf8("Layer1_Label"))
        self.Lyer2_Label = QtGui.QLabel(self.Layers_GroupBox)
        self.Lyer2_Label.setGeometry(QtCore.QRect(10, 140, 151, 16))
        self.Lyer2_Label.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Layer 2", None, QtGui.QApplication.UnicodeUTF8))
        self.Lyer2_Label.setObjectName(_fromUtf8("Lyer2_Label"))
        self.Points_GroupBox = QtGui.QGroupBox(TransformationCalcDialog)
        self.Points_GroupBox.setGeometry(QtCore.QRect(210, 10, 381, 251))
        self.Points_GroupBox.setTitle(QtGui.QApplication.translate("TransformationCalcDialog", "Points", None, QtGui.QApplication.UnicodeUTF8))
        self.Points_GroupBox.setObjectName(_fromUtf8("Points_GroupBox"))
        self.listView = QtGui.QListView(self.Points_GroupBox)
        self.listView.setGeometry(QtCore.QRect(20, 40, 121, 192))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.listView_2 = QtGui.QListView(self.Points_GroupBox)
        self.listView_2.setGeometry(QtCore.QRect(240, 40, 121, 192))
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.Add_PushButton = QtGui.QPushButton(self.Points_GroupBox)
        self.Add_PushButton.setGeometry(QtCore.QRect(150, 60, 81, 23))
        self.Add_PushButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Add >", None, QtGui.QApplication.UnicodeUTF8))
        self.Add_PushButton.setObjectName(_fromUtf8("Add_PushButton"))
        self.Remove_PushButton = QtGui.QPushButton(self.Points_GroupBox)
        self.Remove_PushButton.setGeometry(QtCore.QRect(150, 190, 81, 23))
        self.Remove_PushButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "< Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.Remove_PushButton.setObjectName(_fromUtf8("Remove_PushButton"))
        self.CommonPoints_Label = QtGui.QLabel(self.Points_GroupBox)
        self.CommonPoints_Label.setGeometry(QtCore.QRect(20, 20, 121, 16))
        self.CommonPoints_Label.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Common Points", None, QtGui.QApplication.UnicodeUTF8))
        self.CommonPoints_Label.setObjectName(_fromUtf8("CommonPoints_Label"))
        self.PointsofTrans_Label = QtGui.QLabel(self.Points_GroupBox)
        self.PointsofTrans_Label.setGeometry(QtCore.QRect(240, 20, 141, 16))
        self.PointsofTrans_Label.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Points for Transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.PointsofTrans_Label.setObjectName(_fromUtf8("PointsofTrans_Label"))
        self.TypeTrans_GroupBox = QtGui.QGroupBox(TransformationCalcDialog)
        self.TypeTrans_GroupBox.setGeometry(QtCore.QRect(610, 10, 201, 191))
        self.TypeTrans_GroupBox.setTitle(QtGui.QApplication.translate("TransformationCalcDialog", "Type of Coordinate Transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.TypeTrans_GroupBox.setObjectName(_fromUtf8("TypeTrans_GroupBox"))
        self.Ortogonal_RadioButton = QtGui.QRadioButton(self.TypeTrans_GroupBox)
        self.Ortogonal_RadioButton.setGeometry(QtCore.QRect(20, 30, 191, 17))
        self.Ortogonal_RadioButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Ortogonal Transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.Ortogonal_RadioButton.setObjectName(_fromUtf8("Ortogonal_RadioButton"))
        self.Affine_RadioButton = QtGui.QRadioButton(self.TypeTrans_GroupBox)
        self.Affine_RadioButton.setGeometry(QtCore.QRect(20, 60, 191, 17))
        self.Affine_RadioButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Affine Transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.Affine_RadioButton.setObjectName(_fromUtf8("Affine_RadioButton"))
        self.ThirdOrder_RadioButton = QtGui.QRadioButton(self.TypeTrans_GroupBox)
        self.ThirdOrder_RadioButton.setGeometry(QtCore.QRect(20, 90, 171, 17))
        self.ThirdOrder_RadioButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "3rd order Transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.ThirdOrder_RadioButton.setObjectName(_fromUtf8("ThirdOrder_RadioButton"))
        self.FourthOrder_RradioButton = QtGui.QRadioButton(self.TypeTrans_GroupBox)
        self.FourthOrder_RradioButton.setGeometry(QtCore.QRect(20, 120, 151, 17))
        self.FourthOrder_RradioButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "4th order Transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.FourthOrder_RradioButton.setObjectName(_fromUtf8("FourthOrder_RradioButton"))
        self.FifthOrder_RadioButton = QtGui.QRadioButton(self.TypeTrans_GroupBox)
        self.FifthOrder_RadioButton.setGeometry(QtCore.QRect(20, 150, 181, 17))
        self.FifthOrder_RadioButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "5th order Transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.FifthOrder_RadioButton.setObjectName(_fromUtf8("FifthOrder_RadioButton"))
        self.Calculate_PushButton = QtGui.QPushButton(TransformationCalcDialog)
        self.Calculate_PushButton.setGeometry(QtCore.QRect(710, 220, 91, 23))
        self.Calculate_PushButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Calculate", None, QtGui.QApplication.UnicodeUTF8))
        self.Calculate_PushButton.setObjectName(_fromUtf8("Calculate_PushButton"))
        self.Result_GroupBox = QtGui.QGroupBox(TransformationCalcDialog)
        self.Result_GroupBox.setGeometry(QtCore.QRect(10, 280, 801, 151))
        self.Result_GroupBox.setTitle(QtGui.QApplication.translate("TransformationCalcDialog", "Result of Coordinate Transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.Result_GroupBox.setObjectName(_fromUtf8("Result_GroupBox"))
        self.Result_TextBrowser = QtGui.QTextBrowser(self.Result_GroupBox)
        self.Result_TextBrowser.setGeometry(QtCore.QRect(10, 20, 781, 121))
        self.Result_TextBrowser.setHtml(QtGui.QApplication.translate("TransformationCalcDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.Result_TextBrowser.setObjectName(_fromUtf8("Result_TextBrowser"))
        self.Help_PushButton = QtGui.QPushButton(TransformationCalcDialog)
        self.Help_PushButton.setGeometry(QtCore.QRect(20, 440, 75, 23))
        self.Help_PushButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.Help_PushButton.setObjectName(_fromUtf8("Help_PushButton"))
        self.Close_PushButton = QtGui.QPushButton(TransformationCalcDialog)
        self.Close_PushButton.setGeometry(QtCore.QRect(720, 440, 75, 23))
        self.Close_PushButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.Close_PushButton.setObjectName(_fromUtf8("Close_PushButton"))
        self.NewCalc_PushButton = QtGui.QPushButton(TransformationCalcDialog)
        self.NewCalc_PushButton.setGeometry(QtCore.QRect(600, 440, 101, 23))
        self.NewCalc_PushButton.setText(QtGui.QApplication.translate("TransformationCalcDialog", "New Calculate", None, QtGui.QApplication.UnicodeUTF8))
        self.NewCalc_PushButton.setObjectName(_fromUtf8("NewCalc_PushButton"))

        self.retranslateUi(TransformationCalcDialog)
        QtCore.QMetaObject.connectSlotsByName(TransformationCalcDialog)

    def retranslateUi(self, TransformationCalcDialog):
        pass

