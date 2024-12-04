---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-12-04
---

<span style="color: gray;">Dated: 04-12-2024</span>

# Ch03. Security Hardening of Asterisk Voip - part 1

- http://www.ipcomms.net/asteriskblog/11-steps-to-secure-your-asterisk-pbx  
![[Pasted image 20241204095034.png]]
- Physically secure your IP PBX and network hardware
    - The first step to security of your system
- Never, Never, Never use the default passwords on any system. (Use Strong Passwords)
    - This will stop most of the attacks as hackers use weak passwords to break in
- Never use the same Username and password on your extensions
    - "This is another VERY common issue, especially within the Asterisk community. Using password 101 for extension 101 is asking for big trouble. DON'T DO IT!"
- Place your PBX behind a firewall
	- Use VPNs for remote access and limit to specific IP addresses
	- Allow access on ports which are absolutely necessary
	- Disable anonymous WAN requests (ICMP or PING) access to your IP PBX
- Use the "permit=" and "deny=" lines in sip.conf
    - Use the "permit=" and "deny=" lines in sip.conf to only allow a small range of IP addresses access to extension/user in your sip.conf file. This is true even if you decide to allow inbound calls from “anywhere” (default), it won't let those users reach any authenticated elements."
- Keep inbound and outbound routing separate (asterisk)
    - This is probably the biggest cause and source of toll fraud. By keeping your inbound call routing in a different context than your outbound routing, if an intruder does happen to make it into your system, he can’t get back out again.