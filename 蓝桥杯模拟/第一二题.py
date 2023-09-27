# aci = [0] * 256
#
# for i in list(input()):
#     aci[ord(i)] += 1
#
# res = ''
# for i in range(0, 256):
#     while aci[i] > 0:
#        res = res + chr(i)
#        aci[i]-=1
#
# print(res)  ## 结果： AAAEEEEEEHHHIIILLRRRSSTTWWWY

i=1
while 187*i%33 !=11 or 187*i%34 !=17 or 187*i%41!=1 or 187*i%39!=23 or 187*i%29!=16 or 187*i%31!=27 or 187*i%37 !=22:
    i+=1
print(i * 187)   ## 26777207 * 187 =5007337709
print(187*i%39==23)




