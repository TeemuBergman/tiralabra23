from algorithms.scientific_calculator import ScientificCalculator


def main():
    # Quick setup before UI is beign implemented
    expression = 'x+x*y^3/x'
    variables = 'x=2,y=3,z=5'
    scientific_calc = ScientificCalculator(expression, variables)
    print(scientific_calc.calculate())


if __name__ == "__main__":
    main()
