import datetime
import time

def sleep(n_secs):
    time.sleep(n_secs)

def get_timestamp():
    dtime = datetime.datetime.now()
    un_time = time.mktime(dtime.timetuple())
    return str(un_time)

def print_docId(docId):
    print(docId)


def print_phonepass(phone,password):
    print(phone + "---------" + password)

