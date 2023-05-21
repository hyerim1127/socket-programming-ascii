import socket

def main():
    host = '127.0.0.1'  # 서버 주소
    port = 1127  # 포트 번호

    # 소켓 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 서버에 연결
    client_socket.connect((host, port))
    print('Server Connected')

    # 문자 전송
    character = input('Enter character : ')
    client_socket.send(character.encode())

    # 아스키 코드 값 수신
    ascii_data = client_socket.recv(1024).decode()
    print('The ASCII code is', ascii_data)

    # 클라이언트 소켓 종료
    client_socket.close()

if __name__ == '__main__':
    main()