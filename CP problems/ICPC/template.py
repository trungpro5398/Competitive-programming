import queue


def factorise(m):
	ans = []
	p = 2
	while(m != 1):
		if (m%p != 0):
			p += 1
			continue
		e = 0
		while(m % p == 0) :
			m //= p
			e += 1
		ans.append([p, e])
		p += 1
	return ans

def mulmod(a, b, c):
	res = a * b
	if (res >= c):
		res %= c
	return res


def expo(a, b):
	x = 1
	y = a
	while(b > 0):
		if (b&1):
			x = x * y
		y = y * y
		b >>= 1
	return x

def power(a, b, c):
	x = 1
	y = a
	while(b > 0):
		if (b&1):
			x = mulmod(x, y, c)
		y = mulmod(y, y, c)
		b >>= 1
	return x

def init(p, pk):
	fact = []
	fact.append(1)
	for i in range(1, pk):
		red = i
		if (red % p == 0):
			red = 1
		fact.append(mulmod(fact[i-1], red, pk))
	return fact

def fact_mod(n, p, pk, fact):
	res = 1
	while(n > 0):
		times = n//pk
		res = mulmod(res, power(fact[pk-1], times, pk), pk)
		res = mulmod(res, fact[n%pk], pk)
		n //= p
	return res

def count_fact(n, p):
	ans = 0
	while(n > 0):
		ans += n//p
		n //= p
	return ans

def ncr_pk(n, r, p, e):
	if (r > n or r < 0):
		return 0
	if (r == 0 or n == r):
		return 1
	_e = count_fact(n, p) - count_fact(r, p) - count_fact(n-r, p)
	assert(_e >= 0)
	if (_e >= e):
		return 0
	pk = expo(p, e)
	fact = init(p, pk)
	ans = fact_mod(n, p, pk, fact)
	ans = mulmod(ans, mod_inverse(fact_mod(r, p, pk, fact), pk), pk)
	ans = mulmod(ans, mod_inverse(fact_mod(n-r, p, pk, fact), pk), pk)
	ans = mulmod(ans, expo(p, _e), pk)
	return ans

def pre_process(rem, mods):
	crt = []
	a = 1
	b = 1
	m = mods[0]
	crt.append([mods[0], a, b])
	L =	len(mods)
	for i in range(1, L):
		a = mod_inverse(m, mods[i])
		b = mod_inverse(mods[i], m)
		crt.append([m, a, b])
		m *= mods[i]
	assert(len(crt) == len(mods))
	return crt

def find_crt(rem, mods, crt):
	assert(len(crt) == len(mods))
	ans = rem[0]
	m = crt[0][0]
	L = len(mods)
	for i in range(1, L):
		a = crt[i][1]
		b = crt[i][2]
		m = crt[i][0]
		_m = m * mods[i]
		ans = mulmod(ans, b * mods[i], _m)
		ans = (ans + mulmod(rem[i], a * m, _m)) % (_m)
	return ans

def ncr(n, r, m):
	pf = factorise(m)
	rem = []
	mods = []
	L = len(pf)
	for i in range(L):
		get = ncr_pk(n, r, pf[i][0], pf[i][1])
		rem.append(get)
		mods.append(expo(pf[i][0], pf[i][1]))
	crt = pre_process(rem, mods)
	ans = find_crt(rem, mods, crt)
	return ans
def add(a,b,c):
	res=a+b
	if(res>=c):
		return res-c
	else:
		return res

#returns (a * b) mod c
def mod(a,b,c):
	res=a*b
	if(res>=c):
		return res%c
	else:
		return res
#Complexity: O(max(log2(a), log2(b)))
def lcm(a,b):
	w=a//gcd(a,b)
	return w*b

#return (a ^ b) mod m
#Complexity: O(log2(b))
def power(a,b,m):
	x,y=1,
	while(b>0):
		if(b&1):
			x=mod(x,y,m)
		y=mod(y,y,m)
		b>>=1
	return x

#returns (a ^ (-1)) mod m
#works only for m = prime
#Complexity: O(log2(m))
def inv(a,m):
	return power(a,m-2,m)

def mod_inverse(a, n):
	N = n
	xx = 0
	yy = 1
	y = 0
	x = 1
	while(n > 0):
		q = a // n
		t = n
		n = a % n
		a = t
		t = xx
		xx = x - q * xx
		x = t
		t = yy
		yy = y - q * yy
		y = t
	x %= N
	x += N
	x %= N
	return

import random
def gcd(a,b):
	while b:
		a,b=b,a%b
	return a

def expo(a,b):
	x,y=1,a
	while(b>0):
		if(b&1):
			x=x*y
		y=y*y
		b>>=1
	return x

primes=[0]*100000

def sieve():
	primes[1]=1
	primes[2]=2
	j=4
	while(j<100000):
		primes[j]=2
		j+=2
	j=3
	while(j<100000):
		if primes[j]==0:
			primes[j]=j
			i=j*j
			k=j<<1
			while(i<100000):
				primes[i]=j
				i+=k
		j+=2

#checks if p is prime or not
def rabin_miller(p):
	if(p<100000):
		return primes[p]==p
	if(p%2==0):
		return False
	s=p-1
	while(s%2==0):
		s>>=1
	for i in range(5):
		a=random.randrange(p-1)+1
		temp=s
		mod=pow(a,temp,p)
		while(temp!=p-1 and mod!=1 and mod!=p-1):
			mod=(mod*mod)%p
			temp=temp*2
		if(mod!=p-1 and temp%2==0):
			return False
	return True

#returns a prime factor of N
def brent(N):
	if(N%2==0):
		return 2
	if(N<100000):
		return primes[N]
	y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
	g,r,q = 1,1,1
	while g==1:
		x=y
		for i in range(r):
			y=((y*y)%N+c)%N
		k=0
		while(k<r and g==1):
			ys=y
			for i in range(min(m,r-k)):
				y=((y*y)%N+c)%N
				q=q*(abs(x-y))%N
			g=gcd(q,N)
			k=k+m
		r=r*2
	if g==N:
		while True:
			ys=((ys*ys)%N+c)%N
			g=gcd(abs(x-ys),N)
			if g>1:
				break
	return g

def factorise(n):
	Q_1= queue()
	Q_2=[]
	Q_1.put(n)
	while(not Q_1.empty()):
		l=Q_1.get()
		if(rabin_miller(l)):
			Q_2.append(l)
			continue
		d=brent(l)
		if(d==l):
			Q_1.put(l)
		else:
			Q_1.put(d)
			Q_1.put(l//d)
	return Q_2
def get_z_value(pattern, Z):
    n = len(pattern)
    k, l, r = 0, 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and pattern[r-l] == pattern[r]:
                r += 1
            Z[i] = r - l
            r -= 1
        else:
            k = i - l
            if Z[k] < r - i + 1:
                Z[i] = Z[k]
            else:
                l = i
                while r < n and pattern[r-l] == pattern[r]:
                    r += 1
                Z[i] = r - l
                r -= 1

def lsp(pattern, Z):
    get_z_value(pattern, Z)
    n = len(pattern)

    Z1 = [0 for i in range(n)]
    for j in range(n - 1, 0, -1):
        i = j + Z[j] - 1
        Z1[i] = Z[j]
    return Z1
def patternMatching(txt, pat):
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    j = 0  # index for pat[]
    lps = lsp(pat, lps)
    i = 0
    cnt = 0
    ans = []
    while i < N and j < M:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            ans.append(i-j)
            cnt += 1
            j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return ans
from math import ceil, log2

def buildTree(a, segtree, left, right, index):
    if left == right:
        segtree[index] = a[left]
        return
    mid = (left + right) // 2
    buildTree(a, segtree, left, mid, 2 * index + 1)
    buildTree(a, segtree, mid + 1, right, 2 * index + 2)
    segtree[index] = segtree[ 2 * index + 1] + segtree[2 * index + 2]

def updateQuery(segtree, a, left, right, index, pos, value):
    if pos < left or right < pos:
        return
    if left == right:
        a[pos] += value
        segtree[index] += value
        return
    mid = (left+right) // 2
    if pos <= mid:
        updateQuery(segtree, a, left, mid, 2 * index + 1, pos ,value)
    else:
        updateQuery(segtree, a, mid + 1, right, 2 * index + 2, pos, value)
    segtree[index] = segtree[2 * index + 1] + segtree[ 2 * index + 2]

def sumRange(segtree, left, right, fr, to, index):
    if fr <= left and to >= right:
        return segtree[index]
    if fr > right or to < left:
        return 0
    mid = ( left + right ) // 2
    return sumRange(segtree, left, mid, fr, to, 2 * index + 1) + sumRange(segtree, mid + 1, right, fr, to, 2 * index + 2)


t = int(input())

for o in range(1, t+1):
    print("Case {}:".format(o))
    n, q =  list(map(int, input().split()))
    a =  list(map(int, input().split()))
    n = len(a)
    h = ceil(log2(n))
    sizeTree = 2 * ( 2 ** h ) - 1
    segTree = [float('inf')] * sizeTree
    lazy = [0] * sizeTree
    buildTree(a, segTree, 0, n-1, 0)
    while q:
        q -= 1
        b = list(map(int, input().split()))
        if b[0] == 1:
            print(a[b[1]])
            updateQuery(segTree, a, 0, n - 1, 0, b[1], -a[b[1]])
            a[b[1]] = 0
        elif b[0] == 2:

            updateQuery(segTree, a, 0,n-1,0, b[1], b[2] )
        else:
            print(sumRange(segTree, 0, n - 1, b[1], b[2], 0))

from math import ceil, log2
def buildTree(a, segtree, left, right, index):
    if left == right:
        segtree[index] = a[left]
        return
    mid = (left + right) // 2
    buildTree(a, segtree, left, mid, 2 * index + 1)
    buildTree(a, segtree, mid + 1, right, 2 * index + 2)
    segtree[index] = min(segtree[ 2 * index + 1], segtree[2 * index + 2])
def updateQuerry_sumQueryLazy(segtree, lazy, left, right, fr, to, delta, index):

    if lazy[index] != 0:
        segtree[index] += lazy[index]
        if left != right:
            lazy[2*index+1] += lazy[index]
            lazy[2 * index + 2] += lazy[index]
        lazy[index] = 0
    if fr <= left and right <= to:
        segtree[index] += delta
        if left != right:
            lazy[2 * index + 1] += delta
            lazy[2 * index + 2] += delta
        return
    if min(right,to) < max(left, fr):
        return

    mid = (left + right) // 2
    updateQuerry_sumQueryLazy(segtree, lazy, left, mid, fr, to, delta, 2 * index + 1)
    updateQuerry_sumQueryLazy(segtree, lazy, mid + 1, right, fr, to, delta, 2 * index + 2)
    segtree[index] = min(segtree[2*index+1], segtree[2*index+2])
def minQueryLazy(segtree, lazy, left, right, fr, to, index):
    if min(right, to) < max(left, fr):
        return 10**9
    if lazy[index] != 0:
        segtree[index] += lazy[index]
        if left != right:
            lazy[2 * index + 1] += lazy[index]
            lazy[2 * index + 2] += lazy[index]
        lazy[index] = 0

    if fr <= left and to >= right:
        return segtree[index]

    mid = (left + right) // 2
    return min(minQueryLazy(segtree, lazy, left, mid, fr, to, 2 * index + 1), minQueryLazy(segtree, lazy, mid+1, right, fr, to, 2 * index + 2))
n = int(input())
a =  list(map(int, input().split()))
n = len(a)
h = ceil(log2(n))
sizeTree = 2 * ( 2 ** h ) - 1
segTree = [float('inf')] * sizeTree
lazy = [0] * sizeTree
buildTree(a, segTree, 0, n-1, 0)
m = int(input())
for i in range(m):
    b = list(map(int, input().split()))
    if len(b) == 2:
        if b[0] <= b[1]:
            print(minQueryLazy(segTree, lazy, 0, n - 1, b[0], b[1], 0))
        else:
            print(min(minQueryLazy(segTree, lazy, 0, n - 1, b[0], n-1, 0), minQueryLazy(segTree, lazy, 0, n - 1, 0, b[1], 0)))

    else:
        if b[0] <= b[1]:
            updateQuerry_sumQueryLazy(segTree, lazy, 0, n - 1, b[0], b[1], b[2], 0)
        else:
            updateQuerry_sumQueryLazy(segTree, lazy, 0, n - 1, b[0], n-1, b[2], 0)
            updateQuerry_sumQueryLazy(segTree, lazy, 0, n - 1, 0, b[1], b[2], 0)


import heapq
from collections import defaultdict
class Graph:
    def __init__(self, n):
        self.nodes = set(range(n))
        self.edges = defaultdict(list)
        self.distances = {}

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[from_node, to_node] = distance

def dijkstra(graph, initial):
    visited = {initial: 0}
    h = [(0, initial)]
    path = {}

    nodes = set(graph.nodes)

    while nodes and h:
        current_weight, min_node = heapq.heappop(h)
        try:
            while min_node not in nodes:
                current_weight, min_node = heapq.heappop(h)
        except IndexError:
            break

        nodes.remove(min_node)
        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[min_node, v]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heapq.heappush(h, (weight, v))
                path[v] = min_node

    return visited, path

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.parents = [-1] * vertices

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, a):
        # find root of the tree containing ‘a’
        if self.parents[a] < 0:  # root is reached
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]
    def union(self, a, b):
        root_a = self.find(a) # find root of tree containing ‘a’
        root_b = self.find(b) # find root of tree containing ‘b’
        if root_a == root_b: # ‘a’ and ‘b’ in the same tree
            return
        height_a = -self.parents[root_a] # height+1 of tree containing ‘a’
        height_b = -self.parents[root_b] # height+1 of tree containing ‘b’
        if height_a > height_b:
            self.parents[root_b] = root_a # link shorter tree’s root to taller
        elif height_b > height_a:
            self.parents[root_a] = root_b
        else: # if (height_a == height_b)
            self.parents[root_a] = root_b
            self.parents[root_b] = -(height_b + 1) # update: height grows by 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(u)
            y = self.find(v)
            if x != y:
                e = e + 1
                # we got the edge u,v having the smallest weight w
                result.append([u, v, w])
                self.union(x, y)

"""An optimized implementation of Suffix-Tree."""

# For more infor about the comments you can read http://web.stanford.edu/~mjkay/gusfield.pdf
import sys
from operator import attrgetter
leafEnd = -1
class Node:
	def __init__(self, leaf):
		# children of this node
		self.children = {}
		# True if having a leaf, False if no
		self.leaf = leaf
		# This leaf node contains the suffix index for the route from root to leaf.
		self.suffix_index = None
		self.start = None
		self.end = None
		# pointer to other node via suffix link
		self.suffix_link = None

	def __getattribute__(self, name):
		if name == 'end':
			if self.leaf:
				return leafEnd
		# Calling the super class to avoid recursion
		return super(Node, self).__getattribute__(name)


class SuffixTree:
	"""The Suffix-Tree."""

	def __init__(self, text):
		"""Initiate the tree."""
		self.text_string = text
		self.size = -1  # Length of input string
		self.root = None
		self.last_new_node = None
		self.active_node = None
		self.active_edge = -1
		self.active_length = 0
		# remainder_suffix_count tells how many suffixes yet to
		# be added in tree
		self.remainder_suffix_count = 0
		self.root_end = None
		self.split_end = None

	def edge_length(self, node):
		if node == self.root:
			return 0
		return node.end - node.start + 1

	def skip_counting(self, current_node):
		length = self.edge_length(current_node)
		if self.active_length >= length:
			self.active_edge += length
			self.active_length -= length
			self.active_node = current_node
			return True
		return False

	def create_a_new_node(self, start, end=None, leaf=False):
		node = Node(leaf)
		node.suffix_link = self.root
		node.start = start
		node.end = end
		node.suffix_index = -1
		return node

	def extend_suffix_tree(self, pos):
		global leafEnd
		leafEnd = pos

		self.remainder_suffix_count += 1
		self.last_new_node = None
		# Add all suffixes (yet to be added) one by one in tree
		while self.remainder_suffix_count > 0:
			if self.active_length == 0:
				self.active_edge = pos  # APCFALZ
			if self.active_node.children.get(self.text_string[self.active_edge]) is None:
				self.active_node.children[self.text_string[self.active_edge]] = self.create_a_new_node(pos, leaf=True)
				if self.last_new_node is not None:
					self.last_new_node.suffix_link = self.active_node
					self.last_new_node = None
			else:
				next_node = self.active_node.children.get(self.text_string[self.active_edge])
				if self.skip_counting(next_node):  # Do skip_counting
					continue
				if self.text_string[next_node.start + self.active_length] == self.text_string[pos]:
					if (self.last_new_node is not None) and (self.active_node != self.root):
						self.last_new_node.suffix_link = self.active_node
						self.last_new_node = None
					# APCFER3
					self.active_length += 1
					break
				self.split_end = next_node.start + self.active_length - 1
				# New internal node
				split = self.create_a_new_node(next_node.start, self.split_end)
				self.active_node.children[self.text_string[self.active_edge]] = split
				# New leaf coming out of new internal node
				split.children[self.text_string[pos]] = self.create_a_new_node(pos, leaf=True)
				next_node.start += self.active_length
				split.children[self.text_string[next_node.start]] = next_node
				if self.last_new_node is not None:
					# suffix_link of last_new_node points to current newly
					# created internal node
					self.last_new_node.suffix_link = split
				self.last_new_node = split
			self.remainder_suffix_count -= 1
			if (self.active_node == self.root) and (self.active_length > 0):  # APCFER2C1
				self.active_length -= 1
				self.active_edge = pos - self.remainder_suffix_count + 1
			elif self.active_node != self.root:  # APCFER2C2
				self.active_node = self.active_node.suffix_link
		print()
	def find_the_smallest_string_by_dfs(self, current, lo_start):
		global cnt
		cnt += 1
		start, end = current.start, current.end
		print((self.text_string[start: end + 1], end - (lo_start + end - start), start, end))
		if len(current.children) == 0:
			yield start - lo_start

		for i in range(0, 256):
			ch = chr(i)

			if ch not in current.children:
				continue
			node = current.children[ch]
			if node:
				temp = 0
				if start != -1:
					temp = lo_start + end + 1 - start
				yield from self.find_the_smallest_string_by_dfs(node, temp)

	def build_suffix_tree(self):
		self.size = len(self.text_string)

		"""Root is a special node with start and end indices as -1,
        as it has no parent from where an edge comes to root"""
		self.root_end = -1
		self.root = self.create_a_new_node(-1, self.root_end)
		self.active_node = self.root  # First active_node will be root
		for i in range(self.size):
			self.extend_suffix_tree(i)
	def __str__(self):
		return "\n".join(map(str, self.edges.values()))
	def burrow_wheeler(self):
		global cnt
		cnt = 0
		res = []
		for sub in self.find_the_smallest_string_by_dfs(self.root, 0):
			res.append(sub)
		return res
def pre_cal(string):
	right = len(string) - 1
	location = [0] * len(string)
	for i in range(len(string)):
		location[i] = right
		right += 1
		if right == len(string):
			right = 0
	return location


def readInput(txtFileName):
	# Open and read the text file
	txtFile = open(txtFileName, 'r')
	txt = txtFile.read()
	# Remember to close the file
	txtFile.close()

	return txt


def writeOutput(result):
	# Open output file with correct name
	outputFile = open('output_bwt_1.txt', 'w')
	# Iterate through the occurrence list and write results to an output file
	outputFile.write(result)
	# Remember to close the file
	outputFile.close()


if __name__ == '__main__':
	txtFileName = sys.argv[1]
	txt = readInput(txtFileName, )
	a = SuffixTree(txt)
	a.build_suffix_tree()
	res = a.burrow_wheeler()
	location = pre_cal(txt)
	final_res = ""
	for i in res:
		final_res += txt[location[i]]
	writeOutput(final_res)
