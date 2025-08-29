import ipaddress

class IPUtils:
    @staticmethod
    def isIP(ip_str=None):
        return IPUtils.isIPv4(ip_str) or IPUtils.isIPv6(ip_str)

    @staticmethod
    def isSegment(net_str=None):
        return IPUtils.isIPv4Segment(net_str) or IPUtils.isIPv6Segment(net_str)

    @staticmethod
    def isIPv4(ip_str=None):
        if ip_str is None:
            return False
        try:
            ip_instance = ipaddress.ip_address(ip_str)
            return ip_instance.version == 4
        except ValueError:
            return False

    @staticmethod
    def isIPv4Segment(net_str=None):
        if net_str is None:
            return False

        if '/' in net_str:
            # 检测网段
            try:
                net = ipaddress.ip_network(net_str, strict=False)
                return net.version == 4
            except ValueError:
                return False
        return False

    @staticmethod
    def isIPv6(ip_str=None):
        if ip_str is None:
            return False
        try:
            ip_instance = ipaddress.ip_address(ip_str)
            return ip_instance.version == 6
        except ValueError:
            return False

    @staticmethod
    def isIPv6Segment(net_str=None):
        if net_str is None:
            return False

        if '/' in net_str:
            # 检测网段
            try:
                net = ipaddress.ip_network(net_str, strict=False)
                return net.version == 6
            except ValueError:
                return False
        return False

    @staticmethod
    def isIpInSegment(ip_str=None, net_str=None):
        if ip_str is None or net_str is None:
            return False

        try:
            ip_instance = ipaddress.ip_address(ip_str)
            network = ipaddress.ip_network(net_str, strict=False)
            return ip_instance in network
        except ValueError:
            return False

    @staticmethod
    def ipSegmentExpand(network_cidr, include_network_broadcast=False):
        """解析 IP 网段为所有可用 IP 地址

           Args:
               network_cidr (str): CIDR 格式的 IP 网段
               include_network_broadcast (bool): 是否包含网络地址和广播地址

           Returns:
               list: IP 地址列表
           """
        try:
            network = ipaddress.ip_network(network_cidr, strict=False)

            if include_network_broadcast:
                return [str(ip) for ip in network]
            else:
                if network.version == 4 and network.prefixlen < 31:
                    # 对于 IPv4，排除网络地址和广播地址
                    return [str(ip) for ip in network.hosts()]
                else:
                    # 对于 IPv6 或 /31, /32 IPv4 网络，所有地址都是有效主机地址
                    return [str(ip) for ip in network]
        except ValueError as e:
            print(f"IPUtils ipSegmentExpand Error: {e}")
            return []


# print("isIPv4", IPUtils.isIPv4("192.168.1.1"))  # True
# print("isIPv4:", IPUtils.isIPv4("192.168.1.0/24")) # False
# print("isIPv4:", IPUtils.isIPv4("2001:db8::1")) # False
# print("isIPv4:", IPUtils.isIPv4("2001:db8::/32")) # False
# print("isIPv4:", IPUtils.isIPv4("11111")) # False
# print("isIPv4:", IPUtils.isIPv4()) # False
#
# print("isIPv4Segment:", IPUtils.isIPv4Segment("192.168.1.1"))  # False
# print("isIPv4Segment:", IPUtils.isIPv4Segment("192.168.1.0/24")) # True
# print("isIPv4Segment:", IPUtils.isIPv4Segment("2001:db8::1")) # False
# print("isIPv4Segment:", IPUtils.isIPv4Segment("2001:db8::/32")) # False
# print("isIPv4Segment:", IPUtils.isIPv4Segment("11111")) # False
# print("isIPv4Segment:", IPUtils.isIPv4Segment()) # False
#
# print('isIpInNetwork:', IPUtils.isIpInSegment("192.168.1.100", "192.168.1.0/24"))  # True
# print('isIpInNetwork:', IPUtils.isIpInSegment("10.0.0.1", "192.168.1.0/24"))  # False


# print("isIPv6:", IPUtils.isIPv6("192.168.1.1"))  # False
# print("isIPv6:", IPUtils.isIPv6("192.168.1.0/24")) # False
# print("isIPv6:", IPUtils.isIPv6("2001:db8::1")) # True
# print("isIPv6:", IPUtils.isIPv6("2001:db8::/32")) # False
# print("isIPv6:", IPUtils.isIPv6("11111")) # False
# print("isIPv6:", IPUtils.isIPv6()) # False
#
# print("isIPv6Segment:", IPUtils.isIPv6Segment("192.168.1.1"))  # False
# print("isIPv6Segment:", IPUtils.isIPv6Segment("192.168.1.0/24")) # False
# print("isIPv6Segment:", IPUtils.isIPv6Segment("2001:db8::1")) # False
# print("isIPv6Segment:", IPUtils.isIPv6Segment("2001:db8::/32")) # True
# print("isIPv6Segment:", IPUtils.isIPv6Segment("11111")) # False
# print("isIPv6Segment:", IPUtils.isIPv6Segment()) # False


# 使用示例
print('expandIPv4Segment:', IPUtils.ipSegmentExpand('192.168.1.0/28'))  # []
print('expandIPv4Segment:', IPUtils.ipSegmentExpand('192.168.1.0'))  # []