import operator
import itertools
import random
import ast
import re

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.div
}

ACCEPTABLE_CHARACTERS = ['+', '-', '*', '/', '(', ')']

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

def enter_twenty_four_game_mode():
    while True:
        mode = raw_input('(G)ame mode or (S)olver mode: ').upper()
        if mode != 'G' and mode != 'S':
            print 'Response must be G or S.'
            continue
        else:
            break
    return mode;

def enter_difficulty():
    while True:
        difficulty = raw_input('(B)eginner, (I)ntermediate, or (A)dvanced mode: ').upper()
        if difficulty != 'B' and difficulty != 'I' and difficulty != 'A':
            print 'Response must be B, I, or A'
            continue
        else:
            break
    return difficulty;

def generate_card(range, len, secondrange=None, secondlen=None):
    solutions = 0
    while solutions == 0:
        nums = random.sample(range, len)
        if secondrange:
            nums = nums + random.sample(secondrange, secondlen)
        solutions = find_solutions(nums, mode)
    return nums

def find_solutions(numbers, mode):
    num_combos = list(itertools.permutations(numbers, 4))
    ops_combos = list(itertools.product(ops, repeat=3))
    num_results = 0
    for num_com in num_combos: # Loops through all number permutations (24 possibilities)
        for op_com in ops_combos: # (Loops through all operator combinations (64 possibilities))
            result = 0
            try: # Moves the parenthesis around in the calculation - probably missing some
                zero_two_one = ops[op_com[1]](ops[op_com[0]](num_com[0], num_com[1]), ops[op_com[2]](num_com[2], num_com[3]))
                if zero_two_one == 24:
                    num_results += 1
                    if mode == 'S':
                        print "(" + str(int(num_com[0])) + str(op_com[0]) + str(int(num_com[1])) + ")" + str(op_com[1]) + "(" + str(int(num_com[2])) + str(op_com[2]) + str(int(num_com[3])) + ")"
                zero_one_two = ops[op_com[2]](ops[op_com[1]](ops[op_com[0]](num_com[0], num_com[1]), num_com[2]), num_com[3])
                if zero_one_two == 24:
                    num_results += 1
                    if mode == 'S':
                        print '(((' + str(int(num_com[0])) + ' '  + str(op_com[0]) + ' ' + str(int(num_com[1])) + ') ' + str(op_com[1]) + ' ' + str(int(num_com[2])) + ') ' + str(op_com[2]) + ' ' + str(int(num_com[3])) + ')'
                one_zero_two = ops[op_com[2]](ops[op_com[0]](num_com[0], ops[op_com[1]](num_com[1], num_com[2])), num_com[3])
                if one_zero_two == 24:
                    num_results += 1
                    if mode == 'S':
                        print '(' + str(int(num_com[0])) + ' '  + str(op_com[0]) + ' (' + str(int(num_com[1])) + ' ' + str(op_com[1]) + ' ' + str(int(num_com[2])) + ')) ' + str(op_com[2]) + ' ' + str(int(num_com[3])) + ' '
                one_two_zero = ops[op_com[0]](num_com[0], ops[op_com[2]](ops[op_com[1]](num_com[1], num_com[2]), num_com[3]))
                if one_two_zero == 24:
                    num_results += 1
                    if mode == 'S':
                        print str(int(num_com[0])) + ' '  + str(op_com[0]) + ' ((' + str(int(num_com[1])) + ' ' + str(op_com[1]) + ' ' + str(int(num_com[2])) + ') ' + str(op_com[2]) + ' ' + str(int(num_com[3])) + ')) '
                two_one_zero = ops[op_com[0]](num_com[0], ops[op_com[1]](num_com[1], ops[op_com[2]](num_com[2], num_com[3])))
                if two_one_zero == 24:
                    num_results += 1
                    if mode == 'S':
                        print '(' + str(int(num_com[0])) + ' '  + str(op_com[0]) + ' (' + str(int(num_com[1])) + ' ' + str(op_com[1]) + ' (' + str(int(num_com[2])) + ' ' + str(op_com[2]) + ' ' + str(int(num_com[3])) + '))) '
            except ZeroDivisionError:
                continue

    if num_results == 0 and mode == 'S':
        print "No solutions found!"
    return num_results

def strip_guess(guess):
    new_list = []
    replacement = ''
    concat_indices = []
    for i in range(len(guess)):
        try:
            current = int(guess[i])
            replacement += guess[i]
        except ValueError:
            if replacement:
                new_list.append(replacement)
            new_list.append(guess[i])
            replacement = ''
    if replacement:
        new_list.append(replacement)
    return new_list

def is_valid_guess(guess, card):
    character_error = 'Invalid character(s) used.'
    number_error = 'You used a character that was not on the card.'
    nums_in_solution = []
    string_card = [str(elem) for elem in card]
    for elem in guess:
        if elem not in string_card and elem not in ACCEPTABLE_CHARACTERS:
            if elem not in ACCEPTABLE_CHARACTERS and elem in string_card:
                print character_error
                return False
            if elem not in string_card and elem in ACCEPTABLE_CHARACTERS:
                print number_error
                return False
            print character_error
            print number_error
            return False
        if elem in string_card:
            nums_in_solution.append(elem)
    if sorted(nums_in_solution) != sorted(string_card):
        print 'You did not use all the numbers on the card.'
        return False
    return True

def evaluate_solution(stripped_guess):
    evaluated = eval(''.join(stripped_guess))
    if evaluated == 24:
        print 'That is a correct solution!'
        return True
    else:
        print 'Incorrect. This evaluates to: %s' %evaluated
        return False

def check_guess(card):
    print 'Press Ctrl+C to give up.'
    try:
        while True:
            guess = strip_guess(list(raw_input('Enter solution: ').replace(' ', '')))
            is_valid = is_valid_guess(guess, card)
            if is_valid:
                correct = evaluate_solution(guess)
                if correct:
                    break
            else:
                continue
    except KeyboardInterrupt:
        print '-----------------'
        print 'Give up?'
        print 'Solutions:'
        find_solutions([float(elem) for elem in card], 'S')

print "Welcome to the 24-solver"
print "-----------------------"
mode = enter_twenty_four_game_mode()

if mode == 'S':
    print "SOLVER MODE"
    first_num = enter_integer('first')
    second_num = enter_integer('second')
    third_num = enter_integer('third')
    fourth_num = enter_integer('fourth')
    print "-----------------------"

    nums = [float(first_num), float(second_num), float(third_num), float(fourth_num)]
    find_solutions(nums, mode)

if mode == 'G':
    print "GAME MODE"
    difficulty = enter_difficulty()
    if difficulty == 'B':
        card = generate_card(xrange(2,11), 4)
        print 'Your card is: %s' %str(card)
        check_guess(card)
    elif difficulty == 'I':
        card = generate_card(xrange(2,11), 2, xrange(11,24), 2)
        check_guess(card)
    else:
        print 'No advanced option yet.'
        # print random.randint(2, 23)

# TODO
# Add more cases with parenthesis - probably missing some
# Add option to filter out negative numbers from calculation.
# Group similar calculations together?
# Eliminate calculations that are the same via associate/commutative properties?
# Don't use eval or try to do it safely
# Check that solution equals 24
# Require that only valid characters are in input
# regexp split on operators or parenthesis, but retain operators and parenthesis.
# need to use floats to evaluate
