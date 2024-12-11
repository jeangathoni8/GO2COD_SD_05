import pytest
import logging
import sys
import io
from contextlib import contextmanager
from src.temperature_converter import (
    TemperatureConverter, 
    TemperatureConversionError, 
    TemperatureConverterApp
)

@contextmanager
def capture_stdout():
    """
    Context manager to capture standard output.
    
    Yields:
        StringIO: Captured output stream
    """
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()
    try:
        yield captured_output
    finally:
        sys.stdout = old_stdout

@contextmanager
def simulate_input(monkeypatch, inputs):
    """
    Context manager to simulate user inputs.
    
    Args:
        monkeypatch: Pytest monkeypatch fixture
        inputs (list): List of simulated inputs
    """
    input_generator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_generator))

class TestTemperatureConverter:
    """Test suite for TemperatureConverter class."""

    def test_celsius_to_fahrenheit_conversion(self):
        """Test Celsius to Fahrenheit conversion."""
        converter = TemperatureConverter()
        
        # Test known conversion points
        assert converter.celsius_to_fahrenheit(0) == 32
        assert converter.celsius_to_fahrenheit(100) == 212
        assert converter.celsius_to_fahrenheit(-40) == -40
        
        # Test floating point precision
        assert abs(converter.celsius_to_fahrenheit(37) - 98.6) < 0.1

    def test_fahrenheit_to_celsius_conversion(self):
        """Test Fahrenheit to Celsius conversion."""
        converter = TemperatureConverter()
        
        # Test known conversion points
        assert converter.fahrenheit_to_celsius(32) == 0
        assert converter.fahrenheit_to_celsius(212) == 100
        assert converter.fahrenheit_to_celsius(-40) == -40
        
        # Test floating point precision
        assert abs(converter.fahrenheit_to_celsius(98.6) - 37) < 0.1

    def test_temperature_validation_valid_inputs(self):
        """Test valid temperature inputs."""
        converter = TemperatureConverter()
        
        # Celsius validation
        converter.validate_temperature(0, 'C')
        converter.validate_temperature(-273.15, 'C')
        converter.validate_temperature(1000, 'C')
        
        # Fahrenheit validation
        converter.validate_temperature(32, 'F')
        converter.validate_temperature(-459.67, 'F')
        converter.validate_temperature(1832, 'F')

    def test_temperature_validation_invalid_inputs(self):
        """Test invalid temperature inputs."""
        converter = TemperatureConverter()
        
        # Celsius invalid inputs
        with pytest.raises(TemperatureConversionError):
            converter.validate_temperature(-273.16, 'C')
        with pytest.raises(TemperatureConversionError):
            converter.validate_temperature(1000.1, 'C')
        
        # Fahrenheit invalid inputs
        with pytest.raises(TemperatureConversionError):
            converter.validate_temperature(-459.68, 'F')
        with pytest.raises(TemperatureConversionError):
            converter.validate_temperature(1832.1, 'F')

class TestTemperatureConverterApp:
    """Test suite for TemperatureConverterApp."""

    def test_display_menu(self, capsys):
        """Test menu display functionality."""
        app = TemperatureConverterApp()
        app.display_menu()
        
        captured = capsys.readouterr()
        assert "--- Temperature Converter ---" in captured.out
        assert "1. Celsius to Fahrenheit" in captured.out
        assert "2. Fahrenheit to Celsius" in captured.out
        assert "3. Exit" in captured.out

    def test_get_valid_numeric_input(self, monkeypatch):
        """Test numeric input validation."""
        app = TemperatureConverterApp()
        
        # Simulate valid numeric input
        with simulate_input(monkeypatch, ['25.5']):
            result = app.get_valid_numeric_input("Enter temperature: ")
            assert result == 25.5
        
        # Simulate multiple invalid inputs before valid input
        with simulate_input(monkeypatch, ['abc', '-', '30']):
            result = app.get_valid_numeric_input("Enter temperature: ")
            assert result == 30

    def test_get_valid_menu_choice(self, monkeypatch):
        """Test menu choice validation."""
        app = TemperatureConverterApp()
        
        # Test valid inputs
        with simulate_input(monkeypatch, ['1']):
            assert app.get_valid_menu_choice() == 1
        
        with simulate_input(monkeypatch, ['2']):
            assert app.get_valid_menu_choice() == 2
        
        with simulate_input(monkeypatch, ['3']):
            assert app.get_valid_menu_choice() == 3
        
        # Test invalid inputs before valid input
        with simulate_input(monkeypatch, ['0', '4', 'abc', '2']):
            assert app.get_valid_menu_choice() == 2

    def test_full_conversion_flow(self, monkeypatch, capsys):
        """Test full conversion flow."""
        # Simulate user inputs for Celsius to Fahrenheit conversion
        with simulate_input(monkeypatch, ['1', '25', '3']):
            app = TemperatureConverterApp()
            app.run()
        
        captured = capsys.readouterr()
        assert "25.00°C = 77.00°F" in captured.out
        assert "Thank you for using Temperature Converter. Goodbye!" in captured.out

def test_main_function(monkeypatch, capsys):
    """Test the main function entry point."""
    from src.temperature_converter import main
    
    # Simulate user exiting the application
    with simulate_input(monkeypatch, ['3']):
        try:
            main()
        except SystemExit as e:
            assert e.code == 0
    
    captured = capsys.readouterr()
    assert "Temperature Converter" in captured.out
    assert "Goodbye" in captured.out

# Optional: Logging Tests
def test_logging(caplog):
    """Test logging functionality."""
    app = TemperatureConverterApp()
    caplog.set_level(logging.INFO)
    
    # Simulate a conversion to trigger logging
    with simulate_input(caplog.handler, ['1', '25', '3']):
        app.run()
    
    # Check if conversion is logged
    assert "Converted 25.0°C to 77.0°F" in caplog.text