from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.addresses import IPAddr, IPAddr6, EthAddr


import pox.lib.packet as pkt

log = core.getLogger()

#statically allocate a routing table for hosts
#MACs used in only in part 4
IPS = {
  "h10" : ("10.0.1.10", '00:00:00:00:00:01'),
  "h20" : ("10.0.2.20", '00:00:00:00:00:02'),
  "h30" : ("10.0.3.30", '00:00:00:00:00:03'),
  "serv1" : ("10.0.4.10", '00:00:00:00:00:04'),
  "hnotrust" : ("172.16.10.100", '00:00:00:00:00:05'),
}

class Part3Controller (object):
  """
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    print (connection.dpid)
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)
    #use the dpid to figure out what switch is being created
    if (connection.dpid == 1):
      self.s1_setup()
    elif (connection.dpid == 2):
      self.s2_setup()
    elif (connection.dpid == 3):
      self.s3_setup()
    elif (connection.dpid == 21):
      self.cores21_setup()
    elif (connection.dpid == 31):
      self.dcs31_setup()
    else:
      print ("UNKNOWN SWITCH")
      exit(1)

  def s1_setup(self):
    #put switch 1 rules here
    #pass
    
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
    
    # IP Traffic
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.nw_src = None
    match.nw_dst = None
    match.tp_src = None
    match.tp_dst = None
    match.dl_type = pkt.ethernet.IP_TYPE
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priority = 32768
    action = of.ofp_action_output(port = of.OFPP_FLOOD) 
    msg.actions.append(action)
    self.connection.send(msg)

  def s2_setup(self):
    #put switch 2 rules here
    #pass
    
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
    
    # IP Traffic
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.nw_src = None
    match.nw_dst = None
    match.tp_src = None
    match.tp_dst = None
    match.dl_type = pkt.ethernet.IP_TYPE
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priority = 32768
    action = of.ofp_action_output(port = of.OFPP_FLOOD) 
    msg.actions.append(action)
    self.connection.send(msg)

  def s3_setup(self):
    #put switch 3 rules here
    #pass
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
    
    # IP Traffic
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.nw_src = None
    match.nw_dst = None
    match.tp_src = None
    match.tp_dst = None
    match.dl_type = pkt.ethernet.IP_TYPE
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priority = 32768
    action = of.ofp_action_output(port = of.OFPP_FLOOD) 
    msg.actions.append(action)
    self.connection.send(msg)

  def cores21_setup(self):
    #put core switch rules here
    #pass
    
    #hnotrust
    
    
    
    #hnotrust - h10, h20, h30, serv1 icmp not allow
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.nw_src = IPAddr("172.16.10.100")
    match.nw_dst = None
    match.tp_src = None
    match.tp_dst = None
    match.nw_proto = pkt.ipv4.ICMP_PROTOCOL
    match.dl_type = pkt.ethernet.IP_TYPE
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priority = 32768
    #action = of.ofp_action_output(port = of.OFPP_FLOOD) 
    #msg.actions.append(action)
    self.connection.send(msg)
    
    #hnotrust - serv1 not allow
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.nw_src = IPAddr("172.16.10.100")
    match.nw_dst = IPAddr("10.0.4.10")
    match.tp_src = None
    match.tp_dst = None
    match.dl_type = pkt.ethernet.IP_TYPE
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priority = 32768
    self.connection.send(msg)
    
    # ICMP
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.nw_src = None #IPAddr("10.0.4.10")
    match.nw_dst = None #IPAddr("10.0.4.20")
    match.tp_src = None #1
    match.tp_dst = None #1
    match.nw_proto = pkt.ipv4.ICMP_PROTOCOL
    match.dl_type = pkt.ethernet.IP_TYPE
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priority = 32768
    #action = of.ofp_action_output(port = 2) 
    action = of.ofp_action_output(port = of.OFPP_FLOOD) 
    msg.actions.append(action)
    self.connection.send(msg)
    
    # ARP
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.nw_src = None #IPAddr("10.0.4.10")
    match.nw_dst = None #IPAddr("10.0.4.20")
    match.tp_src = None #1
    match.tp_dst = None #1
    match.nw_proto = pkt.arp.REQUEST
    match.dl_type = pkt.ethernet.ARP_TYPE
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priority = 32768
    #action = of.ofp_action_output(port = 2) 
    action = of.ofp_action_output(port = of.OFPP_FLOOD) 
    msg.actions.append(action)
    self.connection.send(msg)
    
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.nw_src = None #IPAddr("10.0.4.10")
    match.nw_dst = None #IPAddr("10.0.4.20")
    match.tp_src = None #1
    match.tp_dst = None #1
    match.nw_proto = pkt.arp.REPLY
    match.dl_type = pkt.ethernet.ARP_TYPE
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priority = 32768
    #action = of.ofp_action_output(port = 2) 
    action = of.ofp_action_output(port = of.OFPP_FLOOD) 
    msg.actions.append(action)
    self.connection.send(msg)
    
    # IP Traffic
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.nw_src = None
    match.nw_dst = None
    match.tp_src = None
    match.tp_dst = None
    match.dl_type = pkt.ethernet.IP_TYPE
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priority = 32768
    action = of.ofp_action_output(port = of.OFPP_FLOOD) 
    msg.actions.append(action)
    self.connection.send(msg)
    
    '''
    #h10
    #h10 - h20 allow
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.nw_src = IPAddr("10.0.1.10")
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
    
    #h10 - h30 allow
    
    #h10 - hnotrust allow
    
    #h10 - serv1 allow
    
    #h20
    #h20 - h10 allow
    
    #h20 - h30 allow
    
    #h20 - hnotrust allow
    
    #h20 - serv1 allow
    
    #h30
    #h30 - h10 allow
    
    #h30 - h20 allow
    
    #h30 - hnotrust allow
    
    #h30 - serv1 allow
    
    #serv1
    #serv1 - h10 allow
    
    #serv1 - h20 allow
    
    #serv1 - h30 allow
    
    #h30 - hnotrust allow
    
    '''
    
    
    

  def dcs31_setup(self):
    #put datacenter switch rules here
    #pass
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
    
    # IP Traffic
    msg = of.ofp_flow_mod()
    match = of.ofp_match()
    match.nw_src = None
    match.nw_dst = None
    match.tp_src = None
    match.tp_dst = None
    match.dl_type = pkt.ethernet.IP_TYPE
    msg.match = match
    msg.hard_timeout = 0
    msg.soft_timeout = 0
    msg.priority = 32768
    action = of.ofp_action_output(port = of.OFPP_FLOOD) 
    msg.actions.append(action)
    self.connection.send(msg)

  #used in part 4 to handle individual ARP packets
  #not needed for part 3 (USE RULES!)
  #causes the switch to output packet_in on out_port
  def resend_packet(self, packet_in, out_port):
    msg = of.ofp_packet_out()
    msg.data = packet_in
    action = of.ofp_action_output(port = out_port)
    msg.actions.append(action)
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
    print ("Unhandled packet from " + str(self.connection.dpid) + ":" + packet.dump())

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Part3Controller(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
