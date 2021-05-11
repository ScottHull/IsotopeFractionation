from math import sqrt


class Fractionate:
    """
    This is the model of Dauphas et al., 2015.
    https://www.sciencedirect.com/science/article/pii/S0012821X15004355
    """
    def __init__(self, vapor_pressure):
        self.vapor_pressure = vapor_pressure

    def delta_kinetic(self, m_j, m_i, gamma_i=1, gamma_j=1):
        """
        The isotopic fractionation due to kinetic processes.
        :param m_j:
        :param m_i:
        :param gamma_i:
        :param gamma_j:
        :return:
        """
        return 1000 * ((gamma_i / gamma_j) * sqrt(m_j / m_i) - 1)

    def delta_condensation(self, eq_sat_pressure, delta_kinetic, delta_equilibrium):
        """
        The isotopic fractionation due to equilibrium.
        :param eq_sat_pressure:
        :param delta_kinetic:
        :param delta_equilibrium:
        :return:
        """
        return ((eq_sat_pressure / self.vapor_pressure) * delta_equilibrium) + (1)

