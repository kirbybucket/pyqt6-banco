# Form implementation generated from reading ui file 'e:\Documentos\Proyectos\Python\Proyecto1\gui\deposito.ui'
#
# Created by: PyQt6 UI code generator 6.9.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Dialog.resize(602, 639)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 495, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        self.label_7.setGeometry(QtCore.QRect(350, 500, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txtDocumento = QtWidgets.QLineEdit(parent=Dialog)
        self.txtDocumento.setGeometry(QtCore.QRect(350, 170, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtDocumento.setFont(font)
        self.txtDocumento.setObjectName("txtDocumento")
        self.cbTipo = QtWidgets.QComboBox(parent=Dialog)
        self.cbTipo.setGeometry(QtCore.QRect(20, 170, 281, 31))
        self.cbTipo.setObjectName("cbTipo")
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.checkTerminos = QtWidgets.QCheckBox(parent=Dialog)
        self.checkTerminos.setGeometry(QtCore.QRect(20, 589, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkTerminos.setFont(font)
        self.checkTerminos.setObjectName("checkTerminos")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(350, 140, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.cbMotivo = QtWidgets.QComboBox(parent=Dialog)
        self.cbMotivo.setGeometry(QtCore.QRect(20, 530, 281, 31))
        self.cbMotivo.setObjectName("cbMotivo")
        self.cbMotivo.addItem("")
        self.cbMotivo.addItem("")
        self.cbMotivo.addItem("")
        self.cbMotivo.addItem("")
        self.txtMonto = QtWidgets.QLineEdit(parent=Dialog)
        self.txtMonto.setGeometry(QtCore.QRect(350, 530, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtMonto.setFont(font)
        self.txtMonto.setObjectName("txtMonto")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("e:\\Documentos\\Proyectos\\Python\\Proyecto1\\gui\\logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(270, 20, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(103, 187, 187)")
        self.label_3.setObjectName("label_3")
        self.btnRegistrar = QtWidgets.QPushButton(parent=Dialog)
        self.btnRegistrar.setGeometry(QtCore.QRect(350, 590, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setStyleSheet("background-color: rgb(255, 105, 3);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px")
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.label_8 = QtWidgets.QLabel(parent=Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 230, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.txtSegundoNombre = QtWidgets.QLineEdit(parent=Dialog)
        self.txtSegundoNombre.setGeometry(QtCore.QRect(350, 260, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtSegundoNombre.setFont(font)
        self.txtSegundoNombre.setText("")
        self.txtSegundoNombre.setObjectName("txtSegundoNombre")
        self.txtPrimerNombre = QtWidgets.QLineEdit(parent=Dialog)
        self.txtPrimerNombre.setGeometry(QtCore.QRect(20, 260, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtPrimerNombre.setFont(font)
        self.txtPrimerNombre.setText("")
        self.txtPrimerNombre.setObjectName("txtPrimerNombre")
        self.label_9 = QtWidgets.QLabel(parent=Dialog)
        self.label_9.setGeometry(QtCore.QRect(350, 230, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 320, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.txtSegundoApellido = QtWidgets.QLineEdit(parent=Dialog)
        self.txtSegundoApellido.setGeometry(QtCore.QRect(350, 350, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtSegundoApellido.setFont(font)
        self.txtSegundoApellido.setText("")
        self.txtSegundoApellido.setObjectName("txtSegundoApellido")
        self.txtPrimerApellido = QtWidgets.QLineEdit(parent=Dialog)
        self.txtPrimerApellido.setGeometry(QtCore.QRect(20, 350, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtPrimerApellido.setFont(font)
        self.txtPrimerApellido.setText("")
        self.txtPrimerApellido.setObjectName("txtPrimerApellido")
        self.label_11 = QtWidgets.QLabel(parent=Dialog)
        self.label_11.setGeometry(QtCore.QRect(350, 320, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.cbSexo = QtWidgets.QComboBox(parent=Dialog)
        self.cbSexo.setGeometry(QtCore.QRect(20, 445, 121, 31))
        self.cbSexo.setObjectName("cbSexo")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.label_12 = QtWidgets.QLabel(parent=Dialog)
        self.label_12.setGeometry(QtCore.QRect(20, 410, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.txtFecha = QtWidgets.QDateEdit(parent=Dialog)
        self.txtFecha.setGeometry(QtCore.QRect(150, 440, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtFecha.setFont(font)
        self.txtFecha.setCalendarPopup(True)
        self.txtFecha.setObjectName("txtFecha")
        self.label_13 = QtWidgets.QLabel(parent=Dialog)
        self.label_13.setGeometry(QtCore.QRect(150, 410, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=Dialog)
        self.label_14.setGeometry(QtCore.QRect(350, 405, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.cbLugar = QtWidgets.QComboBox(parent=Dialog)
        self.cbLugar.setGeometry(QtCore.QRect(350, 440, 231, 31))
        self.cbLugar.setObjectName("cbLugar")
        self.cbLugar.addItem("")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 130, 621, 2))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frame.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_15 = QtWidgets.QLabel(parent=Dialog)
        self.label_15.setGeometry(QtCore.QRect(20, 100, 591, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 153, 128);")
        self.label_15.setObjectName("label_15")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Reportar Transacciones"))
        self.label_6.setText(_translate("Dialog", "Motivo del giro  *"))
        self.label_7.setText(_translate("Dialog", "Monto en dolares (USD)  *"))
        self.cbTipo.setItemText(0, _translate("Dialog", "--- Seleccione una opción ---"))
        self.cbTipo.setItemText(1, _translate("Dialog", "CI - Carnet de identidad"))
        self.cbTipo.setItemText(2, _translate("Dialog", "PPTE - Pasaporte"))
        self.cbTipo.setItemText(3, _translate("Dialog", "VISA"))
        self.checkTerminos.setText(_translate("Dialog", "Cliente acepta los términos y condiciones?  *"))
        self.label_5.setText(_translate("Dialog", "Numero de documento  *"))
        self.cbMotivo.setItemText(0, _translate("Dialog", "--- Seleccione una opción ---"))
        self.cbMotivo.setItemText(1, _translate("Dialog", "Honorarios/Servicios técnicos"))
        self.cbMotivo.setItemText(2, _translate("Dialog", "Remesas/Giros"))
        self.cbMotivo.setItemText(3, _translate("Dialog", "Donaciones"))
        self.txtMonto.setText(_translate("Dialog", "0"))
        self.label_3.setText(_translate("Dialog", "Depósito Bancario Internacional"))
        self.btnRegistrar.setText(_translate("Dialog", "Registrar"))
        self.label_8.setText(_translate("Dialog", "Primer nombre  *"))
        self.label_9.setText(_translate("Dialog", "Segundo nombre"))
        self.label_10.setText(_translate("Dialog", "Primer apellido  *"))
        self.label_11.setText(_translate("Dialog", "Segundo apellido"))
        self.cbSexo.setItemText(0, _translate("Dialog", "--- Seleccione una opción ---"))
        self.cbSexo.setItemText(1, _translate("Dialog", "Mujer"))
        self.cbSexo.setItemText(2, _translate("Dialog", "Hombre"))
        self.cbSexo.setItemText(3, _translate("Dialog", "Otro"))
        self.label_12.setText(_translate("Dialog", "Sexo  *"))
        self.txtFecha.setDisplayFormat(_translate("Dialog", "dd/MM/yyyy"))
        self.label_13.setText(_translate("Dialog", "Fecha de nacimiento"))
        self.label_14.setText(_translate("Dialog", "Lugar de nacimiento  *"))
        self.cbLugar.setItemText(0, _translate("Dialog", "--- Seleccione una opción ---"))
        self.label_4.setText(_translate("Dialog", "Tipo de documento *"))
        self.label_15.setText(_translate("Dialog", "Los campos con asterisco (*) son obligatorios"))
