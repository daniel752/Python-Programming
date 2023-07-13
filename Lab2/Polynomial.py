def polynomial(factors):

    exponent = len(factors) - 1  # highest exponent in polynom

    def calc_polynom(parameter):
        res = 0
        ctr = 0
        for x in factors:
            if ctr == exponent:
                res += x * parameter
            else:
                res += (parameter ** (exponent - ctr) * x)  # inputting the factors with exponent multiplied with parameter
            ctr += 1
        return res
    return calc_polynom


seq = [1,2,1,0]
value_x = polynomial(seq)(4)
print(value_x)
