# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Eve\Eve\tools\pm\ui\ui_sequence_properties.ui',
# licensing of 'E:\Eve\Eve\tools\pm\ui\ui_sequence_properties.ui' applies.
#
# Created: Tue Dec 24 13:12:10 2019
#      by: pyside2-uic  running on PySide2 5.9.0a1.dev1528389443
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_AssetProperties(object):
    def setupUi(self, AssetProperties):
        AssetProperties.setObjectName("AssetProperties")
        AssetProperties.resize(369, 103)
        self.verticalLayout = QtWidgets.QVBoxLayout(AssetProperties)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layoutSequence = QtWidgets.QVBoxLayout()
        self.layoutSequence.setObjectName("layoutSequence")
        self.verticalLayout.addLayout(self.layoutSequence)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnUpdateSequence = QtWidgets.QPushButton(AssetProperties)
        self.btnUpdateSequence.setMinimumSize(QtCore.QSize(0, 45))
        self.btnUpdateSequence.setObjectName("btnUpdateSequence")
        self.verticalLayout.addWidget(self.btnUpdateSequence)

        self.retranslateUi(AssetProperties)
        QtCore.QMetaObject.connectSlotsByName(AssetProperties)

    def retranslateUi(self, AssetProperties):
        AssetProperties.setWindowTitle(QtWidgets.QApplication.translate("AssetProperties", "Form", None, -1))
        self.btnUpdateSequence.setText(QtWidgets.QApplication.translate("AssetProperties", "Update Sequence Data", None, -1))

