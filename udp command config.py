# coding: utf-8
import socket
import struct



rawdata = 'CC CC 06 01 00 12 13 14 10 0B 1C 00 05 01 DE 03 AA 01 01 00 00 C0 A8 41 01 FF FF FF 00 C0 A8 41 FE 27 10 27 10 C0 A8 41 7A DD DD'
input_data = rawdata.split()

"""
Command:CC CC 06
product_family:01
product_name:00
Hardware Version:12
Embedded Version:13
Date of manufacture:14 10 0B 26
Serial Number:00 01
Product_Role:01
Area ID:DE 03
Node ID:AA 01
Backhual Mode:01

Programming indicator:00 00
Ip:C0 A8 41 01
Subnet mask:FF FF FF 00
Gateway:C0 A8 41 FE
Destination Port:27 10
Source Port：27 10
Destination Ip:C0 A8 41 7A

DD DD

"""

def strconvert(s):
    s = str(s).strip().split(' ')  # get rid of white spaces
    s = ''.join(s)  # get rid of white spaces
    fin = ''
    for i in range(len(s)/2):
        fin = fin+struct.pack('B',int(s[2*i:2*i+2],16))
    return fin

#print 'Command:'+str(input_data[0])+str(input_data[1])+str(input_data[2])

if input_data[3]=='01':
    product_family='PPS'
else:
    product_family='OTHERS'
#print product_family

if input_data[4]=='00':
    product_name='BST'
elif input_data[4]=='01':
    product_name='PT'
elif input_data[4]=='02':
    product_name='DT'
elif input_data[4]=='03':
    product_name='VT'
else:
    product_name='OTHERS'
#print product_name

#print 'Hardware Version:'+str(int(input_data[5][0],16))+'.'+str(int(input_data[5][1],16))
#print int('A',16)
#print 'Embedded Version:'+str(int(input_data[6][0],16))+'.'+str(int(input_data[6][1],16))

#print int(input_data[7][0],16)*16+int(input_data[7][1],16)
# print 'Date of manufacture:' + str(int(input_data[10][0], 16) * 16 + int(input_data[10][1], 16)) + \
#     '/' + str(int(input_data[9][0], 16) * 16 + int(input_data[9][1], 16)) + \
#     '/' + str(int(input_data[7][0], 16) * 16+int(input_data[7][1], 16)) +\
#     str(int(input_data[8][0], 16) * 16 + int(input_data[8][1], 16))

if input_data[13]=='00':
    product_Role='Slave'
elif input_data[13]=='01':
    product_Role='Master'
elif input_data[13]=='02':
    product_Role='Tag'
else:
    product_Role='OTHERS'

#print product_Role

#print input_data[14]+input_data[15]

#print input_data[16]+input_data[17]

if input_data[18]=='00':
    product_backhaul='Ethernet'
else:
    product_backhaul='Wifi'
#print product_backhaul

#print input_data[20]
if input_data[20]=='00':
    Programming_indicator='IP remains'
else:
    Programming_indicator='IP changes'
#print Programming_indicator

# print str(int(input_data[21][0], 16) * 16 + int(input_data[21][1], 16)) + '.' + \
#     str(int(input_data[22][0], 16) * 16 + int(input_data[22][1], 16)) + '.' + \
#     str(int(input_data[23][0], 16) * 16 + int(input_data[23][1], 16)) + '.' + \
#     str(int(input_data[24][0], 16) * 16 + int(input_data[24][1], 16))

# print str(int(input_data[25][0], 16) * 16 + int(input_data[25][1], 16)) + '.' + \
#     str(int(input_data[26][0], 16) * 16 + int(input_data[26][1], 16)) + '.' + \
#     str(int(input_data[27][0], 16) * 16 + int(input_data[27][1], 16)) + '.' + \
#     str(int(input_data[28][0], 16) * 16 + int(input_data[28][1], 16))

# print str(int(input_data[29][0], 16) * 16 + int(input_data[29][1], 16)) + '.' + \
#     str(int(input_data[30][0], 16) * 16 + int(input_data[30][1], 16)) + '.' + \
#     str(int(input_data[31][0], 16) * 16 + int(input_data[31][1], 16)) + '.' + \
#     str(int(input_data[32][0], 16) * 16 + int(input_data[32][1], 16))

# print int(input_data[33][0], 16) * 16 * 16 * 16 + int(input_data[33][1], 16) * 16 * 16 + \
#     int(input_data[34][0], 16) * 16 + int(input_data[34][1], 16)


print 'Command:'+str(input_data[0])+str(input_data[1])+str(input_data[2])
print 'deviceSN:'
print 'Product_family:'+product_family
print 'Product_name:'+product_name
print 'Hardware Version:'+str(int(input_data[5][0], 16)) + '.' + str(int(input_data[5][1], 16))
print 'Embedded Version:'+str(int(input_data[6][0], 16)) + '.' + str(int(input_data[6][1], 16))
print 'Date of manufacture:' + str(int(input_data[10][0], 16) * 16 + int(input_data[10][1], 16)) + \
    '/' + str(int(input_data[9][0], 16) * 16 + int(input_data[9][1], 16)) + \
    '/' + str(int(input_data[7][0], 16) * 16+int(input_data[7][1], 16)) +\
    str(int(input_data[8][0], 16) * 16 + int(input_data[8][1], 16))
print 'Serial Number:' + input_data[11]+input_data[12]
print ''
print 'Product_Role:' + product_Role
print 'Area ID:'+input_data[14]+input_data[15]
print 'Node ID:'+input_data[16]+input_data[17]
print 'Backhual Mode:'+product_backhaul

print ''
print 'IP Configurations:'
print 'Programming indicator:'+Programming_indicator
print 'Ip\t:' + \
    str(int(input_data[21][0], 16) * 16 + int(input_data[21][1], 16)) + '.' + \
    str(int(input_data[22][0], 16) * 16 + int(input_data[22][1], 16)) + '.' + \
    str(int(input_data[23][0], 16) * 16 + int(input_data[23][1], 16)) + '.' + \
    str(int(input_data[24][0], 16) * 16 + int(input_data[24][1], 16))
print 'Subnet Mask:' + \
    str(int(input_data[25][0], 16) * 16 + int(input_data[25][1], 16)) + '.' + \
    str(int(input_data[26][0], 16) * 16 + int(input_data[26][1], 16)) + '.' + \
    str(int(input_data[27][0], 16) * 16 + int(input_data[27][1], 16)) + '.' + \
    str(int(input_data[28][0], 16) * 16 + int(input_data[28][1], 16))
print 'Gateway\t:' + \
    str(int(input_data[29][0], 16) * 16 + int(input_data[29][1], 16)) + '.' + \
    str(int(input_data[30][0], 16) * 16 + int(input_data[30][1], 16)) + '.' + \
    str(int(input_data[31][0], 16) * 16 + int(input_data[31][1], 16)) + '.' + \
    str(int(input_data[32][0], 16) * 16 + int(input_data[32][1], 16))

print 'Destination Port:' + \
    str(int(input_data[33][0], 16) * 16 * 16 * 16 + int(input_data[33][1], 16) * 16 * 16 +
    int(input_data[34][0], 16) * 16 + int(input_data[34][1], 16))

print 'Source Port\t:' + \
    str(int(input_data[35][0], 16) * 16 * 16 * 16 + int(input_data[35][1], 16) * 16 * 16 +
    int(input_data[36][0], 16) * 16 + int(input_data[36][1], 16))

print 'Destination Ip:' + \
    str(int(input_data[37][0], 16) * 16 + int(input_data[37][1], 16)) + '.' + \
    str(int(input_data[38][0], 16) * 16 + int(input_data[38][1], 16)) + '.' + \
    str(int(input_data[39][0], 16) * 16 + int(input_data[39][1], 16)) + '.' + \
    str(int(input_data[40][0], 16) * 16 + int(input_data[40][1], 16))

port = 10000
host = "192.168.3.26"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(("", 10000))
# AF_INET（又称 PF_INET）是 IPv4 网络协议的套接字类型
# SOCK_DGRAM is used for udp protocol
#s.sendto(struct.pack('B', hex(1)), (host, port))
s.sendto(struct.pack('B', 39), (host, port))
print struct.pack('B', 39)
#s.sendto(struct.pack('B', int('27',16)), (host, port))
a = '2710'
#s.sendto(struct.pack('B', int(a[0:2],16)), (host, port))
s.close()

# print 'waiting on port:', port
# while True:
#     data, addr = s.recvfrom(1024)
#     # 接收一个数据报(最大到1024字节)
#     print 'reciveed:', repr(data), "from", addr[0]
#     break

