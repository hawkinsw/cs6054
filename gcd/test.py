from gcd import gcd_r_lindio, gcd_i, gcd_r, testcases, swap
from typing import List
from statistics import mean, stdev

def calculate_linearizations() -> None:
    total_tests = 4000
    tests = testcases(total_tests)
    for test in tests:
        params, result = test
        (l, r) = params
        if r > l:
            (l, r) = swap(l,r)
        (gcd_result, (l_coef, r_coef)) = gcd_r_lindio(l, r, debug=True)
        if result != gcd_result or l*l_coef + r*r_coef != gcd_result:
            print(f"Linearization failed!! {gcd_result} != {l}*{l_coef} + {r}*{r_coef}")
        
def calculate_stats() -> None:
    total_meta_tests = 1000
    relative_prime_ratios: List[float] = []
    for _ in range(total_meta_tests):
        total_tests = 4000
        relatively_prime = 0
        tests = testcases(total_tests)
        for test in tests:
            (params, result) = test
            if gcd_i(*params) != result:
                print(f"Failure: gcd_i({params}) != {result}")
                break
            if gcd_r(*params) != result:
                print(f"Failure: gcd_r({params}) != {result}")
                break
            if result == 1:
                relatively_prime += 1
        relative_prime_ratio: float = relatively_prime / total_tests
        relative_prime_ratios.append(relative_prime_ratio)
    print(f"Average relative prime ratio: {mean(relative_prime_ratios)}.")
    print(f"With standard deviation of {stdev(relative_prime_ratios)}.")


# For the full details: https://docs.python.org/3/reference/expressions.html#calls
def splatter_test(alpha: str, beta: str, charlie:str = "default") -> None:
    print(f"{alpha=}")
    print(f"{beta=}")
    print(f"{charlie=}")

if __name__=="__main__":
    calculate_linearizations()
    calculate_stats()

    params = {}
    # Notice that charlie is not specified and so it's value is "default"
    params["alpha"] = "This is the alpha parameter."
    params["beta"] = "This is the beta parameter."
    splatter_test(**params)
    # Notice that the * turns the params into an iterable by using its .keys() Interesting!
    splatter_test(*params)
