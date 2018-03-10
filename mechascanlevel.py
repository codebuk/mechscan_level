#!/usr/bin/env python3
from PyQt5.QtCore import Qt, QDir, QRect, QTimer
from PyQt5.QtGui import QImage, QPixmap, QTransform, QPainter
from PyQt5.QtWidgets import (QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem,
                             QMenu, QDialog, QFileDialog, QMessageBox, QFrame, QRubberBand, QLabel,
                             QProgressBar)
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from functools import partial
import os
from random import random
import preferences
import logging
# ui generated code
from main_window import *

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s.%(msecs)d-%(name)s-%(threadName)s-%(levelname)s %(message)s",
                    datefmt='%M:%S')
log = logging.getLogger(__name__)


#inherit from QMainWindow, Ui_MainWindow
class MechascanLevelGUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MechascanLevelGUI, self).__init__()
        self.setupUi(self)
        self.show()

        #self.create_actions()
        #self.create_menu()

        #self.setContextMenuPolicy(Qt.CustomContextMenu)
        # noinspection PyUnresolvedReferences
        #self.customContextMenuRequested.connect(self.show_menu)
        #self.read_prefs()
        self.resize(1000, 600)


    # noinspection PyUnresolvedReferences
    #def create_actions(self):
    #    self.horizontalSlider_3.valueChanged.connect(self.sliderchanged)

    def sliderchanged(self):
        print ("fsdvgfrwe")

    def read_prefs(self):
        """Parse the preferences from the config file, or set default values."""
        conf = preferences.Config(__name__ + ".ini")
        try:
            values = conf.read_config()
            self.auto_orient = values[0]
            self.slide_delay = values[1]
            self.quality = values[2]
        except KeyError:
            self.auto_orient = True
            self.slide_delay = 5
            self.quality = 90
        except:
            log.error("Unexpected error:", sys.exc_info()[0])
            raise
        self.reload_img = self.reload_auto if self.auto_orient else self.reload_nonauto

    def set_prefs(self):
        """Write preferences to the config file."""
        dialog = preferences.PrefsDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.auto_orient = dialog.auto_orient
            self.slide_delay = dialog.delay_spinb.value()
            self.quality = dialog.qual_spinb.value()
            conf = preferences.Config(__name__ + '.ini')
            conf.write_config(self.auto_orient, self.slide_delay, self.quality)
        self.reload_img = self.reload_auto if self.auto_orient else self.reload_nonauto

    def help_page(self):
        preferences.HelpDialog(self)

    def about_cm(self):
        about_message = 'Version: 0.0.0\nAuthor: Dan Tyrrell\nwww.dnt.com.au'
        # noinspection PyCallByClass,PyArgumentList,PyTypeChecker
        QMessageBox.about(self, 'About Mechalevel', about_message)

if __name__ == '__main__':  # if we're running file directly and not importing it
    import sys
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = MechascanLevelGUI()
    form.show()
    sys.exit(app.exec_())  # without sys.exit does not exit...