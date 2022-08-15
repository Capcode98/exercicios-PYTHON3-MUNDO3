import socket
from socket import gethostbyname, create_connection


def verificacao(site):

    try:
        create_connection((gethostbyname(site), 80), 2)

    except socket.gaierror:
        return print(f"\033[31mERRO 404: Site não encontrado,"
                     f" verifique sua conexão e tente novamente, por favor! \033[m")

    else:
        return print('\033[32mSite encontrado com sucesso!\033[m')

    finally:
        pass
