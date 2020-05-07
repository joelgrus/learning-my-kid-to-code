import json
import random
import re

pos = {
 'cc': 'Coordinating conjunction',
 'cd': 'Cardinal number',
 'dt': 'Determiner',
 'ex': 'Existential there',
 'fw': 'Foreign word',
 'in': 'Preposition or subordinating conjunction',
 'jj': 'Adjective',
 'jjr': 'Adjective, comparative',
 'jjs': 'Adjective, superlative',
 'ls': 'List item marker',
 'md': 'Modal',
 'nn': 'Noun, singular or mass',
 'nns': 'Noun, plural',
 'nnp': 'Proper noun, singular',
 'nnps': 'Proper noun, plural',
 'pdt': 'Predeterminer',
 'pos': 'Possessive ending',
 'prp': 'Personal pronoun',
 'prp$': 'Possessive pronoun',
 'rb': 'Adverb',
 'rbr': 'Adverb, comparative',
 'rbs': 'Adverb, superlative',
 'rp': 'Particle',
 'sym': 'Symbol',
 'to': 'to',
 'uh': 'Interjection',
 'vb': 'Verb, base form',
 'vbd': 'Verb, past tense',
 'vbg': 'Verb, gerund or present participle',
 'vbn': 'Verb, past participle',
 'vbp': 'Verb, non-3rd person singular present',
 'vbz': 'Verb, 3rd person singular present',
 'wdt': 'Wh-determiner',
 'wp': 'Wh-pronoun',
 'wp$': 'Possessive wh-pronoun',
 'wrb': 'Wh-adverb',
 # others
 'animal': 'Animal',
 'body': 'Body part',
 'body_plural': 'Body part, plural',
 'food': 'Food',
 'liquid': 'Liquid',
 }


with open('stories.json') as f:
    stories = json.load(f)

story = random.choice(stories)

regex = "<.*?::(.*?)/>"

parts = re.split(regex, story)

outparts = []

for i, part in enumerate(parts):
    if i % 2 == 1:
        # remove ':'
        part = part.strip(':')
        # be defensive against accidental blank answers
        while True:
            answer = input(f"{pos.get(part, part)}: ")
            if answer:
                part = answer
                break

    outparts.append(part)

print()
print()

print("".join(outparts))
