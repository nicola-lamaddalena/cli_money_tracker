class Record:
    def __init__(
        self, name: str = "default", type: str = "out", value: float = 0.00
    ) -> None:
        self.name = name
        self.type = type
        self.value = value

    def __str__(self) -> str:
        return f"{self.name} - {self.value} - {self.type}"
