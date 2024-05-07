```mermaid
flowchar TB
    subgraph Information Gathering
    direction LR
        osint[
            OSINT
            -----
            theHarvester
            recon-ng
            shodancli
            whois
        ]
        subgraph Infrastructure Enumeration
        direction TB
            domains[
                Domains
                -------
                subfinder
                sudomy
                ESD
                sublist3r
            ]
            dns[
                DNS
                ---
                dnsrecon
                massDNS
                subbrute
            ]
            cloud[
                Cloud Services
                --------------
                cloud_enum
                cloudbrute
            ]
            host[
                Host Services
                -------------
                nmap
                masscan
            ]
        end
        subgraph WebApp Enumeration
        direction TB
            scanning[
                Scanning
                -------
                whatweb
                nikto
                wafw00f
                aquatone
            ]
            fuzzing[
                Fuzzing
                -------
                ffuf
                wfuzz
                gobuster
            ]
        end
    end
    subgraph "Exploitation"
    direction LR
        host-services[
            Host Services
            -------------
            searchsploit
            MSF
        ]
        webapp[
            WebApp
            ------
            sqlmap
            XSStrike
            XSSer
            wpscan
            CMSeek
            CMSmap
        ]
        password-attack[
            Password Attack
            ---------------
            hashcat
            JohnTheRipper
            Hydra
        ]
    end
    subgraph "Post Exploitation"
    direction LR
        subgraph Host Enumeration
        direction TB
            linux-en[
                Linux
                -----
                LinEnum
                LinuxSmartEnumeration
                Enum4Linux
            ]
            windows-en[
                Windows
                -------
                WindowsEnum
                Mimikatz
            ]
        end
        subgraph Privilege Escalation
        direction TB
            linux-pe[
                Linux
                -----
                LinPEAS
                LinuxExploitSuggester
                LinuxPrivChecker
            ]
            windows-pe[
                Windows
                -------
                WinPEAS
                PrivescChec
                Windows-PrivEsc-Check
                RemotePotato0
            ]
        end
        sniffing[
            Sniffing
            --------
            TCPdump
            Tshark
            Ettercap
        ]
        spoofing[
            Spoofing
            --------
            Bettercap
            Responder
            ARPspoof
        ]
    end
end
```

## Information Gathering

### OSINT
- [TheHarvester](https://github.com/laramies/theHarvester)
- [Recon-ng](https://github.com/lanmaster53/recon-ng)
- [Shodan](https://github.com/malinkinsa/shodancli)
- [Whois](https://github.com/weppos/whois)

### Infrastructure Enumeration

#### Domains
- [Subfinder](https://github.com/projectdiscovery/subfinder)
- [Sudomy](https://github.com/screetsec/Sudomy)
- [ESD](https://github.com/FeeiCN/ESD?tab=readme-ov-file)
- [Sublist3r](https://github.com/aboul3la/Sublist3r)

#### DNS
- [DNSrecon](https://github.com/darkoperator/dnsrecon)
- [massDNS](https://github.com/blechschmidt/massdns)
- [SubBrute](https://github.com/TheRook/subbrute)

#### Cloud Services
- [CloudEnum](https://github.com/initstring/cloud_enum)
- [CloudBrute](https://github.com/0xsha/CloudBrute)

#### Host Services
- [Nmap](https://github.com/nmap/nmap)
- [Masscan](https://github.com/robertdavidgraham/masscan)

### WebApp Enumeration

#### Scanning
- [WhatWeb](https://github.com/urbanadventurer/WhatWeb)
- [Nikto](https://github.com/sullo/nikto)
- [Wafw00f](https://github.com/EnableSecurity/wafw00f)
- [Aquatone](https://github.com/michenriksen/aquatone)

#### Fuzzing
- [Ffuf](https://github.com/ffuf/ffuf)
- [Wfuzz](https://github.com/xmendez/wfuzz)
- [Gobuster](https://github.com/OJ/gobuster)

## Exploitation

### Host Services
- [Searchsploit](https://gitlab.com/exploit-database/exploitdb)
- [MSF](https://github.com/rapid7/metasploit-framework)

### WebApp
- [SQLMap](https://github.com/sqlmapproject/sqlmap)
- [XSStrike](https://github.com/s0md3v/XSStrike)
- [XSSer](https://github.com/epsylon/xsser)
- [WPscan](https://github.com/wpscanteam/wpscan)
- [CMSeeK](https://github.com/Tuhinshubhra/CMSeeK)
- [CMSmap](https://github.com/dionach/CMSmap)

### Password Attack
- [Hashcat](https://github.com/hashcat/hashcat)
- [JohnTheRipper](https://github.com/openwall/john)
- [Hydra](https://github.com/vanhauser-thc/thc-hydra)

## Post Exploitation

### Host Enumeration

#### Linux
- [LinEnum](https://github.com/rebootuser/LinEnum)
- [LinuxSmartEnumeration](https://github.com/diego-treitos/linux-smart-enumeration)
- [Enum4Linux](https://github.com/cddmp/enum4linux-ng)

#### Windows
- [WindowsEnum](https://github.com/absolomb/WindowsEnum)
- [Mimikatz](https://github.com/gentilkiwi/mimikatz/wiki)

### Privilege Escalation

#### Linux
- [LinPEAS](https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS)
- [LinuxExploitSuggester](https://github.com/The-Z-Labs/linux-exploit-suggester)
- [LinuxPrivChecker](https://github.com/sleventyeleven/linuxprivchecker)

#### Windows
- [WinPEAS](https://github.com/peass-ng/PEASS-ng/tree/master/winPEAS)
- [PrivescChec](https://github.com/itm4n/PrivescCheck)
- [Windows-PrivEsc-Check](https://github.com/pentestmonkey/windows-privesc-check)
- [RemotePotato0](https://github.com/antonioCoco/RemotePotato0)

### Sniffing
- [TCPdump](https://github.com/the-tcpdump-group/tcpdump)
- [Tshark](https://github.com/gcla/termshark)
- [Ettercap](https://github.com/Ettercap/ettercap)

### Spoofing
- [Bettercap](https://github.com/bettercap/bettercap)
- [Responder](https://github.com/SpiderLabs/Responder)
- [ARPspoof](https://github.com/alandau/arpspoof)
