include "table.mzn";

    % Define 4-bit integer variables (0..15)
    var 0..15: k_63;
var 0..15: k_65;
var 0..15: k_73;
var 0..15: k_82;
var 0..15: k_83;
var 0..15: k_87;
var 0..15: k_89;
var 0..15: k_92;
var 0..15: x_10_2;
var 0..15: x_11_3;
var 0..15: y_10_2;
var 0..15: y_11_3;
var 0..15: z_0_99;
var 0..15: z_1_99;
var 0..15: z_2_99;

    constraint bit_xor7(z_0_99, y_10_2, x_11_3, k_63, k_65, k_73, k_83);
constraint bit_xor4(z_1_99, x_10_2, k_82, k_92);
constraint bit_xor4(z_2_99, y_11_3, k_87, k_89);
constraint table([x_10_2, y_10_2], sbox_table2);
constraint table([x_11_3, y_11_3], sbox_table3);
array[1..4] of int: possible_values0 = [ 6, 7, 12, 13 ]; 
 var 1..4: i0;
 constraint z_0_99 = possible_values0[i0];
array[1..4] of int: possible_values1 = [ 0, 1, 10, 11 ]; 
 var 1..4: i1;
 constraint z_1_99 = possible_values1[i1];
array[1..4] of int: possible_values2 = [ 1, 3, 8, 10 ]; 
 var 1..4: i2;
 constraint z_2_99 = possible_values2[i2];

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
        (bits[0] = (x div 1) mod 2) /\
        (bits[1] = (x div 2) mod 2) /\
        (bits[2] = (x div 4) mod 2) /\
        (bits[3] = (x div 8) mod 2);


    
predicate bit_xor7(var 0..15: x0, var 0..15: x1, var 0..15: x2, var 0..15: x3, var 0..15: x4, var 0..15: x5, var 0..15: x6) =
    let { 
        array[0..3] of var bool: x0_bits,
        array[0..3] of var bool: x1_bits,
        array[0..3] of var bool: x2_bits,
        array[0..3] of var bool: x3_bits,
        array[0..3] of var bool: x4_bits,
        array[0..3] of var bool: x5_bits,
        array[0..3] of var bool: x6_bits
    } in (
        int2bin(x0, x0_bits) /\ 
        int2bin(x1, x1_bits) /\ 
        int2bin(x2, x2_bits) /\ 
        int2bin(x3, x3_bits) /\ 
        int2bin(x4, x4_bits) /\ 
        int2bin(x5, x5_bits) /\ 
        int2bin(x6, x6_bits) /\ 
        forall(i in 0..3)(
            ( x0_bits[i] + x1_bits[i] + x2_bits[i] + x3_bits[i] + x4_bits[i] + x5_bits[i] + x6_bits[i]) mod 2 = 0
        )
    );

predicate bit_xor4(var 0..15: x0, var 0..15: x1, var 0..15: x2, var 0..15: x3) =
    let { 
        array[0..3] of var bool: x0_bits,
        array[0..3] of var bool: x1_bits,
        array[0..3] of var bool: x2_bits,
        array[0..3] of var bool: x3_bits
    } in (
        int2bin(x0, x0_bits) /\ 
        int2bin(x1, x1_bits) /\ 
        int2bin(x2, x2_bits) /\ 
        int2bin(x3, x3_bits) /\ 
        forall(i in 0..3)(
            ( x0_bits[i] + x1_bits[i] + x2_bits[i] + x3_bits[i]) mod 2 = 0
        )
    );
