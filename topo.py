from mininet.topo import Topo

class MyTopo(Topo):
    def build(self):
        # Hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Links
        self.addLink(h1, s1)
        self.addLink(s1, s2)   # MAIN LINK
        self.addLink(s2, h2)

topos = {'mytopo': (lambda: MyTopo())}
