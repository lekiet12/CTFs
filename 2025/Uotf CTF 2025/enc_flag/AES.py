
class AES_implemented:
    rcon = ([0x01, 0, 0, 0], 
            [0x02, 0, 0, 0], 
            [0x04, 0, 0, 0], 
            [0x08, 0, 0, 0], 
            [0x10, 0, 0, 0], 
            [0x20, 0, 0, 0], 
            [0x40, 0, 0, 0], 
            [0x80, 0, 0, 0], 
            [0x1b, 0, 0, 0], 
            [0x36, 0, 0, 0])
            
    gf_mul_2 = (
        0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e, 
        0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e, 
        0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e, 0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e, 
        0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e, 0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e, 
        0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e, 0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e, 
        0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae, 0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe, 
        0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce, 0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde, 
        0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee, 0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe, 
        0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15, 0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05, 
        0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35, 0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25, 
        0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55, 0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45, 
        0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75, 0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65, 
        0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95, 0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85, 
        0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5, 0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5, 
        0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5, 0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5, 
        0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5, 0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5
    )
    
    gf_mul_3 = (
        0x00, 0x03, 0x06, 0x05, 0x0c, 0x0f, 0x0a, 0x09, 0x18, 0x1b, 0x1e, 0x1d, 0x14, 0x17, 0x12, 0x11, 
        0x30, 0x33, 0x36, 0x35, 0x3c, 0x3f, 0x3a, 0x39, 0x28, 0x2b, 0x2e, 0x2d, 0x24, 0x27, 0x22, 0x21, 
        0x60, 0x63, 0x66, 0x65, 0x6c, 0x6f, 0x6a, 0x69, 0x78, 0x7b, 0x7e, 0x7d, 0x74, 0x77, 0x72, 0x71, 
        0x50, 0x53, 0x56, 0x55, 0x5c, 0x5f, 0x5a, 0x59, 0x48, 0x4b, 0x4e, 0x4d, 0x44, 0x47, 0x42, 0x41, 
        0xc0, 0xc3, 0xc6, 0xc5, 0xcc, 0xcf, 0xca, 0xc9, 0xd8, 0xdb, 0xde, 0xdd, 0xd4, 0xd7, 0xd2, 0xd1, 
        0xf0, 0xf3, 0xf6, 0xf5, 0xfc, 0xff, 0xfa, 0xf9, 0xe8, 0xeb, 0xee, 0xed, 0xe4, 0xe7, 0xe2, 0xe1, 
        0xa0, 0xa3, 0xa6, 0xa5, 0xac, 0xaf, 0xaa, 0xa9, 0xb8, 0xbb, 0xbe, 0xbd, 0xb4, 0xb7, 0xb2, 0xb1, 
        0x90, 0x93, 0x96, 0x95, 0x9c, 0x9f, 0x9a, 0x99, 0x88, 0x8b, 0x8e, 0x8d, 0x84, 0x87, 0x82, 0x81, 
        0x9b, 0x98, 0x9d, 0x9e, 0x97, 0x94, 0x91, 0x92, 0x83, 0x80, 0x85, 0x86, 0x8f, 0x8c, 0x89, 0x8a, 
        0xab, 0xa8, 0xad, 0xae, 0xa7, 0xa4, 0xa1, 0xa2, 0xb3, 0xb0, 0xb5, 0xb6, 0xbf, 0xbc, 0xb9, 0xba, 
        0xfb, 0xf8, 0xfd, 0xfe, 0xf7, 0xf4, 0xf1, 0xf2, 0xe3, 0xe0, 0xe5, 0xe6, 0xef, 0xec, 0xe9, 0xea, 
        0xcb, 0xc8, 0xcd, 0xce, 0xc7, 0xc4, 0xc1, 0xc2, 0xd3, 0xd0, 0xd5, 0xd6, 0xdf, 0xdc, 0xd9, 0xda, 
        0x5b, 0x58, 0x5d, 0x5e, 0x57, 0x54, 0x51, 0x52, 0x43, 0x40, 0x45, 0x46, 0x4f, 0x4c, 0x49, 0x4a, 
        0x6b, 0x68, 0x6d, 0x6e, 0x67, 0x64, 0x61, 0x62, 0x73, 0x70, 0x75, 0x76, 0x7f, 0x7c, 0x79, 0x7a, 
        0x3b, 0x38, 0x3d, 0x3e, 0x37, 0x34, 0x31, 0x32, 0x23, 0x20, 0x25, 0x26, 0x2f, 0x2c, 0x29, 0x2a, 
        0x0b, 0x08, 0x0d, 0x0e, 0x07, 0x04, 0x01, 0x02, 0x13, 0x10, 0x15, 0x16, 0x1f, 0x1c, 0x19, 0x1a
    )
    
    gf_mul_9 = (
        0x00, 0x09, 0x12, 0x1b, 0x24, 0x2d, 0x36, 0x3f, 0x48, 0x41, 0x5a, 0x53, 0x6c, 0x65, 0x7e, 0x77, 
        0x90, 0x99, 0x82, 0x8b, 0xb4, 0xbd, 0xa6, 0xaf, 0xd8, 0xd1, 0xca, 0xc3, 0xfc, 0xf5, 0xee, 0xe7, 
        0x3b, 0x32, 0x29, 0x20, 0x1f, 0x16, 0x0d, 0x04, 0x73, 0x7a, 0x61, 0x68, 0x57, 0x5e, 0x45, 0x4c, 
        0xab, 0xa2, 0xb9, 0xb0, 0x8f, 0x86, 0x9d, 0x94, 0xe3, 0xea, 0xf1, 0xf8, 0xc7, 0xce, 0xd5, 0xdc, 
        0x76, 0x7f, 0x64, 0x6d, 0x52, 0x5b, 0x40, 0x49, 0x3e, 0x37, 0x2c, 0x25, 0x1a, 0x13, 0x08, 0x01, 
        0xe6, 0xef, 0xf4, 0xfd, 0xc2, 0xcb, 0xd0, 0xd9, 0xae, 0xa7, 0xbc, 0xb5, 0x8a, 0x83, 0x98, 0x91, 
        0x4d, 0x44, 0x5f, 0x56, 0x69, 0x60, 0x7b, 0x72, 0x05, 0x0c, 0x17, 0x1e, 0x21, 0x28, 0x33, 0x3a, 
        0xdd, 0xd4, 0xcf, 0xc6, 0xf9, 0xf0, 0xeb, 0xe2, 0x95, 0x9c, 0x87, 0x8e, 0xb1, 0xb8, 0xa3, 0xaa, 
        0xec, 0xe5, 0xfe, 0xf7, 0xc8, 0xc1, 0xda, 0xd3, 0xa4, 0xad, 0xb6, 0xbf, 0x80, 0x89, 0x92, 0x9b, 
        0x7c, 0x75, 0x6e, 0x67, 0x58, 0x51, 0x4a, 0x43, 0x34, 0x3d, 0x26, 0x2f, 0x10, 0x19, 0x02, 0x0b, 
        0xd7, 0xde, 0xc5, 0xcc, 0xf3, 0xfa, 0xe1, 0xe8, 0x9f, 0x96, 0x8d, 0x84, 0xbb, 0xb2, 0xa9, 0xa0, 
        0x47, 0x4e, 0x55, 0x5c, 0x63, 0x6a, 0x71, 0x78, 0x0f, 0x06, 0x1d, 0x14, 0x2b, 0x22, 0x39, 0x30, 
        0x9a, 0x93, 0x88, 0x81, 0xbe, 0xb7, 0xac, 0xa5, 0xd2, 0xdb, 0xc0, 0xc9, 0xf6, 0xff, 0xe4, 0xed, 
        0x0a, 0x03, 0x18, 0x11, 0x2e, 0x27, 0x3c, 0x35, 0x42, 0x4b, 0x50, 0x59, 0x66, 0x6f, 0x74, 0x7d, 
        0xa1, 0xa8, 0xb3, 0xba, 0x85, 0x8c, 0x97, 0x9e, 0xe9, 0xe0, 0xfb, 0xf2, 0xcd, 0xc4, 0xdf, 0xd6, 
        0x31, 0x38, 0x23, 0x2a, 0x15, 0x1c, 0x07, 0x0e, 0x79, 0x70, 0x6b, 0x62, 0x5d, 0x54, 0x4f, 0x46
    )
    
    gf_mul_11 = (
        0x00, 0x0b, 0x16, 0x1d, 0x2c, 0x27, 0x3a, 0x31, 0x58, 0x53, 0x4e, 0x45, 0x74, 0x7f, 0x62, 0x69, 
        0xb0, 0xbb, 0xa6, 0xad, 0x9c, 0x97, 0x8a, 0x81, 0xe8, 0xe3, 0xfe, 0xf5, 0xc4, 0xcf, 0xd2, 0xd9, 
        0x7b, 0x70, 0x6d, 0x66, 0x57, 0x5c, 0x41, 0x4a, 0x23, 0x28, 0x35, 0x3e, 0x0f, 0x04, 0x19, 0x12, 
        0xcb, 0xc0, 0xdd, 0xd6, 0xe7, 0xec, 0xf1, 0xfa, 0x93, 0x98, 0x85, 0x8e, 0xbf, 0xb4, 0xa9, 0xa2, 
        0xf6, 0xfd, 0xe0, 0xeb, 0xda, 0xd1, 0xcc, 0xc7, 0xae, 0xa5, 0xb8, 0xb3, 0x82, 0x89, 0x94, 0x9f, 
        0x46, 0x4d, 0x50, 0x5b, 0x6a, 0x61, 0x7c, 0x77, 0x1e, 0x15, 0x08, 0x03, 0x32, 0x39, 0x24, 0x2f, 
        0x8d, 0x86, 0x9b, 0x90, 0xa1, 0xaa, 0xb7, 0xbc, 0xd5, 0xde, 0xc3, 0xc8, 0xf9, 0xf2, 0xef, 0xe4, 
        0x3d, 0x36, 0x2b, 0x20, 0x11, 0x1a, 0x07, 0x0c, 0x65, 0x6e, 0x73, 0x78, 0x49, 0x42, 0x5f, 0x54, 
        0xf7, 0xfc, 0xe1, 0xea, 0xdb, 0xd0, 0xcd, 0xc6, 0xaf, 0xa4, 0xb9, 0xb2, 0x83, 0x88, 0x95, 0x9e, 
        0x47, 0x4c, 0x51, 0x5a, 0x6b, 0x60, 0x7d, 0x76, 0x1f, 0x14, 0x09, 0x02, 0x33, 0x38, 0x25, 0x2e, 
        0x8c, 0x87, 0x9a, 0x91, 0xa0, 0xab, 0xb6, 0xbd, 0xd4, 0xdf, 0xc2, 0xc9, 0xf8, 0xf3, 0xee, 0xe5, 
        0x3c, 0x37, 0x2a, 0x21, 0x10, 0x1b, 0x06, 0x0d, 0x64, 0x6f, 0x72, 0x79, 0x48, 0x43, 0x5e, 0x55, 
        0x01, 0x0a, 0x17, 0x1c, 0x2d, 0x26, 0x3b, 0x30, 0x59, 0x52, 0x4f, 0x44, 0x75, 0x7e, 0x63, 0x68, 
        0xb1, 0xba, 0xa7, 0xac, 0x9d, 0x96, 0x8b, 0x80, 0xe9, 0xe2, 0xff, 0xf4, 0xc5, 0xce, 0xd3, 0xd8, 
        0x7a, 0x71, 0x6c, 0x67, 0x56, 0x5d, 0x40, 0x4b, 0x22, 0x29, 0x34, 0x3f, 0x0e, 0x05, 0x18, 0x13, 
        0xca, 0xc1, 0xdc, 0xd7, 0xe6, 0xed, 0xf0, 0xfb, 0x92, 0x99, 0x84, 0x8f, 0xbe, 0xb5, 0xa8, 0xa3
    )
    
    gf_mul_13 = (
        0x00, 0x0d, 0x1a, 0x17, 0x34, 0x39, 0x2e, 0x23, 0x68, 0x65, 0x72, 0x7f, 0x5c, 0x51, 0x46, 0x4b, 
        0xd0, 0xdd, 0xca, 0xc7, 0xe4, 0xe9, 0xfe, 0xf3, 0xb8, 0xb5, 0xa2, 0xaf, 0x8c, 0x81, 0x96, 0x9b, 
        0xbb, 0xb6, 0xa1, 0xac, 0x8f, 0x82, 0x95, 0x98, 0xd3, 0xde, 0xc9, 0xc4, 0xe7, 0xea, 0xfd, 0xf0, 
        0x6b, 0x66, 0x71, 0x7c, 0x5f, 0x52, 0x45, 0x48, 0x03, 0x0e, 0x19, 0x14, 0x37, 0x3a, 0x2d, 0x20, 
        0x6d, 0x60, 0x77, 0x7a, 0x59, 0x54, 0x43, 0x4e, 0x05, 0x08, 0x1f, 0x12, 0x31, 0x3c, 0x2b, 0x26, 
        0xbd, 0xb0, 0xa7, 0xaa, 0x89, 0x84, 0x93, 0x9e, 0xd5, 0xd8, 0xcf, 0xc2, 0xe1, 0xec, 0xfb, 0xf6, 
        0xd6, 0xdb, 0xcc, 0xc1, 0xe2, 0xef, 0xf8, 0xf5, 0xbe, 0xb3, 0xa4, 0xa9, 0x8a, 0x87, 0x90, 0x9d, 
        0x06, 0x0b, 0x1c, 0x11, 0x32, 0x3f, 0x28, 0x25, 0x6e, 0x63, 0x74, 0x79, 0x5a, 0x57, 0x40, 0x4d, 
        0xda, 0xd7, 0xc0, 0xcd, 0xee, 0xe3, 0xf4, 0xf9, 0xb2, 0xbf, 0xa8, 0xa5, 0x86, 0x8b, 0x9c, 0x91, 
        0x0a, 0x07, 0x10, 0x1d, 0x3e, 0x33, 0x24, 0x29, 0x62, 0x6f, 0x78, 0x75, 0x56, 0x5b, 0x4c, 0x41, 
        0x61, 0x6c, 0x7b, 0x76, 0x55, 0x58, 0x4f, 0x42, 0x09, 0x04, 0x13, 0x1e, 0x3d, 0x30, 0x27, 0x2a, 
        0xb1, 0xbc, 0xab, 0xa6, 0x85, 0x88, 0x9f, 0x92, 0xd9, 0xd4, 0xc3, 0xce, 0xed, 0xe0, 0xf7, 0xfa, 
        0xb7, 0xba, 0xad, 0xa0, 0x83, 0x8e, 0x99, 0x94, 0xdf, 0xd2, 0xc5, 0xc8, 0xeb, 0xe6, 0xf1, 0xfc, 
        0x67, 0x6a, 0x7d, 0x70, 0x53, 0x5e, 0x49, 0x44, 0x0f, 0x02, 0x15, 0x18, 0x3b, 0x36, 0x21, 0x2c, 
        0x0c, 0x01, 0x16, 0x1b, 0x38, 0x35, 0x22, 0x2f, 0x64, 0x69, 0x7e, 0x73, 0x50, 0x5d, 0x4a, 0x47, 
        0xdc, 0xd1, 0xc6, 0xcb, 0xe8, 0xe5, 0xf2, 0xff, 0xb4, 0xb9, 0xae, 0xa3, 0x80, 0x8d, 0x9a, 0x97
    )
    
    gf_mul_14 = (
        0x00, 0x0e, 0x1c, 0x12, 0x38, 0x36, 0x24, 0x2a, 0x70, 0x7e, 0x6c, 0x62, 0x48, 0x46, 0x54, 0x5a, 
        0xe0, 0xee, 0xfc, 0xf2, 0xd8, 0xd6, 0xc4, 0xca, 0x90, 0x9e, 0x8c, 0x82, 0xa8, 0xa6, 0xb4, 0xba, 
        0xdb, 0xd5, 0xc7, 0xc9, 0xe3, 0xed, 0xff, 0xf1, 0xab, 0xa5, 0xb7, 0xb9, 0x93, 0x9d, 0x8f, 0x81, 
        0x3b, 0x35, 0x27, 0x29, 0x03, 0x0d, 0x1f, 0x11, 0x4b, 0x45, 0x57, 0x59, 0x73, 0x7d, 0x6f, 0x61, 
        0xad, 0xa3, 0xb1, 0xbf, 0x95, 0x9b, 0x89, 0x87, 0xdd, 0xd3, 0xc1, 0xcf, 0xe5, 0xeb, 0xf9, 0xf7, 
        0x4d, 0x43, 0x51, 0x5f, 0x75, 0x7b, 0x69, 0x67, 0x3d, 0x33, 0x21, 0x2f, 0x05, 0x0b, 0x19, 0x17, 
        0x76, 0x78, 0x6a, 0x64, 0x4e, 0x40, 0x52, 0x5c, 0x06, 0x08, 0x1a, 0x14, 0x3e, 0x30, 0x22, 0x2c, 
        0x96, 0x98, 0x8a, 0x84, 0xae, 0xa0, 0xb2, 0xbc, 0xe6, 0xe8, 0xfa, 0xf4, 0xde, 0xd0, 0xc2, 0xcc, 
        0x41, 0x4f, 0x5d, 0x53, 0x79, 0x77, 0x65, 0x6b, 0x31, 0x3f, 0x2d, 0x23, 0x09, 0x07, 0x15, 0x1b, 
        0xa1, 0xaf, 0xbd, 0xb3, 0x99, 0x97, 0x85, 0x8b, 0xd1, 0xdf, 0xcd, 0xc3, 0xe9, 0xe7, 0xf5, 0xfb, 
        0x9a, 0x94, 0x86, 0x88, 0xa2, 0xac, 0xbe, 0xb0, 0xea, 0xe4, 0xf6, 0xf8, 0xd2, 0xdc, 0xce, 0xc0, 
        0x7a, 0x74, 0x66, 0x68, 0x42, 0x4c, 0x5e, 0x50, 0x0a, 0x04, 0x16, 0x18, 0x32, 0x3c, 0x2e, 0x20, 
        0xec, 0xe2, 0xf0, 0xfe, 0xd4, 0xda, 0xc8, 0xc6, 0x9c, 0x92, 0x80, 0x8e, 0xa4, 0xaa, 0xb8, 0xb6, 
        0x0c, 0x02, 0x10, 0x1e, 0x34, 0x3a, 0x28, 0x26, 0x7c, 0x72, 0x60, 0x6e, 0x44, 0x4a, 0x58, 0x56, 
        0x37, 0x39, 0x2b, 0x25, 0x0f, 0x01, 0x13, 0x1d, 0x47, 0x49, 0x5b, 0x55, 0x7f, 0x71, 0x63, 0x6d, 
        0xd7, 0xd9, 0xcb, 0xc5, 0xef, 0xe1, 0xf3, 0xfd, 0xa7, 0xa9, 0xbb, 0xb5, 0x9f, 0x91, 0x83, 0x8d
    )
    
    sbox =  (
        117, 147, 8, 226, 253, 254, 14, 191, 255, 23, 31, 89, 111, 175, 19, 160, 102, 173, 133, 47, 43, 104, 156, 59, 95, 177, 186, 20, 35, 159, 195, 204, 83, 75, 139, 215, 53, 84, 164, 40, 194, 30, 50, 51, 25, 150, 221, 122, 171, 222, 91, 11, 15, 68, 148, 236, 245, 4, 52, 158, 196, 197, 48, 179, 32, 109, 130, 123, 131, 161, 146, 67, 27, 124, 178, 180, 183, 55, 13, 38, 7, 71, 143, 172, 63, 193, 207, 60, 217, 18, 103, 105, 155, 37, 9, 116, 163, 176, 187, 66, 62, 79, 24, 208, 5, 125, 41, 45, 85, 127, 129, 113, 90, 10, 76, 3, 118, 39, 87, 28, 99, 107, 115, 26, 119, 135, 93, 151, 97, 17, 33, 153, 88, 157, 12, 162, 140, 56, 167, 108, 166, 192, 86, 199, 70, 81, 73, 182, 29, 200, 72, 201, 46, 61, 82, 128, 65, 80, 64, 112, 142, 100, 69, 134, 202, 22, 174, 181, 0, 126, 44, 184, 185, 189, 190, 138, 203, 209, 210, 211, 98, 110, 120, 121, 137, 132, 54, 213, 218, 206, 168, 219, 220, 58, 57, 223, 154, 224, 225, 227, 42, 229, 230, 114, 49, 231, 6, 92, 136, 106, 170, 233, 144, 235, 78, 238, 239, 205, 240, 36, 74, 2, 77, 234, 241, 243, 21, 169, 149, 244, 101, 198, 94, 165, 141, 216, 232, 237, 242, 16, 246, 214, 34, 212, 145, 247, 248, 249, 250, 1, 228, 96, 251, 188, 252, 152
    )
    
    sbox_inv = (
        168, 249, 221, 115, 57, 104, 206, 80, 2, 94, 113, 51, 134, 78, 6, 52, 239, 129, 89, 14, 27, 226, 165, 9, 102, 44, 123, 72, 119, 148, 41, 10, 64, 130, 242, 28, 219, 93, 79, 117, 39, 106, 200, 20, 170, 107, 152, 19, 62, 204, 42, 43, 58, 36, 186, 77, 137, 194, 193, 23, 87, 153, 100, 84, 158, 156, 99, 71, 53, 162, 144, 81, 150, 146, 220, 33, 114, 222, 214, 101, 157, 145, 154, 32, 37, 108, 142, 118, 132, 11, 112, 50, 207, 126, 232, 24, 251, 128, 180, 120, 161, 230, 16, 90, 21, 91, 209, 121, 139, 65, 181, 12, 159, 111, 203, 122, 95, 0, 116, 124, 182, 183, 47, 67, 73, 105, 169, 109, 155, 110, 66, 68, 185, 18, 163, 125, 208, 184, 175, 34, 136, 234, 160, 82, 212, 244, 70, 1, 54, 228, 45, 127, 255, 131, 196, 92, 22, 133, 59, 29, 15, 69, 135, 96, 38, 233, 140, 138, 190, 227, 210, 48, 83, 17, 166, 13, 97, 25, 74, 63, 75, 167, 147, 76, 171, 172, 26, 98, 253, 173, 174, 7, 141, 85, 40, 30, 60, 61, 231, 143, 149, 151, 164, 176, 31, 217, 189, 86, 103, 177, 178, 179, 243, 187, 241, 35, 235, 88, 188, 191, 192, 46, 49, 195, 197, 198, 3, 199, 250, 201, 202, 205, 236, 211, 223, 213, 55, 237, 215, 216, 218, 224, 238, 225, 229, 56, 240, 245, 246, 247, 248, 252, 254, 4, 5, 8
    )
    
    def __init__(self, key):
        assert isinstance(key, bytes) and len(key) == 16
        self._block_size = 16
        self._round = 10
        self._round_keys = self._expand_key(key)
        self._state = []
        
    def _transpose(self, m):
        return [m[4 * j + i] for i in range(4) for j in range(4)]
        
    def _xor(self, a, b):
        return [x ^ y for x, y in zip(a, b)]
        
    def _expand_key(self, key):
        round_keys = [[c for c in key]]
        for round_n in range(self._round):
            prev_round_key = round_keys[round_n]
            round_key = prev_round_key[-4:]
            round_key = round_key[1:] + round_key[:1]
            round_key = [self.sbox[i] for i in round_key]
            round_key = self._xor(
                self._xor(round_key, prev_round_key[:4]), self.rcon[round_n]
            )
            for i in range(0, 12, 4):
                round_key += self._xor(round_key[i : i + 4], prev_round_key[i + 4 : i + 8])
            round_keys.append(round_key)
            
        for round_n in range(self._round + 1):
            round_keys[round_n] = self._transpose(round_keys[round_n])
            
        return round_keys
        
    def _add_round_key(self, round_n):
        self._state = self._xor(self._state, self._round_keys[round_n])
        
    def _sub_bytes(self):
        self._state = [self.sbox[c] for c in self._state]
        
    def _sub_bytes_inv(self):
        self._state = [self.sbox_inv[c] for c in self._state]
        
    def _shift_rows(self):
        self._state = [
            self._state[0], self._state[1], self._state[2], self._state[3],
            self._state[5], self._state[6], self._state[7], self._state[4],
            self._state[10], self._state[11], self._state[8], self._state[9],
            self._state[15], self._state[12], self._state[13], self._state[14]
        ]
        
    def _shift_rows_inv(self):
        self._state = [
            self._state[0], self._state[1], self._state[2], self._state[3],
            self._state[7], self._state[4], self._state[5], self._state[6],
            self._state[10], self._state[11], self._state[8], self._state[9],
            self._state[13], self._state[14], self._state[15], self._state[12]
        ]
        
    def _mix_columns(self):
        s = [0] * self._block_size
        for i in range(4):
            s[i] = self.gf_mul_2[self._state[i]] ^ self.gf_mul_3[self._state[i + 4]] ^ self._state[i + 8] ^ self._state[i + 12]
            s[i + 4] = self._state[i] ^ self.gf_mul_2[self._state[i + 4]] ^ self.gf_mul_3[self._state[i + 8]] ^ self._state[i + 12]
            s[i + 8] = self._state[i] ^ self._state[i + 4] ^ self.gf_mul_2[self._state[i + 8]] ^ self.gf_mul_3[self._state[i + 12]]
            s[i + 12] = self.gf_mul_3[self._state[i]] ^ self._state[i + 4] ^ self._state[i + 8] ^ self.gf_mul_2[self._state[i + 12]]
        self._state = s
        
    def _mix_columns_inv(self):
        s = [0] * self._block_size
        for i in range(4):
            s[i] = self.gf_mul_14[self._state[i]] ^ self.gf_mul_11[self._state[i + 4]] ^ self.gf_mul_13[self._state[i + 8]] ^ self.gf_mul_9[self._state[i + 12]]
            s[i + 4] = self.gf_mul_9[self._state[i]] ^ self.gf_mul_14[self._state[i + 4]] ^ self.gf_mul_11[self._state[i + 8]] ^ self.gf_mul_13[self._state[i + 12]]
            s[i + 8] = self.gf_mul_13[self._state[i]] ^ self.gf_mul_9[self._state[i + 4]] ^ self.gf_mul_14[self._state[i + 8]] ^ self.gf_mul_11[self._state[i + 12]]
            s[i + 12] = self.gf_mul_11[self._state[i]] ^ self.gf_mul_13[self._state[i + 4]] ^ self.gf_mul_9[self._state[i + 8]] ^ self.gf_mul_14[self._state[i + 12]]
        self._state = s
        
    def _encrypt(self, plaintext):
        self._state = self._transpose(plaintext)
        
        self._add_round_key(0)
        for round_n in range(1, self._round):
            self._sub_bytes()
            self._shift_rows()
            self._mix_columns()
            self._add_round_key(round_n)
        self._sub_bytes()
        self._shift_rows()
        self._add_round_key(self._round)
        
        return bytes(self._transpose(self._state))
        
    def _decrypt(self, ciphertext):
        self._state = self._transpose(ciphertext)
        
        self._add_round_key(self._round)
        self._shift_rows_inv()
        self._sub_bytes_inv()
        for round_n in range(self._round - 1, 0, -1):
            self._add_round_key(round_n)
            self._mix_columns_inv()
            self._shift_rows_inv()
            self._sub_bytes_inv()
        self._add_round_key(0)
        
        return bytes(self._transpose(self._state))
        
    def encrypt(self, plaintext):
        assert len(plaintext) % self._block_size == 0
        
        ciphertext = b''
        for i in range(0, len(plaintext), self._block_size):
            ciphertext += self._encrypt(plaintext[i : i + self._block_size])
        return ciphertext
        
    def decrypt(self, ciphertext):
        assert len(ciphertext) % self._block_size == 0
        
        plaintext = b''
        for i in range(0, len(ciphertext), self._block_size):
            plaintext += self._decrypt(ciphertext[i : i + self._block_size])
        return plaintext
        
        
if __name__ == '__main__':
    ciphertext = [150, 20, 145, 213, 26, 179, 49, 243, 137, 165, 161, 85, 61, 116, 78, 201, 230, 5, 134, 127, 113, 63, 68, 16, 230, 80, 222, 26, 73, 32, 53, 170]
    key = [0x57, 0x2D, 0xAF, 0x32, 0x00, 0x00, 0x00, 0x00, 0x4A, 0x0A, 
  0x27, 0x7E, 0x00, 0x00, 0x00, 0x00]
    plaintext = AES_implemented(bytes(key)).decrypt(bytes(ciphertext))
    print(plaintext)
# b'uoftctf{175_ju57_435_bu7_w0r53}\xc9'