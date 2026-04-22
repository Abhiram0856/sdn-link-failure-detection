# SDN Link Failure Detection using POX and Mininet

## Name: Abhiram  
## SRN: PES1UG24CS232  

---

## How to Run

### Install Requirements
```bash
sudo apt update
sudo apt install -y mininet git python3
```

### Download POX
```bash
git clone https://github.com/noxrepo/pox.git
cd pox
```

### Start Controller
```bash
./pox.py log.level --DEBUG forwarding.l2_learning
```

### Run Topology (new terminal)
```bash
sudo mn --custom topo.py --topo mytopo --controller remote
```

### Test Network
```bash
pingall
```

### Simulate Link Failure
```bash
link s1 s2 down
```

### Restore Link
```bash
link s1 s2 up
```

### Exit
```bash
exit
sudo mn -c
```

---

## Brief Explanation

This project demonstrates basic Software Defined Networking using POX controller and Mininet.

- The POX controller uses L2 learning to forward packets.
- Mininet creates a simple topology with two switches and hosts.
- Under normal conditions, hosts communicate successfully.
- When the link between switches is turned off, packet loss occurs.
- When the link is restored, communication resumes.

This shows how network behavior depends on link status in SDN.
