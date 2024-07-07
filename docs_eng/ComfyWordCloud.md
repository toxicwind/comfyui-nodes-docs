# Documentation
- Class name: ComfyWordCloud
- Category: 😺dzNodes/WordCloud
- Output node: True
- Repo Ref: https://github.com/chflame163/ComfyUI_WordCloud.git

The ComfyWordCloud node is designed to visualize text data by generating word clouds, which is a graphical indication of the frequency of words in input text. This node helps to identify the most common words and their importance in context and provides a visual summary that can be easily understood and analysed.

# Input types
## Required
- text
    - Text parameters are the main input of the node, containing text data that will be processed to generate the word cloud. It is important because it directly affects the content and distribution of words in the word cloud.
    - Comfy dtype: STRING
    - Python dtype: str
- width
    - The width parameter defines the width of the word cloud image generated, influencing the layout and scaling of visual expressions. It is important to adjust the size of the canvas to the desired width ratio and display dimensions.
    - Comfy dtype: INT
    - Python dtype: int
- height
    - The height sets the height of the word cloud image and, together with the width parameters, determines the overall size and width ratio of the output visualization.
    - Comfy dtype: INT
    - Python dtype: int
- scale
    - Scale parameters adjust the overall size of the word cloud by increasing or reducing the font size of the word. This is essential for fine-tuning the density and appearance of the word cloud.
    - Comfy dtype: FLOAT
    - Python dtype: float
- margin
    - The margin parameter specifies the amount of space that will be left blank on the edge of the word cloud image, which enhances clarity and attention to the central content.
    - Comfy dtype: INT
    - Python dtype: int
- font_path
    - The font path parameter is essential to define the font styles and features used in the word cloud. It affects the visual beauty and readability of the text in the word cloud.
    - Comfy dtype: FONT_PATH
    - Python dtype: str
- min_font_size
    - The smallest font size parameter sets the minimum font size used in the word cloud to ensure that fewer words appear in smaller sizes, which helps the overall hierarchy and the emphasis on more common words.
    - Comfy dtype: INT
    - Python dtype: int
- max_font_size
    - The largest font size parameter determines the largest font size in the word cloud, which is essential to highlight the most frequent words and to establish the visual visibility of the text.
    - Comfy dtype: INT
    - Python dtype: int
- relative_scaling
    - Relatively zoom parameters adjust the font size to the frequency of words, which helps to control the emphasis on more common words in the vocabulary.
    - Comfy dtype: FLOAT
    - Python dtype: float
- colormap
    - Colour mapping parameters are essential for defining the colour scheme of the word cloud, affecting the ability to visualize the attraction and convey different word frequencies through colour changes.
    - Comfy dtype: COLOR_MAP
    - Python dtype: str
- background_color
    - Background colour parameters set the background colour of the word cloud, which acts for overall visual contrasts and the prominence of the text.
    - Comfy dtype: STRING
    - Python dtype: str
- transparent_background
    - A transparent background parameter determines whether the context of the word cloud is transparent, which may be important for adding the word cloud to other images or elements.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- prefer_horizontal
    - A higher-priority-level parameter affects the direction of the word in the word cloud, and a higher value promotes a higher distribution, which may affect the overall layout and readability.
    - Comfy dtype: FLOAT
    - Python dtype: float
- max_words
    - The parameters of the maximum word count limit the number of words displayed in the vocabulary, help to focus on the most relevant and common terms and also affect the clarity of visualization.
    - Comfy dtype: INT
    - Python dtype: int
- repeat
    - Repeated parameters control whether a word can appear several times in the word cloud, which may affect the visual expression of the word frequency and the overall density of the word cloud.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- include_numbers
    - It may be important for some types of text-data analysis to include numerical parameters to determine whether values should be included in the vocabulary.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool
- random_state
    - Random status parameters introduce randomity in the positioning of words in the word cloud, which may lead to different visual outcomes and increase the variability of the layout.
    - Comfy dtype: INT
    - Python dtype: int
- stopwords
    - Disaggregated word parameters allow for the exclusion of common words that may not carry significant significance, thereby optimizing the vocabulary to emphasize more relevant terms.
    - Comfy dtype: STRING
    - Python dtype: str
## Optional
- color_ref_image
    - Colour reference image parameters use a reference image to define the colour board of the word cloud and produce a visually consistent expression that is relevant to the context.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- mask_image
    - The mask image parameters provide a shape or model to limit the layout of the word cloud and ensure that the word is located within the defined mask boundary.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- contour_width
    - The contour parameters adjust the width of the contour around the word cloud to enhance the definition of the word cloud and its separation from the background.
    - Comfy dtype: FLOAT
    - Python dtype: float
- contour_color
    - The contour colour parameters set the colour of the contour around the word cloud and contribute to overall visual contrast and beauty.
    - Comfy dtype: STRING
    - Python dtype: str
- keynote_words
    - Subject-word parameters allow for the designation of words to be emphasized in the vocabulary, which may highlight key themes or topics in the text.
    - Comfy dtype: STRING
    - Python dtype: str
- keynote_weight
    - The weight parameters of the subject matter are adjusted to the weight assigned to the subject word, affecting their visibility and size in the word cloud.
    - Comfy dtype: INT
    - Python dtype: int

# Output types
- image
    - The image output provides the resulting word cloud as a visual expression of the input text, the size and colour of which are adjusted to their frequency and importance.
    - Comfy dtype: IMAGE
    - Python dtype: PIL.Image
- mask
    - The mask output is a binary expression that outlines the shape and boundaries of the word cloud that can be used for further image processing or analysis.
    - Comfy dtype: MASK
    - Python dtype: torch.Tensor

# Usage tips
- Infra type: CPU

# Source code
```
class ComfyWordCloud:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {'required': {'text': ('STRING', {'default': '', 'multiline': True}), 'width': ('INT', {'default': 512}), 'height': ('INT', {'default': 512}), 'scale': ('FLOAT', {'default': 1, 'min': 0.1, 'max': 1000.0, 'step': 0.01}), 'margin': ('INT', {'default': 0}), 'font_path': (font_list,), 'min_font_size': ('INT', {'default': 4}), 'max_font_size': ('INT', {'default': 128}), 'relative_scaling': ('FLOAT', {'default': 0.5, 'min': 0.01, 'max': 1.0, 'step': 0.01}), 'colormap': (COLOR_MAP,), 'background_color': ('STRING', {'default': '#FFFFFF'}), 'transparent_background': ('BOOLEAN', {'default': True}), 'prefer_horizontal': ('FLOAT', {'default': 0.9, 'min': 0.0, 'max': 1.0, 'step': 0.01}), 'max_words': ('INT', {'default': 200}), 'repeat': ('BOOLEAN', {'default': False}), 'include_numbers': ('BOOLEAN', {'default': False}), 'random_state': ('INT', {'default': -1, 'min': -1, 'max': 18446744073709551615}), 'stopwords': ('STRING', {'default': ''})}, 'optional': {'color_ref_image': ('IMAGE',), 'mask_image': ('IMAGE',), 'contour_width': ('FLOAT', {'default': 0, 'min': 0, 'max': 9999, 'step': 0.1}), 'contour_color': ('STRING', {'default': '#000000'}), 'keynote_words': ('STRING', {'default': ''}), 'keynote_weight': ('INT', {'default': 60})}}
    RETURN_TYPES = ('IMAGE', 'MASK')
    RETURN_NAMES = ('image', 'mask')
    FUNCTION = 'wordcloud'
    CATEGORY = '😺dzNodes/WordCloud'
    OUTPUT_NODE = True

    def wordcloud(self, text, width, height, margin, scale, font_path, min_font_size, max_font_size, relative_scaling, colormap, background_color, transparent_background, prefer_horizontal, max_words, repeat, include_numbers, random_state, stopwords, color_ref_image=None, mask_image=None, contour_width=None, contour_color=None, keynote_words=None, keynote_weight=None):
        if text == '':
            text = default_text
            log(f'text input not found, use demo string.')
        freq_dict = WordCloud().process_text(' '.join(jieba.cut(text)))
        if not keynote_words == '':
            keynote_list = list(re.split('[，,\\s*]', keynote_words))
            keynote_list = [x for x in keynote_list if x != '']
            keynote_dict = {keynote_list[i]: keynote_weight + max(freq_dict.values()) for i in range(len(keynote_list))}
            freq_dict.update(keynote_dict)
        log(f'word frequencies dict generated, include {len(freq_dict)} words.')
        font_path = font_dict[font_path]
        if not os.path.exists(font_path):
            font_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.normpath(__file__))), 'font'), 'Alibaba-PuHuiTi-Heavy.ttf')
            log(f'font_path not found, use {font_path}')
        else:
            log(f'font_path = {font_path}')
        stopwords_set = set('')
        if not stopwords == '':
            stopwords_list = re.split('[，,\\s*]', stopwords)
            stopwords_set = set([x for x in stopwords_list if x != ''])
            for item in stopwords_set:
                if item in freq_dict.keys():
                    del freq_dict[item]
        bg_color = background_color
        mode = 'RGB'
        if transparent_background:
            bg_color = None
            mode = 'RGBA'
        if random_state == -1:
            random_state = None
        mask = None
        image_width = width
        image_height = height
        if not mask_image == None:
            p_mask = tensor2pil(mask_image)
            mask = np.array(img_whitebackground(p_mask))
            image_width = p_mask.width
            image_height = p_mask.height
        wc = WordCloud(width=width, height=height, scale=scale, margin=margin, font_path=font_path, min_font_size=min_font_size, max_font_size=max_font_size, relative_scaling=relative_scaling, colormap=colormap, mode=mode, background_color=bg_color, prefer_horizontal=prefer_horizontal, max_words=max_words, repeat=repeat, include_numbers=include_numbers, random_state=random_state, stopwords=stopwords_set, mask=mask, contour_width=contour_width, contour_color=contour_color)
        wc.generate_from_frequencies(freq_dict)
        if not color_ref_image == None:
            p_color_ref_image = tensor2pil(color_ref_image)
            p_color_ref_image = p_color_ref_image.resize((image_width, image_height))
            image_colors = ImageColorGenerator(np.array(p_color_ref_image))
            wc.recolor(color_func=image_colors)
        ret_image = wc.to_image().convert('RGBA')
        ret_mask = getRGBAmask(ret_image)
        return (pil2tensor(ret_image), ret_mask)
```