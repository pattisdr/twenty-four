import operator
import itertools

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.div
}

print "Welcome to the 24-solver"
first_num = input('Enter first number: ')
second_num = input('Enter second number: ')
third_num = input('Enter third number: ')
fourth_num = input('Enter fourth number: ')
print "-----------------------"

nums = [float(first_num), float(second_num), float(third_num), float(fourth_num)]
num_combos = list(itertools.permutations(nums, 4))
ops_combos = list(itertools.product(ops, repeat=3))
results = []
for num_com in num_combos:
    for op_com in ops_combos:
        result = 0
        try:
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
