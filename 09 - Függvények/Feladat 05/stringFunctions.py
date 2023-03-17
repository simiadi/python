def getSameLetters(n1: str, n2: str) -> str:
    intersection: str = ""

    for c in n1:
        x: bool = n2.find(c) > 0
        y: bool = intersection.find(c) == -1
        if ( x and y ):
            intersection += x

    return intersection