from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt6.QtGui import QPixmap, QIcon

def create_navigation_buttons(parent):
    # Navigation bar layout
    nav_bar = QHBoxLayout()
    nav_bar.setContentsMargins(0, 0, 0, 0)
    nav_bar.setSpacing(0) 

    # Home button
    home_button = QPushButton() # Home button
    home_icon = QIcon("assets/button/home.png") # Home icon
    home_button.setStyleSheet("border: none;") # Remove border for a cleaner look
    if home_icon.isNull(): ## Check if the icon is valid
        print("⚠️ Error: not found 'assets/button/home.png'")
    home_button.setIcon(home_icon) # Set the icon for the button
    home_button.setFixedSize(40, 40)    # Set the size of the button
    home_button.clicked.connect(parent.home) # Connect the button to the home function

    # Back and forward
    back_button = QPushButton() # Back button
    back_icon = QIcon("assets/button/back.png") # Back icon
    back_button.setStyleSheet("border: none;") # Remove border for a cleaner look
    if back_icon.isNull(): ## Check if the icon is valid
        print("⚠️ Error: not found 'assets/back.png'")
    back_button.setIcon(back_icon) # Set the icon for the button
    back_button.setFixedSize(40, 40) # Set the size of the button
    back_button.clicked.connect(parent.back) # Connect the button to the back function

    forward_button = QPushButton()
    forward_icon = QIcon("assets/button/forward.png")
    forward_button.setStyleSheet("border: none;")
    if forward_icon.isNull():
        print("⚠️ Error: not found 'assets/button/forward.png'")
    forward_button.setIcon(forward_icon)
    forward_button.setFixedSize(40, 40)
    forward_button.clicked.connect(parent.forward)

    # Refresh button
    refresh_button = QPushButton() 
    refresh_icon = QIcon("assets/button/reload.png")
    refresh_button.setStyleSheet("border: none;") # Remove border for a cleaner look
    if refresh_icon.isNull():
        print("⚠️ Error: not found 'assets/button/reload.png'")
    refresh_button.setIcon(refresh_icon)
    refresh_button.setFixedSize(40, 40)
    refresh_button.clicked.connect(parent.refresh)

    # URL Bar
    url_bar = QLineEdit()
    url_bar.setPlaceholderText("Enter a URL...")
    url_bar.returnPressed.connect(parent.load_url)
    url_bar.setStyleSheet("border-radius: 10px; padding: 5px; background-color: #f0f0f0; border: 1px solid #ccc;") # Style the URL bar

    # Adding buttons and URL bar to the navigation bar
    nav_bar.addWidget(back_button)
    nav_bar.addWidget(forward_button)
    nav_bar.addWidget(refresh_button)
    nav_bar.addWidget(home_button)
    nav_bar.addWidget(url_bar)
    nav_bar.addStretch() # Add stretch to push the URL bar to the right
    nav_bar.setStretchFactor(url_bar, 1)

    return nav_bar, url_bar