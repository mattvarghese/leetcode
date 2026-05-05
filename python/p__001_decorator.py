import time
from functools import wraps

def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # Execute the actual function
        result = func(*args, **kwargs)
        
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.4f}s")
        return result
    
    return wrapper

@timer_decorator
def transform_patient_data():
    time.sleep(1.5)  # Simulate a heavy task
    return "Data Transformed"

# Calling the function now automatically includes the timing logic
print (transform_patient_data())
print (transform_patient_data.__name__) 
