from ast import pattern
import re

text_to_look = """As mentioned above, a more precise, scientific examination leads to more complex attempts at definition and description. Th.e property of "being a text" is called textuality , the linguistic study of texts is text linguistics . This discipline provides various textuality criteria.

In 1981, Robert-Alain de Beaugrande and Wolfgang Ulrich Dressler presented a series of such criteria. On the one hand, these criteria relate to the characteristics of the text itself ( cohesion , i.e. formal cohesion and coherence , i.e. content-related cohesion), on the other hand to the characteristics of a communication situation from which the text in question arises or in which it is used ( intentionality , acceptability , Informativity , Situationality ).
"""

pattern = r"([A-Z][a-z].)"
x = re.findall(pattern,text_to_look)
print(x)