#!/usr/bin/env python3
"""
Simple HTTP server launcher for the driving test application.
Just double-click this file to start the application.
Auto-shutdowns after 3 hours to save resources.
"""

import http.server
import socketserver
import webbrowser
import os
import time
import threading
from pathlib import Path


def auto_shutdown(server, hours=3):
    """Automatically shutdown the server after specified hours"""
    seconds = hours * 3600
    time.sleep(seconds)
    print(f"\n[AUTO] Server shutting down after {hours} hours")
    server.shutdown()


def main():
    script_dir = Path(__file__).parent.absolute()
    os.chdir(script_dir)
    
    # Check if required files exist
    if not Path("index.html").exists():
        print("[ERROR] index.html not found!")
        print("Make sure this script is in the same folder as index.html")
        input("Press Enter to exit...")
        return
    
    if not Path("pytania.csv").exists():
        print("[ERROR] pytania.csv not found!")
        print("Download the question database from the official source.")
        print("See README.md for instructions.")
        input("Press Enter to exit...")
        return
    
    PORT = 8000
    AUTO_SHUTDOWN_HOURS = 3
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("Driving Test Practice Application")
            print("-" * 40)
            print(f"Serving files from: {script_dir}")
            print(f"Server running at:  http://localhost:{PORT}")
            print(f"Auto-shutdown after {AUTO_SHUTDOWN_HOURS} hours")
            print("Press Ctrl+C to stop the server manually")
            print("-" * 40)
            
            shutdown_timer = threading.Thread(
                target=auto_shutdown, 
                args=(httpd, AUTO_SHUTDOWN_HOURS),
                daemon=True
            )
            shutdown_timer.start()
            
            webbrowser.open(f'http://localhost:{PORT}')
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n[INFO] Server stopped by user")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"[ERROR] Port {PORT} is already in use!")
            print("Try closing other applications or restart your computer")
            input("Press Enter to exit...")
        else:
            print(f"[ERROR] Error starting server: {e}")
            input("Press Enter to exit...")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        input("Press Enter to exit...")


if __name__ == "__main__":
    main()
