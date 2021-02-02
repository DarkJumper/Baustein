import sys
import functools
import time


def runtime_check(repeats):
    """
    runtime_check Eine funktion mehrmals ausführen lassen

    Args:
        repeats (int): Anzahl der gewünschten wiederholungen
    """

    def decorater_runtime_check(func):

        @functools.wraps(func)
        def wrapper_runtime_check(*args, **kwargs):
            print(f'Die Funktion {func.__name__} wird {repeats} ausgeführt!')
            for _ in range(repeats):
                value = func(*args, **kwargs)
            return None

        return wrapper_runtime_check

    return decorater_runtime_check


def debug(func):
    """
    debug Decorater Unterstützung beim debugen. Es wird funktions name Ausgegeben und Return wert der Aufgerufenen Funktion

    Args:
        func (funktion): Name der Ausgeführten Funktion

    Returns:
        None: Rückgabe wert der Aufgerufenen Funktion
    """

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Python Version {sys.version.split(' ')[0]}\nAufruf von: {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned: {value!r}")
        return value

    return wrapper_debug


def timer(func):
    """
    timer Ausgabe der Runtime Dauer

    Args:
        func (Funktion): Name der Ausgeführten Funktion

    Returns:
        None: Rückgabe wert der Aufgerufenen Funktion
    """

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Beendet {func.__name__!r} in {run_time:.4f} sekunden")
        return value

    return wrapper_timer
