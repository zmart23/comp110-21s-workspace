"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730317621"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor that initializes the values attribute."""
        self.values = values
    
    def __repr__(self) -> str:
        """Method to represent the object as a string."""
        return f"Simpy({self.values})"
    
    def fill(self, filling: float, filled: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        self.values = [filling] * filled

    def arange(self, start: float, stop: float, step: float) -> None:
        """Fills in the values attribute with a range of values."""
        result: list[float] = []
        step != 0.0
        while True:
            if start < stop:
                result.append(start)
                start += step

    def sum(self) -> float:
        """Computes and returns the sum of all items in values attribute."""

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds the ability to use addition with Simpy and float."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item + rhs)
            return Simpy(result)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] + rhs.values[i])
            return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
        return Simpy(result)
    
    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item % rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] % rhs.values[i])
        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on the equality of each item in values."""
        result: list[bool] = []
        i = 0
        if isinstance(rhs, float):
            if self.values[i] == rhs:
                result.append(True)
                i += 1
            else:
                result.append(False)
                i += 1
        else:
            if self.values[i] == rhs.values[i]:
                result.append(True)
                i += 1
            else:
                result.append(False)
                i += 1

        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on a greater than relationship."""
        result: list[bool] = []
        i = 0
        for i in range(len(self.values)):
            if isinstance(rhs, float):
                if self.values[i] > rhs:
                    result.append(True)
                    i += 1
                else:
                    result.append(False)
                    i += 1
            else:
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                    i += 1
                else:
                    result.append(False)
                    i += 1
        return result

    def __getitem__(self, rhs: int) -> float:
        """Overload the subscription notation."""
        i = 0
        for i in range(len(self.values)):
            if self.values[i]:
                return self.values[i]
            else:
                i += 1
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows use of subscription operator to filter with a mask."""
        result: list[bool] = []
        return result
