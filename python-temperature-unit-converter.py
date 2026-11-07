class Temperature:
    """A class to convert Celsius into Fahrenheit and Kelvin."""

    def __init__(self, celsius):
        """Initialize temperature in Celsius."""
        self.celsius = celsius

    def to_fahrenheit(self):
        """Convert Celsius to Fahrenheit."""
        return (self.celsius * 9 / 5) + 32

    def to_kelvin(self):
        """Convert Celsius to Kelvin."""
        return self.celsius + 273.15


# Create a temperature object
t = Temperature(100)

# Display temperature conversions
print(f"Celsius: {t.celsius} Fahrenheit: {t.to_fahrenheit()} Kelvin: {t.to_kelvin()}")