#include "./xtools.cpp"

XEvent event;
while (1) {
    XNextEvent(display, &event);
    // Handle events as needed
}

XDestroyWindow(display, window);
XCloseDisplay(display);
