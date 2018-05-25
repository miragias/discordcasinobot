import time

#TODO(JohnMir): Flask subproccess here
def do_something(pipe):
        output_p , input_p = pipe
        input_p.close()
        while True:
                time.sleep(2)
                try:
                        print(output_p.recv())
                except EOFError:
                        break
                pass