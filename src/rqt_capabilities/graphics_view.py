# Software License Agreement (BSD License)
#
# Copyright (c) 2013, Open Source Robotics Foundation, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Open Source Robotics Foundation, Inc. nor
#    the names of its contributors may be used to endorse or promote
#    products derived from this software without specific prior
#    written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Author: William Woodall <william@osrfoundation.org>

"""Extends the InteractiveGraphicsView from rqt_graph to handle special actions
"""

from PySide.QtCore import Qt
from PySide.QtCore import QPoint

from PySide.QtGui import QMenu

from rqt_graph.interactive_graphics_view import InteractiveGraphicsView


class CapabilitiesInteractiveGraphicsView(InteractiveGraphicsView):
    """Extends the InteractiveGraphicsView from rqt_graph"""
    def __init__(self, parent=None):
        super(InteractiveGraphicsView, self).__init__(parent)
        self._last_pan_point = None
        self._last_scene_center = None

    def mousePressEvent(self, mouse_event):
        if mouse_event.button() == Qt.RightButton:
            pos = mouse_event.pos()
            item = self.itemAt(pos)
            if not item:
                print('nothing there')
                return

            def trigger():
                print(item)

            menu = QMenu()
            action = menu.addAction('Test')
            action.triggered.connect(trigger)
            pos = mouse_event.globalPos()
            pos = QPoint(pos.x(), pos.y())
            menu.exec_(pos)
        else:
            InteractiveGraphicsView.mousePressEvent(self, mouse_event)
