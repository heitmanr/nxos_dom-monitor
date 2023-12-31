# nxos_dom-monitor

allows to Cisco Nexus (NXOS Operating-System) to monitor it's optical transceivers and generate Syslog-Events

the following Warning/Alarm-Levels are possible:
  low alarm (--)
  low warning (-)
  high warning (+)
  high alarm (++)

For example "rx_pwr+:Eth2/9,Eth2/10;rx_pwr--:Eth1/16,Eth1/22,Eth1/23,Eth1/26,Eth1/34,Eth1/35,Eth2/19" is the message generated for a bunch of interfaces receiving to much(warning) or not enough power(alarm).

It requires two components:
(a) scheduler to run the script, e.g. 1x a day, and send the syslog-message
(b) the script itself which generates the list of affected interfaces

## installation
(1) copy the python-script to the local bootdisk: into the /scripts/-Directory
## test
run the script manually
(2) cd scripts
(3) source nxos_dom.py
Expected result:
* list of interfaces with any transceiver warnings/alarms to be printed to the console
## automate
(2) add the EEM-Commands found in "nxos_dom-eem.cfg" to the running-config
The Applet should run 1x immedeately and after 24h again and then every day.
* check "show logging logfile" or remote syslog-log
