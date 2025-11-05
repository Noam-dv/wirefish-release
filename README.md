# Wirefish
<p align="center">
  <img src="img/icon.png" width="50%" alt="">
</p>

Wireshark ripoff made with **PySide6 + Scapy**.  
captures packets shows them in a readable fashion, lets you pick an interface, filter the view, and save to **PCAP** (incase u wanna view it in wireshark beacuse its better)

## Features
- live capture with scapy (`tcp or udp` filter is on by default)
- interface picker (includes your default iface)
- view filter (ui only, so ur pcap files are still capturing everything)
- toggle **save to PCAP** writes out to `output.pcap`
- capped table (so ur pc doesnt kill itself)

## Install
1. download **Python 3.10+** and **Npcap** (you already have it if u installed wireshark).
2. download repository.
3. run the **`run.bat`** script  
   – upgrades pip, installs from `requirements.txt`, and launches the app.