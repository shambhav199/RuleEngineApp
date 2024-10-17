class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type  # "operator" or "operand"
        self.left = left  # Left child Node (used if type is "operator")
        self.right = right  # Right child Node (used if type is "operator")
        self.value = value  # Used if type is "operand" (condition)

    def __repr__(self):
        return f"Node(type={self.type}, left={self.left}, right={self.right}, value={self.value})"

from pyparsing import Word, alphas, nums, oneOf, infixNotation, opAssoc, Literal

def create_rule(rule_string):
    operand = Word(alphas) | Word(nums)  # Supports words and numbers as operands
    operator = oneOf("AND OR")
    comparison = oneOf("> < =")  # Supports comparison operators
    
    rule_expr = infixNotation(
        operand,
        [
            (comparison, 2, opAssoc.LEFT),
            (operator, 2, opAssoc.LEFT),
        ],
    )

    parsed_rule = rule_expr.parseString(rule_string)
    return parsed_rule  # Return the parsed rule in AST-like form

def evaluate_rule(ast_node, data):
    if ast_node.type == "operand":
        if 'AND' in ast_node.value or 'OR' in ast_node.value:
            sub_conditions = ast_node.value.split(' AND ') if 'AND' in ast_node.value else ast_node.value.split(' OR ')
            results = []

            for condition in sub_conditions:
                components = condition.strip().split(" ", 2)
                attribute, operator, value = components[0], components[1], components[2]

                if value.isdigit():
                    value = int(value)
                else:
                    value = value.strip("'")

                attribute_value = data.get(attribute)

                print(f"Evaluating: {attribute} {operator} {value} with data value: {attribute_value}")

                result = False
                if operator == '>':
                    result = attribute_value > value
                elif operator == '<':
                    result = attribute_value < value
                elif operator == '=':
                    result = attribute_value == value

                results.append(result)

            return all(results) if 'AND' in ast_node.value else any(results)

        else:
            components = ast_node.value.split(" ", 2)
            attribute, operator, value = components[0], components[1], components[2]

            if value.isdigit():
                value = int(value)
            else:
                value = value.strip("'")

            attribute_value = data.get(attribute)

            print(f"Evaluating: {attribute} {operator} {value} with data value: {attribute_value}")

            if operator == '>':
                return attribute_value > value
            elif operator == '<':
                return attribute_value < value
            elif operator == '=':
                return attribute_value == value

    elif ast_node.type == "operator":
        left_result = evaluate_rule(ast_node.left, data)
        right_result = evaluate_rule(ast_node.right, data)
        print(f"Evaluating Operator: {ast_node.value} with left result: {left_result} and right result: {right_result}")
        if ast_node.value == "AND":
            return left_result and right_result
        elif ast_node.value == "OR":
            return left_result or right_result

    return False

def combine_rules(rules):
    root_node = Node(type="operator", value="AND")
    current = root_node

    for rule_string in rules:
        rule_ast = create_rule(rule_string)
        node = Node(type="operand", value=rule_string)
        if not current.left:
            current.left = node
        elif not current.right:
            current.right = node
        else:
            new_root = Node(type="operator", value="AND")
            new_root.left = current
            new_root.right = node
            current = new_root

    return current

if __name__ == "__main__":
    rule1 = "age > 30 AND department = 'Sales'"
    rule2 = "salary > 50000 OR experience > 5"

    combined_rule = combine_rules([rule1, rule2])
    print(f"Combined AST: {combined_rule}")

    data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    result = evaluate_rule(combined_rule, data)
    print(f"Evaluation Result: {result}")
