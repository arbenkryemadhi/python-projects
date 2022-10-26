import time


def main():
    def generate_random_number(seed: int, num_len: int):
        new_seed = seed
        temp_string = str(seed)
        result = ""

        for i in range(num_len):
            # Gets a random one digit number from time.
            rand_variable = int(str(time.time() * 1000)[-1])

            # Produces a new random (int) seed from the existing seed.
            new_seed = pow(new_seed, len(temp_string) * rand_variable)

            result += str(new_seed)[-1]

        # Returns result
        return int(result)

    generate_random_number(6, 100)


if __name__ == "__main__":
    main()
