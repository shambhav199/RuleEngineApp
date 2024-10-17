# RuleEngineApp
The Rule Engine Application evaluates user eligibility based on attributes like age, department, income, and experience. It uses Abstract Syntax Trees (AST) for dynamic rule creation and evaluation. Users define rules in a natural format, which are parsed and evaluated against user data to determine eligibility.


# Rule Engine Application

**Overview**
This is a simple 3-tier rule engine application designed to determine user eligibility based on attributes such as age, department, income, and experience. The system uses an Abstract Syntax Tree (AST) to represent conditional rules and allows for dynamic creation, combination, and modification of these rules.

**Features**
- Create individual rules using a structured grammar.
- Combine multiple rules into a single AST.
- Evaluate the rules against user data.

**Build Instructions**
To build and run this application, follow these steps:

**Prerequisites**
- Python 3.x
- pip (Python package installer)
- Docker (optional, for containerization)

**Installation**
1. Clone the repository:
   
   git clone https://github.com/yourusername/RuleEngineApp.git
   
   cd RuleEngineApp

2.Navigate to the project directory:

   cd RuleEngineApp
  
3.Install dependencies:

  pip install -r requirements.txt


## Usage
_**Here’s an example of how to use the Rule Engine Application:**_

from rule_engine import create_rule, evaluate_rule

**Create rules** :
rule1 = create_rule("age > 30 AND department = 'Sales'")
rule2 = create_rule("salary > 50000 OR experience > 5")

**Combine rules** :
combined_rule = combine_rules([rule1, rule2])

**Sample user data** :
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

**Evaluate combined rules** :
result = evaluate_rule(combined_rule, data)
print(result)  # Output: True


## API Functions
### create_rule(rule_string)
- **Input:** A string representing a rule.
- **Output:** A Node object representing the corresponding AST.

### combine_rules(rules)
- **Input:** A list of rule strings.
- **Output:** The root node of the combined AST.

### evaluate_rule(ast_node, data)
- **Input:** An AST node and a dictionary of user attributes.
- **Output:** A boolean indicating if the user meets the criteria.

## Data Structure
The AST is represented by a `Node` class with the following attributes:
- `type`: Indicates if the node is an "operator" or "operand".
- `left`: Reference to the left child node.
- `right`: Reference to the right child node (if applicable).
- `value`: Holds the value for operand nodes (e.g., comparison value).

## Testing
To run tests, you can execute the following command:
pytest

