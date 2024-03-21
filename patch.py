import os
import math

def create_patch_files(patch_folder, ratio_value, scaling_factor, visual_fixes):

    def make_hex(x, r):
        p = math.floor(math.log(x, 2))
        a = round(16*(p-2) + x / 2**(p-4))
        if a<0: a += 128
        a = 2*a + 1
        h = hex(a).lstrip('0x').rjust(2,'0').upper()
        hex_value = f'0{r}' + h[1] + '02' + h[0] + '1E' 
        print(hex_value)
        return hex_value

    visual_fixesa = visual_fixes[0]
    visual_fixesb = visual_fixes[1]
    visual_fixesc = visual_fixes[2]
    scaling_factor = float(scaling_factor)
    ratio_value = float(ratio_value)
    print(f"The scaling factor is {scaling_factor}.")
    hex_value = make_hex(ratio_value, 0)
    version_variables = ["5.5.1"]
    for version_variable in version_variables:
        file_name = f"main-{version_variable}.pchtxt"
        file_path = os.path.join(patch_folder, file_name)

        if version_variable == "5.5.1":
            nsobidid = "03DCAD95E1AC643072F3A684F6740C8500000000000000000000000000000000"
            replacement_value = "01735BEC"
            visual_fix = visual_fixesa

        patch_content = f'''@nsobid-{nsobidid}

@flag print_values
@flag offset_shift 0x100

# Splatoon 2 [01003bc0000a0000] v5.5.1 - Ultrawide Camera

@enabled
{replacement_value} {hex_value}
@stop

{visual_fix}

// Generated using SPLATOON2-AAR by Fayaz (github.com/fayaz12g/splatoon2-aar)'''
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as patch_file:
            patch_file.write(patch_content)
        print(f"Patch file created: {file_path}")
