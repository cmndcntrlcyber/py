{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "### Hunting Tasks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Object `string` not found.\n"
     ]
    }
   ],
   "source": [
    "# Task 1: How many HTTP packets contain the \"password\" string?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pyshark'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-65a0714c5489>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mpyshark\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mcount\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mcapture\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpyshark\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mFileCapture\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;34m'.pcap'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdisplay_filter\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'http contains password'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'pyshark'"
     ]
    }
   ],
   "source": [
    "import pyshark\n",
    "\n",
    "count = 0\n",
    "\n",
    "capture = pyshark.FileCapture(path+'.pcap', display_filter='http contains password')\n",
    "\n",
    "for packet in capture:\n",
    "    count = count + 1\n",
    "\n",
    "print(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Task 2: Which IP address sent GET requests for New York Times (www.nytimes.com)?\n",
    "\n",
    "import pyshark\n",
    "\n",
    "count = 0\n",
    "ip_list = []\n",
    "\n",
    "capture = pyshark.FileCapture('HTTP_traffic.pcap', display_filter='http.request.method==GET && http.host==\"www.nytimes.com\"')\n",
    "\n",
    "for packet in capture:\n",
    "    if packet.ip.dst not in ip_list:\n",
    "        ip_list.append(packet.ip.dst)\n",
    "\n",
    "print(ip_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Task 3: What is the session ID being used by 192.168.252.128 for Amazon India store (amazon.in)?\n",
    "\n",
    "import pyshark\n",
    "\n",
    "count = 0\n",
    "\n",
    "capture = pyshark.FileCapture('HTTP_traffic.pcap', display_filter='ip contains amazon.in && ip.src==192.168.252.128')\n",
    "\n",
    "for packet in capture:\n",
    "    print(packet.http.cookie)\n",
    "    break\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Task 4: What type of OS the machine on IP address 192.168.252.128 is using (i.e. Windows/Linux/MacOS/Solaris/Unix/BSD)? Bonus: Can you also guess the distribution/flavor?\n",
    "\n",
    "import pyshark\n",
    "\n",
    "count = 0\n",
    "\n",
    "capture = pyshark.FileCapture('HTTP_traffic.pcap', display_filter='ip.src==192.168.252.128 && http')\n",
    "\n",
    "for packet in capture:\n",
    "    print(packet.http.user_agent)\n",
    "    break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Task 1: Create a unique list of websites visited from IP 192.168.252.128?\n",
    "\n",
    "import pyshark\n",
    "\n",
    "count = 0\n",
    "\n",
    "url_list = []\n",
    "\n",
    "capture = pyshark.FileCapture('HTTP_traffic.pcap', display_filter='ip.src==192.168.252.128 && http && http.request.method==\"GET\"')\n",
    "\n",
    "for packet in capture:\n",
    "    host_name = packet.http.host\n",
    "    host_name = \".\".join(host_name.split('.')[-2:])\n",
    "    if host_name not in url_list:\n",
    "        url_list.append(host_name)\n",
    "        \n",
    "print(url_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Task 2: Create a unique list of DNS servers were used to make DNS resolutions?\n",
    "\n",
    "import pyshark\n",
    "\n",
    "count = 0\n",
    "\n",
    "unique_list = []\n",
    "\n",
    "capture = pyshark.FileCapture('HTTP_traffic.pcap', display_filter='dns.flags.response == 1')\n",
    "\n",
    "for packet in capture:\n",
    "    if packet.ip.src not in unique_list:\n",
    "        unique_list.append(packet.ip.src)\n",
    "        \n",
    "print(unique_list)"
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
