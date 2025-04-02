
# Import necessary libraries like PyQt6 and QWebEngineView
import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEngineSettings
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtGui import QIcon

# Importing custom modules
from navigation_buttons import create_navigation_buttons
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

# Browser class that inherits from QMainWindow
class browser(QMainWindow):
    # Initialize the browser window
    def __init__(self):
        super().__init__()

        profile = QWebEngineProfile.defaultProfile()

        self.homepage_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "examples", "homepage.html")
        if not os.path.isfile(self.homepage_path):
            print(f"⚠️ Error: not found {self.homepage_path}")

        # Window title and size
        self.setWindowTitle("Spaceship Browser")
        self.setGeometry(100, 100, 800, 600) # Set the window size


        #Icon
        icon_path = 'assets/spaceshipai_browser_logo.png'
        if os.path.isfile(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # lAYOUT
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()

        # Control
        nav_bar, self.url_bar = create_navigation_buttons(self)
        layout.addLayout(nav_bar)

        # Web Engine View

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(QUrl.fromLocalFile(self.homepage_path)))
        self.browser.urlChanged.connect(self.update_url_bar)

        # Layout
        layout.addLayout(nav_bar)
        layout.addWidget(self.browser)

        self.central_widget.setLayout(layout)


    def load_url(self):
        url = self.url_bar.text()
        # If the URL is a search query, use Google search
        if not url.startswith("http") and not "." in url:
            url = f"https://www.google.com/search?q={url.replace(' ', '+')}"

        # Check if the URL starts with http or https, if not, add https
        elif not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

        # Load the URL in the browser
        self.browser.setUrl(QUrl(url))

    # Update the URL bar when the page changes
    def update_url_bar(self, url):
        self.url_bar.setText(url.toString())

    # Home button to go to Google
    def home(self):
        self.browser.setUrl(QUrl(QUrl.fromLocalFile(self.homepage_path)))

    # Back, forward and refresh
    def back(self):
        self.browser.back()

    def forward(self):
        self.browser.forward()

    def refresh(self):
        self.browser.reload()

# Start the browser
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = browser()
    window.show()
    sys.exit(app.exec())