# error handling
# try-except-else-finally

# 1. try: code that might raise exception is placed here
# 2. except: code that run if exception occurs
# 3. else: code thar runs if no exception occurs
# 4. finally: code that runs no exception occurs or not(common used for cleanup actions)

try: 
    # code that might raise an exception
    result = 10/0 
except ZeroDivisionError as e:
    # code that run if ZeroDivisionError occurs
    print(f"Error occured: {e}")
except Exception as e:
    # code that runs if any other exception occurs
    print(f"An unexpected error occurred: {e}")
else:
    # code that runs in no exception occurs
    print("operation successful")
finally:
    # code that runs no matter what
    print("cleanup acctions, if any, go here")