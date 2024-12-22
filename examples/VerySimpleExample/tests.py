from src import Tester, assertEq

from .some_funcs import clear_cookies, add_cookies, get_all_cookies, COOKIE_MESSAGE

def main():
    cookie_tester = Tester()

    @cookie_tester.test
    def func1():
        assertEq(get_all_cookies(), COOKIE_MESSAGE)
        clear_cookies()

    @cookie_tester.test
    def func2():
        add_cookies()
        assertEq(get_all_cookies(), COOKIE_MESSAGE)
        clear_cookies()

    @cookie_tester.test
    def func3():
        add_cookies()
        assertEq(get_all_cookies(), "Hello I am a cookie!")
        clear_cookies()

    cookie_tester.run_all_tests()