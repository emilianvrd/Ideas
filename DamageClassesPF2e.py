class DPRmartials:
    def __init__(self, damage, hit_chance1, hit_chance2, hit_chance3, unused_act, name):
        self.damage = damage
        self.hit_chance1 = hit_chance1
        self.hit_chance2 = hit_chance2
        self.hit_chance3 = hit_chance3
        self.unused_act = unused_act
        self.name = name
        if self.unused_act == 0:
            self.dpr = ((3 - self.unused_act) * self.damage) * (
                self.hit_chance1 + self.hit_chance2 + self.hit_chance3
            ) + (self.hit_chance1 - 0.5) * self.damage
        elif self.unused_act == 1:
            self.dpr = ((3 - self.unused_act) * self.damage) * (
                self.hit_chance1 + self.hit_chance2
            ) + (self.hit_chance1 - 0.5) * self.damage
        elif unused_act == 2:
            self.dpr = ((3 - self.unused_act) * self.damage) * self.hit_chance1 + (
                self.hit_chance1 - 0.5
            ) * self.damage
        elif self.unused_act == 3:
            self.dpr = 0
        self.dpr = (
            self.dpr
            + 3 * self.damage * (self.hit_chance1 + self.hit_chance2 + self.hit_chance3)
            + (self.hit_chance1 - 0.5) * 2 * self.damage
        ) / 3
        print(f"{self.name}'s average DPR is:", float(round(self.dpr, 2)))


barbarian = DPRmartials(14.5, 0.65, 0.4, 0.15, 2, "barbarian")
ranger = DPRmartials(10.5, 0.65, 0.5, 0.35, 2, "ranger")
# fighter = DPRmartials(10.5, 0.75, 0.5, 0.25, 1, "fighter")
alt_fighter = DPRmartials(10.5, 0.7, 0.45, 0.2, 1, "altfighter")
martial = DPRmartials(10.5, 0.65, 0.4, 0.15, 2, "martial")
# twoweaponfighter = DPRmartials(7.5, 0.65, 0.60, 0.25, 1, "twoweaponfighter")
snb_fighter = DPRmartials(8.5, 0.7, 0.45, 0, 1, "snbfighter")
rng_fighter = DPRmartials(5.5, 0.7, 0.45, 0.2, 0, "rngfighter")
# xbow_fighter = DPRmartials(4.5, 0.7, 0.45, 0, 2, "xbowfighter")
# upg_xbowfighter = DPRmartials(5.5, 0.7, 0.45, 0, 2, "upg_xbowfighter")
# upg2_xbowfighter = DPRmartials(4.5, 0.7, 0.45, 0.2, 1, "upg2_xbowfighter")
# upg3_xbowfighter = DPRmartials(5.5, 0.7, 0.45, 0.2, 1, "upg3_xbowfighter")
# upg4_xbowfighter = DPRmartials(6.5, 0.7, 0.45, 0.2, 1, "upg4_xbowfighter")
# warpriest = DPRmartials(7.5, 0.75, 0.75, 0, 2, "warpriest")
