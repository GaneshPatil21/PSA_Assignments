import copy
import time
start = time.time()

# preferences list for Super Group 1 teams
super_group_1 = {
 'g1_t1':  ['g2_t1', 'g2_t5', 'g2_t3', 'g2_t4', 'g2_t6', 'g2_t2', 'g2_t8', 'g2_t7'],
 'g1_t2':  ['g2_t3', 'g2_t8', 'g2_t1', 'g2_t4', 'g2_t5', 'g2_t6', 'g2_t2', 'g2_t7'],
 'g1_t3':  ['g2_t8', 'g2_t5', 'g2_t1', 'g2_t4', 'g2_t2', 'g2_t6', 'g2_t7', 'g2_t3'],
 'g1_t4':  ['g2_t6', 'g2_t4', 'g2_t7', 'g2_t8', 'g2_t5', 'g2_t2', 'g2_t3', 'g2_t1'],
 'g1_t5':  ['g2_t4', 'g2_t2', 'g2_t3', 'g2_t6', 'g2_t5', 'g2_t1', 'g2_t8', 'g2_t7'],
 'g1_t6':  ['g2_t2', 'g2_t1', 'g2_t4', 'g2_t7', 'g2_t5', 'g2_t3', 'g2_t8', 'g2_t6'],
 'g1_t7':  ['g2_t7', 'g2_t5', 'g2_t2', 'g2_t3', 'g2_t1', 'g2_t4', 'g2_t8', 'g2_t6'],
 'g1_t8':  ['g2_t1', 'g2_t5', 'g2_t8', 'g2_t6', 'g2_t3', 'g2_t2', 'g2_t7', 'g2_t4']}

# preferences list for Super Group 2 teams
super_group_2 = {
 'g2_t1':  ['g1_t2', 'g1_t6', 'g1_t7', 'g1_t1', 'g1_t4', 'g1_t5', 'g1_t3', 'g1_t8'],
 'g2_t2':  ['g1_t2', 'g1_t1', 'g1_t3', 'g1_t6', 'g1_t7', 'g1_t4', 'g1_t5', 'g1_t8'],
 'g2_t3':  ['g1_t6', 'g1_t2', 'g1_t5', 'g1_t7', 'g1_t8', 'g1_t3', 'g1_t1', 'g1_t4'],
 'g2_t4':  ['g1_t6', 'g1_t3', 'g1_t1', 'g1_t8', 'g1_t7', 'g1_t4', 'g1_t2', 'g1_t5'],
 'g2_t5':  ['g1_t8', 'g1_t6', 'g1_t4', 'g1_t1', 'g1_t7', 'g1_t3', 'g1_t5', 'g1_t2'],
 'g2_t6':  ['g1_t2', 'g1_t1', 'g1_t5', 'g1_t4', 'g1_t6', 'g1_t7', 'g1_t3', 'g1_t8'],
 'g2_t7':  ['g1_t7', 'g1_t8', 'g1_t6', 'g1_t2', 'g1_t1', 'g1_t3', 'g1_t5', 'g1_t4'],
 'g2_t8':  ['g1_t7', 'g1_t2', 'g1_t1', 'g1_t4', 'g1_t8', 'g1_t5', 'g1_t3', 'g1_t6']}

group1 = sorted(super_group_1.keys())
group2 = sorted(super_group_2.keys())

def check(engaged):
    inverseengaged = dict((v,k) for k,v in engaged.items())
    for she, he in engaged.items():
        shelikes = super_group_2[she]
        shelikesbetter = shelikes[:shelikes.index(he)]
        helikes = super_group_1[he]
        helikesbetter = helikes[:helikes.index(she)]
        for guy in shelikesbetter:
            guysgirl = inverseengaged[guy]
            guylikes = super_group_1[guy]
            if guylikes.index(guysgirl) > guylikes.index(she):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (she, guy, he, guysgirl))
                return False
        for gal in helikesbetter:
            girlsguy = engaged[gal]
            gallikes = super_group_2[gal]
            if gallikes.index(girlsguy) > gallikes.index(he):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (he, gal, she, girlsguy))
                return False
    return True

def matchmaker():
    guysfree = group1[:]
    engaged  = {}
    guyprefers2 = copy.deepcopy(super_group_1)
    galprefers2 = copy.deepcopy(super_group_2)
    while guysfree:
        guy = guysfree.pop(0)
        guyslist = guyprefers2[guy]
        gal = guyslist.pop(0)
        fiance = engaged.get(gal)
        if not fiance:
            # She's free
            engaged[gal] = guy
        else:
            # The bounder proposes to an engaged lass!
            galslist = galprefers2[gal]
            if galslist.index(fiance) > galslist.index(guy):
                # She prefers new guy
                engaged[gal] = guy
                if guyprefers2[fiance]:
                    # Ex has more girls to try
                    guysfree.append(fiance)
            else:
                # She is faithful to old fiance
                if guyslist:
                    # Look again
                    guysfree.append(guy)
    return engaged

engaged = matchmaker()

# Print all fixtures among teamss
print('Fixtures:')
print('  ' + ',\n  '.join('%s - %s' % couple
                          for couple in sorted(engaged.items())))
print()
print('Matching stability check PASSED'
      if check(engaged) else 'Matching stability check FAILED')

end = time.time()
print("Execution Time:", (end - start)*1000)
