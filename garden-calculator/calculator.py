import argparse
import sys
import decimal

# Description

# This command line program validates the arguments supplied and calculates the area from those arguments.
# Additionally it generates costs for lawn, patio and soil.

# Usage:
# python3 calculator.py {gardenLength} {gardenWidth} {lawnLength} {lawnWidth} {patioLength} {patioWidth}
# python3 calculator.py -h

# Currency symbol
CURRENCY = '£'

# Development costs
LAWN_COST = 3
PATIO_COST = 5
SOIL_COST = 2.5


# Formats a number to 2 decimal places
# Depending on value, 2 decimal places might not always be the case
# Use {:.2f} when formatting value to ensure 2 decimal places
def number_formatter(number: float) -> float:
    return float(round(decimal.Decimal(number), 2))


try:
    # Create argument parser to accept garden dimensions
    parser = argparse.ArgumentParser(description='Garden Calculator')
    parser.add_argument('gardenLength', help='Length of garden in meters', type=float)
    parser.add_argument('gardenWidth', help='width of garden in meters', type=float)
    parser.add_argument('lawnLength', help='Length of lawn in meters', type=float)
    parser.add_argument('lawnWidth', help='width of lawn in meters', type=float)
    parser.add_argument('patioLength', help='Length of patio in meters', type=float)
    parser.add_argument('patioWidth', help='width of patio in meters', type=float)
    args = parser.parse_args()

    # Ensure that all dimensions given are greater than 0
    for attr, value in vars(args).items():
        if value <= 0:
            raise Exception('{} needs to be greater than 0'.format(attr))

    # Ensure lawn and patio length is less than or equal to garden length
    if args.gardenLength < (args.lawnLength + args.patioLength):
        raise Exception(
            'Lawn length ({}) plus patio length ({}) cannot be more than garden length ({})'.format(
                args.lawnLength,
                args.patioLength,
                args.gardenLength
            )
        )

    # Ensure that lawn width is less than or equal to garden width
    if args.lawnWidth > args.gardenWidth:
        raise Exception(
            'Lawn width ({}) cannot be greater than garden width ({})'.format(args.lawnWidth, args.gardenWidth)
        )

    # Ensure that patio width is less than or equal to garden width
    if args.patioWidth > args.gardenWidth:
        raise Exception(
            'Patio width ({}) cannot be greater than garden width ({})'.format(args.patioWidth, args.gardenWidth)
        )

    print('\n#### Areas ####\n')

    # Calculate the area of the garden
    gardenArea = number_formatter(args.gardenLength * args.gardenWidth)
    print('Garden area: ({:.2f}) mtr2'.format(gardenArea))

    # Calculate the area of the lawn
    lawnArea = number_formatter(args.lawnLength * args.lawnWidth)
    print('Lawn area: ({:.2f}) mtr2'.format(lawnArea))

    # Calculate the area of the patio
    patioArea = number_formatter(args.patioLength * args.patioWidth)
    print('Patio area: ({:.2f}) mtr2'.format(patioArea))

    # Calculate the area of the soil
    soilArea = number_formatter(gardenArea - (lawnArea + patioArea))
    print('Soil area: ({:.2f}) mtr2'.format(soilArea))

    print('\n#### Costs ####\n')

    # Calculate the lawn cost
    lawnCost = number_formatter(lawnArea * LAWN_COST)
    print('Lawn cost: {}{:.2f}'.format(CURRENCY, lawnCost))

    # Calculate the patio cost
    patioCost = number_formatter(patioArea * PATIO_COST)
    print('Patio cost: {}{:.2f}'.format(CURRENCY, patioCost))

    # Calculate the soil cost
    soilCost = number_formatter(soilArea * SOIL_COST)
    print('Soil cost: {}{:.2f}'.format(CURRENCY, soilCost))

    print('\n#### Total ####\n')

    # Calculate the total cost
    totalCost = number_formatter(lawnCost + patioCost + soilCost)
    print('Total cost: {}{:.2f}'.format(CURRENCY, totalCost))

    # Exit with success
    sys.exit(0)

except Exception as e:
    # Print the exception message
    print(str(e))
    # Exit with error code
    sys.exit(1)
