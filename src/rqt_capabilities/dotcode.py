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

"""Provides functions to produce dotcode which represents the capability graph
"""

from capabilities.discovery import spec_index_from_service

from qt_dotgraph.pydotfactory import PydotFactory


def generate_dotcode_from_capability_info():
    spec_index, errors = spec_index_from_service()
    assert not errors
    dotcode_factory = PydotFactory()
    dotgraph = dotcode_factory.get_graph(rankdir="BT")
    for name in spec_index.interfaces:
        dotcode_factory.add_node_to_graph(dotgraph, nodename=name, shape="box")
    for name in spec_index.semantic_interfaces:
        dotcode_factory.add_node_to_graph(dotgraph, nodename=name, shape="box")
    for name, provider in spec_index.providers.items():
        dotcode_factory.add_node_to_graph(dotgraph, nodename=name, shape="ellipse")
        dotcode_factory.add_edge_to_graph(dotgraph, name, provider.implements, label="provides")
        for dep in provider.dependencies:
            dotcode_factory.add_edge_to_graph(dotgraph, name, dep, label="requires")
    return dotcode_factory.create_dot(dotgraph)
