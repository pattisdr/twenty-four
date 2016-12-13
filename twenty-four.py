import operator
import itertools

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.div
}

def enter_integer(order):
    while True:
        try:
            num = int(raw_input('Enter your %s number: '% order))
        except ValueError:
            print "Must be an integer."
            continue
        else:
            break
    return num

print "Welcome to the 24-solver"
first_num = enter_integer('first')
second_num = enter_integer('second')
third_num = enter_integer('third')
fourth_num = enter_integer('fourth')
print "-----------------------"

nums = [float(first_num), float(second_num), float(third_num), float(fourth_num)]
num_combos = list(itertools.permutations(nums, 4))
ops_combos = list(itertools.product(ops, repeat=3))
results = []
for num_com in num_combos: # Loops through all number permutations (24 possibilities)
    for op_com in ops_combos: # (Loops through all operator combinations (64 possibilities))
        result = 0
        try: # Moves the parenthesis around in the calculation - probably missing some
            zero_two_one = ops[op_com[1]](ops[op_com[0]](num_com[0], num_com[1]), ops[op_com[2]](num_com[2], num_com[3]))
            if zero_two_one == 24:
                print "(" + str(int(num_com[0])) + str(op_com[0]) + str(int(num_com[1])) + ")" + str(op_com[1]) + "(" + str(int(num_com[2])) + str(op_com[2]) + str(int(num_com[3])) + ")"
            zero_one_two = ops[op_com[2]](ops[op_com[1]](ops[op_com[0]](num_com[0], num_com[1]), num_com[2]), num_com[3])
            if zero_one_two == 24:
                print '(((' + str(int(num_com[0])) + ' '  + str(op_com[0]) + ' ' + str(int(num_com[1])) + ') ' + str(op_com[1]) + ' ' + str(int(num_com[2])) + ') ' + str(op_com[2]) + ' ' + str(int(num_com[3])) + ')'
            one_zero_two = ops[op_com[2]](ops[op_com[0]](num_com[0], ops[op_com[1]](num_com[1], num_com[2])), num_com[3])
            if one_zero_two == 24:
                print '(' + str(int(num_com[0])) + ' '  + str(op_com[0]) + ' (' + str(int(num_com[1])) + ' ' + str(op_com[1]) + ' ' + str(int(num_com[2])) + ')) ' + str(op_com[2]) + ' ' + str(int(num_com[3])) + ' '
            one_two_zero = ops[op_com[0]](num_com[0], ops[op_com[2]](ops[op_com[1]](num_com[1], num_com[2]), num_com[3]))
            if one_two_zero == 24:
                print str(int(num_com[0])) + ' '  + str(op_com[0]) + ' ((' + str(int(num_com[1])) + ' ' + str(op_com[1]) + ' ' + str(int(num_com[2])) + ') ' + str(op_com[2]) + ' ' + str(int(num_com[3])) + ')) '
            two_one_zero = ops[op_com[0]](num_com[0], ops[op_com[1]](num_com[1], ops[op_com[2]](num_com[2], num_com[3])))
            if two_one_zero == 24:
                print '(' + str(int(num_com[0])) + ' '  + str(op_com[0]) + ' (' + str(int(num_com[1])) + ' ' + str(op_com[1]) + ' (' + str(int(num_com[2])) + ' ' + str(op_com[2]) + ' ' + str(int(num_com[3])) + '))) '
        except ZeroDivisionError:
            continue

# TODO
# Validate that inputs are integers
# Add more cases with parenthesis - probably missing some
# Add option to filter out negative numbers from calculation.
# Group similar calculations together?
# Eliminate calculations that are the same via associate/commutative properties?
