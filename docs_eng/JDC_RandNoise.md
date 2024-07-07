# Documentation
- Class name: RandNoise
- Category: image/noise
- Output node: False
- Repo Ref: https://github.com/Jordach/comfy-plasma.git

The Randnoise node is designed to generate random noise images. It operates by creating images of specified dimensions and applying random colours within the user-defined range for each pixel. The function of the node is concentrated in generating noise patterns that can be used for various image processing tasks, such as data enhancement or noise filtering.

# Input types
## Required
- width
    - The width parameter specifies the width of the noise image generated. It is essential because it determines the horizontal resolution of the output image, affecting the overall size of the image and the level of detail of the noise pattern.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The altimeter sets the vertical dimensions of the noise image. It is important for building a vertical resolution and defines the overall size of the noise mode with width.
    - Comfy dtype: INT
    - Python dtype: int
- value_min
    - The value_min parameter allows the minimum amount of noise intensity to be set. It affects the lower limit of the random colour value assigned to each pixel, thus affecting the overall brightness of the noise image.
    - Comfy dtype: INT
    - Python dtype: int
- value_max
    - The value_max parameter sets the upper limit for noise intensity. It works with the value_min to define the random range of values that can be assigned to each pixel and form the dynamic range of noise.
    - Comfy dtype: INT
    - Python dtype: int
- red_min
    - The red_min parameter specifies the minimum value of the red channel in the noise image. It is important to control the red colour strength in the noise and helps the image's final colour composition.
    - Comfy dtype: INT
    - Python dtype: int
- red_max
    - The red_max parameter sets the maximum value of the red channel. Together with the red_min, it determines the range of red colour values in the noise, affecting the overall colour of the noise pattern.
    - Comfy dtype: INT
    - Python dtype: int
- green_min
    - The green_min parameter establishes the minimum value of the green channel. It plays a role in determining the intensity of the green colour in the noise, affecting the colour balance of the image.
    - Comfy dtype: INT
    - Python dtype: int
- green_max
    - Green_max parameters define the maximum value of the green channel. Together with green_min, it sets the range of green channel colour values, which affects the dynamics of green in noise images.
    - Comfy dtype: INT
    - Python dtype: int
- blue_min
    - The blue_min parameter sets the minimum value of the blue channel in the noise image. It is essential to control the strength of the blue colour and helps to generate the final colour formula for the noise.
    - Comfy dtype: INT
    - Python dtype: int
- blue_max
    - The blue_max parameter specifies the maximum value for the blue channel. Together with the blue_min, it determines the range of blue colour values in the noise and affects the overall colour composition of the image.
    - Comfy dtype: INT
    - Python dtype: int
- seed
    - The Seed parameter is used to initialize the random number generator to ensure repeatability of noise patterns. It is important when you need to generate the same noise image in different operations.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The output of the Randnoise node is an image containing random noise. This image can be used for a variety of purposes, such as adding noise data to machine learning, testing image processing algorithms or creating visual effects.
    - Comfy dtype: IMAGE
    - Python dtype: Tuple[str, torch.Tensor]

# Usage tips
- Infra type: CPU

# Source code
```
class RandNoise:

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
                nr = random.randint(lr, mr)
                ng = random.randint(lg, mg)
                nb = random.randint(lb, mb)
                outimage.putpixel((x, y), (nr, ng, nb))
            step += 1
            pbar.update_absolute(step, ah)
        return conv_pil_tensor(outimage)
```