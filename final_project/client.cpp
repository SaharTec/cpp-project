#include <arpa/inet.h>
#include <sys/socket.h>  // socket, bind, listen, accept, send, recv
#include <unistd.h>      // close
#include <cstring>       // strlen
#include <iostream>
#include <sstream>
#include <thread>
using namespace std;

int nain(){
    int fd = socket(AF_INET, SOCK_STREAM, 0);

    sockaddr_in srv{};
    srv.sin_family = AF_INET;
    srv.sin_port = htons(5555);
    inet_pton(AF_INET, "127.0.0.1", &srv.sin_addr);

    connect(fd, (sockaddr*)&srv, sizeof(srv)); //conect to the server
}