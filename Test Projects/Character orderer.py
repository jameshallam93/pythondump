count = {}
speech = "I will achieve what I set out to achieve, and I will not let obstacles and temptations sway me from the good path that awaits."
for character in speech:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
count_alph = sorted(count)  
print(count_alph)
