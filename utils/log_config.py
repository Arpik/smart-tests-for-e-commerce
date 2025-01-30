"""
1.Creates a logs/ folder automatically.
2.Generates a timestamped log file.
3.Logs messages to both console and file.
4.Uses INFO level (you can change it to DEBUG).

"""
import logging
import os
from datetime import datetime

# Ensure logs directory exists and create the log file name
def check_log_directory(log_dir="logs"):
    os.makedirs(log_dir, exist_ok=True)
    return os.path.join(log_dir, f"test_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Create and return logger with handlers
def setup_logger(log_dir="logs"):

    # Ensure directory exists and get log file path
    log_file = check_log_directory(log_dir)

    # Create logger instance and set level
    logger = logging.getLogger("SmartTestsLogger")
    logger.setLevel(logging.DEBUG)

    # Create handlers
    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    console_handler = logging.StreamHandler()

    # Set level for handlers
    file_handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.INFO)

    # Set formatter and add to handlers
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Add logging to pytest capture
def pytest_configure(config):

    logger = setup_logger()
    pytest_log_handler = logging.StreamHandler()
    pytest_log_handler.setLevel(logging.DEBUG)
    logger.addHandler(pytest_log_handler)

    logging.basicConfig(level=logging.DEBUG)

logger = setup_logger()
