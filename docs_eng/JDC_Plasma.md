# Documentation
- Class name: PlasmaNoise
- Category: image/noise
- Output node: False
- Repo Ref: https://github.com/Jordach/comfy-plasma.git

Plasmanoise node is designed to generate noise patterns similar to plasma. It creates the basic image by using fractal noise algorithms, and then adjusts the colour channel and the clamp to produce visual enrichment and diversity of output. This node is particularly suitable for creating texture or background with natural, organic senses.

# Input types
## Required
- width
    - The width parameter defines the width in which the image is generated. It is essential to determine the overall size of the output and affects the details and resolution of the noise pattern.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - Altitude parameters set the height at which the image is generated. It works with width to determine the vertical ratio and overall size of the image.
    - Comfy dtype: INT
    - Python dtype: int
- turbulence
    - The flow parameters control the level of detail in the noise mode. Higher values produce more complex and variable noises, while lower values produce more smooth and evener patterns.
    - Comfy dtype: FLOAT
    - Python dtype: float
- value_min
    - The value_min parameter allows minimum values to be set for noise mode that can be used to adjust overall brightness or create specific visual effects.
    - Comfy dtype: INT
    - Python dtype: int
- value_max
    - Value_max parameters set maximum values for noise mode that can be used to control contrasts or achieve the aesthetic effects required.
    - Comfy dtype: INT
    - Python dtype: int
- red_min
    - Red_min parameters specify a minimum value for the red channel to fine-tune the colour balance and saturation within the noise mode.
    - Comfy dtype: INT
    - Python dtype: int
- red_max
    - Red_max parameters determine the maximum value of the red channel and allow control of the strength and vitality of the red colour in the noise mode.
    - Comfy dtype: INT
    - Python dtype: int
- green_min
    - The green_min parameter sets the minimum value for the green channel, which is important for achieving the required colour composition and harmony in the noise mode.
    - Comfy dtype: INT
    - Python dtype: int
- green_max
    - Green_max parameters control the maximum value of the green channel, affecting the overall tone of noise patterns and the prominence of green in them.
    - Comfy dtype: INT
    - Python dtype: int
- blue_min
    - The blue_min parameter defines the minimum value of the blue channel, which can be adjusted to create a specific colour mood or some visual aspect of the enhanced noise mode.
    - Comfy dtype: INT
    - Python dtype: int
- blue_max
    - The blue_max parameter sets the maximum value for the blue channel, which is essential to define the depth and abundance of the blue shadow in the noise mode.
    - Comfy dtype: INT
    - Python dtype: int
- seed
    - Seed parameters are used to initialize random number generators to ensure that results are repeated when using the same feed values. This is particularly useful for generating consistent noise patterns in multiple cases.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- IMAGE
    - The IMAGE output provides a plasma noise mode generated as an image. It is the final result of node processing and represents the final visual result of the noise generation algorithm.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image.Image

# Usage tips
- Infra type: CPU

# Source code
```
class PlasmaNoise:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'width': ('INT', {'default': 512, 'min': 128, 'max': 8192, 'step': 8}), 'height': ('INT', {'default': 512, 'min': 128, 'max': 8192, 'step': 8}), 'turbulence': ('FLOAT', {'default': 2.75, 'min': 0.5, 'max': 32, 'step': 0.01}), 'value_min': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'value_max': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'red_min': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'red_max': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'green_min': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'green_max': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'blue_min': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'blue_max': ('INT', {'default': -1, 'min': -1, 'max': 255, 'step': 1}), 'seed': ('INT', {'default': 0, 'min': 0, 'max': 18446744073709551615})}}
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = 'generate_plasma'
    CATEGORY = 'image/noise'

    def generate_plasma(self, width, height, turbulence, value_min, value_max, red_min, red_max, green_min, green_max, blue_min, blue_max, seed):
        w = width
        h = height
        aw = copy.deepcopy(w)
        ah = copy.deepcopy(h)
        outimage = Image.new('RGB', (aw, ah))
        if w >= h:
            h = w
        else:
            w = h
        clamp_v_min = value_min
        clamp_v_max = value_max
        clamp_r_min = red_min
        clamp_r_max = red_max
        clamp_g_min = green_min
        clamp_g_max = green_max
        clamp_b_min = blue_min
        clamp_b_max = blue_max
        roughness = turbulence
        pixmap = []
        random.seed(seed)

        def adjust(xa, ya, x, y, xb, yb):
            if pixmap[x][y] == 0:
                d = math.fabs(xa - xb) + math.fabs(ya - yb)
                v = (pixmap[xa][ya] + pixmap[xb][yb]) / 2.0 + (random.random() - 0.555) * d * roughness
                c = int(math.fabs(v + random.randint(-48, 48)))
                if c < 0:
                    c = 0
                elif c > 255:
                    c = 255
                pixmap[x][y] = c

        def subdivide(x1, y1, x2, y2):
            if not (x2 - x1 < 2.0 and y2 - y1 < 2.0):
                x = int((x1 + x2) / 2.0)
                y = int((y1 + y2) / 2.0)
                adjust(x1, y1, x, y1, x2, y1)
                adjust(x2, y1, x2, y, x2, y2)
                adjust(x1, y2, x, y2, x2, y2)
                adjust(x1, y1, x1, y, x1, y2)
                if pixmap[x][y] == 0:
                    v = int((pixmap[x1][y1] + pixmap[x2][y1] + pixmap[x2][y2] + pixmap[x1][y2]) / 4.0)
                    pixmap[x][y] = v
                subdivide(x1, y1, x, y)
                subdivide(x, y1, x2, y)
                subdivide(x, y, x2, y2)
                subdivide(x1, y, x, y2)
        pbar = comfy.utils.ProgressBar(4)
        step = 0
        pixmap = [[0 for i in range(h)] for j in range(w)]
        pixmap[0][0] = random.randint(0, 255)
        pixmap[w - 1][0] = random.randint(0, 255)
        pixmap[w - 1][h - 1] = random.randint(0, 255)
        pixmap[0][h - 1] = random.randint(0, 255)
        subdivide(0, 0, w - 1, h - 1)
        r = copy.deepcopy(pixmap)
        step += 1
        pbar.update_absolute(step, 4)
        pixmap = [[0 for i in range(h)] for j in range(w)]
        pixmap[0][0] = random.randint(0, 255)
        pixmap[w - 1][0] = random.randint(0, 255)
        pixmap[w - 1][h - 1] = random.randint(0, 255)
        pixmap[0][h - 1] = random.randint(0, 255)
        subdivide(0, 0, w - 1, h - 1)
        g = copy.deepcopy(pixmap)
        step += 1
        pbar.update_absolute(step, 4)
        pixmap = [[0 for i in range(h)] for j in range(w)]
        pixmap[0][0] = random.randint(0, 255)
        pixmap[w - 1][0] = random.randint(0, 255)
        pixmap[w - 1][h - 1] = random.randint(0, 255)
        pixmap[0][h - 1] = random.randint(0, 255)
        subdivide(0, 0, w - 1, h - 1)
        b = copy.deepcopy(pixmap)
        step += 1
        pbar.update_absolute(step, 4)
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
        for y in range(ah):
            for x in range(aw):
                nr = int(remap(r[x][y], 0, 255, lr, mr))
                ng = int(remap(g[x][y], 0, 255, lg, mg))
                nb = int(remap(b[x][y], 0, 255, lb, mb))
                outimage.putpixel((x, y), (nr, ng, nb))
        step += 1
        pbar.update_absolute(step, 4)
        return conv_pil_tensor(outimage)
```