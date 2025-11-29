
def handle_command(message):
    match message:
        case ['BEEPER', frequency, times]:
            return f"Beeping at {frequency}Hz for {times} times."
        
        case ['NECK', angle]:
            return f"Turning neck to {angle} degrees."
        
        case ['LED', ident, intensity]:
            return f"Setting LED {ident} to intensity {intensity}."
        
        case ['LED', ident, red, green, blue]:
            return f"Setting LED {ident} to color RGB({red}, {green}, {blue})."
        
        case _:
            raise ValueError("Unknown command")
        

# Example usage:
print(handle_command(['BEEPER', 440, 3]))  # Beeping at 440Hz for 3 times.
        