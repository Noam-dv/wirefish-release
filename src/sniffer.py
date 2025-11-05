from scapy.all import *
from scapy.utils import PcapWriter
from cap_list import cap_list

class Sniffer:
    def __init__(self, filter_text="tcp or udp", iface=None):
        self.interface = iface
        if self.interface == None: 
            self.interface = conf.iface
        print(f"interfaec is - {self.interface}")
        self.writer = PcapWriter("output.pcap", append=True, sync=True)
        self.create_sniffer()
        self.write = False

    def create_sniffer(self):
        self.sniffer = AsyncSniffer( iface=self.interface, filter="tcp or udp",prn=self.on_packet,store=False)

    @staticmethod #js writing here for organization
    def ret_ifaces():
        return get_if_list()
    @staticmethod #default interface
    def d_iface():
        return conf.iface
        
    def toggle_writer(self):
        self.write = not self.write

    def add_to_list(self,l,s):
        l.append(s)

    def on_packet(self,pkt):
        if IP in pkt:
            p = "TCP" if TCP in pkt else "UDP" if UDP in pkt else "OTHER"
            self.add_to_list(cap_list(), f"{p}  ||  {pkt[IP].src} => {pkt[IP].dst}    |   {pkt.summary()}")
        if self.write:
            self.writer.write(pkt)

    def start_sniff(self):
        self.sniffer.start()
