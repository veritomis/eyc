

while True:
    import time
    time.sleep(5) # espera en segundos
    fechas=time.strftime('%d/%m/%y')
    print(fechas)
    horas=time.strftime('%H:%M:%S') #Formato de 24 horas
    print (horas)
    
    from pyModbusTCP.client import ModbusClient
# TCP auto connect on first modbus request
    c = ModbusClient(host='192.168.0.43', port=502, unit_id=10, auto_open=True)
#Read 2x 16 bits registers at modbus address 0 :
    regs = c.read_holding_registers(3207)
    if regs:
      print(regs[0]/10)
    else:
      print('read error')
    
    try:
        import cx_Oracle
        import config 
        conexion=None
        conexion = cx_Oracle.connect(
        user='system', 
        password='maria123456', 
        dsn='DESKTOP-OBGDB5N/xepdb1')     
    except Exception as err:
        print('error en la conexion', err)
    else:
        print('conectado a oracle', conexion.version)

    try:
        regs1=regs[0]/10
        cur_01 = conexion.cursor()
        insert_datos="insert into voltage1 (voltage_in) values (:valor)"
        cur_01.execute(insert_datos, valor=regs1)
    except Exception as err:
        print('error insertando datos', err)
        
    else:
        print('datos insertados correctamente')
        print(regs1)
        conexion.commit()
        conexion.close()
