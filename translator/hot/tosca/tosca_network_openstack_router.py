#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from translator.hot.syntax.hot_resource import HotResource

# Name used to dynamically load appropriate map class.
TARGET_CLASS_NAME = 'ToscaNetworkOpenstackRouter'


class ToscaNetworkOpenstackRouter(HotResource):
    '''Translate TOSCA node type tosca.nodes.network.openstack.Router.'''

    toscatype = 'tosca.nodes.network.openstack.Router'
    ROUTER_PROPS = ['external_network']

    def __init__(self, nodetemplate, csar_dir=None):
        super(ToscaNetworkOpenstackRouter, self).__init__(nodetemplate,
                                                  type='OS::Neutron::Router',
                                                  csar_dir=csar_dir)
        pass

    def handle_properties(self):
        tosca_props = self.get_tosca_props()

        net_props = {}

        for key, value in tosca_props.items():
            if key in self.ROUTER_PROPS:
                if key == 'external_network':
                    net_props['external_gateway_info'] = value

        self.properties = net_props
        # pass
