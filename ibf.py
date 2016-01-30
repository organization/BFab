import bf, sys

# Improved BrainFuck - 더 편리한(?) BF 인터프리터
# 디버깅, 시각화가 주 목적입니다.

help_ =  """사용법:

"""

if len(sys.argv) < 2:
    print("Usage: %s <.bf file>" % sys.argv[0])
    sys.exit()

fp = open(sys.argv[1], "r")
tape = fp.read()
fp.close()
runtime = bf.Runtime(tape)
print(runtime.tape)
while True:
    off = runtime.offset
    code = runtime.tape[off]
    runtime.readTape(code)
    print(" " * max(0, 10-off) + runtime.tape[max(0, off - 10):off + 10])
    print(" " * 10 + "^")
    try:
        cmd = input("Type command(? for help): ").split(" ")
    except EOFError:
        sys.exit()
    runtime.offset += 1
