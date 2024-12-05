import random
import time

# The generator function simulating a data stream
def data_stream(limit=10):  # Limit set for the number of items
    for _ in range(limit):
        yield random.randint(1, 100)

# The decorator function to log execution time
def time_logger(generator_func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = generator_func(*args, **kwargs)
        count = 0
        for item in result:
            count += 1  # Iterate through the generator
        end_time = time.time()  # Record end time
        print(f"Processed {count} items in {end_time - start_time:.6f} seconds.")
        return result  # Return the generator back
    return wrapper

# Apply the decorator to the generator
@time_logger
def data_stream(limit=10):
    for _ in range(limit):  # Ensure limited iterations
        yield random.randint(1, 100)

# Testing the generator with the decorator
if __name__ == "__main__":
    try:
        # Create a generator that will yield 10 random numbers
        stream = data_stream(limit=10)
        
        # Consume the numbers from the generator
        for _ in range(10):  # We process exactly 10 numbers
            next(stream)
    except KeyboardInterrupt:
        print("\nProcess was interrupted manually!")
