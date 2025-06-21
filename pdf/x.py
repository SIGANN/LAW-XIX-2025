import spacy

nlp = spacy.load("en_core_web_sm")

text = "Climate change is expected to create hundreds of millions of refugees, but right now climate refugees have no legal rights."

doc = nlp(text)

for tok in doc:
	if tok.text == "refugees":
		print([x for x in tok.head.subtree])
