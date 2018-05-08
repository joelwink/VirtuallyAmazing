#!/usr/bin/env python
# script.py -*-python-*-

import json
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


if __name__ == "__main__":
  c = Connector()
  c.show_list()
