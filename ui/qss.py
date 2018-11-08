#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module provides Houdini Qss Style.

Author: Andy
Last edited: Sep 2017
"""

uiQss = '''
/*************** QWidget ***************/

QWidget
{
    color: #b1b1b1;
    background-color: #3a3a3a;
    font-family: Tahoma;
    font-size: 13px;
    /*font-style: normal;*/
    /*font-weight: bold;*/
}

QWidget:disabled
{
    color: #b1b1b1;
    background-color: #252525;
}

QAbstractScrollArea,
QTableView
{
    border: 1px solid #222;
}


/*************** QMainWindow ***************/

QMainWindow::separator
{
    background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #161616,
        stop: 0.5 #151515,
        stop: 0.6 #212121,
        stop: 1 #343434
    );
    color: white;
    padding-left: 4px;
    border: 1px solid #4c4c4c;
    spacing: 2px;
}

QMainWindow::separator:hover
{
    background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #d7801a,
        stop: 0.5 #b56c17,
        stop: 1 #ffa02f
    );
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
    spacing: 3px;
}


/*************** QToolTip ***************/

QToolTip
{
     border: 1px solid black;
     background-color: #eeeeee;
     padding: 1px;
     padding-left: 4px;
     padding-right: 4px;
     border-radius: 3px;
     color: black;
     opacity: 100;
}


/*************** QMenuBar ***************/

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background-color: #555555;
    color: #fff;
}

QMenuBar::item:pressed
{
    background: #444;
    border: 1px solid #000;
    background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 1 #212121,
        stop: 0.4 #343434
    );
    margin-bottom: -1px;
    padding-bottom: 1px;
}


/*************** QMenu ***************/

QMenu
{
    border: 1px solid #000;
}

QMenu::item
{
    padding: 2px 20px 2px 20px;
}

QMenu::item:selected
{
    color: #fff;
    background-color: #555555;
}

QMenu::separator
{
    height: 2px;
    background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #161616,
        stop: 0.5 #151515,
        stop: 0.6 #212121,
        stop: 1 #343434
    );
    color: white;
    padding-left: 4px;
    margin-left: 20px;
    margin-right: 5px;
}


/*************** QAbstractItemView ***************/

QAbstractItemView
{
    background-color: #353535;
    alternate-background-color: #323232;
    outline: 0;
    height: 20px;
}


/*************** QTreeView ***************/

/*ST*/
QTreeView
{
    background-color: #3a3a3a;
    alternate-background-color: #2e2e2e;
    show-decoration-selected: 1;
}

/*ST*/
QTreeView::item
{
    height: 20px;
}

QTreeView::branch:has-siblings:!adjoins-item
{
    border-image: url(:/vline.svg) 0;
}

QTreeView::branch:has-siblings:adjoins-item
{
    border-image: url(:/more.svg) 0;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item
{
    border-image: url(:/end.svg) 0;
}

QTreeView::branch:closed:has-children:has-siblings
{
    border-image: url(:/closed_siblings.svg) 0;
}

QTreeView::branch:closed:has-children:!has-siblings
{
    border-image: url(:/closed_no_siblings.svg) 0;
}

QTreeView::branch:open:has-children:has-siblings
{
    border-image: url(:/open_siblings.svg) 0;
}

QTreeView::branch:open:has-children:!has-siblings
{
    border-image: url(:/open_no_siblings.svg) 0;
}

/*ST*/
QTreeView::item:hover,
QTreeView::branch:hover
{
    border-top: 1px solid #605132;
    border-bottom: 1px solid #605132;
    background-color: rgba(255, 255, 255, 40);
}

/*ST*/
QTreeView::item:selected,
QTreeView::branch:selected
{
    /*background: #18A7E3;*/
    background: #605132;
}


/*************** QLabel ***************/

QLabel
{
    background: rgba(255, 255, 255, 0);
}


/*************** QListView ***************/

/*QListView::item
{
    border-color: #272727;
    border-width: 3px;
    border-style: solid;
    border: 1px solid #272727;
}*/

QListView::item:selected
{
    background-color: #5285A6;
    border-color: #5285A6;
}

QListView::item:hover
{
    border: 1px solid #5285A6;
    /*background-color: #5285A6;*/
}

/*QListView::branch:hover
{

}*/


/*************** QTableView ***************/

QHeaderView::section
{
    background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #393939,
        stop: 1 #272727
    );
    border: 1px solid #232323;
    padding-left: 30px;
    padding-right: 30px;
    padding-top: 5px;
    padding-bottom: 5px;
}

QTableView::item:selected
{
    background: #605132;
    border: 1px solid #b98620;
    color: rgb(220, 220, 220);
}

QTableView QTableCornerButton::section
{
    background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #393939,
        stop: 1 #272727
    );
    border: 1px solid #191919;
    border-top-width: 0px;
    border-left-width: 0px;
}


/*************** QLineEdit ***************/

QLineEdit, QDateEdit, QDateTimeEdit, QSpinBox
{
    background-color: #131313;
    padding: 1px;
    border-style: solid;
    border-width: 2px;
    border-color: #2b2b2b;
    border-radius: 0;
    color: rgb(255, 255, 255);
    min-height: 16px;
    selection-background-color: rgb(185, 134, 32);
    selection-color: rgb(0, 0, 0);
}


/*************** QPushButton ***************/

QPushButton
{
    color: #b1b1b1;
    background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #535353,
        stop: 0.1 #515151,
        stop: 0.5 #474747,
        stop: 0.9 #3d3d3d,
        stop: 1 #3a3a3a
    );
    border: 1px solid #232323;
    /*border-top-width: 2px;
    border-left-width: 2px;
    border-top-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #101010,
        stop: 1 #818181);
    border-left-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 1, y2: 0,
        stop: 0 #101010,
        stop: 1 #818181
    );
    border-radius: 0;*/
    padding: 3px;
    font-size: 12px;
    padding-left: 10px;
    padding-right: 10px;
}

QPushButton:disabled
{
    color: #b1b1b1;
    border: 1px solid #232323;
    padding: 3px;
    font-size: 12px;
    padding-left: 10px;
    padding-right: 10px;
}

QPushButton:checked
{
    border-color: #000;
    background-color: #2d2d2d;
    color: #cacaca;
    border-width: 1px;
}

QPushButton:hover
{
    background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #606060,
        stop: 0.1 #585858,
        stop: 0.5 #545454,
        stop: 0.9 #3d3d3d,
        stop: 1 #3a3a3a
    );
}

QPushButton:pressed
{
    background-color: #af8021;
    color: #fff;
}


/*************** QScrollBar ***************/

QScrollBar:horizontal
{
    border: 1px solid #222222;
    background: #222;
    height: 15px;
    margin: 0px 14px 0 14px;
}

QScrollBar:vertical
{
      border: 1px solid #222222;
      background: #222;
      width: 15px;
      margin: 14px 0 14px 0;
      border: 1px solid #222222;
}

QScrollBar::handle:vertical
{
    background: QLinearGradient(
        x1: 0, y1: 0,
        x2: 1, y2: 0,
        stop: 0 #535353,
        stop: 0.1 #515151,
        stop: 0.5 #474747,
        stop: 0.9 #3d3d3d,
        stop: 1 #3a3a3a
    );
    min-height: 20px;
    border-radius: 0px;
    border: 1px solid #222222;
    border-left-width: 0px;
    border-right-width: 0px;
}

QScrollBar::handle:horizontal
{
    background: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #535353,
        stop: 0.1 #515151,
        stop: 0.5 #474747,
        stop: 0.9 #3d3d3d,
        stop: 1 #3a3a3a
    );
    min-height: 20px;
    border-radius: 0px;
    border: 1px solid #222222;
    border-top-width: 0px;
    border-bottom-width: 0px;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal
{
    border: 1px solid #1b1b19;
    border-radius: 0px;
    background: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #535353,
        stop: 0.1 #515151,
        stop: 0.5 #474747,
        stop: 0.9 #3d3d3d,
        stop: 1 #3a3a3a
    );
    width: 14px;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical
{
    border: 1px solid #1b1b19;
    border-radius: 1px;
    background: QLinearGradient(
        x1: 0, y1: 0,
        x2: 1, y2: 0,
        stop: 0 #535353,
        stop: 0.1 #515151,
        stop: 0.5 #474747,
        stop: 0.9 #3d3d3d,
        stop: 1 #3a3a3a
    );
    height: 14px;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal:pressed,
QScrollBar::sub-line:horizontal:pressed,
QScrollBar::add-line:vertical:pressed,
QScrollBar::sub-line:vertical:pressed
{
    background: #5b5a5a;
}

QScrollBar::sub-line:vertical
{
    subcontrol-position: top;
}

QScrollBar::add-line:vertical
{
    subcontrol-position: bottom;
}

QScrollBar::sub-line:horizontal
{
    subcontrol-position: left;
}

QScrollBar::add-line:horizontal
{
    subcontrol-position: right;
}

QScrollBar::add-page:horizontal,
QScrollBar::sub-page:horizontal
{
    background: none;
}

QScrollBar::up-arrow:vertical
{
    border-image: url(:/arrow_up.png) 1;
}

QScrollBar::down-arrow:vertical
{
    border-image: url(:/arrow_down.png) 1;
}

QScrollBar::right-arrow:horizontal
{
    border-image: url(:/arrow_right.png) 1;
}

QScrollBar::left-arrow:horizontal
{
    border-image: url(:/arrow_left.png) 1;
}

QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical
{
    background: none;
}


/*************** QSlider ***************/

QSlider::groove:horizontal
{
    border: 1px solid #000;
    background: #000;
    height: 3px;
    border-radius: 0px;
}

QSlider::sub-page:horizontal
{
    background: #404040;
    border: 1px solid #000;
    height: 10px;
    border-radius: 0px;
}

QSlider::add-page:horizontal
{
    background: #626262;
    border: 1px solid #000;
    height: 10px;
    border-radius: 0px;
}

QSlider::handle:horizontal
{
    background: QLinearGradient(
        x1: 0, y1: 0,
        x2: 1, y2: 1,
        stop: 0 #696969,
        stop: 1 #505050
    );
    border: 1px solid #000;
    width: 5px;
    margin-top: -8px;
    margin-bottom: -8px;
    border-radius: 0px;
}

QSlider::hover
{
    background: #3f3f3f;
}

QSlider::groove:vertical
{
    border: 1px solid #ffaa00;
    background: #ffaa00;
    width: 3px;
    border-radius: 0px;
}

QSlider::add-page:vertical
{
    background: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #ffaa00,
        stop: 1 #ffaa00
    );
    background: #404040;
    border: 1px solid #000;
    width: 8px;
    border-radius: 0px;
}

QSlider::sub-page:vertical
{
    background: #626262;
    border: 1px solid #000;
    width: 8px;
    border-radius: 0px;
}

QSlider::handle:vertical
{
    background: QLinearGradient(
        x1: 0, y1: 0,
        x2: 1, y2: 1,
        stop: 0 #696969,
        stop: 1 #505050
    );
    border: 1px solid #000;
    height: 5px;
    margin-left: -8px;
    margin-right: -8px;
    border-radius: 0px;
}

/* disabled */

QSlider::sub-page:disabled,
QSlider::add-page:disabled
{
    border-color: #3a3a3a;
    background: #414141;
    border-radius: 0px;
}

QSlider::handle:disabled
{
    background: #3a3a3a;
    border: 1px solid #242424;
}

QSlider::disabled
{
    background: #3a3a3a;
}


/*************** QProgressBar ***************/

QProgressBar
{
    border: 1px solid #6d6c6c;
    border-radius: 0px;
    text-align: center;
    background: #262626;
    color: gray;
    border-bottom: 1px #545353;
}

QProgressBar::chunk
{
    background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #f0d66e,
        stop: 0.09 #f0d66e,
        stop: 0.1 #ecdfa8,
        stop: 0.7 #d9a933,
        stop: 0.91 #b88822
    );
}


/*************** QComboBox ***************/

QComboBox
{
    color: #b1b1b1;
    background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #535353,
        stop: 0.1 #515151,
        stop: 0.5 #474747,
        stop: 0.9 #3d3d3d,
        stop: 1 #3a3a3a
    );
    border: 1px solid #232323;
    /*padding: 3px;
    font-size: 12px;
    padding-left: 10px;
    padding-right: 10px;*/
}

/*QComboBox
{
    selection-background-color: #ffaa00;
    background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #515151,
        stop: 0.5 #484848,
        stop: 1 #3d3d3d
    );
    border-style: solid;
    border: 1px solid #000;
    border-radius: 0;
    padding-left: 9px;
    min-height: 20px;
    font: 10pt;
}*/

QComboBox:hover
{
    /*background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #555555,
        stop: 0.5 #4d4d4d,
        stop: 1 #414141
        );*/
    /*font: 14pt;*/
}

/*QComboBox:on
{
    background-color: #b98620;
    color: #fff;
    selection-background-color: #494949;
}*/

QComboBox::drop-down
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #3d3d3d,
        stop: 1 #282828
    );
    border-width: 0px;
}

/*QComboBox::down-arrow
{
    width: 10px;
    height: 10px;
    image: url(:/sort-down.svg);
}*/

/*QComboBox QAbstractItemView
{
    background-color: #3a3a3a;
    border-radius: 0px;
    border: 1px solid #101010;
    border-top-color:  #818181;
    border-left-color: #818181;
    selection-background-color: #606060;
    padding: 2px;
}*/

QComboBox QAbstractItemView::item
{
    margin-top: 3px;
}

/*QListView#comboListView
{
    background: rgb(80, 80, 80);
    color: rgb(220, 220, 220);
    min-height: 90px;
    margin: 0 0 0 0;
}

QListView#comboListView::item
{
    background-color: rgb(80, 80, 80);
}

QListView#comboListView::item:hover
{
    background-color: rgb(95, 95, 95);
}*/


/*************** QCheckBox ***************/

QCheckBox::indicator
{
    width: 13px;
    height: 13px;
}

QCheckBox::indicator:unchecked
{
    background-color: #282828;
}

/*QCheckBox::indicator:unchecked
{
    border: 1px solid #5A5A5A;
    image: url(:/checkbox_unchecked.png);
}*/

/*QCheckBox::indicator:checked
{
    background-color: #282828;
    image: url(:/checkmark.svg);
}*/


/*************** QRadioButton ***************/

QRadioButton::indicator:unchecked
{
    image: url(Z:/houdini/python/icons/radio_unchecked_disabled.png);
}

QRadioButton::indicator:checked
{
    image: url(Z:/houdini/python/icons/radio_checked_disabled.png);
}

QTableView
{
    background-color: #353535;
    alternate-background-color: #323232;
}


/*************** QTabWidget ***************/

QTabWidget::pane
{
    border: 1px solid #5285A6;
    margin-top: 2px;
}
/*hide line under selected tab*/

QTabWidget::tab-bar
{
    left: 5px;
    /*move to the right by 5px*/
}

QTabBar::tab
{
    border-radius: 1px;
    min-height: 2ex;
    min-width: 10ex;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
}

/*QTabBar::tab
{
    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
    border-radius: 0px;
    min-width: 15ex;
    padding-left: 3px;
    padding-right: 5px;
    padding-top: 1px;
    padding-bottom: 2px;
    background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #4b4b4b,
        stop: 1 #252525
    );
}*/
/*QTabBar::tab:hover*/

QTabBar::tab:selected
{
    /*border-bottom: 0px;*/
    /*background-color: #5285A6;*/
    color:QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
    padding:1px
    /*background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #4b4b4b,
        stop: 1 #3a3a3a
    );*/
}
QTabBar:selected
{
    /*border-bottom: 0px;*/
    /*background-color: #5285A6;*/
    color:QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
    padding:10px
    /*background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #4b4b4b,
        stop: 1 #3a3a3a
    );*/
}

/*QTabBar::tab:only-one
{
    margin: 0;
}*/


/*************** QGroupBox ***************/

QGroupBox
{
    /*border-left-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 1, y2: 0,
        stop: 0 #4b4b4b,
        stop: 1 #3a3a3a
    );*/
    /*border-right-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 1, y2: 0,
        stop: 0 #111,
        stop: 1 #3a3a3a
    );*/
    /*border-top-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #4b4b4b,
        stop: 1 #3a3a3a
    );*/
    /*border-bottom-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #111,
        stop: 1 #3a3a3a
    );*/
    border-width: 1px;
    border-color: #2d2d2d;
    border-style: solid;
    border-radius: 0px;
    padding-top: 10px;
}

/*QGroupBox::title
{
    background-color: transparent;
    subcontrol-position: top left;
    padding: 4 10px;
}*/


/*************** QSpinBox ***************/
/*, QDoubleSpinBox*/

QSpinBox::up-button,
QDoubleSpinBox::up-button,
QTimeEdit::up-button
{
    /*background:QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #535353,
        stop: 1 #3a3a3a
    );*/
    subcontrol-origin: border;
    subcontrol-position: top right;
    width: 16px;
    /*border: 1px solid #333;*/
}

QSpinBox::down-button,
QDoubleSpinBox::down-button,
QTimeEdit::down-button
{
    /*background: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #535353,
        stop: 1 #3a3a3a
    );*/
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width: 16px;
    /*border: 1px solid #333;*/
}

QSpinBox::down-button,
QDoubleSpinBox::down-button,
QTimeEdit::down-button,
QSpinBox::up-button,
QDoubleSpinBox::up-button,
QTimeEdit::up-button
{
    color: #b1b1b1;
    background-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #535353,
        stop: 0.1 #515151,
        stop: 0.5 #474747,
        stop: 0.9 #3d3d3d,
        stop: 1 #3a3a3a
    );
    border: 2px solid #232323;
    border-top-width: 2px;
    border-left-width: 2px;
    border-top-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 0, y2: 1,
        stop: 0 #101010,
        stop: 1 #818181
    );
    border-left-color: QLinearGradient(
        x1: 0, y1: 0,
        x2: 1, y2: 0,
        stop: 0 #101010,
        stop: 1 #818181
    );
    border-radius: 0;
}

QSpinBox::up-button:pressed,
QDoubleSpinBox::up-button:pressed,
QTimeEdit::up-button:pressed,
QSpinBox::down-button:pressed,
QDoubleSpinBox::down-button:pressed,
QTimeEdit::down-button:pressed
{
    background-color: #828282;
}

QSpinBox::up-button,
QDoubleSpinBox::up-button
{
    image: url(:/spin_up.png);
}

QSpinBox::down-button,
QDoubleSpinBox::down-button
{
    image: url(:/spin_down.png);
}

'''
