fname = 'input.txt'

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

used_coordinates = {}
claim_candidates = set()
for word in content:
    splits = word.split(" ")
    claim = splits[0]
    coordinates = splits[2][:-1].split(",")
    lengths = splits[3].split("x")

    # (0,0) is upper left coordinate
    x0 = int(coordinates[0]) + 1
    y0 = int(coordinates[1]) + 1

    lengthX = int(lengths[0])
    lengthY = int(lengths[1])

    overlapping_claim = False
    for i in range(0, lengthX):
        for j in range(0, lengthY):
            x = x0 + i
            y = y0 + j
            if (x, y) not in used_coordinates:
                if claim not in claim_candidates and not overlapping_claim:
                    claim_candidates.add(claim)
                used_coordinates[(x, y)] = claim
            else:
                overlapping_claim = True
                previous_claim = used_coordinates[(x, y)]
                if previous_claim in claim_candidates:
                    claim_candidates.remove(previous_claim)
                if claim in claim_candidates:
                    claim_candidates.remove(claim)
                used_coordinates[(x, y)] = True

print(len(claim_candidates))
assert len(claim_candidates) == 1, "More than one candidate to claim"

print("Candidate: ", str(next(iter(claim_candidates))))