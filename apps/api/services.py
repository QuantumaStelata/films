
def is_int(obj):
    try:
        obj = int(obj)
        return obj
    except (ValueError, TypeError):
        return False