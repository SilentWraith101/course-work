# Description

# This program will take inputs and assign them to variables.
# Additionally it will calculate the area of the lawn, patio, soil and garden.calculate the price of the materials
# It will also calculate the price of the materials needed

# Currency symbol
CURRENCY = '£'

# Development costs
LAWN_COST = 3
PATIO_COST = 5
SOIL_COST = 2.5


try:
    gardenLength = float(input("Enter the length of the garden: "))
    gardenWidth = float(input("Enter the width of the garden: "))
    patioLength = float(input("Enter the length of the patio: "))
    patioWidth = float(input("Enter the width of the patio: "))
    lawnLength = float(input("Enter the length of the lawn: "))
    lawnWidth = float(input("Enter the width of the lawn: "))

    # Ensure that all dimensions given are greater than 0
    if gardenLength <= 0:
        raise Exception('Garden length needs to be greater than 0 ({})'.format(gardenLength))

    if gardenWidth <= 0:
        raise Exception('Garden width needs to be greater than 0 ({})'.format(gardenWidth))

    if patioLength <= 0:
        raise Exception('Patio length needs to be greater than 0 ({})'.format(patioLength))

    if patioWidth <= 0:
        raise Exception('Patio width needs to be greater than 0 ({})'.format(patioWidth))

    if lawnLength <= 0:
        raise Exception('Lawn length needs to be greater than 0 ({})'.format(lawnLength))

    if lawnWidth <= 0:
        raise Exception('Lawn width needs to be greater than 0 ({})'.format(lawnWidth))

    # Ensure lawn and patio length is less than or equal to garden length
    if gardenLength < (lawnLength + patioLength):
        raise Exception(
            'Lawn length ({}) plus patio length ({}) cannot be more than garden length ({})'.format(
                lawnLength,
                patioLength,
                gardenLength
            )
        )

    # Ensure that lawn width is less than or equal to garden width
    if lawnWidth > gardenWidth:
        raise Exception(
            'Lawn width ({}) cannot be greater than garden width ({})'.format(lawnWidth, gardenWidth)
        )

    # Ensure that patio width is less than or equal to garden width
    if patioWidth > gardenWidth:
        raise Exception(
            'Patio width ({}) cannot be greater than garden width ({})'.format(patioWidth, gardenWidth)
        )

    print('\n#### Areas ####\n')

    # Calculate the area of the garden
    gardenArea = gardenLength * gardenWidth
    print('Garden area: ({:.2f}) mtr2'.format(gardenArea))

    # Calculate the area of the lawn
    lawnArea = lawnLength * lawnWidth
    print('Lawn area: ({:.2f}) mtr2'.format(lawnArea))

    # Calculate the area of the patio
    patioArea = patioLength * patioWidth
    print('Patio area: ({:.2f}) mtr2'.format(patioArea))

    # Calculate the area of the soil
    soilArea = gardenArea - (lawnArea + patioArea)
    print('Soil area: ({:.2f}) mtr2'.format(soilArea))

    print('\n#### Costs ####\n')

    # Calculate the lawn cost
    lawnCost = lawnArea * LAWN_COST
    print('Lawn cost: {}{:.2f}'.format(CURRENCY, lawnCost))

    # Calculate the patio cost
    patioCost = patioArea * PATIO_COST
    print('Patio cost: {}{:.2f}'.format(CURRENCY, patioCost))

    # Calculate the soil cost
    soilCost = soilArea * SOIL_COST
    print('Soil cost: {}{:.2f}'.format(CURRENCY, soilCost))

    print('\n#### Total ####\n')

    # Calculate the total cost
    totalCost = lawnCost + patioCost + soilCost
    print('Total cost: {}{:.2f}'.format(CURRENCY, totalCost))


except Exception as e:
    # Print the exception message
    print(str(e))
