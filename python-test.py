import logging
from typing import Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

MESSAGE = "Hello, World!"


def greet(name: Optional[str] = None) -> str:
    """Generate and return a greeting message."""
    message = f"{MESSAGE} Welcome, {name}!" if name else MESSAGE
    logger.info("Greeting generated")
    return message


def main() -> None:
    """Main entry point for the application."""
    logger.info("Application started")

    try:
        result = greet("Enterprise")
        print(result)
    except Exception:
        logger.exception("Application failed")


if __name__ == "__main__":
    main()