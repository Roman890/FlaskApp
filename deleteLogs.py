from __init__ import Bots, Logs, db
import datetime
from Templates import Templates

def delete_logs_tab():
    all_data = db.session.query(Logs).filter(Logs.created_date<'2020-07-31 21:55:00.000000').all()
    for item in all_data:
        db.session.delete(item)
    db.session.commit()
    return True
    
delete_logs_tab()