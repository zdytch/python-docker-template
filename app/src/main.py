from settings import DEBUG

if DEBUG:
    import debugpy

    debugpy.listen(('0.0.0.0', 5678))

    if DEBUG == 2:
        debugpy.wait_for_client()


if __name__ == '__main__':
    # Start here
    ...
