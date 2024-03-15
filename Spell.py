from Card import Card


class Spell(Card):
    spell_type = None  # one of two types

    def set_spell_type(self, spell_type):
        self.spell_type = spell_type


# Create spell cards
spell1 = "Block"
spell2 = "DestroyCreature"
