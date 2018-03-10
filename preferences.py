#!/usr/bin/env python3
from PyQt5.QtWidgets import (QDialog, QDialogButtonBox, QLabel, QSpinBox, QCheckBox,
                             QGridLayout, QVBoxLayout, QScrollArea)
import os
import configparser
import logging
log = logging.getLogger(__name__)


class Config(object):
    """Read, write / create config file."""

    def __init__(self, config_file):
        config_dir = os.environ.get('XDG_CONFIG_HOME') or os.path.expanduser('~/.config')
        self.config_dir = os.path.join(config_dir, config_file)
        if not os.path.isdir(self.config_dir):
            os.mkdir(self.config_dir)
        self.config_file = os.path.join(self.config_dir, config_file)

        self.config = configparser.ConfigParser()

    def read_config(self):
        self.config.read(self.config_file)
        com = self.config['Common']
        orientation = com.getboolean('AutoOrientation')
        slide_delay = int(com['SlideTimeDelay'])
        quality = int(com['Quality'])
        return orientation, slide_delay, quality

    def write_config(self, orientation, slide_delay, quality):
        self.config['Common'] = {}
        com = self.config['Common']
        com['AutoOrientation'] = str(orientation)
        com['SlideTimeDelay'] = str(slide_delay)
        com['Quality'] = str(quality)
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)



class HelpDialog(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)

        self.setWindowTitle('Help!')
        base_dir = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(base_dir, 'data', 'help_page')) as help_file:
            text = help_file.read()

        layout = QVBoxLayout()
        self.setLayout(layout)
        label = QLabel(text)
        label.setWordWrap(True)
        label.setMargin(12)
        scrollwin = QScrollArea()
        scrollwin.setWidget(label)
        layout.addWidget(scrollwin)

        buttons = QDialogButtonBox(QDialogButtonBox.Close)
        # noinspection PyUnresolvedReferences
        buttons.accepted.connect(self.accept)
        # noinspection PyUnresolvedReferences
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.resize(650, 500)
        self.show()
