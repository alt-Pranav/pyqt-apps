# The PEP 484 type hints stub file for the QtSvgWidgets module.
#
# Generated by SIP 6.6.2
#
# Copyright (c) 2022 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import enum
import typing

import PyQt6.sip

from PyQt6 import QtWidgets
from PyQt6 import QtSvg
from PyQt6 import QtGui
from PyQt6 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class QGraphicsSvgItem(QtWidgets.QGraphicsObject):

    @typing.overload
    def __init__(self, parent: typing.Optional[QtWidgets.QGraphicsItem] = ...) -> None: ...
    @typing.overload
    def __init__(self, fileName: str, parent: typing.Optional[QtWidgets.QGraphicsItem] = ...) -> None: ...

    def type(self) -> int: ...
    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionGraphicsItem, widget: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    def boundingRect(self) -> QtCore.QRectF: ...
    def maximumCacheSize(self) -> QtCore.QSize: ...
    def setMaximumCacheSize(self, size: QtCore.QSize) -> None: ...
    def elementId(self) -> str: ...
    def setElementId(self, id: str) -> None: ...
    def renderer(self) -> QtSvg.QSvgRenderer: ...
    def setSharedRenderer(self, renderer: QtSvg.QSvgRenderer) -> None: ...


class QSvgWidget(QtWidgets.QWidget):

    @typing.overload
    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    @typing.overload
    def __init__(self, file: str, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    def paintEvent(self, event: QtGui.QPaintEvent) -> None: ...
    @typing.overload
    def load(self, file: str) -> None: ...
    @typing.overload
    def load(self, contents: QtCore.QByteArray) -> None: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def renderer(self) -> QtSvg.QSvgRenderer: ...
