from time import sleep
from souper import souper
from display import display_loading_msg
import threading
import os
from parse_html import get_newest_html

def main():
    # loads the display_loading_msg() in a separate thread
    loading_thread = threading.Thread(target=display_loading_msg)
    # setting Thread.daemon to True ensures that it doesnt quit until program concludes
    loading_thread.daemon = True
    loading_thread.start()
    doc_name = souper()
    os.remove(doc_name)
    print('\nWord document saved to current directory')


if __name__ == '__main__':
    main()
