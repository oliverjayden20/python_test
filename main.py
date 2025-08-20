def in_autotests_we_trust(a, b):
    if a == b:
        print('boy this boring time to make some real code!!')
    else:
        print('Test failed')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)
