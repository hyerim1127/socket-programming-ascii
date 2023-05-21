import socket

def convert_to_ascii(data):
    #입력된 데이터가 문자인 경우
    if len(data) == 1:
        return ord(data)
    #입력된 데이터가 문자열인 경우
    else:
        return ' '.join(str(ord(char)) for char in data)

def main():
    host = '127.0.0.1'  # 서버 주소
    port = 1127  # 포트 번호

    # 소켓 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 서버 소켓을 주소에 바인딩
    server_socket.bind((host, port))

    # 클라이언트의 연결 요청 대기
    server_socket.listen(1)
    print('Server Started')

    while True:
        # 클라이언트와 연결 수락
        # addr = 서버와 연결된 클라이언트의 주소 정보
        client_socket, addr = server_socket.accept()
        print('Client Connected')
        print('Client Addr : ', addr)

        # 클라이언트로부터 데이터 수신
        # data = 클라이언트로부터 수신된 데이터
        data = client_socket.recv(1024).decode()
        print('Received Data:', data)

        # 데이터를 아스키 코드로 변환
        ascii_data = convert_to_ascii(data)

        # 아스키 코드 값을 클라이언트에게 전송
        client_socket.send(str(ascii_data).encode())

        # 클라이언트 소켓 종료
        client_socket.close()

if __name__ == '__main__':
    main()