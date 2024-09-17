---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Cells Vs Packets
ATM designers choose `cells` over `packets` because:
1. Cells are fixed sized and do not cause memory fragmentation and are simpler to manage.
2. Since `packets` are of variable lengths, they need additional data to indicate the start and the end. With `cells`, we can just count them as they arrive.
3. Since the `packet` sizes are variable, there have to be complex interrupt schemes because they take variable times to complete the transmission.

## ATM Speed
ATMs are designed to operate with optical fibers but can also work with `twisted wired pair`.  
The throughput speed is `OC-3` (`155Mbps`).

# ATM Critique
- ATM is far more expansive than the typical LAN hardware.  
- Connection setup time may be excessive for short communications.  
- Call tax consumes 10% of network capacity.
- QoS requirements might be unknown, leading to applications picking values that are too high or too low.

# Network Ownership
There are 2 categories

## Private Network
This is also called `intranet` and is usually a LAN technology, owned by single or multiple organizations.

### Private Network Architecture
It usually includes one or few closely managed external connections.  
They may restrict access at connections.

### Managing Private Network
An organization buys hardware and hires staff to design, implement and manage the networks.

### Extending Private Network
The large organizations may have separate campuses.  
They can install cables on their own property.  
They can also contact leased lines for common carrier.

## Public Network
This is owned by common carrier such as a phone company.  
These are networks which are managed by common carriers by using leased lines.

| **Networks** | **Advantages**                                                      | **Disadvantages**                                 |
| ------------ | ------------------------------------------------------------------- | ------------------------------------------------- |
| Public       | They are flexible                                                   | There is no decision making equipment or policies |
| Private      | The owner has complete control over technical decision and policies | They are expensive to install and maintain        |
