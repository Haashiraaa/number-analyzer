# number-analyzer

A CLI tool for basic number analysis. Accepts interactive input and runs three operations: even/odd detection, primality testing, and square root calculation.

---

## Project Structure

```
number-analyzer/
├── number_analyzer/
│   ├── __init__.py
│   ├── main.py            # Entry point and menu loop
│   ├── number_utils.py    # Core math logic
│   ├── input_validator.py # Input parsing and operation controllers
│   └── types.py           # Shared type aliases
├── tests/
│   ├── test_number_utils.py
│   └── test_input_validator.py
└── pytest.ini
```

---

## Dependencies

- Python 3.10+
- [`haashi_pkg`](https://github.com/haashiraaa/haashi-analytics-toolkit) — used for logging (`Logger`) and screen utilities (`ScreenUtil`)

No third-party packages beyond `haashi_pkg`. Standard library only (`math`, `sys`, `logging`).

---

## Installation

Clone the repo and ensure `haashi_pkg` is installed in your environment.

```bash
git clone https://github.com/Haashiraaa/number-analyzer.git
cd number-analyzer
pip install -r requirements.txt
```

---

## Usage

```bash
python -m number_analyzer.main
```

Or directly:

```bash
python number_analyzer/main.py
```

You will be presented with a menu:

```
Choose an operation:
1. Even or Odd Checker
2. Prime Checker
3. Square Root Calculator
4. Exit.
```

Enter a number (1-4) to select. From any operation, enter `q` to return to the menu. `Ctrl+C` exits cleanly at any point.

---

## Modules

### `types.py`

Shared type aliases used across the package:

- `NumberLike = Union[int, float]`
- `SquareRoot = Tuple[float, float, int, int]` — `(exact, rounded_to_sf, rounded_int, sf)`

---

### `number_utils.py`

Stateless math operations. All methods are `@staticmethod`.

| Method | Signature | Description |
|---|---|---|
| `is_even` | `(num: NumberLike) -> bool` | Returns `True` if `num % 2 == 0` |
| `is_prime` | `(num: NumberLike) -> bool` | Trial division up to `sqrt(n)`. Returns `False` for values less than 2 |
| `square_root` | `(num: NumberLike, sf: int = 2) -> SquareRoot` | Returns `(exact, rounded_to_sf, rounded_int, sf)` |

---

### `input_validator.py`

Two classes handling input parsing and wiring operations to user prompts.

**`InputHandler`**

- `get_input(msg0, msg1, prompt, logger)` — Prints messages, reads stdin, delegates to `parse_input`
- `parse_input(user_input, logger)` — Returns `int` if whole number, `float` otherwise, `None` on `q` or invalid input

**`NumberController`**

- `check_even(logger)` — Delegates to `NumberUtils.is_even`
- `check_prime(logger)` — Delegates to `NumberUtils.is_prime`
- `check_square_root(logger)` — Delegates to `NumberUtils.square_root`, formats multi-line output

---

### `main.py`

Entry point. Contains:

- `main_menu(logger)` — Prints the operation list
- `main(logger)` — Runs the `while True` menu loop, dispatches to `NumberController` via `choice_map`, handles `KeyboardInterrupt` and unexpected exceptions (logs errors to JSON on crash)

---

## Tests

```bash
pytest
```

`pytest.ini` sets `pythonpath = .` and `testpaths = tests`.

**`test_number_utils.py`** — covers `NumberUtils` with parametrized cases for valid inputs, edge cases, and invalid types (expects `TypeError`).

**`test_input_validator.py`** — covers `InputHandler.parse_input` with valid inputs (`q`, integers, floats) and invalid inputs, using a mocked `Logger` and patched `ScreenUtil`.

---

## Error Handling

| Scenario | Behaviour |
|---|---|
| Non-numeric input | Warning logged, falls back to main menu |
| `q` entered | Returns `None`, loop continues |
| Out-of-range menu choice | User notified, re-prompted |
| `KeyboardInterrupt` | Clean exit with message |
| Unhandled exception | Error logged to JSON, `sys.exit(1)` |

---

## Author

Haashiraaa
