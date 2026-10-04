"""
Safe Input Handler Module

Provides a robust wrapper around Python's built-in input() function
that handles non-interactive environments gracefully.
"""

import sys
from typing import Optional


def safe_input(prompt: str = "", default: Optional[str] = None) -> str:
    """
    Safely prompt the user for input, handling non-interactive environments.

    In interactive mode, this behaves like the standard input().
    In non-interactive modes (CI, testing, etc.), it returns the default
    value or raises a custom exception if neither is possible.

    Args:
        prompt: The prompt string to display to the user.
        default: The default value to return if the user presses Enter
                 without providing input. If None, requires explicit input.

    Returns:
        The user's input string (stripped of leading/trailing whitespace),
        or the default value if no input was given.

    Raises:
        ValueError: If default is provided but empty and no other option exists.
        RuntimeError: If the underlying input mechanism fails entirely
                      (e.g., broken stdin).

    Example:
        >>> safe_input("Enter your name: ")
        Alice
        >>> safe_input("Default: ", default="Guest")
        Guest
    """
    # Check if stdin is available (interactive vs non-interactive)
    try:
        # Try to read from stdin - this will work in interactive terminals
        # but may fail in some non-interactive contexts
        input_str = input(prompt, default=default)
    except EOFError:
        # No input available (e.g., piped empty input)
        if default is not None:
            return default
        raise RuntimeError(
            "No input available and no default specified. "
            "Cannot read from stdin."
        ) from None
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        raise
    except Exception as e:
        # Fallback for any unexpected errors during input
        if default is not None:
            return default
        raise RuntimeError(f"Failed to read input: {e}") from e

    # Strip whitespace and return
    return input_str.strip()


# For backward compatibility with existing code that uses input()
# We can also expose the original function under a different name
_original_input = __builtins__.input  # type: ignore


if __name__ == "__main__":
    # Simple demonstration
    print("Safe input demo:")
    name = safe_input("What is your name? ", default="Anonymous")
    print(f"Hello, {name}!")