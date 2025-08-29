import ipaddress

# 1、通常用于编写与类相关但不依赖类或实例状态的工具函数 / 逻辑
# 2、相关功能组织在一起，让代码更清晰、更模块化

tb_name = "cars"

# 需要插入的数据
data = {
    "name": "111",
    "rate": 100,
    "oil": "Test",
    "age": None,  # 可能存在的空数据
}

data_temp = []
if isinstance(data, list):
    data_temp
else:
    data_temp = [(k, v) for k, v in data.items() if v is not None]

# 根据需要更新的列，生成tuple数组
data_temp = [(k, v) for k, v in data.items() if v is not None]
print("data_temp:", data_temp)

# 需要更新的列名
columns = '(' + ','.join([cols[0] for cols in data_temp]) + ')'
print("columns:", columns)

# repr() 类似 str() 的功能
values = '(' + ','.join(repr(vals[1]) for vals in data_temp) + ')'
print("values:", values)

sql = 'insert into %s' % tb_name + columns + ' values ' + values + ',' + values + ';'
print(sql)


class SqlUtils:
    """组装Insert、Select、Update、Delete SQL字符串语句"""

    @staticmethod
    def GetKeys(target):
        keys = set()
        if isinstance(target, dict) or isinstance(target, tuple):
            [keys.add(key) for key in target]

        if isinstance(target, list):
            [[keys.add(key) for key in item] for item in target]

        return list(keys)

    @staticmethod
    def InsertSqlStr(tb_name, insert_vals, duplicate_key_update_columns=None):
        tb_fields = None
        tb_values = None

        if isinstance(insert_vals, dict):
            tb_insert_fields = []
            tb_insert_values = []
            for key in insert_vals:
                tb_insert_fields.append(key)
                tb_insert_values.append(repr(insert_vals[key]))
            tb_fields = '(' + ','.join(tb_insert_fields) + ')'
            tb_values = '(' + ','.join(tb_insert_values) + ')'

        if isinstance(insert_vals, list):
            tb_insert_fields = []
            tb_insert_values = []
            for field in insert_vals[0]:
                tb_insert_fields.append(field)

            for val in insert_vals:
                tb_insert_values.append('(' + ','.join(repr(val[field]) for field in tb_insert_fields) + ')')

            tb_fields = '(' + ','.join(tb_insert_fields) + ')'
            tb_values = ','.join(tb_insert_values)

        if tb_fields is None or tb_values is None:
            return None

        tb_insert_sql = 'insert into %s' % tb_name + tb_fields + ' values ' + tb_values

        if isinstance(duplicate_key_update_columns, list) and len(duplicate_key_update_columns) > 0:
            tb_duplicate_key_update_columns = ' on duplicate key update ' + ','.join(
                f'{column}=values({column})' for column in duplicate_key_update_columns)
            return tb_insert_sql + tb_duplicate_key_update_columns

        return tb_insert_sql

    @staticmethod
    def SelectSqlStr(tb_name, select_columns="*", where_vals=None):
        tb_columns = '*'

        # 元祖
        if isinstance(select_columns, tuple):
            tb_columns = repr(select_columns)

        # 数组
        if isinstance(select_columns, list):
            tb_columns = ','.join(select_columns)

        fields = SqlUtils.GetKeys(where_vals)

        # 查询条件：字典
        tb_where = None
        if isinstance(where_vals, dict):
            tb_where_values = [f"{field}='{where_vals[field]}'" for field in fields]
            tb_where = ' and '.join(tb_where_values)

        # 查询条件：列表
        if isinstance(where_vals, list):
            tb_where_values = []
            for val in where_vals:
                tb_where_values.append('(' + ','.join(repr(val[field]) for field in fields) + ')')

            tb_where = '(' + ','.join(fields) + ')' + ' in (' + ','.join(tb_where_values) + ')'

        tb_select_sql = 'select ' + tb_columns + ' from %s' % tb_name
        if tb_where is not None:
            return tb_select_sql + ' where ' + tb_where
        return tb_select_sql

    @staticmethod
    def UpdateSqlStr(tb_name, update_vals=None, where_fields=None):
        if update_vals is None:
            return None

        if where_fields is None:
            return None

        fields = SqlUtils.GetKeys(update_vals)
        tb_where_values = []
        tb_update_set_values = []
        if isinstance(update_vals, dict):
            for field in fields:
                if field in where_fields:
                    tb_where_values.append(f"{field} = {repr(update_vals[field])}")
                else:
                    tb_update_set_values.append(f"{field} = {repr(update_vals[field])}")

        tb_update_sql = 'update ' + tb_name + ' set ' + ' , '.join(tb_update_set_values) + ' where ' + ' and '.join(
            tb_where_values)
        return tb_update_sql

    @staticmethod
    def DeleteSqlStr(tb_name, delete_vals=None, match_mode=None):
        if delete_vals is None:
            return None

        tb_where_fields = SqlUtils.GetKeys(delete_vals)
        tb_delete_sql = "delete from %s" % tb_name
        if isinstance(delete_vals, dict):
            if match_mode is None:
                match_mode = "="
            tb_where_values = " and ".join([f"{key}{match_mode}{repr(delete_vals[key])}" for key in tb_where_fields])
            tb_delete_sql += " where " + tb_where_values

        if isinstance(delete_vals, list):
            if match_mode is None:
                match_mode = "in"
            tb_where_values = ','.join(
                ['(' + ','.join([repr(delete_val[field]) for field in tb_where_fields]) + ')' for delete_val in
                 delete_vals])
            tb_delete_sql += " where " '(' + ','.join(tb_where_fields) + ') ' + match_mode + ' (' + tb_where_values + ')'

        return tb_delete_sql


tb_name = 'duty_daily_user'
insert_values = [
    {
        'name': '111',
        'qwname': 'zhangsan',
        'id': 0,
    },
    {
        'name': '222',
        'qwname': 'zhangsan1',
        'id': 1,
    },
    {
        'name': '333',
        'qwname': 'zhangsan2',
        'id': 2,
    },
    {
        'name': '444',
        'qwname': 'zhangsan3',
        'id': 3,
    }
]

select_values = {
    'name': '122',
    'qwname': 'zhangsan',
}

# update_values = {
#     'name': '111',
#     'qwname': '222',
# }
update_values = insert_values
update_values = {
    "appid": 11111,
    "ip":"1.1.1.1",
    "date": "202507",
    "used": "used-1",
    "update_time": "2025-07-03 12:00:00",
}

print("InsertSqlStr:", SqlUtils.InsertSqlStr(tb_name, insert_values, ["name"]))
print("SelectSqlStr:", SqlUtils.SelectSqlStr(tb_name, '*', insert_values))

if isinstance(update_values, dict):
    print("UpdateSqlStr:", SqlUtils.UpdateSqlStr(tb_name, update_values, ['qwname', 'id']))

if isinstance(update_values, list):
    for update_value in update_values:
        print("UpdateSqlStr:", SqlUtils.UpdateSqlStr(tb_name, update_value, ['qwname', 'id']))

print("DeleteSqlStr:", SqlUtils.DeleteSqlStr(tb_name, update_values, "not in"))


class IPUtils:
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
    def isIpInNetwork(ip_str=None, network_str=None):
        if ip_str is None or network_str is None:
            return False

        try:
            ip_instance = ipaddress.ip_address(ip_str)
            network = ipaddress.ip_network(network_str, strict=False)
            return ip_instance in network
        except ValueError:
            return False

    @staticmethod
    def ipNetworkExpand(network_cidr, include_network_broadcast=False):
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
            print(f"错误: {e}")
            return []

def isIPv4(ip_str=None):
    if ip_str is None:
        return False
    try:
        ip = ipaddress.ip_address(ip_str)
        return ip.version == 4
    except ValueError:
        return False


print("isIPv4 192.168.1.1:", isIPv4("192.168.1.1"))  # True
print("isIPv4:", isIPv4("192.168.1.0/24")) # False
print("isIPv4:", isIPv4("2001:db8::1")) # False
print("isIPv4:", isIPv4("2001:db8::/32")) # False
print("isIPv4:", isIPv4("11111")) # False
print("isIPv4:", isIPv4()) # False


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

print("isIPv4Segment:", isIPv4Segment("192.168.1.1"))  # False
print("isIPv4Segment:", isIPv4Segment("192.168.1.0/24")) # True
print("isIPv4Segment:", isIPv4Segment("2001:db8::1")) # False
print("isIPv4Segment:", isIPv4Segment("2001:db8::/32")) # False
print("isIPv4Segment:", isIPv4Segment("11111")) # False
print("isIPv4Segment:", isIPv4Segment()) # False


def isIPv6(ip_str=None):
    try:
        ip = ipaddress.ip_address(ip_str)
        return ip.version == 6
    except ValueError:
        return False

print("isIPv6:", isIPv6("192.168.1.1"))  # False
print("isIPv6:", isIPv6("192.168.1.0/24")) # False
print("isIPv6:", isIPv6("2001:db8::1")) # True
print("isIPv6:", isIPv6("2001:db8::/32")) # False
print("isIPv6:", isIPv6("11111")) # False
print("isIPv6:", isIPv6()) # False

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

print("isIPv6Segment:", isIPv6Segment("192.168.1.1"))  # False
print("isIPv6Segment:", isIPv6Segment("192.168.1.0/24")) # False
print("isIPv6Segment:", isIPv6Segment("2001:db8::1")) # False
print("isIPv6Segment:", isIPv6Segment("2001:db8::/32")) # True
print("isIPv6Segment:", isIPv6Segment("11111")) # False
print("isIPv6Segment:", isIPv6Segment()) # False

def check_ip_address(ip_str):
    """检测 IP 地址类型 (IPv4/IPv6) 并验证有效性

    Args:
        ip_str (str): 要检测的 IP 地址字符串

    Returns:
        str: 返回 "IPv4", "IPv6" 或 "Invalid"
    """
    try:
        ip = ipaddress.ip_address(ip_str)
        if ip.version == 4:
            return "IPv4"
        elif ip.version == 6:
            return "IPv6"
    except ValueError:
        return "Invalid"


print(check_ip_address("192.168.1.1"))  # 输出: IPv4
print(check_ip_address("192.168.1.0/24"))  # 输出: IPv4
print(check_ip_address("2001:db8::1"))  # 输出: IPv6
print(check_ip_address("2001:db8::/32"))  # 输出: IPv4
print(check_ip_address("invalid.ip"))  # 输出: Invalid


def check_ip_network(net_str):
    """检测 IP 网段类型 (IPv4/IPv6) 并验证有效性

    Args:
        net_str (str): 要检测的 IP 网段 (CIDR表示法)

    Returns:
        str: 返回 "IPv4 Network", "IPv6 Network" 或 "Invalid Network"
    """
    try:
        net = ipaddress.ip_network(net_str, strict=False)
        if net.version == 4:
            return "IPv4 Network"
        elif net.version == 6:
            return "IPv6 Network"
    except ValueError:
        return "Invalid Network"


# 使用示例
print('check_ip_network:', check_ip_network("192.168.1.1"))  # 输出: IPv4
print('check_ip_network:', check_ip_network("2001:db8::1"))  # 输出: IPv6
print('check_ip_network:', check_ip_network("192.168.1.0/24"))  # 输出: IPv4 Network
print('check_ip_network:', check_ip_network("2001:db8::/32"))  # 输出: IPv6 Network
print('check_ip_network:', check_ip_network("invalid.network/24"))  # 输出: Invalid Network


def isIpInNetwork(ip_str=None, network_str=None):
    if ip_str is None or network_str is None:
        return False

    try:
        ip = ipaddress.ip_address(ip_str)
        network = ipaddress.ip_network(network_str, strict=False)
        return ip in network
    except ValueError:
        return False

# 使用示例
print('isIpInNetwork:', isIpInNetwork("192.168.1.100", "192.168.1.0/24"))  # True
print('isIpInNetwork:', isIpInNetwork("10.0.0.1", "192.168.1.0/24"))  # False


def expandIPv4Segment(network_cidr):
    """将 CIDR 格式的 IP 网段解析为所有 IP 地址

    Args:
        network_cidr (str): CIDR 格式的 IP 网段 (如 '192.168.1.0/24')

    Returns:
        list: 包含所有 IP 地址的列表
    """
    try:
        network = ipaddress.ip_network(network_cidr, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError as e:
        print(f"无效的 IP 网段: {e}")
        return []


# 使用示例
print('expandIPv4Segment:', expandIPv4Segment('192.168.1.0/28'))  # []


def ipRangeGenerator(network_cidr, include_network_broadcast=False):
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
        print(f"错误: {e}")
        return []

# 使用示例
print("IPv4 示例:", ipRangeGenerator('192.168.1.0/28'))
print("IPv6 示例:", ipRangeGenerator('2001:db8::/126'))

class IP:
    def __init__(self, ip_str):
        self._ip_str = ip_str

    @property
    def IPVersion(self):
        try:
            ip = ipaddress.ip_address(self._ip_str)
            return ip.version
        except ValueError:
            return 0

    @property
    def IPNetwork(self):
        if '/' in self._ip_str:
            try:
                net = ipaddress.ip_network(self._ip_str, strict=False)
                return net.version
            except ValueError:
                return 0

        return 0

    @property
    def isIP(self):
        return self.IPVersion == 4 or self.IPVersion == 6

    @property
    def isIPNetwork(self):
        return self.IPNetwork == 4 or self.IPNetwork == 6

    @property
    def isIPv4(self):
        return self.IPVersion == 4

    @property
    def isIPv6(self):
        return self.IPVersion == 6

    @property
    def isIPv4Network(self):
        return self.IPNetwork == 4

    @property
    def isIPv6Network(self):
        return self.IPNetwork == 6

    @staticmethod
    def isIpInNetwork(ip_str=None, network_str=None):
        """检测IP是否处在目标网段中

            Args:
                ip_str (str): IP地址
                network_str（str）: CIDR 格式的 IP 网段

            Returns:
                bool: 检测结果
        """
        if ip_str is None or network_str is None:
            return False

        try:
            ip = ipaddress.ip_address(ip_str)
            network = ipaddress.ip_network(network_str, strict=False)
            return ip in network
        except ValueError:
            return False

    @staticmethod
    def ipNetworkExpand(network_cidr, include_network_broadcast=False):
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
            print(f"错误: {e}")
            return []


# ip_str = "2001:db8::/32"
# network_str = "192.168.1.0/24"
# ip = IP(ip_str)

ip_str = "192.168.1.1"
network_str = "192.168.1.0/24"
ip = IP(ip_str)


# print("isIPv6Segment:", isIPv6Segment("192.168.1.1"))  # False
# print("isIPv6Segment:", isIPv6Segment("192.168.1.0/24")) # False
# print("isIPv6Segment:", isIPv6Segment("2001:db8::1")) # False
# print("isIPv6Segment:", isIPv6Segment("2001:db8::/32")) # True
# print("isIPv6Segment:", isIPv6Segment("11111")) # False
# print("isIPv6Segment:", isIPv6Segment()) # False

# print('check_ip_network:', check_ip_network("192.168.1.1"))  # 输出: IPv4
# print('check_ip_network:', check_ip_network("2001:db8::1"))  # 输出: IPv6
# print('check_ip_network:', check_ip_network("192.168.1.0/24"))  # 输出: IPv4 Network
# print('check_ip_network:', check_ip_network("2001:db8::/32"))  # 输出: IPv6 Network
# print('check_ip_network:', check_ip_network("invalid.network/24"))  # 输出: Invalid Network

# print('isIpInNetwork:', isIpInNetwork("192.168.1.100", "192.168.1.0/24"))  # True
# print('isIpInNetwork:', isIpInNetwork("10.0.0.1", "192.168.1.0/24"))  # False


print("IP - isIP:", ip.isIP)  # False
print("IP - isIPv4:", ip.isIPv4)  # False
print("IP - isIPv6:", ip.isIPv6)  # False
print("IP - isIPNetwork:", ip.isIPNetwork)  # False
print("IP - isIPv4Network:", ip.isIPv4Network)  # False
print("IP - isIPv6Network:", ip.isIPv6Network)  # False
print("IP - isIpInNetwork:", ip.isIpInNetwork(ip_str, network_str))  # True
print("IP - isIpInNetwork:", ip.ipNetworkExpand(network_str))  # True