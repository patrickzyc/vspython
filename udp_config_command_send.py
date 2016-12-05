# coding: utf-8
import socket
import struct
from productSN import *
# import binascii
print SN(a)

class udp_send:
    prefix = 'CCCC'
    command = ''
    suffix = 'DDDD'





ProductSN = productSN()


def SN(hh):
    hh=productSN(hh)
    return hh.family+hh.name+hh.Hversion+hh.Eversion+hh.DOM+hh.SN

SN(ProductSN)


class AnchorInfo:
    wifi = '0001'  # 2bytes
    area_id = 'DE03'  # 2bytes
    boost_role = '0001'  # 2bytes
    node_id = 'AA01'  # 2bytes
    workmode = '0000'  # 2bytes
    blinkperiod = '0000'  # 2bytes


class ipinfo:
    ip = 'C0 A8 41 01'  # 4bytes
    mask = 'FF FF FF 00'  # 4bytes
    gateway = 'C0 A8 41 FE'  # 4bytes
    dport = '27 11'  # 2bytes
    sport = '27 10'  # 2bytes
    dip = 'C0 A8 41 7A'  # 4bytes


def strconvert(s):
    s = str(s).strip().split(' ')  # get rid of white spaces
    s = ''.join(s)  # get rid of white spaces
    fin = ''
    for i in range(len(s)/2):
        fin = fin+struct.pack('B', int(s[2*i:2*i+2], 16))
    return fin


def porthextostr(Ipinfo):
    Ipinfo.dport = str(Ipinfo.dport).strip().split(' ')
    Ipinfo.dport = ''.join(Ipinfo.dport)
    dport = int(Ipinfo.dport[0], 16) * 16 * 16 * 16 + \
        int(Ipinfo.dport[1], 16) * 16 * 16 + \
        int(Ipinfo.dport[2], 16) * 16 + \
        int(Ipinfo.dport[3], 16)
    Ipinfo.sport = str(Ipinfo.sport).strip().split(' ')
    Ipinfo.sport = ''.join(Ipinfo.sport)
    sport = int(Ipinfo.sport[0], 16) * 16 * 16 * 16 + \
        int(Ipinfo.sport[1], 16) * 16 * 16 + \
        int(Ipinfo.sport[2], 16) * 16 + \
        int(Ipinfo.sport[3], 16)

    # Ipinfo.dip = str(Ipinfo.dip).strip().split(' ')

    # Ipinfo.dip = ''.join(Ipinfo.dip)
    # DIP = []
    # for i in Ipinfo.dip:
    #     DIP.append(str(int(i, 16)))
    # DIP = '.'.join(DIP)

    # print DIP
    return dport, sport


def sendcommand(UDP, ProductSN, N_AnchorInfo, Ipinfo, C_AnchorInfo, addr):
    dport, sport = porthextostr(Ipinfo)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", sport))
    # AF_INET（又称 PF_INET）是 IPv4 网络协议的套接字类型
    # SOCK_DGRAM is used for udp protocol
    if UDP.command == '00':
        sendtxt = strconvert(UDP.prefix+UDP.command +
                             C_AnchorInfo.area_id+C_AnchorInfo.node_id +
                             '010203040506'+UDP.suffix)
        s.sendto(sendtxt, (addr, dport))
    elif UDP.command == '01':
        sendtxt = strconvert(UDP.prefix+UDP.command +
                             C_AnchorInfo.area_id+C_AnchorInfo.node_id +
                             N_AnchorInfo.wifi+N_AnchorInfo.area_id +
                             N_AnchorInfo.boost_role+N_AnchorInfo.node_id +
                             N_AnchorInfo.workmode+N_AnchorInfo.blinkperiod +
                             UDP.suffix)
        s.sendto(sendtxt, (addr, dport))
    elif UDP.command == '02':
        sendtxt = strconvert(UDP.prefix+UDP.command +
                             C_AnchorInfo.area_id+C_AnchorInfo.node_id +
                             UDP.suffix)
        s.sendto(sendtxt, (addr, dport))
    elif UDP.command == '03':
        sendtxt = strconvert(UDP.prefix+UDP.command + UDP.suffix)
        s.sendto(sendtxt, (addr, dport))
    elif UDP.command == '04':
        sendtxt = strconvert(UDP.prefix+UDP.command +
                             C_AnchorInfo.area_id + UDP.suffix)
        s.sendto(sendtxt, (addr, dport))
    elif UDP.command == '05':
        sendtxt = strconvert(UDP.prefix+UDP.command +
                             C_AnchorInfo.area_id + UDP.suffix)
        s.sendto(sendtxt, (addr, dport))
    elif UDP.command == '06':
        sendtxt = strconvert(UDP.prefix+UDP.command + UDP.suffix)
        s.sendto(sendtxt, (addr, dport))
    elif UDP.command == '07':
        sendtxt = strconvert(UDP.prefix+UDP.command +
                             C_AnchorInfo.area_id+C_AnchorInfo.node_id +
                             '0001'+Ipinfo.ip+Ipinfo.mask+Ipinfo.gateway +
                             Ipinfo.dport+Ipinfo.sport+Ipinfo.dip +
                             UDP.suffix)
        s.sendto(sendtxt, (addr, dport))
    print 'waiting on port:', sport
    while True:
        data, Addr = s.recvfrom(1024)
        # 接收一个数据报(最大到1024字节)
        data = data.replace('A', '').replace('z', '').replace('\'', '')  # why???
        revdata = ''
        for i in range(len(repr(data))/4):
            revdata = revdata + repr(data)[4*i+3:4*i+5]
        print 'reciveed:', revdata, "from", Addr[0]
        print 'received command:' + revdata[4:6]
        if revdata[4:6] == '00' or revdata[4:6] == '01' or \
           revdata[4:6] == '02' or revdata[4:6] == '05':
            if revdata[14:16] == '00':
                print 'Config result: Failed.'
            else:
                print 'Config result: Successed.'
        elif revdata[4:6] == '03':
            # print revdata[6:30]
            if revdata[6:10] == '0000':
                print 'Backhual: Ethernet'
            else:
                print 'Backhual: Wifi'
            print 'Area id:'+revdata[10:14]
            print 'Boost and Role:'+revdata[14:18]
            print 'Node id:'+revdata[18:22]
            print 'Workmode:'+revdata[22:26]
            print 'Blinkperiod:'+revdata[26:30]
        elif revdata[4:6] == '04':
            print 'Configured Offset:'+revdata[14:26]
        elif revdata[4:6] == '06':
            print revdata[6:80]
        elif revdata[4:6] == '07':
            if revdata[26:28] == '00':
                print 'Config result: Failed.'
            else:
                print 'Config result: Successed.'
        s.close()
        break


UDP = udp_send()
UDP.command = '07'
ProductSN = productSN()
N_AnchorInfo = AnchorInfo()
N_AnchorInfo.area_id = 'DE03'  # Wanted area id configuration
N_AnchorInfo.node_id = 'CC05'  # Wanted node id configuration
N_AnchorInfo.wifi = '0001'  # Wanted Anchor backhaul mode
N_AnchorInfo.boost_role = '0000'
# 0000 for slave without boost, 0100 for slave with boost
# 0001 for master without boost, 0101 for master with boost
# 0002 for tag
N_AnchorInfo.workmode = '0000'
N_AnchorInfo.blinkperiod = '0000'
C_AnchorInfo = AnchorInfo()
C_AnchorInfo.area_id = 'DE01'  # Current area id configuration
C_AnchorInfo.node_id = 'AA01'  # Current node id configuration
Ipinfo = ipinfo()
Ipinfo.sport = '27 10'
Ipinfo.dport = '27 10'
Ipinfo.ip = 'C0 A8 41 CD'
Ipinfo.mask = 'FF FF FF 00'
Ipinfo.gateway = 'C0 A8 41 FE'
Ipinfo.dip = 'C0 A8 41 7A'  # ip address to be sent in Anchor
addr = '192.168.3.26'  # ip address to be sent using UDP
sendcommand(UDP, ProductSN, N_AnchorInfo, Ipinfo, C_AnchorInfo, addr)
