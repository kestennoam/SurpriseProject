from Routes.Surprise.Surprises.SurpriseFrame import SurpriseFrame


class NumSum(SurpriseFrame):
    """
    This class NumSum is type of Surprise, (option 3).
    it calculate the sum of the value of chars of the username
    it heritage from surprise most of attributes.
    work standalone
    """
    DIFF_UPPER = 64  # @ ascii val (last before A)
    DIFF_LOWER = 96  # ` ascii val (last before A)
    SPACE = " "
    TYPE = "name-sum"

    def __init__(self):
        super().__init__()

    def get_query(self):
        """
        This method calculate the sum of the char values of username
        it run on every char and make it uppercase (to ensure accept
        case sensitivity ) and sum it (ignoring space char)
        :return: total- sum of the char values
        """
        total = 0
        for ch in self.get_val(0):  # make upper to ensure no lower
            ascii_ch = ord(ch)
            if ch != self.SPACE:  # check if its space to avoid calculate it
                if ascii_ch < self.DIFF_LOWER:
                    total += ascii_ch - self.DIFF_UPPER
                else:
                    total += ascii_ch - self.DIFF_LOWER

        return total
