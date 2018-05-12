e96 = [1,1,2]
magnitude = [1,1,2]
target_sum = float(input("Input target value:"))
target_num = float(input("Input target num:"))
a_det = 0
b_det = 0
fixed_val = 100
def_target = 2

for i in e96:
    for j in e96:
        for k in magnitude:
            ii = i/k
            jj = j/k
            sum_val = ii + jj
            print(sum_val)
            
            if sum_val > target_sum:
                tag_cal = (ii + jj)/fixed_val + ii + jj
                diff = (tag_cal - target_num)

                if diff < def_target:
                    def_target = diff
                    a_det = i
                    b_det = j

print("Target nums are {} and {}.".format(a_det, b_det))
                