import math


def calculate_gross_salary(basic_salary, allowance):
    return basic_salary + allowance


def calculate_tax(gross_salary, tax_rate):
    return gross_salary * tax_rate / 100


def calculate_net_salary(gross_salary, tax_amount):
    return gross_salary - tax_amount


def validate_salary_details(basic_salary, allowance, tax_rate):
    values = (basic_salary, allowance, tax_rate)
    if not all(math.isfinite(value) for value in values):
        raise ValueError("Enter finite numbers only.")
    if basic_salary < 0 or allowance < 0:
        raise ValueError("Salary and allowance cannot be negative.")
    if not 0 <= tax_rate <= 100:
        raise ValueError("Tax rate must be between 0 and 100.")


def display_salary(name, gross_salary, tax_amount, net_salary):
    print("\nEmployee Salary Summary")
    print("Employee:", name)
    print(f"Gross salary: PKR {gross_salary:.2f}")
    print(f"Tax deduction: PKR {tax_amount:.2f}")
    print(f"Net salary: PKR {net_salary:.2f}")


def main():
    name = input("Employee name: ")
    try:
        basic = float(input("Basic salary: "))
        allowance = float(input("Allowance: "))
        rate = float(input("Tax rate (%): "))
        validate_salary_details(basic, allowance, rate)
        gross = calculate_gross_salary(basic, allowance)
        tax = calculate_tax(gross, rate)
        net = calculate_net_salary(gross, tax)
        display_salary(name, gross, tax, net)
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
