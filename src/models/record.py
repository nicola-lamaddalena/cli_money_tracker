class Record:
    def __init__(
        self, name: str = "default", type: str = "out", value: float | int = 0.00
    ) -> None:
        self.name = name
        self.type = type
        self.set_type()
        self.value = value
        self.set_value()

    def __str__(self) -> str:
        return f"{self.name} - {self.value} - {self.type}"

    def set_type(self) -> None:
        if self.type == "":
            self.type == "out"

    def set_value(self) -> None:
        if self.type == "out":
            self.value = -self.value
