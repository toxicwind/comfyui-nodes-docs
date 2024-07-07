import os
import re
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, MarianForCausalLM, AutoModel, pipeline

# Model dictionary
models_dict = {
    'opus': 'Helsinki-NLP/opus-mt-zh-en',
    'nllb-3.3B': 'facebook/nllb-200-3.3B',
    'nllb-distilled-600M': 'facebook/nllb-200-distilled-600M',
    'nllb-distilled-1.3B': 'facebook/nllb-200-distilled-1.3B',
}

def load_model(model_name):
    print(f'\tLoading model: {model_name}')
    model = AutoModelForSeq2SeqLM.from_pretrained(models_dict[model_name])
    tokenizer = AutoTokenizer.from_pretrained(models_dict[model_name], use_fast=True)
    return model, tokenizer

def extract_chinese_lines(text):
    lines = text.split('\n')
    chinese_lines = []
    for i, line in enumerate(lines):
        if re.search(r'[\u4e00-\u9fff]', line):
            leading_whitespace = re.match(r'^\s*', line).group()
            trailing_whitespace = re.match(r'.*?(\s*)$', line).group(1)
            line_content = line.strip()
            if line_content.startswith('- '):
                line_content = line_content[2:]
                prefix = '- '
            else:
                prefix = ''
            chinese_lines.append((i, line_content, leading_whitespace, trailing_whitespace, prefix))
    return chinese_lines

def translate_batch(translator, batch_texts):
    outputs = translator(batch_texts, return_text=True, clean_up_tokenization_spaces=True)
    return [output['translation_text'] if not output['translation_text'].lower().startswith("i don") else original for output, original in zip(outputs, batch_texts)]

def translate_lines(translator, text, lines):
    lines_split = text.split('\n')
    batch_texts = [line for _, line, _, _, _ in lines]
    translations = translate_batch(translator, batch_texts)

    for (i, _, leading_whitespace, trailing_whitespace, prefix), translation in zip(lines, translations):
        lines_split[i] = leading_whitespace + prefix + translation + trailing_whitespace

    return '\n'.join(lines_split)

def list_md_files(folder_path):
    return [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.md')]

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def translate_folder(source, target, folder_path, output_folder, model_name='opus'):
    model, tokenizer = load_model(model_name)
    translator = pipeline(
        "translation", model=model, tokenizer=tokenizer, src_lang=source, tgt_lang=target, device=0
    )

    md_files = list_md_files(folder_path)
    for md_file in md_files:
        output_file_path = os.path.join(output_folder, os.path.basename(md_file))
        if os.path.exists(output_file_path):
            print(f'Skipping already translated file: {md_file}')
            continue

        print(f'Translating file: {md_file}')
        content = read_file(md_file)
        chinese_lines = extract_chinese_lines(content)
        if chinese_lines:
            translated_content = translate_lines(translator, content, chinese_lines)
        else:
            translated_content = content
            print(f'No Chinese text found in file: {md_file}')
        
        write_file(output_file_path, translated_content)
        print(f'Translated file saved to: {output_file_path}')

if __name__ == '__main__':
    source_language = 'zho'
    target_language = 'eng'
    input_folder = 'D:\\sd\\ComfyUI\\custom_nodes\\comfyui-nodes-docs\\docs'
    output_folder = 'D:\\sd\\ComfyUI\\custom_nodes\\comfyui-nodes-docs\\docs_eng'
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    translate_folder(source_language, target_language, input_folder, output_folder)
