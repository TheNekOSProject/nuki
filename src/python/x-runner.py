from Xlib import X, display

# Initialize a connection to the X server
d = display.Display()

# Create an invisible window
root = d.screen().root
window = root.create_window(0, 0, 1, 1, 0, X.CopyFromParent, X.InputOutput, X.CopyFromParent)

# Set the window properties
window.change_attributes(override_redirect=True)

# Map the window to make it visible
window.map()

# Handle events (optional)
while True:
    event = d.next_event()
    # Handle events as needed
    break

# Clean up and close the connection when done
window.destroy()
d.close()
