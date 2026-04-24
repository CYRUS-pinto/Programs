def generator_display(data: list):
    """A function that yields items one by one (a Generator)."""
    print("--- Starting Generator ---")
    for item in data:
        print(f"Yielding item: {item}")
        yield item  # Pause execution and send the value back

# Create a list
my_list = [10, 20, 30]

# When we call the function, it returns a generator object
gen = generator_display(my_list)

print("\n--- Iterating over the Generator ---")
# Now we iterate over the generator object
for result in gen:
    print(f"Received from generator: {result}")
