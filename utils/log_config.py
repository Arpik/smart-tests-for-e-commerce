"""
1.Creates a logs/ folder automatically.
2.Generates a timestamped log file.
3.Logs messages to both console and file.
4.Uses INFO level (you can change it to DEBUG).

"""

import logging
import os
from datetime import datetime

# Ensure logs directory exists
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Define log file name with timestamp
log_file = os.path.join(log_dir, f"test_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Create logger instance
logger = logging.getLogger("SmartTestsLogger")
logger.setLevel(logging.DEBUG)

# Remove existing handlers to avoid duplication
if logger.hasHandlers():
    logger.handlers.clear()

# File handler to capture logs to the log file
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Console handler to print logs to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Log format definition
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add both handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Add logging to pytest capture
# This ensures pytest captures all log messages during the test run
def pytest_configure(config):
    logging.basicConfig(level=logging.DEBUG)
    pytest_log_handler = logging.StreamHandler()
    pytest_log_handler.setLevel(logging.DEBUG)
    logger.addHandler(pytest_log_handler)
