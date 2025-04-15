def calculator(a, b, operator):
    """
    Performs a calculation based on the given operator.
    
    :param a: First number (int/float)
    :param b: Second number (int/float)
    :param operator: String representing an operation (+, -, *, /, %, **)
    :return: Computed result or error message
    """
    try:
        # TODO: Implement operation handling and raise exceptions for invalid cases
       if operator=="+":
           return a + b
       elif operator=="-":
           return a + b
       elif operator=="*":
           return a * b
       elif operator=="/":
           return a / b
       elif operator=="%":
           return a % b
       elif operator=="**":
           return a ** b
       else:
         raise ValueError("Unsupported operator provided")
       print(a/b)
       
        
    except ZeroDivisionError as e:
         return "Error: Division by zero"  # TODO: Handle division by zero
    except ValueError as e:
        print(e)  # TODO: Handle invalid numbers
    except TypeError as e:
        return  "Error: Invalid input type" # TODO: Handle non-numeric input
    except Exception as e:
        print(e)  # TODO: Handle any unexpected exceptions

# Example Usage:
print(calculator(10, 0, "/"))  # Should return: "Error: Division by zero"
print(calculator(10, "five", "+"))  # Should return: "Error: Invalid input type"
print(calculator(10, 5, "$"))  # Should return: "Error: Unsupported operator"
 
