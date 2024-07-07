# Documentation
- Class name: FaceEmbedDistance
- Category: FaceAnalysis
- Output node: False
- Repo Ref: https://github.com/cubiq/ComfyUI_FaceAnalysis.git

FaceEmbedDistance nodes are designed to analyse and compare facial features using Euclid and cosine distance measurements. It processes input images and reference images to determine similarities and to facilitate facial recognition and validation. The main objective of this node is to enhance facial recognition tasks by providing a comprehensive analysis of facial embedding.

# Input types
## Required
- analysis_models
    - This parameter, which contains the models required for facial testing and embedded extraction, is essential for the node to perform facial analysis functions.
    - Comfy dtype: DICTIONARY
    - Python dtype: Dict[str, Any]
- reference
    - Reference images are essential for comparison with input images. They have a significant impact on the ability of nodes to analyse facial similarities as baselines for calculating distance and identifying matching.
    - Comfy dtype: LIST
    - Python dtype: List[PIL.Image.Image]
- image
    - These are images that will be analysed and compared with reference images. The quality and relevance of these images directly influence the output of nodes and their validity in facial recognition.
    - Comfy dtype: LIST
    - Python dtype: List[PIL.Image.Image]
## Optional
- filter_thresh_eucl
    - The Euclid threshold is used to filter images that are too different. It plays a key role in controlling the degree of rigour in the assessment of facial similarities.
    - Comfy dtype: FLOAT
    - Python dtype: float
- filter_thresh_cos
    - The cosine distance threshold is used in conjunction with the Euclid threshold to fine-tune facial similarities assessment, focusing on the direction of facial implantation and not just their range.
    - Comfy dtype: FLOAT
    - Python dtype: float
- generate_image_overlay
    - When this option is enabled, it generates a layer of coverage on the input image, displays a distance measure, and thus provides a visual representation of the results of facial analysis.
    - Comfy dtype: BOOLEAN
    - Python dtype: bool

# Output types
- IMAGE
    - Output images, which may contain layers, represent the analysed input images. They are essential for visual validation and further analysis.
    - Comfy dtype: LIST
    - Python dtype: List[PIL.Image.Image]
- euclidean
    - This output provides Euro-Grail distance values, quantifys the differences between reference and input images and helps to assess facial similarities.
    - Comfy dtype: FLOAT
    - Python dtype: float
- cosine
    - Cosine distance values provide a measure of directional difference between facial embedding and supplement Euclidian distance to allow for more detailed facial similarities assessment.
    - Comfy dtype: FLOAT
    - Python dtype: float
- csv
    - The CSV output contains structured records of facial analysis, including distance measures, which can be used for further statistical analysis and reporting.
    - Comfy dtype: STRING
    - Python dtype: str

# Usage tips
- Infra type: CPU

# Source code
```
class FaceEmbedDistance:

    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'analysis_models': ('ANALYSIS_MODELS',), 'reference': ('IMAGE',), 'image': ('IMAGE',), 'filter_thresh_eucl': ('FLOAT', {'default': 1.0, 'min': 0.001, 'max': 2.0, 'step': 0.001}), 'filter_thresh_cos': ('FLOAT', {'default': 1.0, 'min': 0.001, 'max': 2.0, 'step': 0.001}), 'generate_image_overlay': ('BOOLEAN', {'default': True})}}
    RETURN_TYPES = ('IMAGE', 'FLOAT', 'FLOAT', 'STRING')
    RETURN_NAMES = ('IMAGE', 'euclidean', 'cosine', 'csv')
    OUTPUT_NODE = True
    FUNCTION = 'analize'
    CATEGORY = 'FaceAnalysis'

    def analize(self, analysis_models, reference, image, filter_thresh_eucl=1.0, filter_thresh_cos=1.0, generate_image_overlay=True):
        if generate_image_overlay:
            font = ImageFont.truetype(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Inconsolata.otf'), 32)
            background_color = ImageColor.getrgb('#000000AA')
            txt_height = font.getmask('Q').getbbox()[3] + font.getmetrics()[1]
        self.analysis_models = analysis_models
        ref = []
        for i in reference:
            ref_emb = self.get_descriptor(np.array(T.ToPILImage()(i.permute(2, 0, 1)).convert('RGB')))
            if ref_emb is not None:
                ref.append(torch.from_numpy(ref_emb))
        if ref == []:
            raise Exception('No face detected in reference image')
        ref = torch.stack(ref)
        ref = np.array(torch.mean(ref, dim=0))
        out = []
        out_eucl = []
        out_cos = []
        for i in image:
            img = np.array(T.ToPILImage()(i.permute(2, 0, 1)).convert('RGB'))
            img = self.get_descriptor(img)
            if img is None:
                eucl_dist = 1.0
                cos_dist = 1.0
            elif np.array_equal(ref, img):
                eucl_dist = 0.0
                cos_dist = 0.0
            else:
                eucl_dist = np.float64(np.linalg.norm(ref - img))
                cos_dist = 1 - np.dot(ref, img) / (np.linalg.norm(ref) * np.linalg.norm(img))
            if eucl_dist <= filter_thresh_eucl and cos_dist <= filter_thresh_cos:
                print(f'\x1b[96mFace Analysis: Euclidean: {eucl_dist}, Cosine: {cos_dist}\x1b[0m')
                if generate_image_overlay:
                    tmp = T.ToPILImage()(i.permute(2, 0, 1)).convert('RGBA')
                    txt = Image.new('RGBA', (image.shape[2], txt_height), color=background_color)
                    draw = ImageDraw.Draw(txt)
                    draw.text((0, 0), f'EUC: {round(eucl_dist, 3)} | COS: {round(cos_dist, 3)}', font=font, fill=(255, 255, 255, 255))
                    composite = Image.new('RGBA', tmp.size)
                    composite.paste(txt, (0, tmp.height - txt.height))
                    composite = Image.alpha_composite(tmp, composite)
                    out.append(T.ToTensor()(composite).permute(1, 2, 0))
                else:
                    out.append(i)
                out_eucl.append(eucl_dist)
                out_cos.append(cos_dist)
        if not out:
            raise Exception('No image matches the filter criteria.')
        img = torch.stack(out)
        csv = 'id,euclidean,cosine\n'
        if len(out_eucl) == 1:
            out_eucl = out_eucl[0]
            out_cos = out_cos[0]
            csv += f'0,{out_eucl},{out_cos}\n'
        else:
            for (id, (eucl, cos)) in enumerate(zip(out_eucl, out_cos)):
                csv += f'{id},{eucl},{cos}\n'
        return (img, out_eucl, out_cos, csv)

    def get_descriptor(self, image):
        embeds = None
        if self.analysis_models['library'] == 'insightface':
            faces = self.analysis_models['detector'].get(image)
            if len(faces) > 0:
                embeds = faces[0].normed_embedding
        else:
            faces = self.analysis_models['detector'](image)
            if len(faces) > 0:
                shape = self.analysis_models['shape_predict'](image, faces[0])
                embeds = np.array(self.analysis_models['face_recog'].compute_face_descriptor(image, shape))
        return embeds
```