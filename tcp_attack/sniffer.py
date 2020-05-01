from scapy.all import sniff


class Sniffer:
    def __init__(self):
        self.sniffing = sniff(
            filter='tcp',
            prn=lambda x: x.sprintf(
                '{IP:%IP.src% -> %IP.dst%\n}{Raw: %Raw.load%\n}'))

    def show_result(self):
        self.sniffing.show()
        for package in self.sniffing:
            print(package.show())


if __name__ == '__main__':
    sn = Sniffer()
    sn.show_result()
