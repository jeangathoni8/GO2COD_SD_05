import typing
import sys
import logging

class TemperatureConversionError(Exception):
    """Custom exception for temperature conversion errors."""
    pass

class TemperatureConverter:
    """A utility class for temperature conversions."""

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """
        Convert Celsius to Fahrenheit.
        
        Args:
            celsius (float): Temperature in Celsius
        
        Returns:
            float: Temperature in Fahrenheit
        """
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """
        Convert Fahrenheit to Celsius.
        
        Args:
            fahrenheit (float): Temperature in Fahrenheit
        
        Returns:
            float: Temperature in Celsius
        """
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def validate_temperature(temp: float, scale: str) -> None:
        """
        Validate temperature input based on physical limits.
        
        Args:
            temp (float): Temperature value to validate
            scale (str): Temperature scale ('C' or 'F')
        
        Raises:
            TemperatureConversionError: If temperature is outside valid range
        """
        if scale == 'C' and (temp < -273.15 or temp > 1000):
            raise TemperatureConversionError(f"Invalid Celsius temperature: {temp}")
        elif scale == 'F' and (temp < -459.67 or temp > 1832):
            raise TemperatureConversionError(f"Invalid Fahrenheit temperature: {temp}")

class TemperatureConverterApp:
    """CLI application for temperature conversions."""

    def __init__(self, logger: typing.Optional[logging.Logger] = None):
        """
        Initialize the temperature converter application.
        
        Args:
            logger (Optional[logging.Logger]): Logger for tracking application events
        """
        self.converter = TemperatureConverter()
        self.logger = logger or logging.getLogger(__name__)

    def display_menu(self) -> None:
        """Display conversion menu options."""
        print("\n--- Temperature Converter ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

    def get_valid_numeric_input(self, prompt: str) -> float:
        """
        Get and validate numeric input from user.
        
        Args:
            prompt (str): Input prompt message
        
        Returns:
            float: Validated numeric input
        
        Raises:
            KeyboardInterrupt: If user interrupts input
        """
        while True:
            try:
                value = float(input(prompt).strip())
                return value
            except ValueError:
                print("Error: Please enter a valid number.")
            except KeyboardInterrupt:
                self.logger.warning("Input interrupted by user")
                print("\nOperation cancelled.")
                sys.exit(1)

    def get_valid_menu_choice(self) -> int:
        """
        Get and validate menu choice.
        
        Returns:
            int: Valid menu choice
        
        Raises:
            KeyboardInterrupt: If user interrupts input
        """
        while True:
            try:
                choice = int(input("Enter your choice (1-3): ").strip())
                if 1 <= choice <= 3:
                    return choice
                print("Invalid choice. Please select 1, 2, or 3.")
            except ValueError:
                print("Error: Please enter a number between 1 and 3.")
            except KeyboardInterrupt:
                self.logger.warning("Menu selection interrupted")
                print("\nOperation cancelled.")
                sys.exit(1)

    def run(self) -> None:
        """
        Main application loop for temperature conversions.
        """
        try:
            while True:
                self.display_menu()
                choice = self.get_valid_menu_choice()

                if choice == 3:
                    print("Thank you for using Temperature Converter. Goodbye!")
                    break

                try:
                    if choice == 1:
                        # Celsius to Fahrenheit
                        celsius = self.get_valid_numeric_input("Enter temperature in Celsius: ")
                        self.converter.validate_temperature(celsius, 'C')
                        fahrenheit = self.converter.celsius_to_fahrenheit(celsius)
                        print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
                        self.logger.info(f"Converted {celsius}°C to {fahrenheit}°F")

                    elif choice == 2:
                        # Fahrenheit to Celsius
                        fahrenheit = self.get_valid_numeric_input("Enter temperature in Fahrenheit: ")
                        self.converter.validate_temperature(fahrenheit, 'F')
                        celsius = self.converter.fahrenheit_to_celsius(fahrenheit)
                        print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
                        self.logger.info(f"Converted {fahrenheit}°F to {celsius}°C")

                except TemperatureConversionError as e:
                    print(f"Conversion Error: {e}")
                    self.logger.error(f"Temperature conversion error: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
                    self.logger.error(f"Unexpected error: {e}", exc_info=True)

        except KeyboardInterrupt:
            print("\nApplication terminated by user.")
            sys.exit(0)

def main():
    """
    Entry point for the temperature converter application.
    
    Configures logging and initializes the application.
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('temperature_converter.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    logger = logging.getLogger(__name__)
    
    try:
        app = TemperatureConverterApp(logger)
        app.run()
    except Exception as e:
        logger.critical(f"Critical error in application: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()