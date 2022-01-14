#! /usr/bin/env python
# -*- coding: utf-8 -*

class deal_content_type:
    __charset = "UTF-8"

    def __init__(self, charset="UTF-8"):
        self.__charset = charset

    # 输入data(hex)，len(声明)长度
    def LF_BCD_unpack(self,data,len,offset):
        len=len
        padding=1 if len%2 else 0
        return (data[offset+padding:offset+len+padding],len+padding)

    # 输入data(hex)，len(声明)长度
    def RF_BCD_unpack(self,data,len,offset):
        len=len
        padding=1 if len%2 else 0
        return (data[offset:offset+len],len+padding)

    # 输入data(hex)，len(声明)长度
    def BINARY_unpack(self, data, len, offset):
        len = int(len*2)
        return (data[offset:offset + len], len)

    # 输入data(hex)，len(声明)长度
    def ASCII_unpack(self,data,len,offset):
        len=int(len*2)
        bys = bytearray.fromhex(data[offset:offset + len])
        return (str(bys,self.__charset),len)

    # 输入data(hex)，len(声明)长度，hex展开存储，应用于LLVAR、LLLVAR
    def ASCII_HEX_unpack(self,data,len,offset):
        len=int(len*2)
        return (data[offset:offset+len],len)

    #pack
    def LF_BCD_pack(self,data):
        data_len=len(data)
        padding="0" if data_len%2 else ""
        d_data = padding + data
        return d_data

    def RF_BCD_pack(self,data):
        data_len=len(data)
        padding="0" if data_len%2 else ""
        d_data = data + padding
        return d_data

    def BINARY_pack(self, data):
        return data

    def ASCII_pack(self,data):
        bys = bytes(data, self.__charset)
        return bys.hex()

    # 输入data(hex)，hex展开存储，应用于LLVAR、LLLVAR
    def ASCII_HEX_pack(self,data):
        return data

class deal_len_type:
    __charset = "UTF-8"

    def __init__(self, charset="UTF-8"):
        self.__charset = charset

    # 返回数据(声明)长度、len(hex)长度
    def fixed_unpack(self,cfg,data,offset,tag):
        return (cfg["max_len"],0)

    # 返回数据(声明)长度、len(hex)长度
    def BINARY_unpack(self,cfg,data,offset,tag):
        return (cfg["max_len"]/8,0)

    # 返回数据(声明)长度、len(hex)长度
    def LLVAR_unpack(self,cfg,data,offset,tag):
        len = 2
        data_len=int(data[offset:offset+len])
        assert data_len <= 99,tag+" LLVAR len err"
        return (data_len,len)

    # 返回数据(声明)长度、len(hex)长度
    def LLVAR_ASC_unpack(self,cfg,data,offset,tag):
        len = 2*2
        bys = bytearray.fromhex(data[offset:offset + len])
        data_len = int(str(bys, self.__charset))
        assert data_len <= 99,tag+" LLVAR len err"
        return (data_len,len)

    # 返回数据(声明)长度、len(hex)长度
    def LLLVAR_unpack(self,cfg,data,offset,tag):
        len = 2*2
        data_len=int(data[offset:offset+len])
        assert data_len <= 999,tag+" LLLVAR len err"
        return (data_len,len)

    # 返回数据(声明)长度、len(hex)长度
    def LLLVAR_ASC_unpack(self,cfg,data,offset,tag):
        len = 3*2
        bys = bytearray.fromhex(data[offset:offset + len])
        data_len=int(str(bys, self.__charset))
        assert data_len <= 999,tag+" LLLVAR len err"
        return (data_len,len)

    #pack
    # 输入data(hex)，输出data(hex)
    def fixed_pack(self,cfg,data,tag):
        max_len = cfg["max_len"]
        data_len = len(data)
        if cfg["content_type"]=="ASCII_HEX" :
            data_len = len(data)/2
        assert data_len == max_len,tag+" fixed len err"
        len_val = ""
        return len_val

    # 输入data(hex)，输出data(hex)
    def BINARY_pack(self,cfg,data,tag):
        max_len = cfg["max_len"]
        data_len = len(data)
        # set hex 故data长度的4倍是定义长度
        assert data_len*4 == max_len,tag+" BINARY len err"
        len_val = ""
        return len_val

    # 输入data(hex)，输出data(hex)
    def LLVAR_pack(self,cfg,data,tag):
        max_len = cfg["max_len"]
        data_len = len(data)
        if cfg["content_type"]=="ASCII_HEX":
            data_len = len(data)/2
        assert data_len <= max_len,tag+" LLVAR len err"
        len_val = "%02d" % data_len
        return len_val

    def LLVAR_ASC_pack(self,cfg,data,tag):
        max_len = cfg["max_len"]
        data_len = len(data)
        if cfg["content_type"]=="ASCII_HEX":
            data_len = len(data)/2
        assert data_len <= max_len,tag+" LLVAR len err"
        bys = bytes(("%02d" % data_len), self.__charset)
        return bys.hex()
    
    def LLLVAR_pack(self,cfg,data,tag):
        max_len = cfg["max_len"]
        data_len = len(data)
        if cfg["content_type"] == "ASCII_HEX":
            data_len = len(data) / 2
        assert data_len <= max_len,tag+" LLLVAR len err"
        len_val = "%04d" % data_len
        return len_val

    def LLLVAR_ASC_pack(self,cfg,data,tag):
        max_len = cfg["max_len"]
        data_len = len(data)
        if cfg["content_type"]=="ASCII_HEX":
            data_len = len(data)/2
        assert data_len <= max_len,tag+" LLLVAR len err"
        bys = bytes(("%03d" % data_len), self.__charset)
        return bys.hex()
