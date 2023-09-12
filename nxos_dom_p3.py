#!/bin/env python
#
# nxos_dom.py
#
import re
#
# return a list of interfaces, which are shutdown
# => their SFP/DOM-Measurements are irrelevant
#
def get_shutdown():
  result = []
  cli_result = cli('show int | egrep ignore-case ^Ethernet.*admin.*down | cut -d " " -f 1 | sed "s/Ethernet/Eth/g"')
  #
  for l in cli_result.split("\n"):
    result.append(l)
  #
  return result
#
# return: a string
# - containing up to 4 sub-strings
#   - separated by ";"
# - 1x substring per alarm/warning-level (--, -, +, ++)
#   - listing (","-separated) all interfaces affected by that DOM alarm/warning
#
def get_dom_alarm(shutdown):
  # 
  cli_result = cli('show int transceiver details | xml | inc "(<interface|flag)" | excl "> <" | sed "s/Ethernet/Eth/g"')
  #
  #
  result = {}
  #
  int_name = ""
  int_flags = {}
  #
  for l in cli_result.split("\n"):
    lm=re.match(".*\<interface\>(.*)\<.*", l)
    if lm:
      if int_name and int_flags and int_name not in shutdown:
        for k,v in int_flags.items():
          kv='{}{}'.format(k,v)
          if not kv in result:
            result[kv]=[]
          result[kv].append(int_name)
      #
      int_name = lm.groups()[0]
      int_flags = {}
    #
    lm=re.match(".*\<(.*)_flag\>(.*)\<.*", l)
    if lm:
      int_flags[lm.groups()[0]] = lm.groups()[1]
  #
  kvs = ";".join('{}:{}'.format(k,",".join(v)) for k,v in result.items())
  #
  return kvs
#
#
down = get_shutdown()
dom_alarm = get_dom_alarm(down)
#
# rx_pwr--:Eth1/16,Eth1/22,Eth1/23,Eth1/26,Eth1/34,Eth1/35,Eth2/19
#
print ("DOM",dom_alarm)
