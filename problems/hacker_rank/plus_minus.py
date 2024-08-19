"""
Given a list of ints calculate to the 6th decimal place the number of:
- Proportion of positive elems
- Proportion of 0 elems
- Proportion of negative elems

Implement the plusMinus(arr) function.
"""

from decimal import Decimal


def plusMinus(arr: list) -> None:
    numElems = len(arr)

    positiveElems = len(list(filter(lambda elem: elem > 0, arr)))
    negativeElems = len(list(filter(lambda elem: elem < 0, arr)))
    zeroElems = len(list(filter(lambda elem: elem == 0, arr)))

    positiveElemsRatio = Decimal(format(positiveElems / numElems, '.6f'))
    negativeElemsRatio = Decimal(format(negativeElems / numElems, '.6f'))
    zeroElemsRatio = Decimal(format(zeroElems / numElems, '.6f'))

    outputs = [
        positiveElemsRatio,
        negativeElemsRatio,
        zeroElemsRatio
    ]

    for elem in outputs:
        print(elem)
