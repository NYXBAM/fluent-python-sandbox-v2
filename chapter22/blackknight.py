# property deleter example


class BlackKnight:
    def __init__(self):
        self.phrases = [
            ("an arm", "Tis but a scratch."),
            ("another arm", "It's just a flesh wound."),
            ("a leg", "I'm invincible!"),
            ("another leg", "All right, we'll call it a draw."),
        ]

    @property
    def member(self):
        print("next member is:")
        return self.phrases[0][0]

    @member.deleter
    def member(self):
        member, text = self.phrases.pop(0)
        print(f"BLACK KNIGHT (loses {member}) -- {text}")

    # __delattr__ low level example
    # def __delattr__(self, name):
    #     if name == "member":
    #         if self.phrases:
    #             member, text = self.phrases.pop(0)
    #             print(f"BLACK KNIGHT (loses {member}) -- {text}")
    #     else:
    #         super().__delattr__(name)


knight = BlackKnight()
print(knight.member)
del knight.member
del knight.member
del knight.member
del knight.member
"""
next member is:
an arm
BLACK KNIGHT (loses an arm) -- Tis but a scratch.
BLACK KNIGHT (loses another arm) -- It's just a flesh wound.
BLACK KNIGHT (loses a leg) -- I'm invincible!
BLACK KNIGHT (loses another leg) -- All right, we'll call it a draw.
"""
