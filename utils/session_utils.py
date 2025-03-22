import time

def check_session_timeout(last_activity, timeout):
    return time.time() - last_activity > timeout