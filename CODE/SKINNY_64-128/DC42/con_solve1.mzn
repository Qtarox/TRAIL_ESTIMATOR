include "table.mzn";

    % Define 4-bit integer variables (0..15)
    var 0..15: k1_6;
var 0..15: k2_6;
var 0..15: k2_6_4;
var 0..15: z_0_99;

    constraint table([k2_6_4, k2_6], sbox_table4);
array[1..4] of int: possible_values0 = [ 0, 1, 12, 13 ]; 
 var 1..4: i0;
 constraint z_0_99 = possible_values0[i0];

    array[0..15, 1..2] of int: sbox_table = 
        array2d(0..15, 1..2, [
            0, 12,  1, 6,  2, 9,  3, 0,
            4, 1,   5, 10, 6, 2,  7, 11,
            8, 3,   9, 8,  10, 5, 11, 13,
            12, 4,  13, 14, 14, 7, 15, 15
        ]);
    array[0..15, 1..2] of int: sbox_table0 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 1 ,2, 2 ,3, 3 ,4, 4 ,5, 5 ,6, 6 ,7, 7 ,8, 8 ,9, 9 ,10, 10 ,11, 11 ,12, 12 ,13, 13 ,14, 14 ,15, 15
 ]);
    array[0..15, 1..2] of int: sbox_table1 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 2 ,2, 4 ,3, 6 ,4, 9 ,5, 11 ,6, 13 ,7, 15 ,8, 1 ,9, 3 ,10, 5 ,11, 7 ,12, 8 ,13, 10 ,14, 12 ,15, 14
 ]);
    array[0..15, 1..2] of int: sbox_table2 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 4 ,2, 9 ,3, 13 ,4, 3 ,5, 7 ,6, 10 ,7, 14 ,8, 2 ,9, 6 ,10, 11 ,11, 15 ,12, 1 ,13, 5 ,14, 8 ,15, 12
 ]);
    array[0..15, 1..2] of int: sbox_table3 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 9 ,2, 3 ,3, 10 ,4, 6 ,5, 15 ,6, 5 ,7, 12 ,8, 4 ,9, 13 ,10, 7 ,11, 14 ,12, 2 ,13, 11 ,14, 1 ,15, 8
 ]);
    array[0..15, 1..2] of int: sbox_table4 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 3 ,2, 6 ,3, 5 ,4, 13 ,5, 14 ,6, 11 ,7, 8 ,8, 9 ,9, 10 ,10, 15 ,11, 12 ,12, 4 ,13, 7 ,14, 2 ,15, 1
 ]);
    array[0..15, 1..2] of int: sbox_table5 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 6 ,2, 13 ,3, 11 ,4, 10 ,5, 12 ,6, 7 ,7, 1 ,8, 3 ,9, 5 ,10, 14 ,11, 8 ,12, 9 ,13, 15 ,14, 4 ,15, 2
 ]);
    array[0..15, 1..2] of int: sbox_table6 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 13 ,2, 10 ,3, 7 ,4, 5 ,5, 8 ,6, 15 ,7, 2 ,8, 6 ,9, 11 ,10, 12 ,11, 1 ,12, 3 ,13, 14 ,14, 9 ,15, 4
 ]);
    array[0..15, 1..2] of int: sbox_table7 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 10 ,2, 5 ,3, 15 ,4, 11 ,5, 1 ,6, 14 ,7, 4 ,8, 13 ,9, 7 ,10, 8 ,11, 2 ,12, 6 ,13, 12 ,14, 3 ,15, 9
 ]);
    array[0..15, 1..2] of int: sbox_table8 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 5 ,2, 11 ,3, 14 ,4, 7 ,5, 2 ,6, 12 ,7, 9 ,8, 10 ,9, 15 ,10, 1 ,11, 4 ,12, 13 ,13, 8 ,14, 6 ,15, 3
 ]);
    array[0..15, 1..2] of int: sbox_table9 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 11 ,2, 7 ,3, 12 ,4, 15 ,5, 4 ,6, 8 ,7, 3 ,8, 5 ,9, 14 ,10, 2 ,11, 9 ,12, 10 ,13, 1 ,14, 13 ,15, 6
 ]);
    array[0..15, 1..2] of int: sbox_table10 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 7 ,2, 15 ,3, 8 ,4, 14 ,5, 9 ,6, 1 ,7, 6 ,8, 11 ,9, 12 ,10, 4 ,11, 3 ,12, 5 ,13, 2 ,14, 10 ,15, 13
 ]);
    array[0..15, 1..2] of int: sbox_table11 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 15 ,2, 14 ,3, 1 ,4, 12 ,5, 3 ,6, 2 ,7, 13 ,8, 7 ,9, 8 ,10, 9 ,11, 6 ,12, 11 ,13, 4 ,14, 5 ,15, 10
 ]);
    array[0..15, 1..2] of int: sbox_table12 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 14 ,2, 12 ,3, 2 ,4, 8 ,5, 6 ,6, 4 ,7, 10 ,8, 15 ,9, 1 ,10, 3 ,11, 13 ,12, 7 ,13, 9 ,14, 11 ,15, 5
 ]);
    array[0..15, 1..2] of int: sbox_table13 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 12 ,2, 8 ,3, 4 ,4, 1 ,5, 13 ,6, 9 ,7, 5 ,8, 14 ,9, 2 ,10, 6 ,11, 10 ,12, 15 ,13, 3 ,14, 7 ,15, 11
 ]);
    array[0..15, 1..2] of int: sbox_table14 =
       array2d(0..15, 1..2, [
     0, 0 ,1, 8 ,2, 1 ,3, 9 ,4, 2 ,5, 10 ,6, 3 ,7, 11 ,8, 12 ,9, 4 ,10, 13 ,11, 5 ,12, 14 ,13, 6 ,14, 15 ,15, 7
 ]);


    % Predicate for bitwise XOR (n variables)
    predicate int2bin(var 0..15: x, array[0..3] of var bool: bits) =
        (bits[0] = (x div 1) mod 2) /\
        (bits[1] = (x div 2) mod 2) /\
        (bits[2] = (x div 4) mod 2) /\
        (bits[3] = (x div 8) mod 2);


    