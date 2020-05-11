class BaseLogicGateException(Exception):
    pass


class NoFreeInputs(BaseLogicGateException):
    pass


class IncorrectInputValue(BaseLogicGateException):
    pass


class NotFinishedGateValue(BaseLogicGateException):
    pass


class LogicGate:
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return f"{self.__class__.__name__}({self.label})"

    def perform_logic(self):
        pass

    def set_input(self):
        pass

    def reset_inputs(self):
        pass


class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.input_signal = None

    def set_input(self, value):
        if value not in (0, 1, ):
            raise IncorrectInputValue("value should be 0 or 1")
        if not self.input_signal:
            self.input_signal = value
        else:
            raise NoFreeInputs("No free inputs are available")

    def reset_inputs(self):
        self.input_signal = None

    def __str__(self):
        return f"{self.__class__.__name__}({self.label}:({self.input_signal}))"


class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.input_signal_one = None
        self.input_signal_two = None

    def set_input(self, value):
        if value not in (0, 1, ):
            raise NoFreeInputs("value should be 0 or 1")
        if self.input_signal_one is None and self.input_signal_two is None:
            self.input_signal_one = value
        elif self.input_signal_two is None:
            self.input_signal_two = value
        else:
            raise NoFreeInputs("No free inputs are available")

    def reset_inputs(self):
        self.input_signal_one = None
        self.input_signal_two = None

    def __str__(self):
        return f"{self.__class__.__name__}({self.label}:({self.input_signal_one} and {self.input_signal_two}))"


class LogicAndGate(BinaryGate):
    def perform_logic(self):
        if self.input_signal_one is None and self.input_signal_two is None:
            raise NotFinishedGateValue("Not finished Gate")

        if self.input_signal_one == 1 and self.input_signal_two == 1:
            return 1
        return 0


class LogicOrGate(BinaryGate):
    def perform_logic(self):
        if self.input_signal_one is None and self.input_signal_two is None:
            raise NotFinishedGateValue("Not finished Gate")

        if self.input_signal_one or self.input_signal_two:
            return 1
        return 0


class LogicNotGate(UnaryGate):
    def perform_logic(self):
        if self.input_signal is None:
            raise NotFinishedGateValue("Not finished Gate")

        if self.input_signal:
            return 0
        return 1


class ConnectorError(Exception):
    pass


class Connector:
    def __init__(self):
        self.in_ = None

    def set_in(self, value):
        self.in_ = value

    def set_out(self):
        if self.in_ is None:
            raise ConnectorError("You should set input first ")

        return self.in_


if __name__ == '__main__':
    a = LogicAndGate("A")
    b = LogicOrGate("B")
    c = LogicNotGate("C")
    d = LogicOrGate("D")
    a.set_input(1)
    a.set_input(1)
    b.set_input(0)
    b.set_input(0)

    con_ac = Connector()
    con_ac.set_in(a.perform_logic())

    c = LogicNotGate("c")
    c.set_input(con_ac.set_out())

    conn_bd = Connector()
    conn_bd.set_in(b.perform_logic())


    conn_cd = Connector()
    conn_cd.set_in(c.perform_logic())

    d.set_input(conn_cd.set_out())
    d.set_input(conn_bd.set_out())
    print(d)

    print(d.perform_logic())
