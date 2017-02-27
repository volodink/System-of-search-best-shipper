def getReliabilityRating(numBrokeSupply, numLawsuitsNow, LawsuitsPast, CompanyAge, financPosition, numberOfClient):
    weightedNumberOfClient = 0.13
    weightedFinancPosition = 0.2
    weightedCompanyAge = 0.12
    weightednumLawsuitsPast = 0.1
    weightedNumLawsuitsNow = 0.15
    weightedNumBrokeSupply = 0.3
                
    return (weightedNumBrokeSupply * numBrokeSupply - \
            weightedNumLawsuitsNow * numLawsuitsNow - \
            weightednumLawsuitsPast * LawsuitsPast + \
            weightedCompanyAge * CompanyAge + \
            weightedFinancPosition * financPosition + \
            weightedNumberOfClient * numberOfClient) 

def getPartnerRating(reliabilityRating, qualityRating, maxReliabilityRating, maxQualityRating, weightedReliability, weightedQuality):
    return  reliabilityRating * ((maxReliabilityRating/100) * weightedReliability) + \
            qualityRating * ((maxQualityRating/100) * weightedQuality)