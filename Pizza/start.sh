pc=$1
main=$2
python3 "$main" input_data/a_an_example.in.txt "${pc}" output_data/a_an_example.out.txt
python3 "$main" input_data/b_basic.in.txt "${pc}" output_data/b_basic.out.txt
python3 "$main" input_data/c_coarse.in.txt "${pc}" output_data/c_coarse.out.txt
python3 "$main" input_data/d_difficult.in.txt "${pc}" output_data/d_difficult.out.txt
python3 "$main" input_data/e_elaborate.in.txt "${pc}" output_data/e_elaborate.out.txt
