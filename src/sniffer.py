from scapy.all import *
from scapy.utils import PcapWriter
from cap_list import cap_list

class Sniffer:
    """simple sniffer class using scapy. this feels like cheating"""
    
    def __init__(self, filter_text="tcp or udp", iface=None):
        self.interface = iface
        if self.interface == None: 
            self.interface = conf.iface
        print(f"interface is - {self.interface}")
        self.writer = PcapWriter("output.pcap", append=True, sync=True)
        self.create_sniffer() 
        self.write = False

    def create_sniffer(self):
        self.sniffer = AsyncSniffer( iface=self.interface, filter="tcp or udp",prn=self.on_packet,store=False) # async sniffer to update logs at the same time

    @staticmethod 
    def ret_ifaces():
        return get_if_list()
        
    @staticmethod
    def d_iface():
        """return default iface"""
        return conf.iface
        
    def toggle_writer(self):
        """toggle the writer"""
        self.write = not self.write

    def add_to_list(self,l,s):
        l.append(s)

    def on_packet(self,pkt):
        """categorize and display correct format"""
        if IP in pkt:
            p = "TCP" if TCP in pkt else "UDP" if UDP in pkt else "OTHER"
            self.add_to_list(cap_list(), f"{p}  ||  {pkt[IP].src} => {pkt[IP].dst}    |   {pkt.summary()}")
        if self.write:
            self.writer.write(pkt)

    def start_sniff(self):
        self.sniffer.start()
