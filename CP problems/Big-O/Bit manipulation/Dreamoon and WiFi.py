# import copy
#
# s = input()
# s1 = input()
#
# cnt = 0
# cnt1 = 0
#
# for i in s:
#     if i == '+':
#         cnt += 1
#     else:
#         cnt1 += 1
#
# for i in s1:
#
#     if i == '+':
#         cnt -= 1
#     elif i == '-':
#         cnt1 -= 1
# if cnt == cnt1 == 0:
#     print(1)
# elif min(cnt, cnt1) < 0:
#     print(0)
# else:
#     res = 0
#     cnt_1 = copy.deepcopy(cnt)
#     cnt_2 = copy.deepcopy(cnt1)
#     cnt_3 = cnt_1 + cnt_2
#     while cnt:
#         res |= 1
#         if cnt > 1:
#             res <<= 1
#         cnt -= 1
#
#     while cnt1:
#         res <<= 1
#         cnt1 -= 1
#     def count(a):
#         cnt = 0
#         cnt1 = 0
#         cnt2 = 0
#         while a:
#             if a & 1:
#                 cnt += 1
#             else:
#                 cnt1 += 1
#             cnt2 += 1
#             a >>= 1
#         return (cnt, cnt1, cnt2)
#     cnt2 = 0
#
#     for i in range(0, max(1, res+1)):
#
#         if i ^ res == 0:
#             cnt2 += 1
#
#         else:
#             b = count(i)
#             if  b[0] == cnt_1 or cnt_3 - b[0] == cnt_2 :
#                 cnt2 += 1
#
#             elif b[0] == cnt_3:
#                 cnt2 += 1
#
#             elif b[1] == cnt_3:
#                 cnt2 += 1
#
#     print(cnt2 / ( 2 ** cnt_3))
#
s1 = input()
s2 = input()
expected = 0
cases = 0
valid = 0
for c in s1:
	if c == '+': expected += 1
	else: expected -= 1

def recursive(z, val):
	global expected, cases, valid
	if z == len(s2):
		if val == expected: valid += 1
		cases += 1
		return
	if s2[z] != '-': recursive(z+1, val+1)
	if s2[z] != '+': recursive(z+1, val-1)

recursive(0, 0)
print('{:.10f}'.format(1.0 * valid / cases))