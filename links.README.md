theHarvester:https://github.com/laramies/theHarvester

recon-ng:https://github.com/lanmaster53/recon-ng

shodancli:https://github.com/malinkinsa/shodancli

whois:https://github.com/weppos/whois

WhatWeb:https://github.com/urbanadventurer/WhatWeb

nikto:https://github.com/sullo/nikto

wafw00f:https://github.com/EnableSecurity/wafw00f

aquatone:https://github.com/michenriksen/aquatone

ffuf:https://github.com/ffuf/ffuf

wfuzz:https://github.com/xmendez/wfuzz

gobuster:https://github.com/OJ/gobuster

subfinder:https://github.com/projectdiscovery/subfinder

Sudomy:https://github.com/screetsec/Sudomy

ESD:https://github.com/FeeiCN/ESD?tab=readme-ov-file

Sublist3r:https://github.com/aboul3la/Sublist3r

CloudEnum:https://github.com/initstring/cloud_enum

CloudBrute:https://github.com/0xsha/CloudBrute

dnsrecon:https://github.com/darkoperator/dnsrecon

massdns:https://github.com/blechschmidt/massdns

subbrute:https://github.com/TheRook/subbrute

nmap:https://github.com/nmap/nmap

masscan:https://github.com/robertdavidgraham/masscan

searchsploit:https://gitlab.com/exploit-database/exploitdb

metasploit-framework:https://github.com/rapid7/metasploit-framework

sqlmap:https://github.com/sqlmapproject/sqlmap

XSStrike:https://github.com/s0md3v/XSStrike

xsser:https://github.com/epsylon/xsser

wpscan:https://github.com/wpscanteam/wpscan

CMSeeK:https://github.com/Tuhinshubhra/CMSeeK

CMSmap:https://github.com/dionach/CMSmap

hashcat:https://github.com/hashcat/hashcat

john:https://github.com/openwall/john

thc-hydra:https://github.com/vanhauser-thc/thc-hydra

LinEnum:https://github.com/rebootuser/LinEnum

linux-smart-enumeration:https://github.com/diego-treitos/linux-smart-enumeration

enum4linux-ng:https://github.com/cddmp/enum4linux-ng

WindowsEnum:https://github.com/absolomb/WindowsEnum

mimikatz:https://github.com/gentilkiwi/mimikatz

linPEAS:https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS

linux-exploit-suggester:https://github.com/The-Z-Labs/linux-exploit-suggester

linuxprivchecker:https://github.com/sleventyeleven/linuxprivchecker

winPEAS:https://github.com/peass-ng/PEASS-ng/tree/master/winPEAS

PrivescCheck:https://github.com/itm4n/PrivescCheck

windows-privesc-check:https://github.com/pentestmonkey/windows-privesc-check

RemotePotato0:https://github.com/antonioCoco/RemotePotato0

tcpdump:https://github.com/the-tcpdump-group/tcpdump

termshark:https://github.com/gcla/termshark

ettercap:https://github.com/Ettercap/ettercap

bettercap:https://github.com/bettercap/bettercap

arpspoof:https://github.com/alandau/arpspoof

Responder:https://github.com/SpiderLabs/Responder

> `dst=README.md; cp base.$dst $dst; while read line; do x=$(cut -d: -f1 <<< $line); y=$(cut -d: -f2- <<< $line); sed -i "s;⠀$x;⠀<a href='$y'>$x</a>;" $dst;done< <(grep ':http' links.$dst | grep -v '^>')`