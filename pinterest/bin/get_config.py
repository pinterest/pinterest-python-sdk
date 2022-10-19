"""
command to get config variables
"""
import sys


def main(_):
    # pylint: disable=import-outside-toplevel
    """
    function to get config variables
    """
    try:
        from pinterest.client import config as module
    except ImportError as exc:
        raise exc

    variables = [
        (key, value)
        for (key, value) in vars(module).items()
        if (isinstance(value, (str, int, float)))
        and not (key.startswith("_") or key.startswith("__"))
    ]

    for (key, value) in variables:
        print(key, '=', value)


if __name__ == "__main__":
    main(sys.argv)
