class Category:

    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = list()

    def __str__(self):
        length_of_category_name = len(self.category_name)
        transactions = ''
        for transaction in self.ledger:
            description = transaction['description'][:23]
            amount = transaction['amount']
            amount = str(amount)

            # Adding trailing decimal 0
            if type(eval(amount)) == float:
                # display first seven digits if number has more than seven digits
                if len(amount) > 5:
                    amount = amount[:7]
                else:
                    # Add a 0 is number already has a single decimal place
                    amount += '0' if (len(amount.split('.')[1]) == 1) else ''
            else:
                # display first seven digits if number has more than seven digits
                if len(amount) > 5:
                    amount = amount[:7]
                else:
                    # Add two 0s if number has no decimal place
                    amount += '.00'
            space = (30 - len(description)) - len(amount)
            transactions = transactions + description + (' ' * space) + amount + '\n'

        # first line of output if category name has odd number of characters
        if length_of_category_name % 2:
            length_of_category_name += 1
            disp1 = ('*' * int(15 - length_of_category_name / 2))
            disp2 = '*' * (30 - len(disp1) - len(self.category_name))
            disp = disp1 + self.category_name + disp2

        # first line of output if category name has even number of characters
        else:
            disp1 = '*' * int(15 - length_of_category_name / 2)
            disp2 = '*' * (30 - len(disp1) - len(self.category_name))
            disp = disp1 + self.category_name + disp2

        # balance left in the category
        balance = self.get_balance()
        balance = str(balance)

        # adding trailing zeros to the balance amount
        if type(eval(balance)) == float:
            balance += '0' if (len(balance.split('.')[1]) == 1) else ''
        else:
            balance += '.00'
        balance = f'Total: {balance}'

        return disp + '\n' + transactions + balance

    def deposit(self, amount, description=''):
        """
        A `deposit` method that accepts an amount and description. If no description is given, it should default to
        an empty string. The method should append an object to the ledger list in the form of `{"amount": amount,
        "description": description}`.

        :param amount:
        :param description:
        :return: None
        """
        new_ledger = {'amount': amount, 'description': description}
        self.ledger.append(new_ledger)

    def withdraw(self, amount, description=''):
        """
        A `withdraw` method that is similar to the `deposit` method, but the amount passed in should be stored in the
        ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This
        method should return `True` if the withdrawal took place, and `False` otherwise.

        :param amount: Amount to be withdrawn
        :param description: Description
        :return: None
        """
        if self.check_funds(amount):
            amount *= -1
            new_ledger = {'amount': amount, 'description': description}
            self.ledger.append(new_ledger)
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            amount = transaction['amount']
            balance += amount
        return balance

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination.category_name}')
            destination.deposit(amount, f'Transfer from {self.category_name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True

    def total_withdrawal(self) -> float or int:
        tot = 0
        for transaction in self.ledger:
            amount = transaction['amount']
            if amount < 0:
                tot += abs(amount)
        return tot


def create_spend_chart(categories: list) -> str:
    amounts = list()
    spending = dict()
    longest = categories[0].category_name

    for cat in categories:
        amounts.append(cat.total_withdrawal())
        name = cat.category_name
        if len(name) > len(longest):
            longest = name
    longest = len(longest)

    total_withdrawal = sum(amounts)

    for cat in categories:
        total = cat.total_withdrawal()
        percent = (((total/total_withdrawal) * 100) // 10) * 10
        spending[cat.category_name] = percent

    line_list = ["100|", " 90|", " 80|", " 70|", " 60|", " 50|", " 40|", " 30|", " 20|", " 10|", "  0|"]
    line_1 = "Percentage spent by category"

    position_in_values = 0
    position_in_line_list = 0
    values = [i for i in spending.values()]
    check_point = 100

    while position_in_values <= len(values):
        if values[position_in_values] >= check_point:
            if position_in_values == (len(values) - 1):
                line_list[position_in_line_list] += ' o  '
            else:
                line_list[position_in_line_list] += ' o '
        else:
            if position_in_values == (len(values) - 1):
                line_list[position_in_line_list] += '    '
            else:
                line_list[position_in_line_list] += '   '

        if position_in_values == (len(values) - 1):
            position_in_values = 0
            check_point -= 10
            if position_in_line_list < len(line_list) - 1:
                position_in_line_list += 1
            else:
                break
        else:
            position_in_values += 1

    line_list.append((4 * ' ') + "-")
    spending_keys = [i for i in spending.keys()]
    for i in spending_keys:
        line_list[-1] += 3 * "-"
    line_list.append(5 * " ")

    position_in_cat_name = 0
    while longest >= 1:
        for i in spending_keys:
            try:
                line_list[-1] += (i[position_in_cat_name] + "  ")
            except IndexError:
                line_list[-1] += "   "
        longest -= 1
        position_in_cat_name += 1
        line_list.append(5 * " ")

    line_list.insert(0, line_1)
    del line_list[-1]

    return "\n".join(line_list)


if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    # print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    # print(food)
    # print(clothing)

    print(create_spend_chart([clothing, auto, food]))
