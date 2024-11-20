import logging

# Configure logging
log_file = "math_logging.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Logging decorator
def log_operations(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Calling function '{func.__name__}' with arguments: {args}")
        result = func(*args, **kwargs)
        logger.info(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

@log_operations
def division(n1, n2, n3):
    if n2 == 0 or n3 == 0:
        raise ValueError("Division by zero is not allowed.")
    return n1 / n2 / n3

@log_operations
def multiplication(n1, n2, n3):
    return n1 * n2 * n3

@log_operations
def addition(n1, n2, n3):
    return n1 + n2 + n3

# Example usage
if __name__ == "__main__":
    try:
        print(division(12, 3, 0))
        print(multiplication(2, 3, 4))
        print(addition(5, 7, 2))
    except Exception as e:
        logger.error(f"An error occurred: {e}")
