import os
import sys


class Main:

    def run(self, string):
        sys.stdout.write(''.join(self.parse(string)))

    def parse(self, string):
        return eval(
            string, 
            None, 
            {'_': self.read()}
        )

    def read(self):
        fd = sys.stdin.fileno()
        while True:
            ch = os.read(fd, 1)
            if ch is None or len(ch) == 0:
                break
            else:
                yield ch
    

def main(args=None):
    exp = '_'
    if args is not None and len(args):
        exp = args[0]
    Main().run(exp)
    


if __name__ == '__main__':
    main(sys.argv[1:])
