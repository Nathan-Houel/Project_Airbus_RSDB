import sqlite3
from datetime import datetime


def update_spec(equip_id, new_val):
    
    # Opening the database
    conn = sqlite3.connect('avionics.db')
    cur = conn.cursor()

    # Retrieve old value
    old_value = cur.execute("SELECT max_value FROM Limits WHERE ID = ?", (equip_id,)).fetchone()[0]

    # Modifying the value
    cur.execute("UPDATE Limits SET max_value = ? WHERE ID = ?", (new_val, equip_id))

    # Adding the data in the History table
    cur.execute("INSERT OR IGNORE INTO History \
                (equipment_id, old_value, new_value, change_date) VALUES (?, ?, ?, ?)", \
                (equip_id, old_value, new_val, datetime.now().isoformat()))

    conn.commit()
    conn.close()
