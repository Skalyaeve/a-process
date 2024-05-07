```mermaid
flowchart LR
    subgraph post-exploitation[Post Exploitation]
    direction TB
        subgraph host-enumeration[Host Enumeration]
        direction LR
            linux-en[
                Linux
                ----
                <a href='https://github.com/rebootuser/LinEnum'>LinEnum</a>

                <a href='https://github.com/diego-treitos/linux-smart-enumeration'>linux-smart-enum</a>

                <a href='https://github.com/cddmp/enum4linux-ng'>enum4linux-ng</a>
            ]
            windows-en[
                Windows
                ----
                <a href='https://github.com/absolomb/WindowsEnum'>WindowsEnum</a>

                <a href='https://github.com/gentilkiwi/mimikatz'>mimikatz</a>
            ]
        end
        subgraph privilege-escalation[Privilege Escalation]
        direction LR
            linux-pe[
                Linux
                ----
                <a href='https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS'>linPEAS</a>

                <a href='https://github.com/The-Z-Labs/linux-exploit-suggester'>linux-exploit-suggester</a>

                <a href='https://github.com/sleventyeleven/linuxprivchecker'>linuxprivchecker</a>
            ]
            windows-pe[
                Windows
                ----
                <a href='https://github.com/peass-ng/PEASS-ng/tree/master/winPEAS'>winPEAS</a>

                <a href='https://github.com/itm4n/PrivescCheck'>PrivescCheck</a>

                <a href='https://github.com/pentestmonkey/windows-privesc-check'>windows-privesc-check</a>

                <a href='https://github.com/antonioCoco/RemotePotato0'>RemotePotato0</a>
            ]
        end
        sniffing[
            Sniffing
            ----
            <a href='https://github.com/the-tcpdump-group/tcpdump'>tcpdump</a>

            <a href='https://github.com/gcla/termshark'>termshark</a>

            <a href='https://github.com/Ettercap/ettercap'>ettercap</a>
        ]
        spoofing[
            Spoofing
            ----
            <a href='https://github.com/bettercap/bettercap'>bettercap</a>

            <a href='https://github.com/SpiderLabs/Responder'>Responder</a>

            <a href='https://github.com/alandau/arpspoof'>arpspoof</a>
        ]
    end
    subgraph exploitation[Exploitation]
    direction TB
        host-services[
            Host Services
            ----
            <a href='https://gitlab.com/exploit-database/exploitdb'>searchsploit</a>

            <a href='https://github.com/rapid7/metasploit-framework'>metasploit-framework</a>
        ]
        webapp[
            WebApp
            ----
            <a href='https://github.com/sqlmapproject/sqlmap'>sqlmap

            <a href='https://github.com/s0md3v/XSStrike'>XSStrike</a>

            <a href='https://github.com/epsylon/xsser'>xsser</a>

            <a href='https://github.com/wpscanteam/wpscan'>wpscan</a>

            <a href='https://github.com/Tuhinshubhra/CMSeeK'>CMSeeK</a>

            <a href='https://github.com/dionach/CMSmap'>CMSmap</a>
        ]
        password-attack[
            Password Attack
            ----
            <a href='https://github.com/hashcat/hashcat'>hashcat</a>

            <a href='https://github.com/openwall/john'>john</a>

            <a href='https://github.com/vanhauser-thc/thc-hydra'>thc-hydra</a>
        ]
    end
    subgraph information-gathering[Information Gathering]
    direction TB
        osint[
            OSINT
            ----
            <a href='https://github.com/laramies/theHarvester'>theHarvester</a>

            <a href='https://github.com/lanmaster53/recon-ng'>recon-ng</a>

            <a href='https://github.com/malinkinsa/shodancli'>shodancli</a>

            <a href='https://github.com/weppos/whois'>whois</a>
        ]
        subgraph infrastructure-enumeration[Infrastructure Enumeration]
        direction LR
            domains[
                Domains
                ----
                <a href='https://github.com/projectdiscovery/subfinder'>subfinder</a>

                <a href='https://github.com/screetsec/Sudomy'>sudomy</a>

                <a href='https://github.com/aboul3la/Sublist3r'>sublist3r</a>
            ]
            dns[
                DNS
                ----
                <a href='https://github.com/darkoperator/dnsrecon'>dnsrecon</a>

                <a href='https://github.com/blechschmidt/massdns'>massdns</a>

                <a href='https://github.com/TheRook/subbrute'>subbrute</a>
            ]
            cloud[
                Cloud Services
                ----
                <a href='https://github.com/initstring/cloud_enum'>cloud_enum</a>

                <a href='https://github.com/0xsha/CloudBrute'>cloudbrute</a>
            ]
            host[
                Host Services
                ----
                <a href='https://github.com/nmap/nmap'>nmap</a>

                <a href='https://github.com/robertdavidgraham/masscan'>masscan</a>
            ]
        end
        subgraph webapp-enumeration[WebApp Enumeration]
        direction LR
            scanning[
                Scanning
                ----
                <a href='https://github.com/urbanadventurer/WhatWeb'>whatweb</a>

                <a href='https://github.com/sullo/nikto'>nikto</a>

                <a href='https://github.com/EnableSecurity/wafw00f'>wafw00f</a>

                <a href='https://github.com/michenriksen/aquatone'>aquatone</a>
            ]
            fuzzing[
                Fuzzing
                ----
                <a href='https://github.com/ffuf/ffuf'>ffuf</a>

                <a href='https://github.com/xmendez/wfuzz'>wfuzz</a>

                <a href='https://github.com/OJ/gobuster'>gobuster</a>
            ]
        end
    end
style information-gathering fill:#080808,stroke:#ff8080
style infrastructure-enumeration fill:#080808,stroke:#606060
style webapp-enumeration fill:#080808,stroke:#606060
style exploitation fill:#080808,stroke:#8080ff
style post-exploitation fill:#080808,stroke:#80ff80
style host-enumeration fill:#080808,stroke:#606060
style privilege-escalation fill:#080808,stroke:#606060
```
