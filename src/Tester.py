
global colorama_present
colorama_present = False

try:
    from colorama import Fore, Style
    from colorama import init as init_colors
    init_colors()
    colorama_present = True

except:
    pass


def log_result(func) -> bool:
    global colorama_present
    success = True
    error = None
    try:
        func()
    except Exception as err:
        error = err
        success = False

    if success:
        if colorama_present:
            print(Style.DIM + " " + Fore.GREEN + "-> success", end = "")
            print(Style.RESET_ALL)
        else:
            print(" -> success", end="")
    else:
        if colorama_present:
            print(Style.BRIGHT, Fore.RED + "-> failed", end = "")
            print(Style.RESET_ALL, "\nError is as follows:")
            print(f"{Style.BRIGHT}error = {error}\n{error.args = }{Style.RESET_ALL}")
        else:
            print(" -> failed", end="")
            print("\nError is as follows:")
            print("error = {error}\n{error.args = }")

    return success


class Tester:
    def __init__(self):
        global colorama_present
        self.tests: list = []
        if not colorama_present:
            print("[Tester]: colorama is not installed which is recommended for test results to be more clear.")            

    def test(self, func: object) -> object:
        global colorama_present
        idx = len(self.tests) + 1
        def wrapper() -> bool:
            if colorama_present:
                print(Style.BRIGHT + f"[{idx}:{func.__name__=}]" + Style.RESET_ALL, end="")
            else:
                print(f"[{idx}:{func.__name__=}]", end="")
            return log_result(func)

        self.tests.append(wrapper)
        return wrapper

    def run_all_tests(self) -> None:
        global colorama_present
        all_success: bool = True
        fails = 0

        for test in self.tests:
            if not test():
                all_success = False
                fails += 1

        if all_success:
            if colorama_present:
                print(Fore.GREEN + "All tests ran successfully.", end="")
                print(Style.RESET_ALL)
                return
            print("All tests ran successfully.")
        else:
            if colorama_present:
                print(Fore.RED + f"{fails} tests failed.", end="")
                print(Style.RESET_ALL)
                return
            print(f"{fails} tests failed.")