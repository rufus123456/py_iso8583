
def __gen_bitmap_list(bitmap):
    bitmap_list = []
    index = 1
    for x in bitmap:
        b = "%4s" % bin(int(x, 16))[2:]
        j = 0
        for y in b:
            if y == '1':
                bitmap_list.append(index + j)
            j += 1

        index += 4
    return bitmap_list

padding="0" if 2%2 else ""
print("1:",padding)

padding="0" if 3%2 else ""
print("2:",padding)

print("%04d" % 123)

print("%03d" % 123)