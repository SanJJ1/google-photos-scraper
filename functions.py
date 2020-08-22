import time


def wait_until_load(element_wait_for_load):
    def link_has_gone_stale():
        try:
            # poll the link with an arbitrary call
            exec(element_wait_for_load)
            print('loaded')
            return False
        except:
            return True

    while link_has_gone_stale():
        time.sleep(.1)
        print('t')
        pass


def check_element(element):
    try:
        # poll the link with an arbitrary call
        exec(element)
        print('true check')
        return True
    except Exception as e:
        print('false check', e)
        return False