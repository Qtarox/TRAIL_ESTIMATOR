import re
from CP_SOLVER.auto_func import *
from CP_SOLVER.con_solve import cons_cp_solve
from cons_16r_lbk import *

        
# Z10={'z_0_99': {12, 4, 6, 14}, 'z_1_99': {1, 2, 4, 7}}
def trans_equ(input_text,file_name,variable_constraints):
    variables = set(re.findall(r'[a-z]_\d+_\d+|k_\d+', input_text))

    variable_declarations = "\n".join(f"var 0..15: {var};" for var in sorted(variables))


    xor_constraints = []
    sbox_constraints = []
    range_constraints = []
    type_lst=[]
    for line in input_text.strip().split("\n"):
        line = re.sub(r'[\[\]]', '', line) 
        line = line.replace("= 0", "").strip()
        
    
        match = re.match(r'\+?\s*(x_\d+_\d+)\s*\+\s*(y_\d+_\d+)', line)
        
        if match:
            x_var, y_var = match.groups()
            number=x_var[-1]
            sbox_constraints.append(f"constraint table([{x_var}, {y_var}], sbox_table{number});")
        else:
            vars_in_eq = re.findall(r'[a-z]_\d+_\d+|k_\d+', line)
            if len(vars_in_eq) > 1:
                constraint_type = f"bit_xor{len(vars_in_eq)}"
                xor_constraints.append(f"constraint {constraint_type}({', '.join(vars_in_eq)});")
                type_lst.append(constraint_type)
    cnt=0
    for var in sorted(variables):
        if var in variable_constraints:
            values = ", ".join(map(str, variable_constraints[var])) 
            range_constraints.append(f"array[1..{ len(variable_constraints[var]) }] of int: possible_values{cnt} = [ {values} ]; \n var 1..{ len(variable_constraints[var]) }: i{cnt};\n constraint {var} = possible_values{cnt}[i{cnt}];")
            # range_constraints.append(f"set of int: possible_values{cnt} = {{ {values} }};\n var possible_values{cnt} : {var};")
            cnt+=1
    # range_constraints.append("constraint k_26 in {1, 2, 4, 7};")



    constraint_definitions = "\n".join(xor_constraints + sbox_constraints + range_constraints)


    minizinc_code = f"""include "table.mzn";

    % Define 4-bit integer variables (0..15)
    {variable_declarations}

    {constraint_definitions}

array[0..15, 1..2] of int: sbox_table0 =
        array2d(0..15, 1..2, [
       0 , 14 ,  1 , 9 ,  2 , 15 ,  3 , 0 ,  4 , 13 ,  5 , 4 ,  6 , 10 ,  7 , 11 ,  8 , 1 ,  9 , 2 ,  10 , 8 ,  11 , 3 ,  12 , 7 ,  13 , 6 ,  14 , 12 ,  15 , 5
         ]);
array[0..15, 1..2] of int: sbox_table1 =
        array2d(0..15, 1..2, [
       0 , 4 ,  1 , 11 ,  2 , 14 ,  3 , 9 ,  4 , 15 ,  5 , 13 ,  6 , 0 ,  7 , 10 ,  8 , 7 ,  9 , 12 ,  10 , 5 ,  11 , 6 ,  12 , 2 ,  13 , 8 ,  14 , 1 ,  15 , 3
         ]);
array[0..15, 1..2] of int: sbox_table2 =
        array2d(0..15, 1..2, [
       0 , 1 ,  1 , 14 ,  2 , 7 ,  3 , 12 ,  4 , 15 ,  5 , 13 ,  6 , 0 ,  7 , 6 ,  8 , 11 ,  9 , 5 ,  10 , 9 ,  11 , 3 ,  12 , 2 ,  13 , 4 ,  14 , 8 ,  15 , 10
         ]);
array[0..15, 1..2] of int: sbox_table3 =
        array2d(0..15, 1..2, [
       0 , 7 ,  1 , 6 ,  2 , 8 ,  3 , 11 ,  4 , 0 ,  5 , 15 ,  6 , 3 ,  7 , 14 ,  8 , 9 ,  9 , 10 ,  10 , 12 ,  11 , 13 ,  12 , 5 ,  13 , 2 ,  14 , 4 ,  15 , 1
         ]);
array[0..15, 1..2] of int: sbox_table4 =
        array2d(0..15, 1..2, [
       0 , 14 ,  1 , 5 ,  2 , 15 ,  3 , 0 ,  4 , 7 ,  5 , 2 ,  6 , 12 ,  7 , 13 ,  8 , 1 ,  9 , 8 ,  10 , 4 ,  11 , 9 ,  12 , 11 ,  13 , 10 ,  14 , 6 ,  15 , 3
         ]);
array[0..15, 1..2] of int: sbox_table5 =
        array2d(0..15, 1..2, [
       0 , 2 ,  1 , 13 ,  2 , 11 ,  3 , 12 ,  4 , 15 ,  5 , 14 ,  6 , 0 ,  7 , 9 ,  8 , 7 ,  9 , 10 ,  10 , 6 ,  11 , 3 ,  12 , 1 ,  13 , 8 ,  14 , 4 ,  15 , 5
         ]);
array[0..15, 1..2] of int: sbox_table6 =
        array2d(0..15, 1..2, [
       0 , 11 ,  1 , 9 ,  2 , 4 ,  3 , 14 ,  4 , 0 ,  5 , 15 ,  6 , 10 ,  7 , 13 ,  8 , 6 ,  9 , 12 ,  10 , 5 ,  11 , 7 ,  12 , 3 ,  13 , 8 ,  14 , 1 ,  15 , 2
         ]);
array[0..15, 1..2] of int: sbox_table7 =
        array2d(0..15, 1..2, [
       0 , 13 ,  1 , 10 ,  2 , 15 ,  3 , 0 ,  4 , 14 ,  5 , 4 ,  6 , 9 ,  7 , 11 ,  8 , 2 ,  9 , 1 ,  10 , 8 ,  11 , 3 ,  12 , 7 ,  13 , 5 ,  14 , 12 ,  15 , 6
         ]);

    % Predicate for bitwise XOR (n variables)
    predicate int2bin(var 0..15: x, array[0..3] of var bool: bits) =
        (bits[0] = (x div 1) mod 2) /\\
        (bits[1] = (x div 2) mod 2) /\\
        (bits[2] = (x div 4) mod 2) /\\
        (bits[3] = (x div 8) mod 2);


    """
    ind_lst=[]
    for i in type_lst:
        num=int(i[7:])
        if(num not in ind_lst):
            ind_lst.append(num)
    print(ind_lst)
    for i in ind_lst:
        minizinc_code+= gen_func_n(i)

    print(minizinc_code)
    with open(file_name, "w") as fw:
        fw.write(minizinc_code)
    fw.close()

def SOLVE_CP(cons_t,z,base_ind,f_pth):
    
    cons_name=f_pth+"./con_solve"+str(base_ind)+".mzn"
    solu_txt=f_pth+"./solve_results"+str(base_ind)+".txt"
    trans_equ(cons_t,cons_name,z)
    print(cons_cp_solve(solu_txt,cons_name))
if __name__=="__main__":
    cons_t=CONS1
    z=Z1

    SOLVE_CP(cons_t,z,0)

    
