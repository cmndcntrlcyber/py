{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'scapy'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-fb6c06862b0c>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;31m# Task 1: Import all scapy modules\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mscapy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mall\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[1;33m*\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'scapy'"
     ]
    }
   ],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# Task 1: Import all scapy modules\n",
    "\n",
    "from scapy.all import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# Task 2: Print the list of all supprted layers by scapy. Layers starting with Dot11 are the one for WiFi packets.\n",
    "\n",
    "ls()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# Task 3: Print the list of all supported operations.\n",
    "\n",
    "lsc()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# Task 4: Load the packets from given PCAP file into a list.\n",
    "\n",
    "packets = rdpcap('WiFi_traffic.pcap')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# Task 5: Print the first packet in detail, showing all the WiFi layers.\n",
    "\n",
    "pkt = packets[0]\n",
    "\n",
    "pkt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# ls(RadioTap)\n",
    "\n",
    "Task 6: Print the layout/format of the RadioTap header."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# Task 7: Print the layout/format of the Dot11 header.\n",
    "\n",
    "ls(Dot11)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# Task 8: Print the layout/format of the Beacon (Dot11Beacon) header.\n",
    "\n",
    "ls(Dot11Beacon)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# Task 9: Print the layout/format of the Information Element (Dot11Elt) header.\n",
    "\n",
    "ls(Dot11Elt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# Task 10: Print only the WiFi layer from the loaded packet.\n",
    "\n",
    "pkt.payload"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# Task 11: Print only the WiFi Beacon layer from the loaded packet. \n",
    "\n",
    "pkt.payload.payload"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# Task 12: Print only the first information element layer from the loaded packet.\n",
    "\n",
    "pkt.payload.payload.payload"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# Task 13: Print the SSID name from the packet.\n",
    "\n",
    "print pkt.payload.payload.info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# Task 14: Print the Beacon layer of the packet by using getlayer() function.\n",
    "\n",
    "beacon_layer = pkt.getlayer(Dot11Beacon)\n",
    "\n",
    "beacon_layer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wi-Fi Layers: Scapy\n",
    "# Task 15: How to check if Beacon layer is present in a packet?\n",
    "\n",
    "pkt.haslayer(Dot11Beacon)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
