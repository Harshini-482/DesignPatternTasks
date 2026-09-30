from datetime import datetime
import threading

from logger import Logger, LogLevel


class LoggerImpl(Logger):

    _instance = None
    _instance_lock = threading.Lock()

    def __new__(cls):
        # TODO:
        # Implement Singleton creation.
        # Consider thread safety while creating the instance.
        if(cls._instance is None):
            with cls._instance_lock:
                if(cls._instance is None):
                    cls._instance=super().__new__(cls)
        return cls._instance

        pass

    def __init__(self):
        # TODO:
        # Initialize the logger only once.
        #
        # You will need fields for:
        # - log file path
        # - file object
        # - lock for log operations
        if(hasattr(self,"_initialized")):
            return 
        self.file=None
        self._initialized=True
        pass

    @classmethod
    def get_instance(cls):
        # TODO:
        # Return the Singleton instance.
        pass

    @classmethod
    def reset_instance(cls):
        # TODO:
        # Reset the Singleton instance.
        # Think about what should happen if a file is still open.
        cls._instance=None

        pass

    def set_log_file(self, file_path):
        # TODO:
        # Open the log file and store the file path.
        self.file=open(file_path,"a")
        pass

    def log(self, level, message):
        # TODO:
        # 1. Check whether the logger has been initialized.
        # 2. Create a timestamp.
        # 3. Format the log entry.
        # 4. Write it to the file.
        # 5. Make the operation thread-safe.
        entry=f"[{level.value}]{message}\n"
        self.file.write(entry)
        pass

    def get_log_file(self):
        # TODO:
        # Return the current log file path.
        pass

    def flush(self):
        # TODO:
        # Flush buffered log entries.
        pass

    def close(self):
        # TODO:
        # Close the file resource.
        self.file.close()
        pass