#! /usr/bin/env python
# -*- coding: utf-8 -*

import iso as iso8583

qiandao="003C600450000060310031000008000020000000C00012000008363030303030303138373431313031343531313236313300110000005300400003303031"
a="008A60000000046022000000000210703A04810ED0801B186229093369942011102000000000000001000000091348480126012602200008100000013638353233323132393330353939383031323132363030303030303138373431313031343531313236313306796565706179313536000823000053001200058300000700034355504532453836443442"

b=iso8583.iso_8583("pos",a)
b.unpack()
b.ISO8583_testOutput()

c=b.pack()

#print a
print c
