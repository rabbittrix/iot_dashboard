import json

def get_devices(cursor):
    cursor.execute('SELECT * FROM devices')
    devices = cursor.fetchall()
    return [{'id': row[0], 'name': row[1], 'type': row[2], 'status': row[3],
             'x_position': row[4], 'y_position': row[5], 'config': json.loads(row[6])} for row in devices]
    
def update_device_status(cursor, device_id, status):
    cursor.execute('UPDATE devices SET status = ? WHERE id = ?', (status, device_id))
   
def configure_device(cursor, device_id):
    new_config = {'threshold': 70, 'alert': True}
    cursor.execute('UPDATE devices SET config = ? WHERE id = ?', (json.dumps(new_config), device_id))    
        