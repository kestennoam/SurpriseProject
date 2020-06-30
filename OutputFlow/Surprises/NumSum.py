from OutputFlow.Surprises.SurpriseFrame import SurpriseFrame


class NumSum(SurpriseFrame):
    """
    This class NumSum is type of Surprise, (option 3).
    it calculate the sum of the value of chars of the username
    it heritage from surprise most of attributes.
    work standalone
    """
    DIFF = 64  # @ ascii val (last before A)
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
        for i in self.get_val(0).upper():  # make upper to ensure no lower
            if i != self.SPACE:  # check if its space to avoid calculate it
                total += (ord(i) - self.DIFF)
        return total
