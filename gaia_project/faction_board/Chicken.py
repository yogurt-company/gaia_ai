from .faction_base import FactionBase


class Chicken(FactionBase):
    def __init__(self):
        pass



# const hadschHallas: FactionBoardVariants = {
#   faction: Faction.HadschHallas,
#   standard: {
#     income: ["3k,4o,15c,q,up-eco", "+o,k,3c"],
#     handlers: {
#       freeActionChoice: (player: Player, pool: ConversionPool) => {
#         if (player.data.hasPlanetaryInstitute()) {
#           pool.push(freeActionsHadschHallas, player);
#         }
#       },
#     },
#   },
#   variants: [
#     {
#       type: "beta",
#       board: {
#         income: ["3k,4o,15c,q,up-eco,up-eco", "+o,k,3c"],
#       },
#       version: 0,
#     },
#   ],
# };
#
# export default hadschHallas;