import os
import json

new = input("New mask? (y/n): ")
name = input("Enter mask name: ")

filepath = os.environ['HOME'] + "/.savedmasks.json"

with open(filepath, 'r') as file:
    saved_masks = json.load(file)

    if new == 'n':
            print("#define " + name.upper() + "_MASK_HIGH " + saved_masks[name]["high_mask"])
            print("#define " + name.upper() + "_MASK_LOW " + saved_masks[name]["low_mask"])

    elif new == 'y':
        if name in saved_masks.keys():
            if input("Mask name already in use. Overwrite? (y/n): ") != 'y':
                print("Exiting...")
                exit()

        high_mask = [0] * 32
        low_mask = [1] * 32

        enter = input("Enter bit (number,position): ")
        while enter != "stop" and enter != "quit" and enter != "exit":
            enter = enter.split(",")
            position = int(enter[1])
            for index, bit in enumerate(enter[0]):
                w_index = len(enter[0]) - index - 1
                if bit == "0":
                    low_mask[w_index + position] = 0
                elif bit == "1":
                    high_mask[w_index + position] = 1

            enter = input("Enter bit (number,position): ")

        high_mask.reverse()
        low_mask.reverse()

        high_mask = [str(bit) for bit in high_mask]
        low_mask = [str(bit) for bit in low_mask]

        high_mask = ''.join(high_mask)
        low_mask = ''.join(low_mask)

        high_mask = hex(int(high_mask, 2))
        low_mask = hex(int(low_mask, 2))

        print("#define " + name.upper() + "_MASK_HIGH " + str(high_mask))
        print("#define " + name.upper() + "_MASK_LOW " + str(low_mask))

        new_mask = {name: {"high_mask": str(high_mask), "low_mask": str(low_mask)}}
        saved_masks.update(new_mask)

with open(filepath, 'w') as file:
    json.dump(saved_masks, file)
