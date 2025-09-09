def test_flaky_fail(page):
    page.goto("https://www.saucedemo.com/")
    page.wait_for_timeout(1000)
    assert False, "This is an intentional failure to test reporting."