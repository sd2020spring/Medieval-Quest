import levelBase
from helpers import load_image


class cave22(levelBase.Level):
    """
    Class that will include this quadrant of the game
    """

    def __init__(self, side):
        """
        Initialize which character value belongs to which type of block/character in the level file
        """

        levelBase.Level.__init__(self, side)

        self.CAVEGROUND = 0
        self.WALL = 1
        self.BREAKABLE_WALL_C = 2
        self.BOWANDQUIVER = 3
        self.PLAYER_C = 4
        self.PASSAGE_C = 5
        self.BLANK = 6
        self.BOMB = 7
        self.BOMBNUM = 8
        self.POTION = 9
        self.POTIONNUM= 10
        self.HEART1 = 11
        self.HEART2 = 12
        self.HEART3 = 13
        self.KINGBOMB = 14
        self.KINGARROW = 15

    def getLayoutCave(self):
        """
        Matrix which would use the previosuly determined characters to show what the level will be
        """
        return [[1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 1, 1],\
                [1, 1, 1, 1, 1, 1, 1, 0, 4, 0, 1, 1],\
                [1, 1, 0, 0, 0, 0 ,0 ,0, 0, 0, 1, 1],\
                [1, 1, 0, 0, 0, 0 ,0 ,0, 0, 0, 1, 1],\
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],\
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],\
                [1, 1, 0, 3, 0, 0, 0, 0, 0 ,0, 1, 1],\
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],\
                [1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1],\
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
                [6, 7, 8, 6, 9, 10, 6, 6, 11, 12, 13, 6]]

    def getSprites(self):
        """
        Using helpers.py this method will load the png files saved in the data folder
        it will then save them in a list to be returned so they are more easily accessible
        """

        ground = load_image('CaveFloor.png')
        wall = load_image('CaveWall.png')
        BreakableWall = [load_image('CaveWallBreakable.png'), load_image('CaveWallBroken.png')]
        bowandquiver = load_image('BowAndQuiver.png')
        player = self.kingCaveImages()
        passage = load_image('CaveFloor.png')
        blank = load_image("Blank.png")
        bomb = load_image("BlankBomb.png")
        nums = self.numberImages()
        potion = load_image("Blank_Potion_Health.png")
        heart = [load_image('Heart_0.png'), load_image("Heart_1.png"), load_image("Heart_2.png"), load_image("Heart_3.png"), load_image("Heart_4.png")]
        kingbomb = load_image("CaveBomb.png")
        kingarrow = self.arrowImages()

        return [ground, wall, BreakableWall, bowandquiver, player, passage, blank, bomb, nums, potion, nums, heart, heart, heart, kingbomb, kingarrow]
