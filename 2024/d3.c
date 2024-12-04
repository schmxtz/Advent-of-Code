/* 
Input: String containing instructions
Output: Sum of all mul(X,Y) instructions
Example:
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Output: (2*4 + 5*5 + 11*8 + 8*5) = 161
*/

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define __LEFT_DIGIT_STATE__ 4
#define __RIGHT_DIGIT_STATE__ 6
#define __N_STATE__ 2
#define __DONT_OPENING_BRACKET_STATE__ 5
#define __DONT_CLOSING_BRACKET_STATE__ 6

int is_m(int c) { return c == 'm'; }
int is_u(int c) { return c == 'u'; }
int is_l(int c) { return c == 'l'; }
int is_d(int c) { return c == 'd'; }
int is_o(int c) { return c == 'o'; }
int is_n(int c) { return c == 'n'; }
int is_apo(int c) { return c == '\''; }
int is_t(int c) { return c == 't'; }
int is_opening_bracket(int c) { return c == '('; }
int is_comma(int c) { return c == ','; }
int is_closing_bracket(int c) { return c == ')'; }
const int ten_multiples[] = { 0, 1, 10, 100, 1000, 10000, 100000, 1000000};

int chars_to_number(char *digits, int digit_count) {
    int accumulator = 0;
    for (int index = 0; index < digit_count; index++) {
        accumulator += (ten_multiples[digit_count-index] * (digits[index] - '0'));
    }
    return accumulator;
}

int main() {
    int left_number = 0;
    int right_number = 0;
    int data_char;
    long result = 0;
    FILE *file_ptr;
    int (*state_transitions[8]) (int) = {is_m, is_u, is_l, is_opening_bracket, isdigit, is_comma, isdigit, is_closing_bracket};
    int (*state_transitions_dont[7]) (int) = {is_d, is_o, is_n, is_apo, is_t, is_opening_bracket, is_closing_bracket};
    char *left_digits = (char *) malloc(sizeof(char) * 8);
    char *right_digits = (char *) malloc(sizeof(char) * 8);

    file_ptr = fopen("./data/day3.txt", "r");

    int digit_count = 0;
    int counter = 0;
    int match;
    int state = 0;
    int state_dont = 0;
    int instruction_enabled = 1;
    int possible_do = 0;
    int do_ctr = 0;
    int dont_ctr = 0;
    while ((data_char = fgetc(file_ptr)) != EOF) {
        match = state_transitions[state](data_char);
        if (instruction_enabled == 1) {
            switch (state) {
            case __LEFT_DIGIT_STATE__:
                if (match != 0) {
                    left_digits[digit_count] = data_char;
                    digit_count++;
                    break;
                }
                if (digit_count > 0) {
                    left_number = chars_to_number(left_digits, digit_count);
                    digit_count = 0;
                    state++;
                    match = state_transitions[state](data_char);
                    if (match != 0) {
                        state++;
                    }
                    break;
                }
                digit_count = 0;
                state = 0;
                break;
            case __RIGHT_DIGIT_STATE__:
                if (match != 0) {
                    right_digits[digit_count] = data_char;
                    digit_count++;
                    break;
                }
                if (digit_count > 0) {
                    right_number = chars_to_number(right_digits, digit_count);
                    digit_count = 0;
                    state++;
                    match = state_transitions[state](data_char);
                    if (match != 0) {
                        result += (left_number * right_number);
                    }
                }
                digit_count = 0;
                state = 0;
                break;
            default:
                if (match != 0) {
                    state++;
                    state_dont = 0;
                    possible_do = 0;
                }
                else {
                    state = 0;
                    digit_count = 0;
                }
                break;
            } 
        }
        switch (state_dont)
        {
        case __N_STATE__:
            match = state_transitions_dont[state_dont](data_char);
            if (match == 0) {
                state_dont = __DONT_OPENING_BRACKET_STATE__;
                match = state_transitions_dont[state_dont](data_char);
                if (match == 0) {
                    state_dont = 0;
                } else {
                    possible_do = 1;
                }
            }
            state_dont++;
            break;
        case __DONT_CLOSING_BRACKET_STATE__:
            match = state_transitions_dont[state_dont](data_char);
            if (match != 0) {
                if (possible_do == 1) {
                    instruction_enabled = 1;
                    do_ctr++;
                } else {
                    instruction_enabled = 0;
                    dont_ctr++;
                }
            }
            state_dont = 0;
            possible_do = 0;
            break;
        default:
            match = state_transitions_dont[state_dont](data_char);
            if (match != 0) {
                state = 0;
                digit_count = 0;
                state_dont++;
            } else {
                state_dont = 0;
                possible_do = 0;
            }
        }
    }
    fclose(file_ptr);

    /* 
    Input: Same string, but no contains do() and don't() instructions
    Output: Sum of all mul(X,Y) instructions
    Example:
    xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
    Output: (2*4 + 8*5) = 48
    */

    printf("Result: %d\n", result);
    printf("do_ctr: %d, dont_ctr: %d", do_ctr, dont_ctr);
    return 0;
}