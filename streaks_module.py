import sqlite3
import datetime

def get_streaks(user_name):
    conn = sqlite3.connect('neurosync.db')
    cursor = conn.cursor()
    user_id = cursor.execute("SELECT id FROM users WHERE name=?", (user_name,)).fetchone()
    
    if user_id:
        cursor.execute("SELECT * FROM streaks WHERE user_id = ?", (user_id[0],))
        result = cursor.fetchone()
        conn.close()
        return {"streak": result[2], "last_update": result[3]} if result else None
    conn.close()
    return None

def update_streaks(user_name):
    conn = sqlite3.connect('neurosync.db')
    cursor = conn.cursor()
    user_id = cursor.execute("SELECT id FROM users WHERE name=?", (user_name,)).fetchone()
    
    if user_id:
        today = datetime.date.today()
        last_update = cursor.execute("SELECT last_update FROM streaks WHERE user_id=?", (user_id[0],)).fetchone()

        # Check if last_update is not None and convert it to a date object
        if last_update and isinstance(last_update[0], str):
            last_update_date = datetime.datetime.strptime(last_update[0], '%Y-%m-%d').date()
        else:
            last_update_date = None

        # Only update streak if the last_update date is different from today
        if last_update_date is None or last_update_date < today:
            if last_update_date is None:
                # First entry for the user
                cursor.execute("INSERT INTO streaks (user_id, streak, last_update) VALUES (?, ?, ?)", (user_id[0], 1, today))
            else:
                # Increment streak and update last_update
                cursor.execute("UPDATE streaks SET streak = streak + 1, last_update = ? WHERE user_id = ?", (today, user_id[0]))
        
        # Commit changes to the database
        conn.commit()
    
    conn.close()
