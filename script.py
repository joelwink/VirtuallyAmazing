#!/usr/bin/env python
# script.py -*-python-*-

import json
import requests
import sys
sys.path.append("./automation/solution/")

from V3 import *
from config import *
from manageBlueprint import *

class Connector(object):
  def __init__(self):
    self.connection = Connection(User(USER, PASSWD),
                                 Host(IPADDRESS, PORT))
    self.data = { 'filter': '',
                  'offset': 0,
                  'length': 20 }

  def _show_list(self, items):
    for item in items:
      print 'type: ' + str(item.type)
      print 'name: ' + str(item.name)
      #print 'description: ' + str(self.description)
      print 'ipaddress: ' + str(item.ipaddress)
      print 'uuid: ' + str(item.uuid)
      print 'power state: ' + str(item.powerState)
      print 'memory: ' + str(item.memory)
      print ' '

  def show_list(self):
    self._show_list(VirtualMachineService().getVMS(self.connection,
                                                   self.data))

    try:
      r = requests.get(
        'https://10.21.72.37:9440/PrismGateway/services/rest/v2.0/cluster/',
        json=self.data,
        verify=False,
        auth=(USER, PASSWD))

      r.raise_for_status()
    except requests.HTTPError as ex:
      print "Failed to create %s\n" % str(ex)

    j = r.json()
    print 'Load = %.3f%%' % (int(j['stats']['hypervisor_cpu_usage_ppm']) /
                             1000000.0 * 100.0)

if __name__ == "__main__":
  c = Connector()
  c.show_list()
