# =========================================================
# Ghostty Configuration
# =========================================================
# Theme:
#   Kanagawa Wave
#
# Font:
#   Maple Mono NF CN
#
# Style:
#   Transparent macOS terminal with blur effect
#
# Features:
#   - Bar cursor
#   - Blinking cursor
#   - Mouse-friendly navigation
#   - Floating window shortcut
#   - Copy on select
# =========================================================


# ---------------------------------------------------------
# Theme
# ---------------------------------------------------------
theme = Kanagawa Wave


# ---------------------------------------------------------
# Font
# ---------------------------------------------------------
font-family = "Maple Mono NF CN"
font-size = 14


# ---------------------------------------------------------
# Window Padding
# ---------------------------------------------------------
window-padding-x = 15
window-padding-y = 15


# ---------------------------------------------------------
# Background / Transparency
# ---------------------------------------------------------
background-opacity = 0.90
background-blur = 250


# ---------------------------------------------------------
# Cursor
# ---------------------------------------------------------
cursor-style = bar
cursor-style-blink = true
cursor-click-to-move = true


# ---------------------------------------------------------
# Mouse Behavior
# ---------------------------------------------------------
mouse-hide-while-typing = true


# ---------------------------------------------------------
# Shell Integration
# ---------------------------------------------------------
shell-integration = detect
shell-integration-features = no-cursor


# ---------------------------------------------------------
# Copy Behavior
# ---------------------------------------------------------
copy-on-select = true


# ---------------------------------------------------------
# macOS Window Style
# ---------------------------------------------------------
macos-titlebar-style = transparent
macos-titlebar-proxy-icon = hidden


# ---------------------------------------------------------
# Keybindings
# ---------------------------------------------------------

# Toggle "always on top" floating window
keybind = opt+t=toggle_window_float_on_top


# ---------------------------------------------------------
# Recommended Shortcuts
# ---------------------------------------------------------
#
# Cmd + T
#   New tab
#
# Cmd + D
#   Split pane vertically
#
# Cmd + Shift + D
#   Split pane horizontally
#
# Cmd + W
#   Close pane/tab
#
# Cmd + Shift + ,
#   Reload config
#
# Cmd + ,
#   Open Ghostty settings
#
# ---------------------------------------------------------