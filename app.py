import os
import gradio as gr

print(os.popen(f'cat /etc/debian_version').read())
print(os.popen(f'cat /etc/issue').read())
print(os.popen(f'apt search tesseract').read())

choices = os.popen('tesseract --list-langs').read().split('\n')[1:-1]


def inference(filepath, languages):
    print('languages', languages)
    languages_str = ' -l ' + '+'.join(languages) if languages else ''
    print('languages_str', languages_str)
    return os.popen(f'tesseract {filepath} -{languages_str}').read()


title = "Tesseract OCR"
description = "Gradio demo for Tesseract. Tesseract is an open source text recognition (OCR) Engine."
article = "<p style='text-align: center'><a href='https://tesseract-ocr.github.io/' target='_blank'>Tesseract documentation</a> | <a href='https://github.com/tesseract-ocr/tesseract' target='_blank'>Github Repo</a></p>"
gr.Interface(
    inference,
    [gr.inputs.Image(type="filepath", label="Input"), gr.inputs.CheckboxGroup(choices, type="value", default=['eng'], label='language')],
    'text',
    title=title,
    description=description,
    article=article,
    examples=[['eurotext.png', ['eng']], ['tesseract_sample.png', ['jpn', 'eng']], ['chi.jpg', ['HanS', 'HanT']]]
).launch(enable_queue=True,cache_examples=True)
