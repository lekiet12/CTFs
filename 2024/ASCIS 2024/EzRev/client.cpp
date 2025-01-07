#include <stdio.h>
#include <winsock2.h>
#include <string.h>
int main(){
    WSADATA WSAData;
    SOCKET server;
    SOCKADDR_IN addr;
    if (WSAStartup(MAKEWORD(2, 2), &WSAData) != 0) {
        printf("WSAStartup failed!\n");
        return 1;
    }
    server = socket(AF_INET, SOCK_STREAM, 0);
    if (server == INVALID_SOCKET) {
        printf("Socket creation failed!\n");
        WSACleanup();
        return 1;
    }
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8080);
    if (connect(server, (SOCKADDR *)&addr, sizeof(addr)) == SOCKET_ERROR) {
        printf("Connection failed!\n");
        closesocket(server);
        WSACleanup();
        return 1;
    }
    // printf("Connected to server!\n");
    char reply[1024];
    // printf("Send a message: ");
    UINT16 buffer[]={0x5c,0x3f,0x3f,0x5c,0x44,0x3a,0x5c,0x66,0x6c,0x61,0x67,0x2e,0x74,0x78,0x74,0,0,0x14,0x06,0x34,0x29,0x3d,0x31,0x1d,0x07,0x3a,0x3c,0x2c,0x32,0x2f,0x1f,0x1b,0x3e,0x10,0x13,0x24,0x15,0x2b,0x25,0x39,0x1c,0x01,0x17,0x3b,0x20,0x0d,0x30,0x1a,0x3f,0x27,0x1e,0x33,0x22,0x35,0x16,0x05,0x09,0x36,0x2a,0x0b,0x12,0x0a,0x2e,0x37,0x38,0x08,0x03,0x02,0x19,0x26,0x04,0x23,0x18,0x11,0x28,0x0f,0x0e,0x2d,0x21,0x0c};
    send(server, (const char*)buffer, 78, 0); 
    // printf("Message sent!\n");
    int bytesReceived = recv(server, reply, sizeof(reply) - 1, 0);
    if (bytesReceived > 0) {
        reply[bytesReceived] = '\0'; 
        // printf("Server reply: ");
        for(int i=0;i<bytesReceived;i++){
            printf("%02x",reply[i]&0xff);
        }
        // printf("\n");
    } else {
        printf("Failed to receive reply from server!\n");
    }
    closesocket(server);
    WSACleanup();
    // printf("Socket closed.\n");

    return 0;
}
