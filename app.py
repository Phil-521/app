import streamlit as st
from transformers import pipeline
from PIL import Image
import time
import base64
import os
import requests
import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import json



# 设置页面标题和图标
st.set_page_config(page_title="译梦空间", page_icon=":ghost:")
st.title('Let me translate your dreams~')
# 在侧边栏创建功能列表
st.sidebar.write("## 功能列表 :gear:")
# 定义Streamlit应用程序
def zhongying():
    # 创建一个下拉菜单，用于选择翻译模型
    model = st.selectbox("选择翻译模型", ["中文到英文", "英文到中文"])
    # 创建一个文本输入框，用于输入待翻译的文本
    text = st.text_area("请输入待翻译的文本")
    # 创建一个按钮，用于触发翻译操作
    if st.button("翻译"):
        # 根据所选的翻译模型选择不同的翻译器对象
        if model == "中文到英文":
            translator = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")
        elif model == "英文到中文":
            translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")
        # 调用翻译器对象的翻译方法，将待翻译的文本翻译成目标语言
        translation = translator(text, max_length=1024)
        # 显示翻译结果
        result = translation[0]['translation_text']
        st.success("翻译结果为：")
        st.text_area("", result)

def yingri():
    # 创建一个下拉菜单，用于选择翻译模型
    model = st.selectbox("选择翻译模型", ["日文到英文", "英文到日文"])
    # 创建一个文本输入框，用于输入待翻译的文本
    text = st.text_area("请输入要翻译的文本")
    # 创建一个按钮，用于触发翻译操作
    if st.button("翻 译"):
        # 根据所选的翻译模型选择不同的翻译器对象
        if model == "日文到英文":
            translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ja-en")
        elif model == "英文到日文":
            translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-jap")
        # 调用翻译器对象的翻译方法，将待翻译的文本翻译成目标语言
        translation = translator(text, max_length=1024)
        # 显示翻译结果
        result = translation[0]['translation_text']
        st.success("翻译结果为：")
        st.text_area("", result)

def zhongde():
    model = st.selectbox("选择翻译模型", ["中文到德语"])
    text = st.text_area("请输入中文")
    if st.button("翻译到德语"):
        if model == "中文到德语":
            translator1 = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-de")
        translation = translator1(text, max_length=1024)
        result = translation[0]['translation_text']
        st.success("翻译结果为：")
        st.text_area("", result)

def zhongyi():
    model = st.selectbox("选择翻译模型", ["中文到意大利语"])
    text = st.text_area("请输入")
    if st.button("翻译到意大利语"):
        if model == "中文到意大利语":
            translator1 = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-it")
        translation = translator1(text, max_length=1024)
        result = translation[0]['translation_text']
        st.success("翻译结果为：")
        st.text_area("", result)

def gu_xian():
    from transformers import (
        EncoderDecoderModel,
        AutoTokenizer
    )
    import torch
    model = st.selectbox("选择翻译模型", ["古文翻译到现代文","现代文翻译成古文"])
    text = st.text_area("请输入文本")
    if st.button("翻译古文"):
        if model == "古文翻译到现代文":
            PRETRAINED = "raynardj/wenyanwen-ancient-translate-to-modern"
        elif model == "现代文翻译成古文":
            PRETRAINED = "raynardj/wenyanwen-chinese-translate-to-ancient"
        tokenizer = AutoTokenizer.from_pretrained(PRETRAINED)
        model = EncoderDecoderModel.from_pretrained(PRETRAINED)
        def inference(text):
            tk_kwargs = dict(
                truncation=True,
                max_length=128,
                padding="max_length",
                return_tensors='pt')

            inputs = tokenizer([text, ], **tk_kwargs)
            with torch.no_grad():
                return tokenizer.batch_decode(
                    model.generate(
                        inputs.input_ids,
                        attention_mask=inputs.attention_mask,
                        num_beams=3,
                        max_length=256,
                        bos_token_id=101,
                        eos_token_id=tokenizer.sep_token_id,
                        pad_token_id=tokenizer.pad_token_id,
                    ), skip_special_tokens=True)
        result = inference(text)[0]
        st.success("翻译结果为：")
        st.text_area("", result)



if __name__ == '__main__':
    tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(["自我介绍","中英互译","古现互译","中德翻译","中意翻译","英日互译"])
    with tab2:
        zhongying()
    with tab3:
        gu_xian()
    with tab4:
        zhongde()
    with tab5:
        zhongyi()
    with tab6:
        yingri()
    with tab1:
        st.write('嘿！欢迎来到吴梦成的私密空间！:heart_eyes: :heart_eyes: :heart_eyes: ')
        st.write(':point_right: 国家：中国 :cn')
        st.write(':point_right: 职业：学生 :smile:')
        st.write(':point_right: 学校：南京农业大学 :thumbsup:')
        st.write(':point_right: 专业：图书情报与档案管理 :rocket:')
        st.write(':point_right: 研究方向：自然语言处理、古籍智能处理 :star:')
        st.write(':point_right: 如果你对这些领域有兴趣，欢迎与我联系！ :heart:')
        st.write(':point_right: 邮箱:17173741929@qq.com :love_letter:')
        st.write('           :dog::dog::dog:            ')
        with st.expander(":leaves: 如果你想了解更多关于我，看这里~ :fallen_leaf:"):
            tab1, tab2, tab3 = st.tabs(["照片", "视频", "我的宠物"])
            with tab1:
                col1, col2, = st.columns(2)
                with col1:
                    image = Image.open('自我介绍图片.jpg')
                    st.image(image, caption='a picture of my daily life ~ ~ ~', width=300)
                with col2:
                    image = Image.open('自我介绍图片1.jpg')
                    st.image(image, caption='a picture of my daily life ~ ~ ~', width=300)
            with tab2:
                with open('可能.mp4', 'rb') as f:
                    video_bytes = f.read()
                st.video(video_bytes, format="video/mp4", start_time=0)
            with tab3:
                col1, col2 = st.columns(2)
                with col1:
                    st.header("A cat")
                    st.image("https://static.streamlit.io/examples/cat.jpg")
                with col2:
                    st.header("A dog")
                    st.image("https://static.streamlit.io/examples/dog.jpg")



# 点击自我介绍按钮后展示自我介绍
if st.sidebar.button("小雪花"):
    st.snow()
if st.sidebar.button("小气球"):
    st.balloons()








