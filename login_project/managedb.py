import mysql.connector

def printErr(err):
    print (f'An error occurred: {err}')    

def dbOpen(): 
    global conn
    global cursor   
    try:
        conn_config = {
            'host': 'localhost',
            'database': 'auth_db',
            'user': 'root',
            'password': 'root'
        }
        conn = mysql.connector.connect(**conn_config)                
    except Exception as err:
        printErr(err)
    else:
        if conn.is_connected():
            cursor = conn.cursor()
            #print(conn.get_server_info())

def dbClose():
    if conn.is_connected():
        cursor.close()
        conn.close()

def dbWrite(sql, val):
    try:
        dbOpen()
        cursor.execute(sql, val)
        conn.commit()
    except Exception as err:
        printErr(err)
    else:
        return True        
    finally:
        dbClose()

def dbRead(sql):
    try:
        dbOpen()
        cursor.execute(sql)
    except Exception as err:
        printErr(err)
    else:                
        return cursor.fetchall()
    finally:        
        dbClose()

def dbCallProcedure(procedure):
    try:
        dbOpen()
        cursor.callproc(procedure)
        #for result in cursor.stored_results():
            #print(result.fetchall())             
    except Exception as err:        
        printErr(err)
    else:                      
        return cursor.stored_results()
    finally:        
        dbClose()
    

def dbAdd(tbl, fld, idval, val):
    sql = 'INSERT into '+ tbl + \
        ' (' + fld + ') '+ \
        'values (' + idval + \
        ');'
    if dbWrite(sql,val):        
        return True

def dbEdit(tbl, fldVal, crit = ' 1 = 1 ', val =()):
    sql = 'UPDATE '+ tbl + \
        ' SET ' + fldVal + \
        ' Where ' + crit + \
        ';'    
    if dbWrite(sql,val):
        return True

def dbDelete(tbl, crit = ' 1 = 1 ', val =()):
    sql = 'DELETE from ' + tbl + \
        ' Where ' + crit + \
        ';'         
    if dbWrite(sql,val):
        return True

def dbSelect(fld, tbl, crit = ' 1 = 1 ', gp = '', ob = ''):    
    sql = 'select'+ ' ' + fld + ' ' + \
        'from' + ' ' + tbl + ' ' + \
        'where' + ' ' + crit        
    if (gp != '' and ob != ''):
        sql = sql + ' Group By ' + ' ' + gp + ' Order By ' + ' ' + ob
    elif (gp == '' and ob != ''):
        sql = sql + ' Order By ' + ' ' + ob
    elif (gp != '' and ob == ''):
        sql = sql + ' Group By ' + ' ' + gp
    sql = sql  + ';'
    #print(sql)
    return dbRead(sql)


