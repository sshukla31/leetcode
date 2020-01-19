class Solution(object):

    def __init__(self):
        self.neigh = "neigh"

    def is_valid_len(self, sound):
        # sound length of 'neigh' os atleast 5
        if not sound or len(sound) < 5:
            return False

        return True

    def get_horse_count(self, sound, n_pos):
        horse_count = 1
        for i in xrange(len(n_pos) - 1):
            # Check if "n" is overlapping. if "n" is after 5 which indicates
            # same horse
            if n_pos[i + 1] - n_pos[i] < 5:
                horse_count += 1

        return horse_count

    def is_valid_sound(self, sound, n_pos):

       # Verify if the sound is valid
        valid_sound_count = 0
        for i in n_pos:
            j = 0
            while j < len(self.neigh) and i < len(sound):
                if sound[i] == self.neigh[j]:
                    j+=1
                    i+=1
                else:
                    i+=1

            if j == len(self.neigh):
                valid_sound_count += 1


        # As each valid sound "neigh" len = 5, do / 5
        # this return one valid count of a horse
        if valid_sound_count != len(sound)/5:
            return False

        return True


    def numHorses(self, sound):
        # 1: Check validity
        if not self.is_valid_len(sound):
            return -1

        # 2: Get index no of char 'n'
        n_pos = [index for index, char in enumerate(sound) if char == "n"]

        # 3: Get horse count
        horse_count = self.get_horse_count(sound, n_pos)

        # 4: Check if all sounds are valid
        if not self.is_valid_sound(sound, n_pos):
            return -1


        return horse_count



s = Solution()

sound = "nei"
assert -1 == s.numHorses(sound)

sound = "neigh"
assert 1 == s.numHorses(sound)

sound = "neighnei"
assert 1 == s.numHorses(sound)

sound = "neighneigh"
assert 1 == s.numHorses(sound)

sound = "nenieghigh"
assert 2 == s.numHorses(sound)
