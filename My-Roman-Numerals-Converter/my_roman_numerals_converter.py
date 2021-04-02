def _getRomanDictOrdered():
    #
    from collections import OrderedDict
    #
    dIntRoman = OrderedDict()
    #
    dIntRoman[1000] = "M"
    dIntRoman[900] = "CM"
    dIntRoman[500] = "D"
    dIntRoman[400] = "CD"
    dIntRoman[100] = "C"
    dIntRoman[90] = "XC"
    dIntRoman[50] = "L"
    dIntRoman[40] = "XL"
    dIntRoman[10] = "X"
    dIntRoman[9] = "IX"
    dIntRoman[5] = "V"
    dIntRoman[4] = "IV"
    dIntRoman[1] = "I"
    #
    return dIntRoman

_dIntRomanOrder = _getRomanDictOrdered() # called once on import

def getRomanNumeralOffInt( iNum ):
    #
    lRomanNumerals = []
    #
    for iKey in _dIntRomanOrder:
        #
        if iKey > iNum: continue
        #
        iQuotient = iNum // iKey
        #
        if not iQuotient: continue
        #
        lRomanNumerals.append( _dIntRomanOrder[ iKey ] * iQuotient )
        #
        iNum -= ( iKey * iQuotient )
        #
        if not iNum: break
        #
    #
    return ''.join( lRomanNumerals )

