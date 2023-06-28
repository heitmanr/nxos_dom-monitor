# nxos_dom-monitor
## use on your own risk
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

allows to Cisco Nexus (NXOS Operating-System) to monitor it's optical transceivers and generate Syslog-Events

the following Warning/Alarm-Levels are possible:
  low alarm (--)
  low warning (-)
  high warning (+)
  high alarm (++)

For example "rx_pwr--:Eth1/16,Eth1/22,Eth1/23,Eth1/26,Eth1/34,Eth1/35,Eth2/19" is the message generated for a bunch of interfaces receiving not enough power.

It requires two components:
(a) scheduler to run the script, e.g. 1x a day, and send the syslog-message
(b) the script itself which generates the list of affected interfaces

## installation
(1) copy the python-script to the local bootdisk:
(2) add the EEM-Commands to the running-config

the Applet should run 1x immedeately and after 24h again and than every day
