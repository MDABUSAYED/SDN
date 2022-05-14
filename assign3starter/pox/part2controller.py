from pox.core import core
import pox.openflow.libopenflow_01 as of

from pox.lib.addresses import IPAddr
import pox.lib.packet as pkt

log = core.getLogger()

class Firewall (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

    #add switch rules here
    
    # ICMP
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.nw_src = None
    match.nw_dst = None
    match.tp_src = None
    match.tp_dst = None
    match.nw_proto = pkt.ipv4.ICMP_PROTOCOL
    match.dl_type = pkt.ethernet.IP_TYPE
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priority = 32768
    action = of.ofp_action_output(port = of.OFPP_FLOOD) 
    msg.actions.append(action)
    self.connection.send(msg)
    
    # ARP
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.nw_src = None
    match.nw_dst = None
    match.tp_src = None
    match.tp_dst = None
    match.nw_proto = pkt.arp.REQUEST
    match.dl_type = pkt.ethernet.ARP_TYPE
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priority = 32768
    action = of.ofp_action_output(port = of.OFPP_FLOOD) 
    msg.actions.append(action)
    self.connection.send(msg)
    
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.nw_src = None
    match.nw_dst = None
    match.tp_src = None
    match.tp_dst = None
    match.nw_proto = pkt.arp.REPLY
    match.dl_type = pkt.ethernet.ARP_TYPE
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priority = 32768
    action = of.ofp_action_output(port = of.OFPP_FLOOD) 
    msg.actions.append(action)
    self.connection.send(msg)
    
    
    
    # Others
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.dl_type = pkt.ethernet.IP_TYPE
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priority = 1
    
    self.connection.send(msg)
    
    

  def _handle_PacketIn (self, event):
    """
    Packets not handled by the router rules will be
    forwarded to this method to be handled by the controller
    """

    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    print ("Unhandled packet :" + str(packet.dump()))

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Firewall(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
