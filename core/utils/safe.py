def safe_run(fn,*a,**k): 
    try: return fn(*a,**k)
    except Exception as e: return {'error': str(e)}
