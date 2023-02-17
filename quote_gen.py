import random

sen = ["<S>"]


S = [["<Q1>"],["<Q2>"],["<Q3>"],["<Q4>"]]

Q1 = [["<Intro>","<Adj>","<Noun>","<Verb>","<Object>"]]
Q2 = [["<Intro>","<Verb>","<Object>"]]
Q3 = [["<Intro>","<NounPhrase>","<Verb>","<Object>"]]
Q4 = [["<Intro>","<Adj>","<Noun>","<Verb>","<Object>","<Conj>","<NounPhrase>"]]


Intro = [["The answer to the ultimate question of life, the universe, and everything is,"] , ["I love deadlines. I love the whooshing noise they make as they go by."] , ["Time is an illusion. Lunchtime doubly so." , "Don't panic."]]
Adj = [["amazing"] , ["impossible"] , ["unbelievable"] , ["incredible"] , ["mind-boggling"] , ["astonishing"]]
Noun = [["universe"] , ["technology"] , ["life"] , ["future"] , ["improbability"] , ["planet"]]
Verb = [["astonishes"] , ["boggles the mind"] , ["defies explanation"] , ["is beyond understanding"] , ["is incomprehensible"] , ["is impossible"]]
Object = [["completely"] , ["totally"] , ["utterly"] , ["absolutely"] , ["entirely"] , ["thoroughly"]]
Conj = [["and"] , ["or"] , ["but"]]
NounPhrase = [["<Adj>","<Noun>"],["<Adj>","<Noun>","that","<Verb>"]]

table = {}

table["<S>"] = S
table["<Q1>"] = Q1
table["<Q2>"] = Q2
table["<Q3>"] = Q3
table["<Q4>"] = Q4
table["<Intro>"] = Intro
table["<Adj>"] = Adj
table["<Noun>"] = Noun
table["<Verb>"] = Verb
table["<Object>"] = Object
table["<Conj>"] = Conj
table["<NounPhrase>"] = NounPhrase

######################################################################################

def subsitute_nodes(lst):
	new_lst = []
	c = 0
	for p in lst:
		if p in table:
			c = 1
			c1 = table[p]
			ll = len(c1)
			rr = random.randrange(0,ll)
			q = c1[rr]
#			print(q)
			for r in q:
#				print("r - ",r)
				new_lst.append(r)
		else:
			new_lst.append(p)
	return [c,new_lst]



######################################################################################
random.seed()
random.setstate(random.getstate())

l1 = [0,sen]


while(True):
	l1 = subsitute_nodes(l1[1])
	r = l1[0]
	lst = l1[1]
		
	if(r == 0):
		break

print(' '.join(l1[1]))




