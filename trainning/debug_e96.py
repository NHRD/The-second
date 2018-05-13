e96 = [10.0, 10.2, 10.5, 100]
magnitude = [1,10,100]
target_sum = float(input("Input target sum value:"))
target_pgain = float(input("Input target pre-gain val:"))
r1_det = 0
r2_det = 0
rmpu = 800
dif_target = 200

for k in magnitude:
    for j in e96:
        for i in magnitude:
            ii = i * k/10
            jj = j * k/10
            sum_val = ii + jj
            #print(sum_val)

            if sum_val >= target_sum:
                tag_cal = ii * jj /(ii + jj) + rmpu
                diff = abs(tag_cal - target_pgain)
                print(tag_cal)

                if diff <= dif_target:
                    def_target = diff
                    r1_det = ii
                    r2_det = jj

print("Target nums are {} and {}.".format(r1_det, r2_det))
                