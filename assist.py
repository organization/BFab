import sys, re

'''
    assist.py는 BF-Assist 언어 컴파일러입니다. 컴파일 결과물은 Brainfuck 코드입니다.

BF-Assist는 Brainfuck으로 1:1 치환이 가능한 간단한 구조의 언어입니다. 확장자는 .bfs입니다.
언어의 요소들은 다음과 같습니다.

add N M: 메모리 주소 N부터 N + K - 1까지에 M만큼의 수를 더합니다. N은 부호 없는 정수, M은 부호 있는 정수 또는 아스키 문자(숫자일 경우 ""를 붙여야 합니다)입니다. K는 자연수이며 생략 시 1입니다.
set N M K: 메모리 주소 N부터 N + K - 1의 값을 M으로 만듭니다 N, M, K의 조건은 add와 같습니다.
copy N M K: 메모리 주소 N부터 N + K - 1까지의 값을 M부터 M + K - 1로 복사합니다. K는 생략 시 1입니다.
move N M K: 메모리 주소 N부터 N + K - 1까지의 값을 M부터 M + K - 1로 복사하고 복사한 주소의 값을 0으로 만듭니다. K는 생략 시 1입니다.
str N <string>: 메모리 주소 N부터 N + len(<string>) - 1까지의 메모리를 <string>의 각 문자로 설정합니다.
for N - rof: 메모리 주소 N이 0이 아닐 동안 루프를 순회합니다.
raw <code>: <code> 부분을 그대로 컴파일 결과로 출력합니다.
ret N <code>: <code> 부분을 N회 반복해 출력합니다.
macro_start <name>: 매크로의 시작입니다. 매크로 이름은 <name>입니다. macro_start와 macro_end 사이에 코드를 넣으면 됩니다.
macro_end: 매크로의 끝입니다.
;<any string>: 주석입니다.

BF 모르면서 이 언어 복잡하다고 하면 내장을 꼬아서 짚신으로 만들어버릴 거니 그렇게 아시면 됩니다.
'''

class Compiler:
    def __init__(self, rawcode):
        self.code = re.sub("^\s+", "\n", rawcode).replace("\r", "")
        if self.code[0] == "\n":
            self.code = self.code[1:]

    def compile(self):
        pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s <.bfs file>" % sys.argv[0])
        sys.exit()

    fp = open(sys.argv[1], "r")
    data = fp.read()
    fp.close()
    compiler = Compiler(data)
    compiler.compile()
