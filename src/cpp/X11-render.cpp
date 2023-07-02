#include <X11/Xlib.h>
#include <X11/Xutil.h>


Display* display = XOpenDisplay(NULL);
if (display == NULL) {
    fprintf(stderr, "Unable to open display\n");
    exit(1);
}


Window root = DefaultRootWindow(display);
Window window = XCreateSimpleWindow(display, root, 0, 0, 1, 1, 0, 0, 0);

XSetWindowAttributes attributes;
attributes.override_redirect = True; // Bypass the window manager
XChangeWindowAttributes(display, window, CWOverrideRedirect, &attributes);

XMapWindow(display, window);


XEvent event;
while (1) {
    XNextEvent(display, &event);
    // Handle events as needed
}

XDestroyWindow(display, window);
XCloseDisplay(display);
