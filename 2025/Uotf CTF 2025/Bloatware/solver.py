#!/usr/bin/env python3

import re
from z3 import *
import random

'''
A = BitVec('A', 32)
B = BitVec('B', 32)
C = BitVec('C', 32)

def simplify_l(l):
	expression = l
	args = get_args_list(expression)
	if len(args) == 3:
		a, b, c = args
	elif len(args) == 2:
		a, b, = args
		c = 'nevergonnagiveyouup'
	else:
		assert False
	expression = expression.replace(a, 'A').replace(b, 'B').replace(c, 'C')
	simplified = str(simplify(eval(expression))).replace('\n', '')
	if '...' not in simplified: # no folding
		if len(simplified) < 20: # should be simple
			try:
				eval(simplified) # no grammer error
				l = simplified.replace('A', a).replace('B', b).replace('C', c)
			except:
				pass
	return l
'''

def proof_constant(expression, proof_count=32): # maybe enough
	args = get_args_list(expression)
	assert len(args) <= 2
	if len(args) == 2:
		a, b = args
	else:
		a, = args
		b = 'nevergonnagiveyouup'
	expression = expression.replace(a, 'A').replace(b, 'B')
	# z3 too slow!!!
	'''
	expression = eval(expression)
	solver = Solver()
	solver.add(expression != 0)
	if solver.check() == unsat: return 0
	model = solver.model()
	v = model.eval(expression).as_long()
	'''
	v = None
	for i in range(proof_count + 1):
		A = random.randrange(1<<32)
		B = random.randrange(1<<32)
		v_r = eval(expression, {'A': A, 'B': B})
		if v == None: v = v_r
		else: assert v == v_r, expression
	return v

def get_args_list(expression):
	return set(re.findall('_0x2a129d\[0x[0-9a-f]+\]', expression))

def remove_bracket(s):
	# don't remove brackets!!!!!
	# while s[0] == '(' and search_right_bracket(s, 0) == len(s) - 1:
	# 	s = s[1: -1]
	return s

def parse_add_elems(s):
	t = []
	t_expr = []
	t_args = set()
	for r in s:
		s_args = get_args_list(r)
		if len(s_args) > 2:
			if t_args.issubset(s_args):
				t_expr.append(r)
				t_args |= s_args
			else:
				t.append(remove_bracket('+'.join(t_expr)))
				t_expr = [r]
				t_args = s_args
		elif len(t_args | s_args) <= 2 or s_args.issubset(t_args):
			t_expr.append(r)
			t_args |= s_args
		else:
			t.append(remove_bracket('+'.join(t_expr)))
			t_expr = [r]
			t_args = s_args
	if t_expr:
		t.append(remove_bracket('+'.join(t_expr)))
	return t

def search_right_bracket(s, left):
	assert s[left] == '('
	right = left + 1
	count = 1
	while count:
		if s[right] == '(': count += 1
		elif s[right] == ')': count -= 1
		right += 1
	assert s[right - 1] == ')'
	return right - 1

def split_add_expr(s):
	assert s[0] != '+'
	t = []
	i = 0
	left = i
	while True:
		if s[i] == '(':
			i = search_right_bracket(s, i)
		elif s[i] == ')':
			assert False
		elif s[i] == '+':
			t.append(s[left: i])
			left = i + 1
		i += 1
		if i == len(s):
			t.append(s[left: i])
			break
	return parse_add_elems(t)

def split_lr_add_expr(s):
	sl, sr = s.split('==')
	l = split_add_expr(sl)
	assert '+'.join(l) == sl
	r = split_add_expr(sr)
	assert '+'.join(r) == sr
	return l, r

def parse_lr_expr(s):
	ls, rs = split_lr_add_expr(s)
	l = None
	for i in ls:
		if len(get_args_list(i)) > 2:
			if l == None:
				l = i
			else:
				args_l = get_args_list(l)
				args_i = get_args_list(i)
				assert len(args_i | args_l) == 3
				l = l + '+' + i
		else:
			v = None
			try:
				v = proof_constant(i)
			except:
				pass
			if v != None:
				assert v == 0
			else:
				if l == None:
					l = i
				else:
					args_l = get_args_list(l)
					args_i = get_args_list(i)
					assert len(args_i | args_l) == 3
					l = l + '+' + i
	r = 0
	for i in rs:
		r += proof_constant(i)
	# return simplify_l(l), r
	return l, r

lrs = []

# filename = 'conds.js'
# lines = open(filename, 'r').read().splitlines()

filename = 'chal.js'
chal_js = open(filename, 'r').read()
start = chal_js.index('conds=[') + 7
end = chal_js.index('];return', start)
lines = chal_js[start: end].split(',')

for i in range(len(lines)):
	line = lines[i]
	print('%d/%d' % (i, len(lines)))
	# if line[0] == '\t':
	# 	assert line[-1] == ','
	# 	lrs.append(parse_lr_expr(line.strip()[: -1]))
	lrs.append(parse_lr_expr(line))

# now we can use z3 to solve equations
_0x2a129d = [BitVec('x%d' % i, 32) for i in range(0x79e)]
solver = Solver()
for i in range(len(lrs)):
	l, r = lrs[i]
	equation = f'{l} == {r}'
	# print(f'{i}/{len(lrs)}: {equation}')
	print(f'{i}/{len(lrs)}')
	solver.add(eval(equation))

print('solving...')
assert solver.check() == sat
print('solved')
model = solver.model()
# print(model)

values = [model[i].as_long() for i in _0x2a129d]
flag = bytes(i & 0xff for i in values)
print(flag)

# b"uoftctf{b104tw4r3_b17wiz3_4nd_3v41_1z_s0_s1mpl3_bu7_z3_15_700_sl0w_2_s0lv3_lm40_unl3zz_y0u_s1mpl1fy_th0z3_MBAz_bec4uz3_th3r3_ar3_ju57_t00_m4ny_v4r14bl3z_XDDDDDDD_n0w_t1me_f0r_a_buNcH_0f_b34ut1fu1_1yr1c5_w3'r3_n0_57r4n63r5_70_l0v3_y0u_kn0w_7h3_rul35_4nd_50_d0_1_4_full_c0mm17m3n7'5_wh47_1'4m_7h1nk1n6_0f_y0u_w0uldn'7_637_7h15_fr0m_4ny_07h3r_6uy_1_ju57_w4nn4_73ll_y0u_h0w_1'4m_f33l1n6_60774_m4k3_y0u_und3r574nd_n3v3r_60nn4_61v3_y0u_up_n3v3r_60nn4_l37_y0u_d0wn_n3v3r_60nn4_run_4r0und_4nd_d353r7_y0u_n3v3r_60nn4_m4k3_y0u_cry_n3v3r_60nn4_54y_600dby3_n3v3r_60nn4_73ll_4_l13_4nd_hur7_y0u_w3'v3_kn0wn_34ch_07h3r_f0r_50_l0n6_y0ur_h34r7'5_b33n_4ch1n6,_bu7_y0u'r3_700_5hy_70_54y_17_1n51d3,_w3_b07h_kn0w_wh47'5_b33n_601n6_0n_w3_kn0w_7h3_64m3_4nd_w3'r3_60nn4_pl4y_17_4nd_1f_y0u_45k_m3_h0w_1'4m_f33l1n6_d0n'7_73ll_m3_y0u'r3_700_bl1nd_70_533_n3v3r_60nn4_61v3_y0u_up_n3v3r_60nn4_l37_y0u_d0wn_n3v3r_60nn4_run_4r0und_4nd_d353r7_y0u_n3v3r_60nn4_m4k3_y0u_cry_n3v3r_60nn4_54y_600dby3_n3v3r_60nn4_73ll_4_l13_4nd_hur7_y0u_n3v3r_60nn4_61v3_y0u_up_n3v3r_60nn4_l37_y0u_d0wn_n3v3r_60nn4_run_4r0und_4nd_d353r7_y0u_n3v3r_60nn4_m4k3_y0u_cry_n3v3r_60nn4_54y_600dby3_n3v3r_60nn4_73ll_4_l13_4nd_hur7_y0u_w3'v3_kn0wn_34ch_07h3r_f0r_50_l0n6_y0ur_h34r7'5_b33n_4ch1n6,_bu7_y0u'r3_700_5hy_70_54y_17_1n51d3,_w3_b07h_kn0w_wh47'5_b33n_601n6_0n_w3_kn0w_7h3_64m3_4nd_w3'r3_60nn4_pl4y_17_1_ju57_w4nn4_73ll_y0u_h0w_1'4m_f33l1n6_60774_m4k3_y0u_und3r574nd_n3v3r_60nn4_61v3_y0u_up_n3v3r_60nn4_l37_y0u_d0wn_n3v3r_60nn4_run_4r0und_4nd_d353r7_y0u_n3v3r_60nn4_m4k3_y0u_cry_n3v3r_60nn4_54y_600dby3_n3v3r_60nn4_73ll_4_l13_4nd_hur7_y0u_n3v3r_60nn4_61v3_y0u_up_n3v3r_60nn4_l37_y0u_d0wn_n3v3r_60nn4_run_4r0und_4nd_d353r7_y0u_n3v3r_60nn4_m4k3_y0u_cry_n3v3r_60nn4_54y_600dby3_n3v3r_60nn4_73ll_4_l13_4nd_hur7_y0u_n3v3r_60nn4_61v3_y0u_up_n3v3r_60nn4_l37_y0u_d0wn_n3v3r_60nn4_run_4r0und_4nd_d353r7_y0u_n3v3r_60nn4_m4k3_y0u_cry_n3v3r_60nn4_54y_600dby3_n3v3r_60nn4_73ll_4_l13_4nd_hur7_y0u_w0w_y0u_r3411y_d1d_17?!}\xaf"