import random
print("\nCode Starting.\n")
trials = int(input("Trials: "))
verbose = int(input("Verbose Mode: "))
blocks = int(input("Blocks to walk: "))
print("Walking " + str(blocks) + " blocks, flipping a coin each time:")
print("Running " + str(trials) + " trials.\n")
total = 0
for counter in range(trials):
    if verbose:
        print("\nTrial: " + str(counter+1))
    position = 0
    path = [x for x in range(0,blocks)]
    flips = 0
    if verbose:
        print(path[0:position] + ["X"] + path [position+1:])
    while (position < blocks):
        outcome = random.randint(0,1)
        if (outcome):
            position += 1
        else:
            if (position > 0):
                position -= 1
        flips += 1
        if verbose:
            print(path[0:position] + ["X"] + path [position+1:])
    if verbose:
        print("Flips taken: " + str(flips))
    total += flips
average = total/trials
print("\nAverage: " + str(flips) + " flips")
print("\nDone.")

