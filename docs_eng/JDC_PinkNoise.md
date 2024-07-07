# Documentation
- Class name: PinkNoise
- Category: image/noise
- Output node: False
- Repo Ref: https://github.com/Jordach/comfy-plasma.git

The Pinknoise node is designed to generate images of noise patterns based on the size and colour range specified, which simulates pink noise spectrums. This node is particularly suitable for creating visual content with natural, non-evented pixel intensity distributions that can be used in a variety of scenarios, such as image processing, computer graphics and machine learning data enhancement.

# Input types
## Required
- width
    - Width determines the horizontal dimension of the output image, which is essential to define the canvas that the noise mode will generate. It directly affects the overall size and resolution of the image generated.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Height sets the vertical dimensions of the output image, working with the width parameters to determine the resolution and overall dimensions of the image. It is an important factor in determining the size of the noise mode.
    - Comfy dtype: INT
    - Python dtype: int
- seed
    - Seed values are used to initialize random number generators to ensure that noise patterns are recreated and consistent in the different operations of nodes. This parameter is essential for maintaining the reliability and predictability of noise generation processes.
    - Comfy dtype: INT
    - Python dtype: int
## Optional
- value_min
    - The minimum value sets the lower limit of the strength that produces the noise, allowing the minimum brightness or darkness of the noise mode to be controlled. This parameter affects the overall visual effects of the noise and contributes to the aesthetic or effect required.
    - Comfy dtype: INT
    - Python dtype: int
- value_max
    - The maximum value sets the upper limit of the strength of the noise to ensure that the noise mode does not exceed a certain brightness level. This parameter is essential for achieving balanced and controlled noise distribution.
    - Comfy dtype: INT
    - Python dtype: int
- red_min
    - The minimum red value specifies the minimum allowable value of the red channel in the noise mode, allowing fine-tuning of the colour spectrum and ensuring that the noise generated meets specific colour requirements.
    - Comfy dtype: INT
    - Python dtype: int
- red_max
    - The maximum red value sets the maximum value of the red channel, controls the upper limit of the red colour in the noise mode and contributes to the overall colour balance.
    - Comfy dtype: INT
    - Python dtype: int
- green_min
    - The minimum green value defines the minimum value of the green channel in the noise, allows for precise control of the green component of the noise and ensures that the final image corresponds to the desired colour configuration.
    - Comfy dtype: INT
    - Python dtype: int
- green_max
    - The maximum green value sets the maximum value for the green channel, ensuring that the green tone in the noise mode does not exceed a certain threshold and contributes to overall colour harmony.
    - Comfy dtype: INT
    - Python dtype: int
- blue_min
    - The minimum blue value sets the minimum value for the blue channel, allowing users to control the presence of the blue in the noise mode and to achieve specific visual effects.
    - Comfy dtype: INT
    - Python dtype: int
- blue_max
    - The maximum blue value defines the maximum value of the blue channel, ensuring that the blue tone in the noise mode is within the desired range and contributing to the overall colour scheme.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - Output is an image with pink noise patterns generated according to the specified parameters. This image can be used as texture, background or input for further processing in various applications.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class PinkNoise:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 512, 'min': 128, 'max': 8192, 'step': 8}), 'height': ('INT', {'default': 512, 'min': 128, 'max': 8192, 'step': 8}), 'value_min': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'value_max': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'red_min': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'red_max': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'green_min': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'green_max': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'blue_min': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'blue_max': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'generate_noise'
    CATEGORY = 'image/noise'

    def generate_noise(self, width, height, value_min, value_max, red_min, red_max, green_min, green_max, blue_min, blue_max, seed):
        w = width
        h = height
        aw = copy.deepcopy(w)
        ah = copy.deepcopy(h)
        outimage = Image.new('RGB', (aw, ah))
        random.seed(seed)
        clamp_v_min = value_min
        clamp_v_max = value_max
        clamp_r_min = red_min
        clamp_r_max = red_max
        clamp_g_min = green_min
        clamp_g_max = green_max
        clamp_b_min = blue_min
        clamp_b_max = blue_max
        lv = 0
        mv = 0
        if clamp_v_min == -1:
            lv = 0
        else:
            lv = clamp_v_min
        if clamp_v_max == -1:
            mv = 255
        else:
            mv = clamp_v_max
        lr = 0
        mr = 0
        if clamp_r_min == -1:
            lr = lv
        else:
            lr = clamp_r_min
        if clamp_r_max == -1:
            mr = mv
        else:
            mr = clamp_r_max
        lg = 0
        mg = 0
        if clamp_g_min == -1:
            lg = lv
        else:
            lg = clamp_g_min
        if clamp_g_max == -1:
            mg = mv
        else:
            mg = clamp_g_max
        lb = 0
        mb = 0
        if clamp_b_min == -1:
            lb = lv
        else:
            lb = clamp_b_min
        if clamp_b_max == -1:
            mb = mv
        else:
            mb = clamp_b_max
        pbar = comfy.utils.ProgressBar(ah)
        step = 0
        for y in range(ah):
            for x in range(aw):
                nr = clamp(int(np.power(random.randint(lr, mr) / 255, 1 / 3) * 255), 0, 255)
                ng = clamp(int(np.power(random.randint(lg, mg) / 255, 1 / 3) * 255), 0, 255)
                nb = clamp(int(np.power(random.randint(lb, mb) / 255, 1 / 3) * 255), 0, 255)
                outimage.putpixel((x, y), (nr, ng, nb))
            step += 1
            pbar.update_absolute(step, ah)
        return conv_pil_tensor(outimage)
```