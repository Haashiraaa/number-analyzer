

# main.py


import sys
import logging
from typing import Optional
from number_analyzer.input_validator import InputHandler, NumberController
from haashi_pkg.utility import Logger, ScreenUtil as su


choice_map = {
    1: NumberController.check_even,
    2: NumberController.check_prime,
    3: NumberController.check_square_root,
}


# ======================
# Main Menu
# ======================


def main_menu(logger: Optional[Logger] = None) -> None:
    """Displays the list of available operations.
    Helps users choose what action to perform.
    """
    logger = logger or Logger(level=logging.INFO)
    options: list[str] = [
        "Even or Odd Checker",
        "Prime Checker",
        "Square Root Calculator",
        "Exit.",
    ]

    logger.info("Choose an operation:")
    for i, option in enumerate(options, start=1):
        logger.info(f"{i}. {option}")


# ======================
# Main
# ======================


def main(logger: Optional[Logger] = None) -> None:
    logger = logger or Logger(level=logging.INFO)

    su.space()
    logger.info("Hello! Welcome to the Number Analyzer!")
    logger.info("This program will help you with some mathematical operations.")
    su.space()
    su.wait_and_enter()

    while True:
        su.clear_screen()
        su.space()
        main_menu()

        try:
            user_choice = InputHandler.get_input(
                msg1=None,
                prompt="Enter your choice (1-4): ",
                logger=logger
            )

            if user_choice == 4:
                su.space()
                logger.info("Exiting Program...")
                sys.exit(0)

            if user_choice and user_choice > 4:
                su.space()
                logger.info(f"Input: ({user_choice}) is out of range!")
                su.wait_and_enter()
                continue

            if user_choice is None:
                continue

            func = choice_map.get(int(user_choice))
            if not func:
                su.space()
                logger.warning(f"Input: ({user_choice}) is invalid")
                su.wait_and_enter()
                continue

            result = func()
            if result is None:
                continue
            su.space()
            logger.info(result)
            su.wait_and_enter()

        except KeyboardInterrupt:
            su.space(2)
            logger.info("Program interrupted by user.")
            sys.exit(0)

        except Exception as exc:
            su.space(2)
            logger.error(f"An error occurred: {exc}")
            logger.error(exception=exc, save_to_json=True)
            sys.exit(1)


if __name__ == "__main__":
    main()
