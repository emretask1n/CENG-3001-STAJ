import json
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Emre.1935",
  database="mydb")

mycursor = mydb.cursor()
sql = "INSERT INTO Data (ip , port, connection_Try, timeout, success, ping) VALUES (%s, %s, %s, %s, %s, %s)"
sql2 = "INSERT INTO Version (Data_ip , version, services, timestamp, nonce, start_height, relay) VALUES (%s, %s, %s, %s, %s, %s, %s)"
sql3 = "INSERT INTO Reciever (Version_Data_ip , recvServices, recvIp, recvPort) VALUES (%s, %s, %s, %s)"
sql4 = "INSERT INTO User_agent (Version_Data_ip , user_agents_bytes, user_agent) VALUES (%s, %s, %s)"
sql5 = "INSERT INTO trans (Version_Data_ip , transServices, transIp, transPort) VALUES (%s, %s, %s, %s)"

with open('deneme.json') as f:
  data = json.load(f)

all_data_of_ips = data['ips']

ListForTable1=[]
ListForTable2=[]
ListForTable3=[]
ListForTable4=[]
ListForTable5=[]


for datas in all_data_of_ips:
    if datas['ping'] is None:
        val = None
    else:
        val = datas['ping']['nonce']
    first_table=(datas['ip'], datas['port'], datas['connectionTry'], datas['timeout'], datas['success'], val)
    ListForTable1.append(first_table)


for datas in all_data_of_ips:
    if datas['version'] is None:
        version1 = None
        services1 = None
        timestamp1 = None
        nonce1 = None
        start_height1 = None
        relay1 =None
    else:
        version1 = datas['version']['version']
        services1 = datas['version']['services']
        timestamp1 = datas['version']['timestamp']
        nonce1 = datas['version']['nonce']
        start_height1 = datas['version']['start_height']
        relay1 = datas['version']['relay']
    second_table = (datas['ip'], version1, services1, timestamp1, nonce1, start_height1, relay1)
    ListForTable2.append(second_table)




for datas in all_data_of_ips:
    if datas['version'] is None:
        recvSer1 = None
        recvIp1 = None
        recvPort = None
    else:
        recvSer1 = datas['version']['recvServices']
        recvIp1 = datas['version']['recvIp']
        recvPort = datas['version']['recvPort']
    third_table = (datas['ip'], recvSer1, recvIp1, recvPort)
    ListForTable3.append(third_table)


for datas in all_data_of_ips:
    if datas['version'] is None:
        user_ag_bytes = None
        user_ag = None
    else:
        user_ag_bytes = datas['version']['user_agents_bytes']
        user_ag = datas['version']['user_agent']
    fourth_table = (datas['ip'], user_ag_bytes,user_ag)
    ListForTable4.append(fourth_table)


for datas in all_data_of_ips:
    if datas['version'] is None:
        transServ1 = None
        transIp = None
        transPort = None
    else:
        transServ1 = datas['version']['transServices']
        transIp = datas['version']['transIp']
        transPort = datas['version']['transPort']
    fifth_table = (datas['ip'], transServ1, transIp, transPort)
    ListForTable5.append(fifth_table)

mycursor.executemany(sql, ListForTable1)
mycursor.executemany(sql2, ListForTable2)
mycursor.executemany(sql3, ListForTable3)
mycursor.executemany(sql4, ListForTable4)
mycursor.executemany(sql5, ListForTable5)

mydb.commit()

print(mycursor.rowcount, "was inserted.")




