from flask import Flask, render_template, request, json, Response, jsonify
import jieba
import sqlite3
import csv
import Terry_toolkit as tkit
import libs
from random import choice
import random
from fun import *

app = Flask(__name__)

def get_post_data():
    """
    从请求中获取参数
    :return:
    """
    data = {}
    if request.content_type.startswith('application/json'):
        data = request.get_data()
        data = json.loads(data)
    else:
        for key, value in request.form.items():
            if key.endswith('[]'):
                data[key[:-2]] = request.form.getlist(key)
            else:
                data[key] = value
    return data

@app.route("/")
def home():
    # print(config.get('site', 'name'))
    return render_template("index.html")


@app.route("/install")
def install():
    conn = sqlite3.connect('terry.db')
    # print(config.get('site', 'name'))
    c = conn.cursor()
    c.execute('''CREATE TABLE COMPANY
        (ID INT PRIMARY KEY     NOT NULL,
        TEXT           TEXT    NOT NULL,
        SIMPLE           TEXT    NOT NULL''')
    conn.commit()
    conn.close()
    return 'install end'


@app.route("/json/text_list_update",methods=['GET', 'POST'])
def json_text_list_update():
    # #句子
    t_text=tkit.Text()

    data= get_post_data()
    print('data',data)
    # paragraph = request.args.get('text')
    # previous_line=request.args.get('sentence')
    text = data['text']
    # text = request.args.get('text')
    text_array= t_text.sentence_segmentation(text)


    # print(text)
    # #python2可以用file替代open
    # with open("text.csv","a") as csvfile: 
    #     writer = csv.writer(csvfile)

    #     # #先写入columns_name
    #     # writer.writerow(["index","a_name","b_name"])
    #     #写入多行用writerows
    #     writer.writerows([text_array])



    return jsonify(text_array)

@app.route("/fenci")
def fenci():
    # print(config.get('site', 'name'))
    return render_template("fenci.html")


# @app.route("/jianxie")
# def fenci():
#     # print(config.get('site', 'name'))
#     return render_template("jianxie.html")



@app.route("/json/fenci_update")

def json_sentence_fenci_update():
    """
    执行提交后处理提交
    """
    # data= get_post_data()
    # print('data',data)
    text1 = request.args.get('text1')
    text2 = request.args.get('text2')
    # previous_line=request.args.get('sentence')
    # text = data['text']
    # text2 = data['text2']
    # seg_list=[]
    # for it in jieba.cut(text, cut_all=False):
    # # print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
    # # print()
    #     seg_list.append(it)



    #保存词性训练数据
    # libs_text= libs.Text()
    text1_pseg  =libs.Text().text_part_pseg(text1)
    text2_pseg  =libs.Text().text_part_pseg(text2)
    file_pseg_write_obj = open("corpus_pseg.txt", 'a')
    #python2可以用file替代open
    # for var in mylist:
    text_pseg = text1_pseg+"\n"+text2_pseg+"\n\n"
    file_pseg_write_obj.writelines(text_pseg)
    file_pseg_write_obj.close()


    #保存训练数据
    file_write_obj = open("corpus.txt", 'a')
    #python2可以用file替代open
    # for var in mylist:
    text = text1+"\n"+text2+"\n\n"
    file_write_obj.writelines(text)

    # 创建bert使用的训练数据
    # #随机产生一条
    # random_sentence_one()

    # 添加一条标记数据
    add_sentence_one(text2)














        #先写入columns_name
        # writer.writerow(["index","a_name","b_name"])
        #写入多行用writerows
        # writer.writerows([[text1,text2]])

    file_write_obj.close()

    return jsonify('')






@app.route("/json/text_get")
def json_text_get():
    """
    获取随机文件
    """
    # text1 = request.args.get('text1')
    # text2 = request.args.get('text2')
    tfile =  tkit.File()
    file_path="/home/terry/pan/github/ai_writer/ai_writer/data/kw2text_mini/"
    file_list=tfile.file_List(file_path)
    
    f = choice(file_list)
    text = tfile.open_file(f)

    return jsonify(text)
@app.route("/json/sentence/fenci")
def json_sentence_fenci():
    """
    获取分词
    
    """
    # data= get_post_data()
    # print('data',data)
    text = request.args.get('text')
    # previous_line=request.args.get('sentence')
    # text = data['text']
    # text2 = data['text2']
    # seg_list=[]
    # # n=text.split()
    # # print('text',n)

    # s = text 
    # L= []
    # for ch in s:
    #     L.append(ch)

    # # print (L)
    # # for it in L:
    # for it in jieba.cut(text, cut_all=False):
    # # print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
    # # print()
    #     seg_list.append(it)

    seg_list=yuce(text)
    data={
        'seg_list':seg_list,
        'text':text

    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()