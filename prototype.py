#! /usr/bin/env python3

import pprint

f0 = open("data/processed.txt").read()
# TODO: splits in multiline commands as well. Need to only split on '\n[0-9]+'
lines = f0.split('\n')
commands = [x.split(']')[1][1:] for x in lines if len(x.split(']')) >= 2 and len(x.split(']')[1]) >= 2]
longest = commands[0]
for c in commands:
  if len(c) > len(longest):
    longest = c

# Only splits off first command: TODO: do for the whole thing, or at least on sub command?
split_commands = [x.split(' ', 1) for x in commands]

trie = {}
for c in split_commands:
    latter = ' '.join(c[1:])
    if not c[0] in trie:
      trie[c[0]] = {latter: 1}
    else:
      if latter in trie[c[0]]:
        trie[c[0]][latter] += 1
      else:
        trie[c[0]][latter] = 1

pp = pprint.PrettyPrinter(indent=4)

sorted_diversity = sorted(
    map(lambda l: (l[0], len(l[1])), trie.items()), 
    key=lambda l: l[1], 
    reverse=True
)
sorted_counts = sorted(
    map(lambda l: (l[0], sum(l[1].values())), trie.items()),
    key=lambda l: l[1],
    reverse=True
)
print("Sorted diversity (unique subcommands)")
pp.pprint(sorted_diversity)
print("Sorted counts")
pp.pprint(sorted_counts)

# Vim vs emacs
print(f"vim: {sum(trie['vim'].values())}")
print(f"emacs: {sum(trie['emacs'].values())}")

# start from the top
for command in trie:
  if command.startswith('/'):
    pp.pprint(f"{command}: {trie[command]}")

# sudo
pp.pprint(trie['sudo'])