import serial
import time

def ByteToHex( bins ):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """

    return ''.join( [ "%02X" % x for x in bins ] ).strip()

ser = serial.Serial('com19', 115200) #建立串口对象并打开


#s = ser.read(33)
#print(s)

#todo

g = 9.8
data_list = []
G_speed_list =[]
A_speed_list =[]
Angle_list = []

while True:
    #ser = serial.Serial('com19', 115200) #建立串口对象并打开
    data_list = []                        #清空三个list，因为后面使用append所以这里要清空
    G_speed_list = []
    A_speed_list = []
    Angle_list = []
    for j in range(0,3):
        for i in range(0,11):
            s = ser.read(1) #多次调用注意清空串口

            #print(s)
            data_list.append(int.from_bytes((s),byteorder='big'))
            #data_list.append(int(s, 16))
            #print('>>>>', int.from_bytes((s),byteorder='big'))
            #print('>>>>',int(s, 16))
    #ser.flushOutput()
    #ser.flushInput()
    #ser.close()                          #关闭串口对象

    #print('读入33个字节(已转换为10进制整型)\r\n',data_list)
    #print('data_list长度:',len(data_list))

    if (data_list[0] == 85):

        if (data_list[0] == 85) & (data_list[1] == 81):
            for i in range(0,11):
                G_speed_list.append(data_list[i])

        if (data_list[11] == 85) & (data_list[12] == 82):
            for i in range(11,22):
                A_speed_list.append(data_list[i])

        if (data_list[22] == 85) & (data_list[23] == 83):
            for i in range(22,33):
                Angle_list.append(data_list[i])

        #print('加速度数据包',G_speed_list)
        #print('角速度数据包',A_speed_list)
        #print('角度数据包',Angle_list)

        #ax = (((G_speed_list[3]<<8 | G_speed_list[2])/32768) * 16 * 9.8)
        #ax
        if ((G_speed_list[3] << 8) | G_speed_list[2]) >= 32768: #意味加速度为负值 正值最大到32768超过这个就是输出负值
            ax = ((((G_speed_list[3] << 8) | G_speed_list[2]) - 32768*2) / 32768 * 16)
        else:
            ax = ((((G_speed_list[3] << 8) | G_speed_list[2])) / 32768 * 16)

        #ay
        if ((G_speed_list[5] << 8) | G_speed_list[4]) >= 32768: #意味加速度为负值 正值最大到32768超过这个就是输出负值
            ay = ((((G_speed_list[5] << 8) | G_speed_list[4]) - 32768 * 2) / 32768 * 16)
        else:
            ay = ((((G_speed_list[5] << 8) | G_speed_list[4])) / 32768 * 16)

        #az
        if ((G_speed_list[7] << 8) | G_speed_list[6]) >= 32768: #意味加速度为负值 正值最大到32768超过这个就是输出负值
            az = ((((G_speed_list[7] << 8) | G_speed_list[6]) - 32768*2) / 32768 * 16)
        else:
            az = ((((G_speed_list[7] << 8) | G_speed_list[6])) / 32768 * 16)


        #A_speedx
        if ((A_speed_list[3] << 8) | A_speed_list[2]) >= 32768: #意味角速度为负值 正值最大到32768超过这个就是输出负值
            A_speedx = ((((A_speed_list[3] << 8) | A_speed_list[2]) - 32768*2) / 32768 * 2000)
        else:
            A_speedx = ((((A_speed_list[3] << 8) | A_speed_list[2])) / 32768 * 2000)

        #A_speedy
        if ((A_speed_list[5] << 8) | A_speed_list[4]) >= 32768: #意味角速度为负值 正值最大到32768超过这个就是输出负值
            A_speedy = ((((A_speed_list[5] << 8) | A_speed_list[4]) - 32768 * 2) / 32768 * 2000)
        else:
            A_speedy = ((((A_speed_list[5] << 8) | A_speed_list[4])) / 32768 * 2000)

        #A_speedz
        if ((A_speed_list[7] << 8) | A_speed_list[6]) >= 32768: #意味角速度为负值 正值最大到32768超过这个就是输出负值
            A_speedz = ((((A_speed_list[7] << 8) | A_speed_list[6]) - 32768*2) / 32768 * 2000)
        else:
            A_speedz = ((((A_speed_list[7] << 8) | A_speed_list[6])) / 32768 * 2000)


        #Angle_Roll--翻滚
        if ((Angle_list[3] << 8) | Angle_list[2]) >= 32768: #意味角度为负值 正值最大到32768超过这个就是输出负值
            Angle_Roll = ((((Angle_list[3] << 8) | Angle_list[2]) - 32768*2) / 32768 * 180)
        else:
            Angle_Roll = ((((Angle_list[3] << 8) | Angle_list[2])) / 32768 * 180)

        #Angle_Pitch--俯仰
        if ((Angle_list[5] << 8) | Angle_list[4]) >= 32768: #意味角度为负值 正值最大到32768超过这个就是输出负值
            Angle_Pitch = ((((Angle_list[5] << 8) | Angle_list[4]) - 32768 * 2) / 32768 * 180)
        else:
            Angle_Pitch = ((((Angle_list[5] << 8) | Angle_list[4])) / 32768 * 180)

        #Angle_Yaw--偏航
        if ((Angle_list[7] << 8) | Angle_list[6]) >= 32768: #意味加角为负值 正值最大到32768超过这个就是输出负值
            Angle_Yaw = ((((Angle_list[7] << 8) | Angle_list[6]) - 32768*2) / 32768 * 180)
        else:
            Angle_Yaw = ((((Angle_list[7] << 8) | Angle_list[6])) / 32768 * 180)


        # print('ax:', ax, 'g')
        # print('ay:', ay, 'g')
        # print('az:', az, 'g')
        # print('\n')
        # print('A_speedx:', A_speedx, '度/s')
        # print('A_speedy:', A_speedy, '度/s')
        # print('A_speedz:', A_speedz, '度/s')
        # print('\n')
        print('Angle_Roll:', Angle_Roll, '度')
        print('Angle_Pitch:', Angle_Pitch, '度')
        print('Angle_Yaw:', Angle_Yaw, '度')
        #time.sleep(1)





